#!/usr/bin/env python3
"""Monitor official URLs referenced by active Atlas API profiles."""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote, urlparse, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "sources" / "source-registry.json"
ATTENTION_STATUSES = {"broken", "changed", "restricted", "unavailable"}


class MonitorConfigError(RuntimeError):
    """Raised when source-monitor configuration is invalid."""


@dataclass(frozen=True)
class Source:
    url: str
    profiles: tuple[str, ...]
    label: str = ""
    required_markers: tuple[str, ...] = ()
    expected_sha256: str = ""


@dataclass(frozen=True)
class Result:
    source: Source
    status: str
    detail: str
    http_status: int | None = None
    sha256: str = ""


def read_json(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        raise MonitorConfigError(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc
    if not isinstance(data, dict):
        raise MonitorConfigError(f"Expected JSON object in {path.relative_to(ROOT)}")
    return data


def validate_url(value: object, label: str) -> str:
    if not isinstance(value, str) or urlparse(value).scheme not in {"http", "https"}:
        raise MonitorConfigError(f"Invalid URL for {label}: {value!r}")
    return value


def load_registry(path: Path = REGISTRY_PATH) -> tuple[dict, dict[str, dict]]:
    data = read_json(path)
    if data.get("version") != 1:
        raise MonitorConfigError("sources/source-registry.json must use version 1")
    defaults = data.get("defaults")
    overrides = data.get("overrides")
    if not isinstance(defaults, dict) or not isinstance(overrides, list):
        raise MonitorConfigError("Registry defaults must be an object and overrides must be a list")

    indexed: dict[str, dict] = {}
    for index, override in enumerate(overrides):
        if not isinstance(override, dict):
            raise MonitorConfigError(f"Override {index} must be an object")
        url = validate_url(override.get("url"), f"override {index}")
        if url in indexed:
            raise MonitorConfigError(f"Duplicate source override: {url}")
        markers = override.get("required_markers", [])
        if not isinstance(markers, list) or not all(isinstance(item, str) and item for item in markers):
            raise MonitorConfigError(f"Invalid required_markers for {url}")
        expected = override.get("expected_sha256", "")
        if expected and (not isinstance(expected, str) or len(expected) != 64):
            raise MonitorConfigError(f"Invalid expected_sha256 for {url}")
        indexed[url] = override

    for field in ("timeout_seconds", "max_bytes", "workers", "user_agent"):
        if field not in defaults:
            raise MonitorConfigError(f"Missing registry default: {field}")
    return defaults, indexed


def collect_sources(root: Path, overrides: dict[str, dict]) -> list[Source]:
    owners: dict[str, set[str]] = {}
    for path in sorted((root / "apis").glob("*/api.json")):
        data = read_json(path)
        profile_id = data.get("id", path.parent.name)
        for value in data.get("sources", []):
            if isinstance(value, str) and urlparse(value).scheme in {"http", "https"}:
                owners.setdefault(value, set()).add(str(profile_id))

    sources: list[Source] = []
    for url, profile_ids in sorted(owners.items()):
        override = overrides.get(url, {})
        sources.append(
            Source(
                url=url,
                profiles=tuple(sorted(profile_ids)),
                label=str(override.get("label", "")),
                required_markers=tuple(override.get("required_markers", [])),
                expected_sha256=str(override.get("expected_sha256", "")),
            )
        )
    return sources


def evaluate_response(source: Source, status: int, body: bytes) -> Result:
    digest = hashlib.sha256(body).hexdigest()
    if status in {401, 403, 429}:
        return Result(source, "restricted", f"HTTP {status}; source may block automated checks", status, digest)
    if status in {404, 410}:
        return Result(source, "broken", f"HTTP {status}", status, digest)
    if status >= 500:
        return Result(source, "unavailable", f"HTTP {status}", status, digest)
    if status < 200 or status >= 400:
        return Result(source, "unavailable", f"HTTP {status}", status, digest)

    text = body.decode("utf-8", errors="replace").casefold()
    missing = [marker for marker in source.required_markers if marker.casefold() not in text]
    if missing:
        return Result(source, "changed", f"Missing marker(s): {', '.join(missing)}", status, digest)
    if source.expected_sha256 and digest != source.expected_sha256:
        return Result(source, "changed", "Content fingerprint changed", status, digest)
    return Result(source, "ok", f"HTTP {status}", status, digest)


def network_url(url: str) -> str:
    parts = urlsplit(url)
    host = parts.hostname.encode("idna").decode("ascii") if parts.hostname else ""
    if parts.port:
        host = f"{host}:{parts.port}"
    if parts.username:
        credentials = quote(parts.username, safe="")
        if parts.password:
            credentials += f":{quote(parts.password, safe='')}"
        host = f"{credentials}@{host}"
    path = quote(parts.path, safe="/%:@-._~!$&'()*+,;=")
    query = quote(parts.query, safe="=&?/%:@-._~!$'()*+,;")
    return urlunsplit((parts.scheme, host, path, query, parts.fragment))


def check_source(source: Source, defaults: dict) -> Result:
    request = urllib.request.Request(
        network_url(source.url),
        headers={"User-Agent": str(defaults["user_agent"]), "Accept": "*/*"},
    )
    try:
        with urllib.request.urlopen(request, timeout=float(defaults["timeout_seconds"])) as response:
            body = response.read(int(defaults["max_bytes"]))
            return evaluate_response(source, int(response.status), body)
    except urllib.error.HTTPError as exc:
        body = exc.read(int(defaults["max_bytes"]))
        return evaluate_response(source, int(exc.code), body)
    except (urllib.error.URLError, TimeoutError, OSError, UnicodeError, ValueError) as exc:
        return Result(source, "unavailable", str(exc))


def render_report(results: list[Result]) -> str:
    counts: dict[str, int] = {}
    for result in results:
        counts[result.status] = counts.get(result.status, 0) + 1
    summary = ", ".join(f"{key}: {counts[key]}" for key in sorted(counts)) or "no sources"
    visible = [result for result in results if result.status != "ok"]
    lines = ["# Atlas Source Monitor", "", f"Checked {len(results)} source(s): {summary}.", ""]
    if not visible:
        return "\n".join(lines + ["No source requires attention.\n"])
    lines.extend(["| Status | Source | Profiles | Detail |", "|---|---|---|---|"])
    for result in sorted(visible, key=lambda item: (item.status, item.source.url)):
        label = result.source.label or result.source.url
        link = f"[{label}]({result.source.url})"
        lines.append(f"| {result.status} | {link} | {', '.join(result.source.profiles)} | {result.detail} |")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validate-config", action="store_true", help="Validate configuration without network access")
    parser.add_argument("--report", type=Path, help="Write a Markdown report")
    parser.add_argument("--json-report", type=Path, help="Write a machine-readable report")
    args = parser.parse_args()

    try:
        defaults, overrides = load_registry()
        sources = collect_sources(ROOT, overrides)
    except MonitorConfigError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.validate_config:
        print(f"Source registry valid; {len(sources)} active external URL(s) discovered.")
        return 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=int(defaults["workers"])) as executor:
        results = list(executor.map(lambda source: check_source(source, defaults), sources))

    report = render_report(results)
    print(report, end="")
    if args.report:
        args.report.write_text(report, encoding="utf-8")
    if args.json_report:
        payload = [
            {"url": item.source.url, "profiles": item.source.profiles, "status": item.status, "detail": item.detail}
            for item in results
        ]
        args.json_report.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 2 if any(item.status in ATTENTION_STATUSES for item in results) else 0


if __name__ == "__main__":
    sys.exit(main())
