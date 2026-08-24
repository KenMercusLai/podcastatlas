from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "prepare-wiki-content.py"
SPEC = importlib.util.spec_from_file_location("prepare_wiki_topics", SCRIPT)
assert SPEC and SPEC.loader
prepare = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = prepare
SPEC.loader.exec_module(prepare)


class ControlledWikiTopicsTest(unittest.TestCase):
    def test_registry_exposes_exactly_the_six_stable_topic_families(self):
        topics = prepare.load_topics(ROOT / "data" / "wiki_topics.json")

        self.assertEqual(
            ("technology", "economics", "history", "politics", "culture", "science"),
            tuple(topic.key for topic in topics),
        )

    def test_classifies_pages_from_case_insensitive_controlled_tag_families(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            concept_path = root / "TechnologyConcept.md"
            concept_path.write_text(
                "---\ntitle: Technology Concept\ntype: concept\ntags: [AI, infrastructure]\n---\n",
                encoding="utf-8",
            )
            history_path = root / "HistoryEntity.md"
            history_path.write_text(
                "---\ntitle: History Entity\ntype: entity\ntags: [chinese-history]\n---\n",
                encoding="utf-8",
            )
            pages = [
                prepare.WikiPage("TechnologyConcept", "Technology Concept", "concepts", concept_path),
                prepare.WikiPage("HistoryEntity", "History Entity", "entities", history_path),
            ]
            topics = [
                prepare.Topic("technology", "Technology", "Technology description", ("technology", "ai", "infrastructure")),
                prepare.Topic("history", "History", "History description", ("history", "chinese-history")),
            ]

            membership = prepare.classify_topics(pages, topics)

        self.assertEqual(("technology",), membership["TechnologyConcept"])
        self.assertEqual(("history",), membership["HistoryEntity"])

    def test_loads_a_small_registry_and_rejects_ambiguous_tag_aliases(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "topics.json"
            path.write_text(
                '{"topics": ['
                '{"key":"technology","label":"Technology","description":"Technology description","tags":["technology","ai"]},'
                '{"key":"science","label":"Science","description":"Science description","tags":["science","ai"]}'
                ']}'
            )

            with self.assertRaisesRegex(ValueError, "assigned to multiple topics"):
                prepare.load_topics(path)

            path.write_text(
                '{"topics": ['
                '{"key":"technology","label":"Technology","description":"Technology description","tags":["technology","ai"]},'
                '{"key":"science","label":"Science","description":"Science description","tags":["science","biology"]}'
                ']}'
            )
            topics = prepare.load_topics(path)

        self.assertEqual(("technology", "science"), tuple(topic.key for topic in topics))
        self.assertEqual(("technology", "ai"), topics[0].tags)

    def test_generates_topic_pages_grouped_by_knowledge_type_and_reverse_membership(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixtures = (
                ("AIConcept", "AI Concept", "concepts", "[ai]"),
                ("InfrastructureCompany", "Infrastructure Company", "entities", "[infrastructure]"),
                ("ScienceSource", "Science Source", "sources", "[science, technology]"),
            )
            pages = []
            for key, title, section, tags in fixtures:
                path = root / f"{key}.md"
                path.write_text(
                    f"---\ntitle: {title}\ntype: {section[:-1]}\ntags: {tags}\n---\n",
                    encoding="utf-8",
                )
                pages.append(prepare.WikiPage(key, title, section, path))
            topics = [
                prepare.Topic("technology", "Technology", "Technology description", ("technology", "ai", "infrastructure")),
                prepare.Topic("science", "Science", "Science description", ("science",)),
            ]

            generated = prepare.expected_topic_files(pages, topics, topics_dir=root / "topics")
            membership = prepare.make_topic_membership(pages, topics)

        self.assertEqual(
            {root / "topics" / "_index.md", root / "topics" / "technology" / "_index.md", root / "topics" / "science" / "_index.md"},
            set(generated),
        )
        technology_page = generated[root / "topics" / "technology" / "_index.md"]
        self.assertIn("topic_total_pages: 3", technology_page)
        self.assertIn("topic_concepts:", technology_page)
        self.assertIn('key: "AIConcept"', technology_page)
        self.assertIn("topic_entities:", technology_page)
        self.assertIn('key: "InfrastructureCompany"', technology_page)
        self.assertIn("topic_sources:", technology_page)
        self.assertIn('key: "ScienceSource"', technology_page)
        parsed = __import__("json").loads(membership)
        self.assertEqual([{"key": "technology", "label": "Technology", "url": "/topics/technology/"}], parsed["AIConcept"])
        self.assertEqual(["technology", "science"], [item["key"] for item in parsed["ScienceSource"]])

    def test_generated_file_manifest_includes_controlled_topics_and_reverse_membership(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            wiki_dir = root / "content" / "wiki"
            topics_dir = root / "content" / "topics"
            data_dir = root / "data"
            concept = wiki_dir / "concepts" / "AIConcept.md"
            concept.parent.mkdir(parents=True)
            concept.write_text(
                "---\ntitle: AI Concept\ntype: concept\ntags: [ai]\n---\n",
                encoding="utf-8",
            )
            page = prepare.WikiPage("AIConcept", "AI Concept", "concepts", concept)
            topic = prepare.Topic("technology", "Technology", "Technology description", ("ai",))
            with (
                mock.patch.object(prepare, "ROOT", root),
                mock.patch.object(prepare, "WIKI_DIR", wiki_dir),
                mock.patch.object(prepare, "DATA_PATH", data_dir / "wiki_links.json"),
                mock.patch.object(prepare, "TOPIC_MEMBERSHIP_PATH", data_dir / "wiki_topic_membership.json"),
                mock.patch.object(prepare, "TOPICS_DIR", topics_dir),
                mock.patch.object(prepare, "discover_pages", return_value=[page]),
                mock.patch.object(prepare, "load_topics", return_value=[topic]),
                mock.patch.object(prepare, "expected_alphabetical_files", return_value={}),
                mock.patch.object(prepare, "expected_safe_page_files", return_value={}),
            ):
                generated = prepare.expected_generated_files()

        self.assertIn(topics_dir / "_index.md", generated)
        self.assertIn(topics_dir / "technology" / "_index.md", generated)
        self.assertIn(data_dir / "wiki_topic_membership.json", generated)

    def test_finds_only_stale_generator_owned_topic_pages_and_rejects_symlinks(self):
        with tempfile.TemporaryDirectory() as directory:
            topics_dir = Path(directory) / "topics"
            stale = topics_dir / "retired" / "_index.md"
            stale.parent.mkdir(parents=True)
            stale.write_text(prepare.GENERATED_NOTICE, encoding="utf-8")
            manual = topics_dir / "manual" / "_index.md"
            manual.parent.mkdir(parents=True)
            manual.write_text("Manual", encoding="utf-8")

            self.assertEqual(
                [stale],
                prepare.find_stale_topic_files({topics_dir / "_index.md"}, topics_dir=topics_dir),
            )

        with tempfile.TemporaryDirectory() as directory, tempfile.TemporaryDirectory() as outside:
            topics_dir = Path(directory) / "topics"
            topics_dir.mkdir()
            (Path(outside) / "_index.md").write_text(prepare.GENERATED_NOTICE, encoding="utf-8")
            (topics_dir / "escaped").symlink_to(outside, target_is_directory=True)
            with self.assertRaisesRegex(RuntimeError, "symlinked topic"):
                prepare.find_stale_topic_files(set(), topics_dir=topics_dir)

    def test_templates_browse_controlled_topics_without_exposing_raw_tags(self):
        landing = (ROOT / "layouts" / "wiki" / "list.html").read_text()
        single = (ROOT / "layouts" / "_default" / "single.html").read_text()
        topics = (ROOT / "layouts" / "topic" / "list.html").read_text()

        self.assertIn('.Site.GetPage "/topics"', landing)
        self.assertIn(".Params.topic_pages", landing)
        self.assertNotIn(".Site.Taxonomies.tags", landing)
        self.assertIn("wiki_topic_membership", single)
        self.assertIn("Topics:", single)
        self.assertNotIn('.GetTerms "tags"', single)
        for label in ("Concepts", "Entities", "Source Notes"):
            self.assertIn(label, topics)
        self.assertIn("relURL", topics)

    def test_hugo_preserves_but_hides_the_raw_tag_taxonomy(self):
        config = (ROOT / "hugo.toml").read_text()
        base = (ROOT / "layouts" / "_default" / "baseof.html").read_text()
        terms = (ROOT / "layouts" / "_default" / "terms.html").read_text()
        taxonomy = (ROOT / "layouts" / "_default" / "taxonomy.html").read_text()
        sitemap = (ROOT / "layouts" / "_default" / "sitemap.xml").read_text()

        self.assertIn("tag = 'tags'", config)
        self.assertIn("legacy-tag-page", terms)
        self.assertIn("legacy-tag-page", taxonomy)
        self.assertIn('content="noindex, follow"', base)
        self.assertIn('data-pagefind-ignore="all"', base)
        self.assertIn('.Data.Plural "tags"', sitemap)


if __name__ == "__main__":
    unittest.main()
