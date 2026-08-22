from __future__ import annotations

import datetime as dt
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_review_due  # noqa: E402
import check_sources  # noqa: E402


class SourceMonitoringTests(unittest.TestCase):
    def test_response_marker_detects_change(self) -> None:
        source = check_sources.Source("https://example.test", ("demo",), required_markers=("API docs",))
        result = check_sources.evaluate_response(source, 200, b"renamed product")
        self.assertEqual(result.status, "changed")

    def test_restricted_source_is_not_broken(self) -> None:
        source = check_sources.Source("https://example.test", ("demo",))
        result = check_sources.evaluate_response(source, 403, b"")
        self.assertEqual(result.status, "restricted")
        self.assertIn(result.status, check_sources.ATTENTION_STATUSES)

    def test_unicode_url_is_percent_encoded(self) -> None:
        encoded = check_sources.network_url("https://example.test/документы?name=тариф")
        self.assertNotIn("документы", encoded)
        self.assertIn("%D0", encoded)

    def test_report_omits_success_rows(self) -> None:
        source = check_sources.Source("https://example.test", ("demo",))
        report = check_sources.render_report([check_sources.Result(source, "ok", "HTTP 200")])
        self.assertIn("ok: 1", report)
        self.assertNotIn("https://example.test", report)

    def test_collects_external_api_sources_only(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            profile = root / "apis" / "demo"
            profile.mkdir(parents=True)
            (profile / "api.json").write_text(
                json.dumps({"id": "demo", "sources": ["https://example.test/docs", "research/demo.md"]}),
                encoding="utf-8",
            )
            sources = check_sources.collect_sources(root, {})
            self.assertEqual([item.url for item in sources], ["https://example.test/docs"])

    def test_review_due_and_needs_recheck(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            profile = root / "apis" / "demo"
            profile.mkdir(parents=True)
            (profile / "api.json").write_text(
                json.dumps({"id": "demo", "last_verified": "2026-01-01", "status": "needs_recheck"}),
                encoding="utf-8",
            )
            items = check_review_due.load_items(root, dt.date(2026, 1, 2))
            self.assertEqual(items[0].status, "needs_recheck")

    def test_api_review_uses_ninety_day_interval(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            profile = root / "apis" / "demo"
            profile.mkdir(parents=True)
            (profile / "api.json").write_text(
                json.dumps({"id": "demo", "last_verified": "2026-01-01", "status": "active"}),
                encoding="utf-8",
            )
            items = check_review_due.load_items(root, dt.date(2026, 4, 2))
            self.assertEqual(items[0].due_on, dt.date(2026, 4, 1))
            self.assertEqual(items[0].status, "overdue")

    def test_explicit_review_date_takes_precedence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            comparison = root / "comparisons" / "demo"
            comparison.mkdir(parents=True)
            (comparison / "comparison.json").write_text(
                json.dumps(
                    {
                        "id": "demo",
                        "verified_on": "2026-01-01",
                        "next_review": {"full": "2026-02-01", "blocked": "credentials_required"},
                    }
                ),
                encoding="utf-8",
            )
            items = check_review_due.load_items(root, dt.date(2026, 2, 1))
            self.assertEqual(items[0].due_on, dt.date(2026, 2, 1))
            self.assertEqual(items[0].status, "due")


if __name__ == "__main__":
    unittest.main()
