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


def validate_language_pairs() -> None:
    for directory_name in ("apis", "comparisons"):
        base = ROOT / directory_name
        if not base.exists():
            continue
        for directory in sorted(path for path in base.iterdir() if path.is_dir()):
            en = directory / "README.md"
            ru = directory / "README.ru.md"
            if en.exists() != ru.exists():
                error(f"Missing bilingual README pair in {directory.relative_to(ROOT)}")

    paired_docs = [
        "README",
        "docs/VISION",
        "docs/PRINCIPLES",
        "docs/METHODOLOGY",
        "docs/ROADMAP",
        "docs/GLOSSARY",
        "docs/CONTRIBUTING",
        "docs/MIGRATION",
    ]
    for stem in paired_docs:
        en = ROOT / f"{stem}.md"
        ru = ROOT / f"{stem}.ru.md"
        if en.exists() != ru.exists():
            error(f"Missing bilingual document pair: {stem}")


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


def main() -> int:
    validate_json()
    validate_language_pairs()
    validate_markdown_links()
    validate_local_paths_and_secrets()
    validate_active_api_metadata()
    validate_comparison_metadata()

    for item in WARNINGS:
        print(f"WARNING: {item}")
    for item in ERRORS:
        print(f"ERROR: {item}")

    print(f"\nValidation complete: {len(ERRORS)} error(s), {len(WARNINGS)} warning(s).")
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
