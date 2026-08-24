#!/usr/bin/env python3
"""Monitor official URLs with credential-free public HTTP GET checks.

The monitor never sends credentials, POST requests or paid method calls. It only
checks URLs already declared as official sources by active profiles.
"""

from __future__ import annotations

import argparse
import datetime as dt
import concurrent.futures
import hashlib
import json
import socket
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote, urlparse, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "sources" / "source-registry.json"
ATTENTION_STATUSES = {"auth_required", "rate_limited", "server_error", "timeout", "dns_error", "unknown"}
PUBLIC_STATUSES = {"healthy", "auth_required", "rate_limited", "server_error", "timeout", "dns_error", "unknown"}


class MonitorConfigError(RuntimeError):
    """Raised when source-monitor configuration is invalid."""


@dataclass(frozen=True)
class Source:
    url: str
    profiles: tuple[str, ...]
    label: str = ""
    required_markers: tuple[str, ...] = ()
    expected_sha256: str = ""


@dataclass
class Result:
    source: Source
    status: str
    detail: str
    http_status: int | None = None
    sha256: str = ""
    response_time_ms: int | None = None
    checked_at: str = ""

    @property
    def error(self) -> str:
        return "" if self.status == "healthy" else self.detail


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
    if status in {401, 403}:
        return Result(source, "auth_required", f"HTTP {status}; authentication or access permission required", status, digest)
    if status == 429:
        return Result(source, "rate_limited", "HTTP 429; public check was rate limited", status, digest)
    if status >= 500:
        return Result(source, "server_error", f"HTTP {status}", status, digest)
    if status < 200 or status >= 400:
        return Result(source, "unknown", f"HTTP {status}", status, digest)

    text = body.decode("utf-8", errors="replace").casefold()
    missing = [marker for marker in source.required_markers if marker.casefold() not in text]
    if missing:
        return Result(source, "unknown", f"Missing marker(s): {', '.join(missing)}", status, digest)
    if source.expected_sha256 and digest != source.expected_sha256:
        return Result(source, "unknown", "Content fingerprint changed", status, digest)
    return Result(source, "healthy", f"HTTP {status}", status, digest)


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
    checked_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    started = time.monotonic()
    request = urllib.request.Request(
        network_url(source.url),
        headers={"User-Agent": str(defaults["user_agent"]), "Accept": "*/*"},
    )
    try:
        with urllib.request.urlopen(request, timeout=float(defaults["timeout_seconds"])) as response:
            body = response.read(int(defaults["max_bytes"]))
            result = evaluate_response(source, int(response.status), body)
    except urllib.error.HTTPError as exc:
        body = exc.read(int(defaults["max_bytes"]))
        result = evaluate_response(source, int(exc.code), body)
    except (TimeoutError, socket.timeout) as exc:
        result = Result(source, "timeout", str(exc) or "request timed out")
    except urllib.error.URLError as exc:
        reason = exc.reason
        if isinstance(reason, socket.gaierror) or "nodename" in str(reason).lower() or "name or service" in str(reason).lower():
            result = Result(source, "dns_error", str(reason))
        else:
            result = Result(source, "unknown", str(reason))
    except (OSError, UnicodeError, ValueError) as exc:
        result = Result(source, "unknown", str(exc))

    result.response_time_ms = round((time.monotonic() - started) * 1000)
    result.checked_at = checked_at
    return result


def render_report(results: list[Result]) -> str:
    counts: dict[str, int] = {}
    for result in results:
        counts[result.status] = counts.get(result.status, 0) + 1
    summary = ", ".join(f"{key}: {counts[key]}" for key in sorted(counts)) or "no sources"
    lines = ["# Atlas Source Monitor", "", f"Checked {len(results)} source(s): {summary}.", ""]
    lines.extend(["| Last checked | Status | HTTP code | Response time | Error | Source | Profiles |", "|---|---|---:|---:|---|---|---|"])
    for result in sorted(results, key=lambda item: item.source.url):
        label = result.source.label or result.source.url
        link = f"[{label}]({result.source.url})"
        http_code = str(result.http_status) if result.http_status is not None else "-"
        response_time = f"{result.response_time_ms} ms" if result.response_time_ms is not None else "-"
        lines.append(f"| {result.checked_at or '-'} | {result.status} | {http_code} | {response_time} | {result.error or '-'} | {link} | {', '.join(result.source.profiles)} |")
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
            {
                "url": item.source.url,
                "profiles": item.source.profiles,
                "last_checked": item.checked_at,
                "status": item.status,
                "http_code": item.http_status,
                "response_time_ms": item.response_time_ms,
                "error": item.error,
            }
            for item in results
        ]
        args.json_report.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 2 if any(item.status in ATTENTION_STATUSES for item in results) else 0


if __name__ == "__main__":
    sys.exit(main())
