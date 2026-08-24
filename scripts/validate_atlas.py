#!/usr/bin/env python3
"""Validate Project Atlas API-first content without third-party dependencies."""

from __future__ import annotations

import json
import os
import re
import sys
import datetime as dt
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import generate_indexes  # noqa: E402
import check_sources  # noqa: E402

ERRORS: list[str] = []
WARNINGS: list[str] = []
IGNORED_PARTS = {".git", ".venv", "node_modules", "_codex_inbox", "__pycache__"}


def error(message: str) -> None:
    ERRORS.append(message)


def warning(message: str) -> None:
    WARNINGS.append(message)


def validate_json() -> None:
    for path in ROOT.rglob("*.json"):
        if any(part in IGNORED_PARTS for part in path.parts):
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            error(f"Invalid JSON: {path.relative_to(ROOT)}: {exc}")


def active_bilingual_pairs() -> list[tuple[Path, Path]]:
    pairs: list[tuple[Path, Path]] = []

    def add_pair(en: Path, ru: Path) -> None:
        if en.exists() != ru.exists():
            missing = ru if en.exists() else en
            error(f"Missing bilingual pair: {missing.relative_to(ROOT)}")
            return
        if en.exists() and ru.exists():
            pairs.append((en, ru))

    for stem in ("README", "API_INDEX", "COMPARISON_INDEX", "NEEDS_INDEX"):
        add_pair(ROOT / f"{stem}.md", ROOT / f"{stem}.ru.md")

    docs = ROOT / "docs"
    if docs.exists():
        for en in sorted(path for path in docs.glob("*.md") if not path.name.endswith(".ru.md")):
            add_pair(en, en.with_name(f"{en.stem}.ru.md"))

    for base_name in ("apis", "comparisons"):
        base = ROOT / base_name
        if not base.exists():
            continue
        for directory in sorted(path for path in base.iterdir() if path.is_dir()):
            for stem in ("README", "evidence", "changes"):
                add_pair(directory / f"{stem}.md", directory / f"{stem}.ru.md")

    procurement = ROOT / "procurement"
    if procurement.exists():
        for en in sorted(path for path in procurement.rglob("*.md") if not path.name.endswith(".ru.md")):
            add_pair(en, en.with_name(f"{en.stem}.ru.md"))

    needs = ROOT / "needs"
    if needs.exists():
        add_pair(needs / "README.md", needs / "README.ru.md")
        for directory in sorted(path for path in needs.iterdir() if path.is_dir()):
            for stem in ("README", "changes"):
                add_pair(directory / f"{stem}.md", directory / f"{stem}.ru.md")

    legacy = ROOT / "legacy"
    if legacy.exists():
        add_pair(legacy / "README.md", legacy / "README.ru.md")

    templates = ROOT / "templates"
    for stem in ("API_CARD_TEMPLATE", "COMPARISON_TEMPLATE"):
        add_pair(templates / f"{stem}.md", templates / f"{stem}.ru.md")

    schemas = ROOT / "schemas"
    if schemas.exists():
        add_pair(schemas / "README.md", schemas / "README.ru.md")

    return pairs


def relative_link(from_path: Path, to_path: Path) -> str:
    return Path(os.path.relpath(to_path, from_path.parent)).as_posix()


def validate_language_link(source: Path, target: Path, label: str) -> None:
    rel = relative_link(source, target)
    expected = f"[{label}]({rel})"
    lines = source.read_text(encoding="utf-8", errors="replace").splitlines()
    path_label = source.relative_to(ROOT)

    if not lines or not lines[0].startswith("# "):
        error(f"Missing top-level heading in {path_label}")
        return

    if expected not in lines[:10]:
        error(f"Missing language link in first 10 lines: {path_label} -> {expected}")
        return

    if len(lines) < 4 or lines[1].strip() or lines[2].strip() != expected or lines[3].strip():
        error(f"Language link must immediately follow heading with blank lines: {path_label}")
        return

    resolved = (source.parent / rel).resolve()
    if resolved != target.resolve():
        error(f"Language link points to wrong file: {path_label} -> {rel}")


