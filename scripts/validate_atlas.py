#!/usr/bin/env python3
"""Validate Project Atlas API-first content without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []
IGNORED_PARTS = {".git", ".venv", "node_modules", "_codex_inbox"}


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


def language_pair_for(en_path: Path) -> Path:
    return en_path.with_name(f"{en_path.stem}.ru.md")


def iter_active_markdown_pairs() -> list[tuple[Path, Path]]:
    pairs: list[tuple[Path, Path]] = []

    for stem in ("README", "API_INDEX", "COMPARISON_INDEX", "NEEDS_INDEX"):
        en = ROOT / f"{stem}.md"
        ru = ROOT / f"{stem}.ru.md"
        if en.exists() or ru.exists():
            pairs.append((en, ru))

    for base_name in ("docs", "apis", "comparisons", "procurement", "needs"):
        base = ROOT / base_name
        if not base.exists():
            continue
        for en in sorted(base.rglob("*.md")):
            if en.name.endswith(".ru.md") or any(part in IGNORED_PARTS or part == "legacy" for part in en.parts):
                continue
            ru = language_pair_for(en)
            if en.exists() or ru.exists():
                pairs.append((en, ru))

    for stem in ("API_CARD_TEMPLATE", "COMPARISON_TEMPLATE"):
        en = ROOT / "templates" / f"{stem}.md"
        ru = ROOT / "templates" / f"{stem}.ru.md"
        if en.exists() or ru.exists():
            pairs.append((en, ru))

    return pairs


def find_language_link(path: Path, expected_label: str) -> tuple[int, str] | None:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    first_ten = lines[:10]
    pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    for index, line in enumerate(first_ten, start=1):
        match = pattern.search(line)
        if not match:
            continue
        if expected_label not in match.group(1):
            continue
        return index, match.group(2).strip().split(maxsplit=1)[0].strip("<>")
    return None


def validate_language_link(en: Path, ru: Path, source: Path, expected_label: str, expected_target: Path) -> None:
    result = find_language_link(source, expected_label)
    if result is None:
        error(f"Missing language link in first 10 lines: {source.relative_to(ROOT)}")
        return

    line_number, raw_target = result
    lines = source.read_text(encoding="utf-8", errors="replace").splitlines()
    if line_number != 3:
        error(f"Language link must be immediately after heading in {source.relative_to(ROOT)}")
    if len(lines) < 4 or lines[1].strip() or lines[3].strip():
        error(f"Language link must have blank lines around it in {source.relative_to(ROOT)}")

    target_without_anchor = unquote(raw_target.split("#", 1)[0])
    resolved = (source.parent / target_without_anchor).resolve()
    if resolved != expected_target.resolve():
        error(
            "Language link points to wrong target: "
            f"{source.relative_to(ROOT)} -> {raw_target}, expected {expected_target.relative_to(ROOT)}"
        )


def validate_language_pairs() -> None:
    for en, ru in iter_active_markdown_pairs():
        if en.exists() != ru.exists():
            error(f"Missing bilingual document pair: {en.relative_to(ROOT)} / {ru.relative_to(ROOT)}")
            continue
        if not en.exists() or not ru.exists():
            continue
        validate_language_link(en, ru, en, "Русская версия", ru)
        validate_language_link(en, ru, ru, "English version", en)


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
    local_path_patterns = [r"/mnt/data/", r"sandbox:/", r"file_000000"]
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


def validate_active_api_metadata() -> None:
    base = ROOT / "apis"
    if not base.exists():
        return

    required_fields = ("id", "name", "maturity", "last_verified", "live_tested", "sources")
    for directory in sorted(path for path in base.iterdir() if path.is_dir()):
        json_path = directory / "api.json"
        if not json_path.exists():
            warning(f"No api.json: {directory.relative_to(ROOT)}")
            continue
        try:
            data = json.loads(json_path.read_text(encoding="utf-8"))
        except Exception:
            continue

        for field in required_fields:
            if field not in data:
                error(f"Missing top-level {field} in {json_path.relative_to(ROOT)}")

        for field in ("id", "name", "maturity", "last_verified"):
            if field in data and not isinstance(data[field], str):
                error(f"Expected string {field} in {json_path.relative_to(ROOT)}")
            elif field in data and not data[field].strip():
                error(f"Empty {field} in {json_path.relative_to(ROOT)}")

        if "live_tested" in data and not isinstance(data["live_tested"], bool):
            error(f"Expected boolean live_tested in {json_path.relative_to(ROOT)}")

        sources = data.get("sources")
        if "sources" in data and (not isinstance(sources, list) or not sources):
            error(f"Expected non-empty sources list in {json_path.relative_to(ROOT)}")


def load_json_file(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    return data if isinstance(data, dict) else {}


def validate_comparison_metadata() -> None:
    base = ROOT / "comparisons"
    if not base.exists():
        return

    for directory in sorted(path for path in base.iterdir() if path.is_dir()):
        json_path = directory / "comparison.json"
        if not json_path.exists():
            warning(f"No comparison.json: {directory.relative_to(ROOT)}")
            continue
        try:
            data = json.loads(json_path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not data.get("id"):
            error(f"Missing id in {json_path.relative_to(ROOT)}")
        if not data.get("verified_on"):
            warning(f"Missing verification date in {json_path.relative_to(ROOT)}")


def validate_need_metadata() -> None:
    base = ROOT / "needs"
    if not base.exists():
        return

    required_fields = (
        "id",
        "name",
        "name_ru",
        "status",
        "last_verified",
        "related_apis",
        "decision_paths",
    )
    list_fields = ("related_apis", "decision_paths")

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
        for field in ("id", "name", "name_ru", "status", "last_verified"):
            if field in data and not isinstance(data[field], str):
                error(f"Expected string {field} in {json_path.relative_to(ROOT)}")
            elif field in data and not data[field].strip():
                error(f"Empty {field} in {json_path.relative_to(ROOT)}")
        for field in list_fields:
            value = data.get(field)
            if field in data and (not isinstance(value, list) or not value):
                error(f"Expected non-empty list {field} in {json_path.relative_to(ROOT)}")


def collect_ids(base_name: str, json_name: str) -> dict[str, Path]:
    ids: dict[str, Path] = {}
    base = ROOT / base_name
    if not base.exists():
        return ids
    for directory in sorted(path for path in base.iterdir() if path.is_dir()):
        json_path = directory / json_name
        if not json_path.exists():
            continue
        data = load_json_file(json_path)
        item_id = data.get("id")
        if isinstance(item_id, str) and item_id:
            ids[item_id] = json_path
    return ids


def path_or_id_exists(value: str, known_ids: dict[str, Path]) -> bool:
    if value in known_ids:
        return True
    candidate = ROOT / value
    return candidate.exists()


def validate_internal_references() -> None:
    api_ids = collect_ids("apis", "api.json")
    comparison_ids = collect_ids("comparisons", "comparison.json")
    procurement_base = ROOT / "procurement"

    for directory in sorted(path for path in (ROOT / "needs").iterdir() if path.is_dir()) if (ROOT / "needs").exists() else []:
        json_path = directory / "need.json"
        if not json_path.exists():
            continue
        data = load_json_file(json_path)
        for value in data.get("related_apis", []):
            if not isinstance(value, str) or not path_or_id_exists(value, api_ids):
                error(f"Broken related_apis reference in {json_path.relative_to(ROOT)}: {value}")
        for value in data.get("related_comparisons", []):
            if not isinstance(value, str) or not path_or_id_exists(value, comparison_ids):
                error(f"Broken related_comparisons reference in {json_path.relative_to(ROOT)}: {value}")
        for value in data.get("related_procurement", []):
            if not isinstance(value, str) or not (ROOT / value).exists():
                error(f"Broken related_procurement reference in {json_path.relative_to(ROOT)}: {value}")
        for value in data.get("sources", []):
            if isinstance(value, str) and not urlparse(value).scheme and not (ROOT / value).exists():
                error(f"Broken need source reference in {json_path.relative_to(ROOT)}: {value}")

    if procurement_base.exists():
        for path in procurement_base.rglob("*.md"):
            if path.name.endswith(".ru.md"):
                continue
            ru = language_pair_for(path)
            if path.exists() != ru.exists():
                error(f"Missing procurement bilingual pair: {path.relative_to(ROOT)} / {ru.relative_to(ROOT)}")


def validate_index_freshness() -> None:
    index_expectations = [
        ("API_INDEX.md", "apis", "api.json", "README.md"),
        ("API_INDEX.ru.md", "apis", "api.json", "README.ru.md"),
        ("COMPARISON_INDEX.md", "comparisons", "comparison.json", "README.md"),
        ("COMPARISON_INDEX.ru.md", "comparisons", "comparison.json", "README.ru.md"),
        ("NEEDS_INDEX.md", "needs", "need.json", "README.md"),
        ("NEEDS_INDEX.ru.md", "needs", "need.json", "README.ru.md"),
    ]
    for index_name, base_name, json_name, readme_name in index_expectations:
        index_path = ROOT / index_name
        base = ROOT / base_name
        if not index_path.exists() or not base.exists():
            continue
        text = index_path.read_text(encoding="utf-8", errors="replace")
        for directory in sorted(path for path in base.iterdir() if path.is_dir()):
            json_path = directory / json_name
            readme_path = directory / readme_name
            if not json_path.exists() or not readme_path.exists():
                continue
            rel = readme_path.relative_to(ROOT).as_posix()
            if rel not in text:
                error(f"Index {index_name} missing active entry: {rel}")


def main() -> int:
    validate_json()
    validate_language_pairs()
    validate_markdown_links()
    validate_local_paths_and_secrets()
    validate_active_api_metadata()
    validate_comparison_metadata()
    validate_need_metadata()
    validate_internal_references()
    validate_index_freshness()

    for item in WARNINGS:
        print(f"WARNING: {item}")
    for item in ERRORS:
        print(f"ERROR: {item}")

    print(f"\nValidation complete: {len(ERRORS)} error(s), {len(WARNINGS)} warning(s).")
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
