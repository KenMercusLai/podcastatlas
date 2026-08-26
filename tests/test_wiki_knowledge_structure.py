from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "prepare-wiki-content.py"
VERIFIER = ROOT / "scripts" / "verify-pages-output.py"
SINGLE = ROOT / "layouts" / "_default" / "single.html"
SOURCES_PARTIAL = ROOT / "layouts" / "partials" / "wiki-knowledge-sources.html"


def load_script():
    spec = importlib.util.spec_from_file_location("prepare_wiki_content_knowledge", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load_verifier():
    spec = importlib.util.spec_from_file_location("verify_pages_output_knowledge", VERIFIER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class WikiKnowledgeStructureTest(unittest.TestCase):
    def fixture(self, root: Path):
        module = load_script()
        wiki = root / "content" / "wiki"
        episodes = root / "content" / "episodes"
        concept = wiki / "concepts" / "Example.md"
        source_a = wiki / "sources" / "source-a.md"
        source_b = wiki / "sources" / "source-b.md"
        write(
            concept,
            "---\ntitle: Example\ntype: concept\nknowledge_schema: synthesis-v1\n"
            "sources:\n  - source-a\n  - source-b\nlast_updated: 2026-08-26\n---\n",
        )
        write(
            source_a,
            "---\ntitle: Source A\ntype: source\nsource_file: raw/episode-a.md\n---\n",
        )
        write(
            source_b,
            "---\ntitle: Source B\ntype: source\nsource_file: raw/episode-b.md\n---\n",
        )
        write(
            episodes / "episode-a.md",
            "+++\ntitle = 'Episode A'\nshow = 'Show One'\n+++\n",
        )
        write(
            episodes / "episode-b.md",
            "+++\ntitle = 'Episode B'\nshow = 'Show Two'\n+++\n",
        )
        pages = [
            module.WikiPage("Example", "Example", "concepts", concept),
            module.WikiPage("source-a", "Source A", "sources", source_a),
            module.WikiPage("source-b", "Source B", "sources", source_b),
        ]
        return module, pages, episodes, source_b

    def test_projection_derives_complete_counts_shows_and_source_links(self):
        with tempfile.TemporaryDirectory() as directory:
            module, pages, episodes, _ = self.fixture(Path(directory))
            payload = json.loads(module.make_knowledge_signals(pages, episodes_dir=episodes))

        self.assertEqual(1, payload["version"])
        signal = payload["pages"]["Example"]
        self.assertEqual("2026-08-26", signal["updated"])
        self.assertEqual(2, signal["source_note_count"])
        self.assertEqual(2, signal["episode_count"])
        self.assertEqual(2, signal["show_count"])
        self.assertEqual(["source-a", "source-b"], [item["key"] for item in signal["sources"]])
        self.assertEqual(["Source A", "Source B"], [item["title"] for item in signal["sources"]])
        self.assertEqual(["Show One", "Show Two"], [item["show"] for item in signal["sources"]])
        self.assertEqual(
            ["/wiki/sources/source-a/", "/wiki/sources/source-b/"],
            [item["url"] for item in signal["sources"]],
        )

    def test_projection_fails_closed_for_missing_source_or_episode_mapping(self):
        with tempfile.TemporaryDirectory() as directory:
            module, pages, episodes, source_b = self.fixture(Path(directory))
            source_b.unlink()
            pages = [page for page in pages if page.key != "source-b"]
            with self.assertRaisesRegex(ValueError, "unknown source note source-b"):
                module.make_knowledge_signals(pages, episodes_dir=episodes)

    def test_artifact_verifier_checks_signal_counts_and_complete_source_inventory(self):
        verifier = load_verifier()
        payload = {
            "version": 1,
            "pages": {
                "Example": {
                    "updated": "2026-08-26",
                    "source_note_count": 2,
                    "episode_count": 2,
                    "show_count": 2,
                    "sources": [
                        {"key": "source-a", "url": "/wiki/sources/source-a/"},
                        {"key": "source-b", "url": "/wiki/sources/source-b/"},
                    ],
                    "url": "/wiki/concepts/example/",
                }
            },
        }
        body = (
            "<p class=wiki-knowledge-signals data-knowledge-schema=synthesis-v1 "
            "data-episode-count=2 data-show-count=2 data-source-count=2>"
            "<time datetime=2026-08-26>2026-08-26</time></p>"
            "<section class=wiki-knowledge-sources data-source-count=2>"
            "<li data-source-key=source-a><a href=/project/wiki/sources/source-a/>A</a></li>"
            "<li data-source-key=source-b><a href=/project/wiki/sources/source-b/>B</a></li>"
            "</section>"
        )
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            write(public / "wiki" / "concepts" / "example" / "index.html", body)
            errors: list[str] = []
            verifier.validate_knowledge_pages(public, payload, errors)
            self.assertEqual([], errors)

            write(
                public / "wiki" / "concepts" / "example" / "index.html",
                body.replace("<li data-source-key=source-b><a href=/project/wiki/sources/source-b/>B</a></li>", ""),
            )
            errors = []
            verifier.validate_knowledge_pages(public, payload, errors)
            self.assertIn("structured Wiki page Example source inventory is incomplete", errors)

    def test_structured_layout_renders_signals_and_all_sources_with_relurl(self):
        single = SINGLE.read_text(encoding="utf-8")
        sources = SOURCES_PARTIAL.read_text(encoding="utf-8")
        self.assertIn('eq .Params.knowledge_schema "synthesis-v1"', single)
        self.assertIn("wiki-knowledge-signals", single)
        self.assertIn('partial "wiki-knowledge-sources.html"', single)
        self.assertIn("data-source-count", sources)
        self.assertIn("range .sources", sources)
        self.assertIn("relURL", sources)
        self.assertIn("<details", sources)


if __name__ == "__main__":
    unittest.main()
