import importlib.util
import json
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


def episode_list_body(slugs, dates=None):
    if dates is None:
        dates = ["2026-01-01"] * len(slugs)
    items = "".join(
        f'<li><a href="/episodes/{slug}/">Episode {slug}</a>'
        f'{f"<time datetime={date}>{date}</time>" if date else ""}</li>'
        for slug, date in zip(slugs, dates)
    )
    return f'<ul class="episode-list">{items}</ul>'


def valid_html(url, body=""):
    payload = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "WebPage",
            "name": "Example | Podcast Atlas",
            "url": url,
            "description": "Example description",
        }
    )
    return (
        "<html><head>"
        f'<link rel="canonical" href="{url}">'
        '<meta name="description" content="Example description">'
        '<meta property="og:title" content="Example | Podcast Atlas">'
        f'<meta property="og:url" content="{url}">'
        '<meta property="og:image" content="https://example.com/social.png">'
        '<meta name="twitter:card" content="summary_large_image">'
        f'<script type="application/ld+json">{payload}</script>'
        f"</head><body>{body}</body></html>"
    )


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
                "about/index.html",
                "about/index.md",
                "methodology/index.html",
                "methodology/index.md",
                "robots.txt",
                "images/podcast-atlas-social.png",
                "episodes/example/index.html",
                "episodes/example.md",
                "episodes/episode.160/index.html",
                "episodes/episode.160.md",
                "episodes/中文标题/index.html",
                "episodes/中文标题.md",
                "pagefind/pagefind.js",
                "pagefind/pagefind-component-ui.js",
                "pagefind/pagefind-component-ui.css",
                "pagefind/pagefind.en-us.pf_meta",
                "pagefind/index/en-us_example.pf_index",
                "pagefind/fragment/en-us_example.pf_fragment",
            ]
            for relative in expected_paths:
                write(public / relative, "content")
            metadata_pages = (
                "index.html",
                "episodes/index.html",
                "tags/index.html",
                "shows/index.html",
                "wiki/index.html",
                "search/index.html",
                "about/index.html",
                "methodology/index.html",
                "episodes/example/index.html",
                "episodes/episode.160/index.html",
                "episodes/中文标题/index.html",
            )
            for relative in metadata_pages:
                url = f"https://podcastatlas.ai/{relative.removesuffix('index.html')}"
                if relative == "index.html":
                    body = "A living knowledge atlas synthesized from podcasts."
                elif relative == "episodes/index.html":
                    body = episode_list_body(("example", "episode.160", "中文标题"))
                else:
                    body = ""
                write(public / relative, valid_html(url, body))
            write(public / "index.xml", "<rss />")
            write(public / "episodes/index.xml", "<rss />")
            write(public / "sitemap.xml", "<urlset />")

            report = verifier.validate(public)

        self.assertEqual([], report["errors"])
        self.assertEqual(len(expected_paths) + 3, report["file_count"])

    def test_accepts_static_episode_pagination_with_one_hundred_items_per_page(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            slugs = [f"episode-{index:03d}" for index in range(101)]
            for slug in slugs:
                write(public / "episodes" / slug / "index.html", valid_html(f"https://podcastatlas.ai/episodes/{slug}/"))
                write(public / "episodes" / f"{slug}.md", "content")
            write(
                public / "episodes" / "index.html",
                valid_html("https://podcastatlas.ai/episodes/", episode_list_body(slugs[:100])),
            )
            write(
                public / "episodes" / "page" / "1" / "index.html",
                '<html><head><meta http-equiv="refresh" content="0; url=/episodes/"></head></html>',
            )
            write(
                public / "episodes" / "page" / "2" / "index.html",
                valid_html("https://podcastatlas.ai/episodes/page/2/", episode_list_body(slugs[100:])),
            )

            report = verifier.validate(public)

        self.assertFalse(
            [error for error in report["errors"] if error.startswith("episode pagination") or error.startswith("episode list")]
        )

    def test_rejects_paginated_episode_canonical_on_wrong_origin_or_base_path(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            slugs = [f"episode-{index:03d}" for index in range(101)]
            for slug in slugs:
                write(public / "episodes" / slug / "index.html", valid_html(f"https://example.test/project/episodes/{slug}/"))
                write(public / "episodes" / f"{slug}.md", "content")
            write(
                public / "episodes" / "index.html",
                valid_html("https://example.test/project/episodes/", episode_list_body(slugs[:100])),
            )
            write(
                public / "episodes" / "page" / "2" / "index.html",
                valid_html("https://wrong.example/episodes/page/2/", episode_list_body(slugs[100:])),
            )

            report = verifier.validate(public)

        self.assertIn(
            "episode pagination canonical mismatch: episodes/page/2/index.html: "
            "expected https://example.test/project/episodes/page/2/, "
            "found https://wrong.example/episodes/page/2/",
            report["errors"],
        )

    def test_rejects_noncontiguous_episode_page_numbers(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            slugs = [f"episode-{index:03d}" for index in range(101)]
            for slug in slugs:
                write(public / "episodes" / slug / "index.html", valid_html(f"https://podcastatlas.ai/episodes/{slug}/"))
                write(public / "episodes" / f"{slug}.md", "content")
            write(
                public / "episodes" / "index.html",
                valid_html("https://podcastatlas.ai/episodes/", episode_list_body(slugs[:100])),
            )
            write(
                public / "episodes" / "page" / "3" / "index.html",
                valid_html("https://podcastatlas.ai/episodes/page/3/", episode_list_body(slugs[100:])),
            )

            report = verifier.validate(public)

        self.assertIn(
            "episode pagination page sequence mismatch: expected [1, 2], found [1, 3]",
            report["errors"],
        )

    def test_rejects_episode_list_links_on_wrong_origin_or_base_path(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            write(
                public / "episodes" / "episode-001" / "index.html",
                valid_html("https://example.test/project/episodes/episode-001/"),
            )
            write(public / "episodes" / "episode-001.md", "content")
            wrong_link = (
                '<ul class="episode-list"><li>'
                '<a href="https://evil.test/episodes/episode-001/">Episode</a>'
                "</li></ul>"
            )
            write(
                public / "episodes" / "index.html",
                valid_html("https://example.test/project/episodes/", wrong_link),
            )

            report = verifier.validate(public)

        self.assertIn(
            "episode list/detail URL mismatch: missing 1, unexpected 1",
            report["errors"],
        )

    def test_rejects_episode_lists_that_do_not_match_detail_pages(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            slugs = [f"episode-{index:03d}" for index in range(101)]
            for slug in slugs:
                write(public / "episodes" / slug / "index.html", valid_html(f"https://podcastatlas.ai/episodes/{slug}/"))
                write(public / "episodes" / f"{slug}.md", "content")
            write(
                public / "episodes" / "index.html",
                valid_html("https://podcastatlas.ai/episodes/", episode_list_body(slugs[:100])),
            )
            write(
                public / "episodes" / "page" / "2" / "index.html",
                valid_html(
                    "https://podcastatlas.ai/episodes/page/2/",
                    episode_list_body(("not-a-real-episode",)),
                ),
            )

            report = verifier.validate(public)

        self.assertIn(
            "episode list/detail mismatch: missing 1, unexpected 1",
            report["errors"],
        )

    def test_rejects_underfilled_nonfinal_episode_pages(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            slugs = [f"episode-{index:03d}" for index in range(101)]
            for slug in slugs:
                write(public / "episodes" / slug / "index.html", valid_html(f"https://podcastatlas.ai/episodes/{slug}/"))
                write(public / "episodes" / f"{slug}.md", "content")
            write(
                public / "episodes" / "index.html",
                valid_html("https://podcastatlas.ai/episodes/", episode_list_body(slugs[:99])),
            )
            write(
                public / "episodes" / "page" / "2" / "index.html",
                valid_html(
                    "https://podcastatlas.ai/episodes/page/2/",
                    episode_list_body(slugs[99:]),
                ),
            )

            report = verifier.validate(public)

        self.assertIn(
            "episode pagination page size mismatch: episodes/index.html: expected 100, found 99",
            report["errors"],
        )

    def test_rejects_episode_pages_that_are_not_newest_first(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            slugs = ["older", "newer"]
            for slug in slugs:
                write(public / "episodes" / slug / "index.html", valid_html(f"https://podcastatlas.ai/episodes/{slug}/"))
                write(public / "episodes" / f"{slug}.md", "content")
            write(
                public / "episodes" / "index.html",
                valid_html(
                    "https://podcastatlas.ai/episodes/",
                    episode_list_body(slugs, ("2026-01-01", "2026-02-01")),
                ),
            )

            report = verifier.validate(public)

        self.assertIn("episode list is not ordered newest first", report["errors"])

    def test_requires_parseable_publication_dates_on_episode_list_items(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            slugs = ["missing-date", "invalid-date"]
            for slug in slugs:
                write(public / "episodes" / slug / "index.html", valid_html(f"https://podcastatlas.ai/episodes/{slug}/"))
                write(public / "episodes" / f"{slug}.md", "content")
            write(
                public / "episodes" / "index.html",
                valid_html(
                    "https://podcastatlas.ai/episodes/",
                    episode_list_body(slugs, (None, "not-a-date")),
                ),
            )

            report = verifier.validate(public)

        self.assertIn("episode list item missing publication date", report["errors"])
        self.assertIn("episode list item has invalid publication date: not-a-date", report["errors"])

    def test_rejects_an_incomplete_episode_pagination_artifact(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            slugs = [f"episode-{index:03d}" for index in range(101)]
            for slug in slugs:
                write(public / "episodes" / slug / "index.html", valid_html(f"https://podcastatlas.ai/episodes/{slug}/"))
                write(public / "episodes" / f"{slug}.md", "content")
            write(
                public / "episodes" / "index.html",
                valid_html("https://podcastatlas.ai/episodes/", episode_list_body(slugs[:100])),
            )

            report = verifier.validate(public)

        self.assertIn("episode pagination page count mismatch: expected 2, found 1", report["errors"])
        self.assertIn("episode list coverage mismatch: expected 101 unique episodes, found 100", report["errors"])

    def test_rejects_invalid_json_ld(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            write(
                public / "index.html",
                '<script type=application/ld+json>{"@context":"https://***@type":"WebSite"}</script>',
            )

            report = verifier.validate(public)

        self.assertTrue(
            any(error.startswith("invalid JSON-LD in index.html:") for error in report["errors"])
        )

    def test_rejects_json_ld_description_entities_that_do_not_match_meta_text(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            page = valid_html("https://podcastatlas.ai/")
            page = page.replace(
                'content="Example description">',
                'content="A&amp;F and YouTube&#39;s description">',
                1,
            ).replace(
                '"description": "Example description"',
                '"description": "A&amp;amp;F and YouTube&amp;#39;s description"',
            )
            write(public / "index.html", page)

            report = verifier.validate(public)

        self.assertIn(
            "JSON-LD description does not match meta description in index.html",
            report["errors"],
        )

    def test_rejects_relative_or_inconsistent_canonical_url(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            page = valid_html("https://podcastatlas.ai/").replace(
                'rel="canonical" href="https://podcastatlas.ai/"',
                'rel="canonical" href="/relative/"',
            )
            write(public / "index.html", page)

            report = verifier.validate(public)

        self.assertIn("invalid canonical URL in index.html: '/relative/'", report["errors"])
        self.assertIn("canonical URL does not match Open Graph URL in index.html", report["errors"])
        self.assertIn("canonical URL does not match JSON-LD URL in index.html", report["errors"])

    def test_rejects_public_github_links(self):
        verifier = load_verifier()
        for href in (
            "https://github.com/example/repository/issues",
            "//github.com/example/repository/issues",
            "https://github&#46;com/example/repository/issues",
            "https://gith&#117;b.com/example/repository/issues",
            "https://&#103;ithub.com/example/repository/issues",
            "https://gith%75b.com/example/repository/issues",
            "https://github%2ecom/example/repository/issues",
            "https://github.com./example/repository/issues",
            "https://pages.github.com/example/repository/issues",
            "https://github.com\\example/repository/issues",
            "https://github.com\\@evil.test/repository/issues",
            "https:\\github.com\\example/repository/issues",
            "https:github.com/example/repository/issues",
            "https:\t//github.com/example/repository/issues",
            "https://git\thub.com/example/repository/issues",
            "https://github．com/example/repository/issues",
            "https://github｡com/example/repository/issues",
            "https://github.\ncom/example/repository/issues",
        ):
            with self.subTest(href=href), tempfile.TemporaryDirectory() as directory:
                public = Path(directory)
                write(
                    public / "methodology/index.html",
                    valid_html(
                        "https://podcastatlas.ai/methodology/",
                        f'<a href="{href}">Report</a>',
                    ),
                )

                report = verifier.validate(public)

                self.assertIn(
                    "public GitHub link found: methodology/index.html", report["errors"]
                )

    def test_requires_trust_pages_robots_and_social_card(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            report = verifier.validate(Path(directory))

        for relative in (
            "about/index.html",
            "about/index.md",
            "methodology/index.html",
            "methodology/index.md",
            "robots.txt",
            "images/podcast-atlas-social.png",
        ):
            self.assertIn(f"missing required file: {relative}", report["errors"])

    def test_rejects_nested_episode_markdown_output(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            write(public / "episodes" / "example" / "index.md", "content")

            report = verifier.validate(public)

        self.assertIn(
            "nested episode Markdown URL is forbidden: episodes/example/index.md",
            report["errors"],
        )

    def test_rejects_flat_episode_html_output(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            write(public / "episodes" / "example.html", "content")

            report = verifier.validate(public)

        self.assertIn(
            "flat episode HTML URL is forbidden: episodes/example.html",
            report["errors"],
        )

    def test_rejects_noncanonical_episode_urls_in_sitemap(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            write(
                public / "sitemap.xml",
                """<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url><loc>https://podcastatlas.ai/episodes/</loc></url>
<url><loc>https://podcastatlas.ai/episodes/example/</loc></url>
<url><loc>https://podcastatlas.ai/episodes/example.html</loc></url>
<url><loc>https://podcastatlas.ai/episodes/example.md</loc></url>
<url><loc>https://podcastatlas.ai/wiki/episodes/</loc></url>
<url><loc>https://podcastatlas.ai/wiki/episodes/example.md</loc></url>
</urlset>""",
            )

            report = verifier.validate(public)

        self.assertIn(
            "noncanonical Episode URL in sitemap: "
            "https://podcastatlas.ai/episodes/example.html",
            report["errors"],
        )
        self.assertIn(
            "noncanonical Episode URL in sitemap: "
            "https://podcastatlas.ai/episodes/example.md",
            report["errors"],
        )
        self.assertNotIn(
            "noncanonical Episode URL in sitemap: "
            "https://podcastatlas.ai/wiki/episodes/example.md",
            report["errors"],
        )

    def test_rejects_malformed_url_in_sitemap_without_crashing(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            write(
                public / "sitemap.xml",
                """<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url><loc>http://[invalid/episodes/example.md</loc></url>
</urlset>""",
            )

            report = verifier.validate(public)

        self.assertTrue(
            any(error.startswith("invalid URL in sitemap: http://[invalid/") for error in report["errors"])
        )

    def test_detects_episode_urls_with_a_deployment_base_path(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            write(
                public / "sitemap.xml",
                """<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url><loc>https://example.com/project/episodes/</loc></url>
<url><loc>https://example.com/project/episodes/example/</loc></url>
<url><loc>https://example.com/project/episodes/example.md</loc></url>
<url><loc>https://example.com/project/wiki/episodes/</loc></url>
<url><loc>https://example.com/project/wiki/episodes/example.md</loc></url>
</urlset>""",
            )

            report = verifier.validate(public)

        self.assertIn(
            "noncanonical Episode URL in sitemap: "
            "https://example.com/project/episodes/example.md",
            report["errors"],
        )
        self.assertNotIn(
            "noncanonical Episode URL in sitemap: "
            "https://example.com/project/wiki/episodes/example.md",
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
