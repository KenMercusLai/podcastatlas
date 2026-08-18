from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "prepare-wiki-content.py"
SPEC = importlib.util.spec_from_file_location("prepare_wiki_content", SCRIPT)
assert SPEC and SPEC.loader
prepare = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = prepare
SPEC.loader.exec_module(prepare)


class AlphabeticalBucketTest(unittest.TestCase):
    def test_uses_canonical_key_for_zero_to_nine_and_a_to_z_buckets(self):
        self.assertEqual("0-9", prepare.alphabetical_bucket("401KPlan"))
        self.assertEqual("o", prepare.alphabetical_bucket("OuyangXiu"))
        self.assertEqual("w", prepare.alphabetical_bucket("WangXing"))
        with self.assertRaisesRegex(ValueError, "Unsupported canonical wiki key"):
            prepare.alphabetical_bucket("王兴")

    def test_groups_by_canonical_key_instead_of_display_title(self):
        pages = [
            prepare.WikiPage("WangXing", "王兴", "entities", Path("WangXing.md")),
            prepare.WikiPage("401KPlan", "退休计划", "entities", Path("401KPlan.md")),
            prepare.WikiPage("Alpha", "Zulu", "concepts", Path("Alpha.md")),
        ]

        groups = prepare.group_alphabetical_pages(pages, "entities")

        self.assertEqual(["401KPlan"], [page.key for page in groups["0-9"]])
        self.assertEqual(["WangXing"], [page.key for page in groups["w"]])
        self.assertEqual([], groups["a"])

    def test_generates_static_zero_to_nine_and_a_to_z_routes_with_a_as_default(self):
        pages = [
            prepare.WikiPage("WangXing", "王兴", "entities", Path("WangXing.md")),
            prepare.WikiPage("401KPlan", "退休计划", "entities", Path("401KPlan.md")),
            prepare.WikiPage("Alpha", "Alpha concept", "concepts", Path("Alpha.md")),
        ]

        generated = prepare.expected_alphabetical_files(pages)

        expected_entity_paths = {
            prepare.WIKI_DIR / "entities" / "_index.md",
            prepare.WIKI_DIR / "entities" / "by-letter" / "_index.md",
            *(
                prepare.WIKI_DIR / "entities" / "by-letter" / bucket / "_index.md"
                for bucket in prepare.ALPHABETICAL_BUCKETS
            ),
        }
        self.assertTrue(expected_entity_paths.issubset(generated))
        self.assertEqual(58, len(generated))

        default_page = generated[prepare.WIKI_DIR / "entities" / "_index.md"]
        self.assertIn('wiki_letter: "a"', default_page)
        self.assertNotIn('key: "WangXing"', default_page)

        w_page = generated[prepare.WIKI_DIR / "entities" / "by-letter" / "w" / "_index.md"]
        self.assertIn('wiki_letter: "w"', w_page)
        self.assertIn('key: "WangXing"', w_page)
        self.assertIn('url: "/wiki/entities/wangxing/"', w_page)
        self.assertNotIn('key: "401KPlan"', w_page)

        numeric_page = generated[
            prepare.WIKI_DIR / "entities" / "by-letter" / "0-9" / "_index.md"
        ]
        self.assertIn('key: "401KPlan"', numeric_page)
        self.assertNotIn('key: "WangXing"', numeric_page)

    def test_writes_an_explicit_empty_list_for_a_bucket_without_pages(self):
        content = prepare.alphabetical_index("entities", "z", [], 0)

        self.assertIn("wiki_pages: []", content)
        self.assertNotIn("wiki_pages:\n---", content)


if __name__ == "__main__":
    unittest.main()