def validate_language_pairs() -> None:
    for en, ru in active_bilingual_pairs():
        validate_language_link(en, ru, "Русская версия")
        validate_language_link(ru, en, "English version")


def iter_markdown_links(text: str):
    # Ignore images and anchors. This intentionally validates ordinary inline links only.
    pattern = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
    for match in pattern.finditer(text):
        target = match.group(1).strip().split(maxsplit=1)[0].strip("<>")
        yield target


def validate_markdown_links() -> None:
    for path in ROOT.rglob("*.md"):
        if any(part in IGNORED_PARTS for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for raw_target in iter_markdown_links(text):
            parsed = urlparse(raw_target)
            if parsed.scheme in {"http", "https", "mailto"} or raw_target.startswith("#"):
                continue
            target_without_anchor = unquote(raw_target.split("#", 1)[0])
            if not target_without_anchor:
                continue
            resolved = (path.parent / target_without_anchor).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                error(f"Relative link escapes repository: {path.relative_to(ROOT)} -> {raw_target}")
                continue
            if not resolved.exists():
                error(f"Broken relative link: {path.relative_to(ROOT)} -> {raw_target}")


def validate_local_paths_and_secrets() -> None:
    local_path_patterns = [
        r"/mnt/data/",
        r"(?<![A-Za-z0-9:/])/Users/[^/]+/",
        r"(?<![A-Za-z0-9:/])/home/[^/]+/",
        r"[A-Za-z]:\\Users\\",
        r"sandbox:/",
        r"file_000000",
    ]
    secret_patterns = [
        r"(?i)(api[_ -]?key|secret|token)\s*[:=]\s*[\"'][A-Za-z0-9_\-]{16,}",
        r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
    ]
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() in {".xlsx", ".png", ".jpg", ".jpeg", ".zip"}:
            continue
        if path.resolve() == Path(__file__).resolve():
            continue
        if any(part in IGNORED_PARTS for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in local_path_patterns:
            if re.search(pattern, text):
                error(f"Local artifact path found in {path.relative_to(ROOT)}: {pattern}")
        for pattern in secret_patterns:
            if re.search(pattern, text):
                error(f"Possible secret found in {path.relative_to(ROOT)}")


def load_json_file(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    return data if isinstance(data, dict) else {}


def validate_active_api_metadata() -> None:
    base = ROOT / "apis"
    if not base.exists():
        return

    required_fields = ("schema_version", "id", "name", "maturity", "last_verified", "live_tested", "sources")
    maturity_levels = {"discovered", "verified", "reviewed", "compared", "gold"}
    for directory in sorted(path for path in base.iterdir() if path.is_dir()):
        json_path = directory / "api.json"
        if not json_path.exists():
            warning(f"No api.json: {directory.relative_to(ROOT)}")
            continue
        data = load_json_file(json_path)
        if not data:
            continue

        for field in required_fields:
            if field not in data:
                error(f"Missing top-level {field} in {json_path.relative_to(ROOT)}")

        for field in ("id", "name", "maturity", "last_verified"):
            if field in data and not isinstance(data[field], str):
                error(f"Expected string {field} in {json_path.relative_to(ROOT)}")
            elif field in data and not data[field].strip():
                error(f"Empty {field} in {json_path.relative_to(ROOT)}")

        if data.get("schema_version") != 1:
            error(f"Expected schema_version 1 in {json_path.relative_to(ROOT)}")
        if isinstance(data.get("last_verified"), str):
            try:
                dt.date.fromisoformat(data["last_verified"])
            except ValueError:
                error(f"Invalid last_verified date in {json_path.relative_to(ROOT)}")

        if "live_tested" in data and not isinstance(data["live_tested"], bool):
            error(f"Expected boolean live_tested in {json_path.relative_to(ROOT)}")

        if data.get("live_tested") is True:
            for field in ("live_tested_on", "live_test_valid_until"):
                value = data.get(field)
                if not isinstance(value, str) or not value.strip():
                    error(f"Missing non-empty {field} for live-tested API in {json_path.relative_to(ROOT)}")
                    continue
                try:
                    parsed = dt.date.fromisoformat(value)
                except ValueError:
                    error(f"Invalid {field} date in {json_path.relative_to(ROOT)}")
                    continue
                if field == "live_test_valid_until" and parsed < dt.date.today():
                    error(f"Expired live-test evidence in {json_path.relative_to(ROOT)}: {value}")

            tested_on = data.get("live_tested_on")
            valid_until = data.get("live_test_valid_until")
            if isinstance(tested_on, str) and isinstance(valid_until, str):
                try:
                    if dt.date.fromisoformat(valid_until) < dt.date.fromisoformat(tested_on):
                        error(f"live_test_valid_until precedes live_tested_on in {json_path.relative_to(ROOT)}")
                except ValueError:
                    pass

        sources = data.get("sources")
        if "sources" in data and (not isinstance(sources, list) or not sources):
            error(f"Expected non-empty sources list in {json_path.relative_to(ROOT)}")

        maturity = data.get("maturity")
        if isinstance(maturity, str) and maturity not in maturity_levels:
            error(f"Invalid maturity in {json_path.relative_to(ROOT)}: {maturity}")


def validate_comparison_metadata() -> None:
    base = ROOT / "comparisons"
    if not base.exists():
        return

    required_fields = ("schema_version", "id", "title", "status", "verified_on", "candidates", "sources")
    api_ids = json_id_map("apis", "api.json")
    for directory in sorted(path for path in base.iterdir() if path.is_dir()):
        json_path = directory / "comparison.json"
        if not json_path.exists():
            warning(f"No comparison.json: {directory.relative_to(ROOT)}")
            continue
        data = load_json_file(json_path)
        if not data:
            continue
        for field in required_fields:
            if field not in data:
                error(f"Missing {field} in {json_path.relative_to(ROOT)}")
        if data.get("schema_version") != 1:
            error(f"Expected schema_version 1 in {json_path.relative_to(ROOT)}")
        if "candidates" in data and not isinstance(data["candidates"], list):
            error(f"Expected candidates list in {json_path.relative_to(ROOT)}")
        if "sources" in data and (not isinstance(data["sources"], list) or not data["sources"]):
            error(f"Expected non-empty sources list in {json_path.relative_to(ROOT)}")
        for candidate in data.get("candidates", []):
            if not isinstance(candidate, dict):
                error(f"Invalid candidate in {json_path.relative_to(ROOT)}: expected object")
                continue
            candidate_id = candidate.get("id")
            if not isinstance(candidate_id, str) or not candidate_id:
                error(f"Invalid candidate id in {json_path.relative_to(ROOT)}")
                continue
            if candidate_id in api_ids:
                continue
            reference = candidate.get("reference")
            if not isinstance(reference, str) or not path_exists(reference):
                error(
                    f"Unknown candidate id without a valid research reference in "
                    f"{json_path.relative_to(ROOT)}: {candidate_id}"
                )


def validate_needs_metadata() -> None:
    base = ROOT / "needs"
    if not base.exists():
        return

    required_fields = (
        "schema_version",
        "id",
        "name",
        "name_ru",
        "status",
        "last_verified",
        "primary_question",
        "related_apis",
        "related_comparisons",
        "related_procurement",
        "decision_paths",
        "open_questions",
        "sources",
    )
    for directory in sorted(path for path in base.iterdir() if path.is_dir()):
        json_path = directory / "need.json"
        if not json_path.exists():
            warning(f"No need.json: {directory.relative_to(ROOT)}")
            continue
        data = load_json_file(json_path)
        if not data:
            continue
        for field in required_fields:
            if field not in data:
                error(f"Missing {field} in {json_path.relative_to(ROOT)}")
        if data.get("schema_version") != 1:
            error(f"Expected schema_version 1 in {json_path.relative_to(ROOT)}")
        for field in ("id", "name", "name_ru", "status", "last_verified", "primary_question"):
            if field in data and not isinstance(data[field], str):
                error(f"Expected string {field} in {json_path.relative_to(ROOT)}")
            elif field in data and not data[field].strip():
                error(f"Empty {field} in {json_path.relative_to(ROOT)}")
        for field in ("related_apis", "related_comparisons", "related_procurement", "decision_paths", "open_questions", "sources"):
            if field in data and not isinstance(data[field], list):
                error(f"Expected list {field} in {json_path.relative_to(ROOT)}")
            elif field in data and not data[field]:
                error(f"Empty {field} in {json_path.relative_to(ROOT)}")


def json_id_map(base_name: str, json_name: str) -> dict[str, Path]:
    result: dict[str, Path] = {}
    base = ROOT / base_name
    if not base.exists():
        return result
    for directory in sorted(path for path in base.iterdir() if path.is_dir()):
        json_path = directory / json_name
        if not json_path.exists():
            continue
        data = load_json_file(json_path)
        item_id = data.get("id")
        if isinstance(item_id, str) and item_id:
            result[item_id] = directory
    return result


def path_exists(value: str) -> bool:
    parsed = urlparse(value)
    if parsed.scheme in {"http", "https", "mailto"}:
        return True
    return (ROOT / value).exists()


def validate_id_or_path(value: object, known_ids: dict[str, Path], label: str, json_path: Path) -> None:
    if not isinstance(value, str) or not value.strip():
        error(f"Invalid {label} reference in {json_path.relative_to(ROOT)}: {value!r}")
        return
    if value in known_ids or path_exists(value):
        return
    error(f"Broken {label} reference in {json_path.relative_to(ROOT)}: {value}")


def validate_need_references() -> None:
    api_ids = json_id_map("apis", "api.json")
    comparison_ids = json_id_map("comparisons", "comparison.json")
    base = ROOT / "needs"
    if not base.exists():
        return

    for directory in sorted(path for path in base.iterdir() if path.is_dir()):
        json_path = directory / "need.json"
        if not json_path.exists():
            continue
        data = load_json_file(json_path)
        if not data:
            continue

        for value in data.get("related_apis", []):
            validate_id_or_path(value, api_ids, "related_apis", json_path)
        for value in data.get("related_comparisons", []):
            validate_id_or_path(value, comparison_ids, "related_comparisons", json_path)
        for value in data.get("related_procurement", []):
            validate_id_or_path(value, {}, "related_procurement", json_path)
        for source in data.get("sources", []):
            validate_id_or_path(source, {}, "sources", json_path)

        for decision_path in data.get("decision_paths", []):
            if not isinstance(decision_path, dict):
                error(f"Invalid decision_paths item in {json_path.relative_to(ROOT)}")
                continue
            next_document = decision_path.get("next_document")
            if next_document is not None:
                validate_id_or_path(next_document, {}, "decision_paths.next_document", json_path)


def validate_index_freshness() -> None:
    try:
        expected = generate_indexes.generate_all()
    except generate_indexes.IndexGenerationError as exc:
        error(str(exc))
        return

    for path, content in expected.items():
        if not path.exists():
            error(f"Missing generated index: {path.relative_to(ROOT)}")
            continue
        if path.read_text(encoding="utf-8") != content:
            error(f"Generated index is stale: {path.relative_to(ROOT)}")


def validate_source_monitor_config() -> None:
    try:
        _, overrides = check_sources.load_registry()
        sources = check_sources.collect_sources(ROOT, overrides)
    except check_sources.MonitorConfigError as exc:
        error(str(exc))
        return
    if not sources:
        error("Source monitor discovered no external URLs in active API profiles")


def main() -> int:
    validate_json()
    validate_language_pairs()
    validate_markdown_links()
    validate_local_paths_and_secrets()
    validate_active_api_metadata()
    validate_comparison_metadata()
    validate_needs_metadata()
    validate_need_references()
    validate_index_freshness()
    validate_source_monitor_config()

    for item in WARNINGS:
        print(f"WARNING: {item}")
    for item in ERRORS:
        print(f"ERROR: {item}")

    print(f"\nValidation complete: {len(ERRORS)} error(s), {len(WARNINGS)} warning(s).")
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
