#!/usr/bin/env python3
"""Generate deterministic Atlas navigation indexes."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class IndexGenerationError(RuntimeError):
    """Raised when an index cannot be generated from repository metadata."""


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        raise IndexGenerationError(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc


def require_mapping(value: object, path: Path) -> dict:
    if not isinstance(value, dict):
        raise IndexGenerationError(f"Expected JSON object in {path.relative_to(ROOT)}")
    return value


def list_metadata(base_name: str, json_name: str) -> list[tuple[str, dict]]:
    base = ROOT / base_name
    if not base.exists():
        return []

    items: list[tuple[str, dict]] = []
    for directory in sorted(path for path in base.iterdir() if path.is_dir()):
        json_path = directory / json_name
        if not json_path.exists():
            continue
        data = require_mapping(read_json(json_path), json_path)
        slug = directory.name
        items.append((slug, data))
    return items


def text_value(data: dict, field: str, default: str = "unknown") -> str:
    value = data.get(field)
    if value is None:
        return default
    if isinstance(value, str):
        return value.strip() or default
    return str(value)


def comparison_title(data: dict, language: str) -> str:
    title = data.get("title")
    if isinstance(title, dict):
        value = title.get(language) or title.get("en") or title.get("ru")
        if isinstance(value, str) and value.strip():
            return value.strip()
    if isinstance(title, str) and title.strip():
        return title.strip()
    return text_value(data, "id")


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join(lines)


def generate_api_index(language: str) -> str:
    entries = []
    for slug, data in list_metadata("apis", "api.json"):
        name = text_value(data, "name")
        maturity = text_value(data, "maturity")
        verified = text_value(data, "last_verified")
        entries.append((name.lower(), slug, name, maturity, verified))
    entries.sort()

    if language == "ru":
        rows = [
            [f"[{name}](apis/{slug}/README.ru.md)", maturity, verified]
            for _, slug, name, maturity, verified in entries
        ]
        body = markdown_table(["API", "Уровень", "Последняя проверка"], rows)
        return f"# Индекс API\n\n[English version](API_INDEX.md)\n\n{body}\n"

    rows = [
        [f"[{name}](apis/{slug}/README.md)", maturity, verified]
        for _, slug, name, maturity, verified in entries
    ]
    body = markdown_table(["API", "Maturity", "Last verified"], rows)
    return f"# API Index\n\n[Русская версия](API_INDEX.ru.md)\n\n{body}\n"


def generate_comparison_index(language: str) -> str:
    entries = []
    for slug, data in list_metadata("comparisons", "comparison.json"):
        title = comparison_title(data, language)
        status = text_value(data, "status", text_value(data, "maturity"))
        verified = text_value(data, "verified_on", text_value(data, "last_verified"))
        entries.append((title.lower(), slug, title, status, verified))
    entries.sort()

    if language == "ru":
        rows = [
            [f"[{title}](comparisons/{slug}/README.ru.md)", status, verified]
            for _, slug, title, status, verified in entries
        ]
        body = markdown_table(["Сравнение", "Статус", "Последняя проверка"], rows)
        return f"# Индекс сравнений\n\n[English version](COMPARISON_INDEX.md)\n\n{body}\n"

    rows = [
        [f"[{title}](comparisons/{slug}/README.md)", status, verified]
        for _, slug, title, status, verified in entries
    ]
    body = markdown_table(["Comparison", "Status", "Last verified"], rows)
    return f"# Comparison Index\n\n[Русская версия](COMPARISON_INDEX.ru.md)\n\n{body}\n"


def generate_needs_index(language: str) -> str:
    entries = []
    for slug, data in list_metadata("needs", "need.json"):
        name = text_value(data, "name_ru" if language == "ru" else "name")
        status = text_value(data, "status")
        verified = text_value(data, "last_verified")
        entries.append((name.lower(), slug, name, status, verified))
    entries.sort()

    if language == "ru":
        rows = [
            [f"[{name}](needs/{slug}/README.ru.md)", status, verified]
            for _, slug, name, status, verified in entries
        ]
        body = markdown_table(["Задача", "Статус", "Последняя проверка"], rows)
        return f"# Индекс задач\n\n[English version](NEEDS_INDEX.md)\n\n{body}\n"

    rows = [
        [f"[{name}](needs/{slug}/README.md)", status, verified]
        for _, slug, name, status, verified in entries
    ]
    body = markdown_table(["Need", "Status", "Last verified"], rows)
    return f"# Needs Index\n\n[Русская версия](NEEDS_INDEX.ru.md)\n\n{body}\n"


def generate_all() -> dict[Path, str]:
    return {
        ROOT / "API_INDEX.md": generate_api_index("en"),
        ROOT / "API_INDEX.ru.md": generate_api_index("ru"),
        ROOT / "COMPARISON_INDEX.md": generate_comparison_index("en"),
        ROOT / "COMPARISON_INDEX.ru.md": generate_comparison_index("ru"),
        ROOT / "NEEDS_INDEX.md": generate_needs_index("en"),
        ROOT / "NEEDS_INDEX.ru.md": generate_needs_index("ru"),
    }


def check_indexes(expected: dict[Path, str]) -> int:
    stale: list[str] = []
    for path, content in expected.items():
        if not path.exists():
            stale.append(f"Missing index: {path.relative_to(ROOT)}")
            continue
        current = path.read_text(encoding="utf-8")
        if current != content:
            stale.append(f"Outdated index: {path.relative_to(ROOT)}")

    for item in stale:
        print(f"ERROR: {item}")
    return 1 if stale else 0


def write_indexes(expected: dict[Path, str]) -> None:
    for path, content in expected.items():
        path.write_text(content, encoding="utf-8")
        print(f"Wrote {path.relative_to(ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check generated indexes without writing files")
    args = parser.parse_args()

    try:
        expected = generate_all()
        if args.check:
            return check_indexes(expected)
        write_indexes(expected)
        return 0
    except IndexGenerationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
