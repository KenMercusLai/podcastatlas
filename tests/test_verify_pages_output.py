import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "verify-pages-output.py"


def load_verifier():
    spec = importlib.util.spec_from_file_location("verify_pages_output", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write(path, content=""):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


class VerifyPagesOutputTest(unittest.TestCase):
    def test_accepts_the_expected_site_output(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            expected_paths = [
                "index.html",
                "episodes/index.html",
                "tags/index.html",
                "shows/index.html",
                "wiki/index.html",
                "search/index.html",
                "episodes/example/index.html",
                "episodes/example.md",
                "episodes/episode.160/index.html",
                "episodes/episode.160.md",
                "pagefind/pagefind.js",
                "pagefind/pagefind-component-ui.js",
                "pagefind/pagefind-component-ui.css",
                "pagefind/pagefind.en-us.pf_meta",
                "pagefind/index/en-us_example.pf_index",
                "pagefind/fragment/en-us_example.pf_fragment",
            ]
            for relative in expected_paths:
                write(public / relative, "content")
            write(
                public / "index.html",
                '<h1>Podcast Atlas</h1><p>A living knowledge atlas synthesized from podcasts.</p>',
            )
            write(public / "index.xml", "<rss />")
            write(public / "episodes/index.xml", "<rss />")
            write(public / "sitemap.xml", "<urlset />")

            report = verifier.validate(public)

        self.assertEqual([], report["errors"])
        self.assertEqual(len(expected_paths) + 3, report["file_count"])

    def test_rejects_nested_episode_markdown_output(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            write(public / "episodes" / "example" / "index.html", "content")
            write(public / "episodes" / "example" / "index.md", "content")

            report = verifier.validate(public)

        self.assertIn(
            "nested episode Markdown URL is forbidden: episodes/example/index.md",
            report["errors"],
        )

    def test_rejects_missing_pagefind_output(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            report = verifier.validate(Path(directory))

        self.assertIn("missing required file: search/index.html", report["errors"])
        self.assertIn("missing required file: pagefind/pagefind.js", report["errors"])
        self.assertIn(
            "missing required file: pagefind/pagefind-component-ui.js",
            report["errors"],
        )
        self.assertIn("missing Pagefind metadata index", report["errors"])
        self.assertIn("missing Pagefind search index", report["errors"])
        self.assertIn("missing Pagefind result fragments", report["errors"])
        self.assertIn("missing required file: index.html", report["errors"])

    def test_rejects_the_old_redirecting_homepage(self):
        verifier = load_verifier()
        redirect_tags = (
            '<meta http-equiv="refresh" content="0; url=/episodes/">',
            '<meta http-equiv=refresh content="0;url=/episodes/">',
            '<meta http-equiv = "refresh" content="0; url=/episodes/">',
        )

        for redirect_tag in redirect_tags:
            with self.subTest(redirect_tag=redirect_tag):
                with tempfile.TemporaryDirectory() as directory:
                    public = Path(directory)
                    write(public / "index.html", redirect_tag)

                    report = verifier.validate(public)

                self.assertIn("homepage is still an automatic redirect", report["errors"])

    def test_rejects_taxonomy_rss(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            write(public / "tags" / "example" / "index.xml", "<rss />")

            report = verifier.validate(public)

        self.assertIn(
            "forbidden taxonomy RSS: tags/example/index.xml",
            report["errors"],
        )

    def test_rejects_unresolved_wiki_links(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            write(
                public / "wiki" / "overview" / "index.html",
                "<p>Episode on [[LifeSettlement|life settlements]].</p>",
            )

            report = verifier.validate(public)

        self.assertIn(
            "unresolved wiki link in generated HTML: "
            "wiki/overview/index.html: [[LifeSettlement|life settlements]]",
            report["errors"],
        )

    def test_rejects_symbolic_links(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            write(public / "target.txt", "content")
            (public / "linked.txt").symlink_to(public / "target.txt")

            report = verifier.validate(public)

        self.assertIn("symbolic link not allowed: linked.txt", report["errors"])

    def test_rejects_artifacts_larger_than_one_gibibyte(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            oversized = public / "oversized.bin"
            with oversized.open("wb") as output:
                output.truncate((1024 ** 3) + 1)

            report = verifier.validate(public)

        self.assertIn(
            "artifact exceeds the GitHub Pages 1 GiB supported limit",
            report["errors"],
        )


if __name__ == "__main__":
    unittest.main()
