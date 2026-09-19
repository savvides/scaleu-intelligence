import hashlib
import json
from pathlib import Path
import re
import tempfile
import unittest

from scripts.check import check_links, check_migration, check_research, markdown_links


class MigrationNavigationTest(unittest.TestCase):
    def test_schedule_links_name_the_actual_transcript(self):
        root = Path(__file__).resolve().parents[1]
        schedule = root / "conferences/2026-asu-gsv/schedule/full-session-index.md"
        links = re.findall(r"📄 \[([^]]+)\]\(([^)]+)\)", schedule.read_text())
        self.assertTrue(links)
        for label, target in links:
            transcript = (schedule.parent / target).read_text()
            title = re.search(r'^title: "(.*)"$', transcript, re.M).group(1)
            self.assertEqual(label, f"Transcript: {title}")


class LibraryChecksTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        return path

    def test_schedule_links_resolve_from_the_schedule_directory(self):
        self.write("transcripts/session.md", "# Session\n")
        schedule = self.write("schedule/index.md", "[Session](transcripts/session.md)")
        self.assertEqual(len(check_links(self.root, [schedule])), 1)
        schedule.write_text("[Session](../transcripts/session.md)")
        self.assertEqual(check_links(self.root, [schedule]), [])

    def test_links_allow_encoded_paths_and_skip_external_urls(self):
        self.write("two words.md", "# Document")
        page = self.write("README.md", "[File](two%20words.md#heading) [Web](https://example.org/a) [Email](mailto:test@example.org)")
        self.assertEqual(check_links(self.root, [page]), [])

    def test_links_check_reference_definitions_but_ignore_examples(self):
        text = '```md\n[Example](missing.md)\n```\n`[Example](missing.md)`\n[Read][ref]\n[ref]: actual.md\n'
        self.assertEqual(markdown_links(text), ["actual.md"])
        page = self.write("README.md", text)
        self.assertEqual(len(check_links(self.root, [page])), 1)
        self.write("actual.md", "# Actual")
        self.assertEqual(check_links(self.root, [page]), [])

    def test_links_cannot_escape_the_repository(self):
        page = self.write("README.md", "[Outside](../)")
        self.assertEqual(len(check_links(self.root, [page])), 1)

    def test_research_counts_detect_a_missing_entry(self):
        self.write("research/README.md", "| Topic | [topic](topic.md) | 1 |\nTotal: 1 paper entries across 1 topics")
        topic = self.write("research/topic.md", "| # | Title | Takeaway | Type | Year | Citations | DOI |\n")
        self.assertTrue(check_research(self.root))
        topic.write_text(topic.read_text() + "| 1 | Paper | Finding | Trial | 2026 | 1 | 10.0/example |\n")
        self.assertEqual(check_research(self.root), [])
        self.write("research/unindexed.md", "# Unindexed")
        self.assertTrue(check_research(self.root))

    def test_migration_detects_lost_files_and_renamed_restricted_content(self):
        manifest = {"sources": [{"files": [
            {"source": "data/operator-lessons.md", "source_sha256": hashlib.sha256(b"Restricted").hexdigest(), "excluded": "No redistribution"},
            {"source": "data/topic.md", "destination": "guides/topic.md"},
        ]}]}
        self.write("provenance/migration.json", json.dumps(manifest))
        self.assertEqual(len(check_migration(self.root)), 1)
        self.write("guides/topic.md", "# Topic")
        self.assertEqual(check_migration(self.root), [])
        self.write("notes/renamed.md", "Restricted")
        self.assertEqual(len(check_migration(self.root)), 1)


if __name__ == "__main__":
    unittest.main()
