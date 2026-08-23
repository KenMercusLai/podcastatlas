from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "prepare-wiki-content.py"
SPEC = importlib.util.spec_from_file_location("prepare_wiki_content", SCRIPT)
assert SPEC and SPEC.loader
prepare = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = prepare
SPEC.loader.exec_module(prepare)


class AlphabeticalBucketTest(unittest.TestCase):
    def test_uses_first_supported_number_or_letter_after_leading_symbols(self):
        self.assertEqual("0-9", prepare.ALPHABETICAL_BUCKETS[0])
        self.assertNotIn("#", prepare.ALPHABETICAL_BUCKETS)
        self.assertEqual("a", prepare.alphabetical_bucket("% Arabica"))
        self.assertEqual("a", prepare.alphabetical_bucket("™ Arabica"))
        self.assertEqual("e", prepare.alphabetical_bucket("% Éclair"))
        self.assertEqual("a", prepare.alphabetical_bucket("#AI"))
        self.assertEqual("o", prepare.alphabetical_bucket("_OpenAI"))
        self.assertEqual("r", prepare.alphabetical_bucket("🤖Robotics"))
        self.assertEqual("0-9", prepare.alphabetical_bucket("#401KPlan"))
        self.assertEqual("0-9", prepare.alphabetical_bucket("401KPlan"))
        self.assertEqual("o", prepare.alphabetical_bucket("OuyangXiu"))
        self.assertEqual("w", prepare.alphabetical_bucket("WangXing"))
        self.assertEqual("w", prepare.alphabetical_bucket("王兴"))
        self.assertEqual("o", prepare.alphabetical_bucket("欧阳修"))
        self.assertEqual("z", prepare.alphabetical_bucket("张良"))
        self.assertEqual("a", prepare.alphabetical_bucket("澳大利亚"))
        self.assertEqual("r", prepare.alphabetical_bucket("弱人工智能"))
        self.assertEqual("s", prepare.alphabetical_bucket("所有权"))
        self.assertEqual("j", prepare.alphabetical_bucket("！警告"))
        with self.assertRaisesRegex(ValueError, "digit or letter"):
            prepare.alphabetical_bucket("%_🤖")

    def test_generated_synthesis_is_excluded_from_canonical_link_scan(self):
        generated = prepare.WIKI_DIR / "_generated" / "synthesis" / "current.md"
        canonical = prepare.WIKI_DIR / "concepts" / "Current.md"

        self.assertTrue(prepare.skip_link_scan(generated))
        self.assertFalse(prepare.skip_link_scan(canonical))

    def test_discovers_symbol_leading_pages_but_not_generated_section_indexes(self):
        self.assertTrue(prepare.is_canonical_page_path(Path("_OpenAI.md")))
        self.assertTrue(prepare.is_canonical_page_path(Path("#AI.md")))
        self.assertTrue(prepare.is_canonical_page_path(Path(".Hidden.md")))
        self.assertFalse(prepare.is_canonical_page_path(Path("_index.md")))

    def test_groups_by_canonical_key_instead_of_display_title(self):
        pages = [
            prepare.WikiPage("WangXing", "王兴", "entities", Path("WangXing.md")),
            prepare.WikiPage("王兴", "Wang Xing", "entities", Path("王兴.md")),
            prepare.WikiPage("% Arabica", "% Arabica", "entities", Path("% Arabica.md")),
            prepare.WikiPage("401KPlan", "退休计划", "entities", Path("401KPlan.md")),
            prepare.WikiPage("Alpha", "Zulu", "concepts", Path("Alpha.md")),
        ]

        groups = prepare.group_alphabetical_pages(pages, "entities")

        self.assertEqual(["% Arabica"], [page.key for page in groups["a"]])
        self.assertEqual(["401KPlan"], [page.key for page in groups["0-9"]])
        self.assertEqual({"WangXing", "王兴"}, {page.key for page in groups["w"]})

    def test_generates_only_number_and_letter_routes_with_a_as_default(self):
        pages = [
            prepare.WikiPage("WangXing", "王兴", "entities", Path("WangXing.md")),
            prepare.WikiPage("王兴", "Wang Xing", "entities", Path("王兴.md")),
            prepare.WikiPage("% Arabica", "% Arabica", "entities", Path("% Arabica.md")),
            prepare.WikiPage("401KPlan", "退休计划", "entities", Path("401KPlan.md")),
            prepare.WikiPage("Alpha", "Alpha concept", "concepts", Path("Alpha.md")),
        ]

        generated = prepare.expected_alphabetical_files(pages)

        expected_entity_paths = {
            prepare.WIKI_DIR / "entities" / "_index.md",
            prepare.WIKI_DIR / "entities" / "by-letter" / "_index.md",
            *(
                prepare.WIKI_DIR
                / "entities"
                / "by-letter"
                / prepare.alphabetical_bucket_slug(bucket)
                / "_index.md"
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
        self.assertIn('url: "/wiki/entities/%E7%8E%8B%E5%85%B4/"', w_page)
        self.assertNotIn('key: "401KPlan"', w_page)

        symbols_path = (
            prepare.WIKI_DIR / "entities" / "by-letter" / "symbols" / "_index.md"
        )
        self.assertNotIn(symbols_path, generated)
        a_page = generated[
            prepare.WIKI_DIR / "entities" / "by-letter" / "a" / "_index.md"
        ]
        self.assertIn('wiki_letter: "a"', a_page)
        self.assertIn('key: "% Arabica"', a_page)
        safe_slug = prepare.safe_page_slug("% Arabica")
        self.assertIn(
            f'url: "/wiki/entities/by-key/{safe_slug}/"',
            a_page,
        )
        self.assertNotIn('key: "401KPlan"', a_page)

        numeric_page = generated[
            prepare.WIKI_DIR / "entities" / "by-letter" / "0-9" / "_index.md"
        ]
        self.assertIn('key: "401KPlan"', numeric_page)
        self.assertNotIn('key: "WangXing"', numeric_page)

    def test_generates_a_safe_derived_page_for_every_symbol_leading_key(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            for key in ("#AI", "_OpenAI", ".Hidden", "!Bang", "🤖Bot", "！警告"):
                source = Path(temp_dir) / f"{key}.md"
                source.write_text(
                    "---\ntitle: Symbol\n---\n\nBody.\n",
                    encoding="utf-8",
                )
                page = prepare.WikiPage(key, "Symbol", "entities", source)

                generated = prepare.expected_safe_page_files([page])

                path = (
                    prepare.WIKI_DIR
                    / "entities"
                    / "by-key"
                    / prepare.safe_page_slug(key)
                    / "index.md"
                )
                self.assertEqual([path], list(generated))
                self.assertIn("Body.", generated[path])
                self.assertIn(prepare.GENERATED_NOTICE, generated[path])
                self.assertEqual(
                    f"/wiki/entities/by-key/{prepare.safe_page_slug(key)}/",
                    prepare.page_url(page),
                )
    def test_generated_safe_pages_are_excluded_from_wiki_link_scans(self):
        proxy = (
            prepare.WIKI_DIR
            / "entities"
            / "by-key"
            / "symbol-route"
            / "index.md"
        )
        canonical = prepare.WIKI_DIR / "entities" / "Alpha.md"

        self.assertTrue(prepare.skip_link_scan(proxy))
        self.assertFalse(prepare.skip_link_scan(canonical))

    def test_generated_safe_pages_do_not_double_count_or_report_stale_links(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            wiki_dir = root / "content" / "wiki"
            entities = wiki_dir / "entities"
            entities.mkdir(parents=True)
            symbol_path = entities / "!One.md"
            symbol_path.write_text("---\ntitle: One\n---\n\n[[Target]]\n", encoding="utf-8")
            target_path = entities / "Target.md"
            target_path.write_text("---\ntitle: Target\n---\n", encoding="utf-8")
            symbol = prepare.WikiPage("!One", "One", "entities", symbol_path)
            target = prepare.WikiPage("Target", "Target", "entities", target_path)

            with (
                mock.patch.object(prepare, "ROOT", root),
                mock.patch.object(prepare, "WIKI_DIR", wiki_dir),
            ):
                generated = prepare.expected_safe_page_files([symbol, target])
                for path, content in generated.items():
                    path.parent.mkdir(parents=True)
                    path.write_text(content, encoding="utf-8")

                total, missing = prepare.scan_wiki_links(
                    {"!One": symbol, "Target": target}
                )
                self.assertEqual(1, total)
                self.assertEqual({}, missing)

                symbol_path.unlink()
                target_path.unlink()
                total, missing = prepare.scan_wiki_links({})
                self.assertEqual(0, total)
                self.assertEqual({}, missing)

    def test_safe_route_collisions_fail_closed_instead_of_overwriting(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            pages = []
            for key in ("!One", "@Two"):
                source = root / f"{key}.md"
                source.write_text("---\ntitle: Symbol\n---\n", encoding="utf-8")
                pages.append(prepare.WikiPage(key, "Symbol", "entities", source))

            with mock.patch.object(prepare, "safe_page_slug", return_value="collision"):
                with self.assertRaisesRegex(ValueError, "safe route collision"):
                    prepare.expected_safe_page_files(pages)

    def test_detects_casefolded_keys_within_the_same_section(self):
        pages = [
            prepare.WikiPage("LibLib", "LibLib", "entities", Path("LibLib.md")),
            prepare.WikiPage("Liblib", "Liblib", "entities", Path("Liblib.md")),
        ]

        collisions = prepare.casefolded_key_collisions(pages)

        self.assertEqual({("entities", "liblib")}, set(collisions))
        self.assertEqual(
            {"LibLib", "Liblib"},
            {page.key for page in collisions[("entities", "liblib")]},
        )

    def test_detects_casefolded_tracked_paths_before_checkout_can_collapse_them(self):
        paths = [
            Path("content/wiki/entities/LibLib.md"),
            Path("content/wiki/entities/Liblib.md"),
            Path("content/wiki/entities/Other.md"),
        ]

        collisions = prepare.casefolded_path_collisions(paths)

        self.assertEqual(
            {"content/wiki/entities/liblib.md"},
            set(collisions),
        )
        self.assertEqual(
            {
                Path("content/wiki/entities/LibLib.md"),
                Path("content/wiki/entities/Liblib.md"),
            },
            set(collisions["content/wiki/entities/liblib.md"]),
        )

    def test_detects_pages_that_publish_to_the_same_route(self):
        pages = [
            prepare.WikiPage(
                "MidJourney", "MidJourney", "entities", Path("MidJourney.md")
            ),
            prepare.WikiPage(
                "Midjourney", "Midjourney", "entities", Path("Midjourney.md")
            ),
        ]

        collisions = prepare.public_route_collisions(pages)

        self.assertEqual({"/wiki/entities/midjourney/"}, set(collisions))
        self.assertEqual(
            {"MidJourney", "Midjourney"},
            {
                page.key
                for page in collisions["/wiki/entities/midjourney/"]
            },
        )

    def test_run_fails_closed_when_canonical_pages_share_a_public_route(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            wiki_dir = root / "content" / "wiki"
            entities = wiki_dir / "entities"
            episodes = root / "content" / "episodes"
            entities.mkdir(parents=True)
            episodes.mkdir(parents=True)
            pages = [
                prepare.WikiPage(
                    "MidJourney", "MidJourney", "entities", entities / "MidJourney.md"
                ),
                prepare.WikiPage(
                    "Midjourney", "Midjourney", "entities", entities / "Midjourney.md"
                ),
            ]

            with (
                mock.patch.object(prepare, "ROOT", root),
                mock.patch.object(prepare, "WIKI_DIR", wiki_dir),
                mock.patch.object(prepare, "EPISODES_DIR", episodes),
                mock.patch.object(prepare, "DATA_PATH", root / "data" / "wiki_links.json"),
                mock.patch.object(prepare, "STATS_PATH", wiki_dir / "stats.md"),
                mock.patch.object(prepare, "discover_pages", return_value=pages),
                mock.patch.object(
                    prepare, "tracked_wiki_path_collisions", return_value={}
                ),
                mock.patch.object(prepare, "find_stale_safe_page_files", return_value=[]),
                mock.patch.object(
                    prepare, "find_stale_alphabetical_files", return_value=[]
                ),
                mock.patch.object(prepare, "write_if_changed", return_value=False),
            ):
                self.assertEqual(1, prepare.run(check=False))

    def test_run_stops_before_generation_when_tracked_paths_case_collide(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            wiki_dir = root / "content" / "wiki"
            wiki_dir.mkdir(parents=True)
            collisions = {
                "content/wiki/entities/liblib.md": [
                    Path("content/wiki/entities/LibLib.md"),
                    Path("content/wiki/entities/Liblib.md"),
                ]
            }

            with (
                mock.patch.object(prepare, "ROOT", root),
                mock.patch.object(prepare, "WIKI_DIR", wiki_dir),
                mock.patch.object(prepare, "discover_pages", return_value=[]),
                mock.patch.object(
                    prepare, "tracked_wiki_path_collisions", return_value=collisions
                ),
                mock.patch.object(prepare, "expected_generated_files") as generate,
            ):
                self.assertEqual(1, prepare.run(check=False))
                generate.assert_not_called()

    def test_finds_only_stale_generated_safe_pages(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            wiki_dir = Path(temp_dir)
            stale = wiki_dir / "entities" / "by-key" / "stale" / "index.md"
            stale.parent.mkdir(parents=True)
            stale.write_text(f"Body.\n\n{prepare.GENERATED_NOTICE}\n")
            manual = wiki_dir / "entities" / "by-key" / "manual" / "index.md"
            manual.parent.mkdir(parents=True)
            manual.write_text("Manual page.\n")

            found = prepare.find_stale_safe_page_files(set(), wiki_dir=wiki_dir)

            self.assertEqual([stale], found)

    def test_finds_obsolete_generated_symbol_indexes_but_preserves_manual_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            wiki_dir = Path(temp_dir)
            stale = wiki_dir / "entities" / "by-letter" / "symbols" / "_index.md"
            stale.parent.mkdir(parents=True)
            stale.write_text(f"Body.\n\n{prepare.GENERATED_NOTICE}\n")
            manual = wiki_dir / "concepts" / "by-letter" / "symbols" / "_index.md"
            manual.parent.mkdir(parents=True)
            manual.write_text("Manual page.\n")

            found = prepare.find_stale_alphabetical_files(set(), wiki_dir=wiki_dir)

            self.assertEqual([stale], found)

    def test_rejects_a_symlinked_alphabetical_bucket_before_stale_cleanup(self):
        with tempfile.TemporaryDirectory() as temp_dir, tempfile.TemporaryDirectory() as outside_dir:
            wiki_dir = Path(temp_dir)
            outside = Path(outside_dir) / "_index.md"
            outside.write_text(f"Body.\n\n{prepare.GENERATED_NOTICE}\n")
            bucket = wiki_dir / "entities" / "by-letter" / "symbols"
            bucket.parent.mkdir(parents=True)
            bucket.symlink_to(Path(outside_dir), target_is_directory=True)

            with self.assertRaisesRegex(RuntimeError, "symlinked alphabetical"):
                prepare.find_stale_alphabetical_files(set(), wiki_dir=wiki_dir)

            self.assertTrue(outside.exists())

    def test_writes_an_explicit_empty_list_for_a_bucket_without_pages(self):
        content = prepare.alphabetical_index("entities", "z", [], 0)

        self.assertIn("wiki_pages: []", content)
        self.assertNotIn("wiki_pages:\n---", content)


if __name__ == "__main__":
    unittest.main()
