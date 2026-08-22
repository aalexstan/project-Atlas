#!/usr/bin/env python3
"""Report active Atlas materials whose evidence review is due."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class ReviewItem:
    kind: str
    item_id: str
    path: Path
    verified_on: dt.date
    due_on: dt.date
    status: str


def parse_date(value: object, path: Path) -> dt.date:
    if not isinstance(value, str):
        raise ValueError(f"Missing review date in {path.relative_to(ROOT)}")
    try:
        return dt.date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"Invalid review date in {path.relative_to(ROOT)}: {value}") from exc


def load_items(root: Path, as_of: dt.date) -> list[ReviewItem]:
    definitions = (
        ("api", "apis", "api.json", "last_verified", 180),
        ("comparison", "comparisons", "comparison.json", "verified_on", 180),
        ("need", "needs", "need.json", "last_verified", 180),
    )
    items: list[ReviewItem] = []
    for kind, base, filename, date_field, interval in definitions:
        for path in sorted((root / base).glob(f"*/{filename}")):
            data = json.loads(path.read_text(encoding="utf-8"))
            verified = parse_date(data.get(date_field), path)
            maturity = data.get("maturity")
            days = 90 if maturity == "gold" else interval
            due_on = verified + dt.timedelta(days=days)
            declared = str(data.get("status", ""))
            if declared == "needs_recheck":
                state = "needs_recheck"
            elif as_of > due_on:
                state = "overdue"
            elif as_of == due_on:
                state = "due"
            else:
                state = "on_schedule"
            items.append(ReviewItem(kind, str(data.get("id", path.parent.name)), path, verified, due_on, state))
    return items


def render_report(items: list[ReviewItem], as_of: dt.date) -> str:
    attention = [item for item in items if item.status != "on_schedule"]
    lines = [
        "# Atlas Review Due Report",
        "",
        f"As of {as_of.isoformat()}: {len(attention)} of {len(items)} active material(s) require attention.",
        "",
        "| State | Kind | ID | Last verified | Target date |",
        "|---|---|---|---|---|",
    ]
    for item in sorted(attention, key=lambda value: (value.status, value.due_on, value.item_id)):
        lines.append(
            f"| {item.status} | {item.kind} | {item.item_id} | {item.verified_on.isoformat()} | {item.due_on.isoformat()} |"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of", type=dt.date.fromisoformat, default=dt.date.today())
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    try:
        items = load_items(ROOT, args.as_of)
    except (ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    report = render_report(items, args.as_of)
    print(report, end="")
    if args.report:
        args.report.write_text(report, encoding="utf-8")
    return 2 if any(item.status != "on_schedule" for item in items) else 0


if __name__ == "__main__":
    sys.exit(main())
