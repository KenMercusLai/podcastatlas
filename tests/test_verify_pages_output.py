import importlib.util
import gzip
import json
from pathlib import Path
import tempfile
import unittest
from urllib.parse import urlsplit


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


def semantic_payload(url, schema_type=None):
    path = urlsplit(url).path
    if schema_type is None:
        path_parts = path.strip("/").split("/")
        if "episodes" in path_parts and path_parts[-2:-1] != ["page"] and path_parts[-1] != "episodes":
            schema_type = "PodcastEpisode"
        elif "shows" in path_parts and path_parts[-1] != "shows":
            schema_type = "PodcastSeries"
        elif "/wiki/concepts/" in path:
            schema_type = "DefinedTerm"
        elif "/wiki/entities/" in path:
            schema_type = "Article"
        elif path.rstrip("/").endswith("/project") or path == "/":
            schema_type = "WebSite"
        else:
            schema_type = "WebPage"

    payload = {
        "@context": "https://schema.org",
        "@type": schema_type,
        "name": "Example | Podcast Atlas",
        "url": url,
        "description": "Example description",
    }
    if schema_type == "WebSite":
        root = url.rstrip("/") + "/"
        payload["potentialAction"] = {
            "@type": "SearchAction",
            "target": {
                "@type": "EntryPoint",
                "urlTemplate": f"{root}search/?q={{search_term_string}}",
            },
            "query-input": "required name=search_term_string",
        }
    elif schema_type == "PodcastEpisode":
        payload.update(
            {
                "datePublished": "2026-01-01T00:00:00Z",
                "duration": "PT60S",
                "partOfSeries": {
                    "@type": "PodcastSeries",
                    "name": "Example Show",
                    "url": "https://podcastatlas.ai/shows/example/",
                },
                "sameAs": "https://audio.example/episode",
            }
        )
    elif schema_type == "PodcastSeries":
        payload["numberOfEpisodes"] = 1
    elif schema_type == "DefinedTerm":
        payload["inDefinedTermSet"] = {
            "@type": "DefinedTermSet",
            "name": "Podcast Atlas Concepts",
            "url": "https://podcastatlas.ai/wiki/concepts/",
        }
    elif schema_type == "Article":
        payload.update({"headline": "Example", "dateModified": "2026-01-01"})
    return payload


def valid_html(url, body="", schema_type=None, payload=None):
    payload = json.dumps(payload or semantic_payload(url, schema_type=schema_type))
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


def synthesis_html_fragments(
    summary="A compact cross-source knowledge map.",
    updated="2026-08-23",
    episodes="10",
    sources="9",
):
    attrs = (
        'data-synthesis-source="compact" '
        f'data-summary="{summary}" data-episode-count="{episodes}" data-source-count="{sources}"'
    )
    detail = (
        f'<article class="current-synthesis" {attrs}>'
        f'<p class="synthesis-updated">Updated <time datetime="{updated}">{updated}</time></p>'
        '<h2>Executive Summary</h2><p>Compact body.</p>'
        '<h2>Synthesis by Domain</h2><p>Domain body.</p></article>'
    )
    card = (
        f'<article class="wiki-feature current-synthesis-card" {attrs}>'
        f'<p class="wiki-feature-summary">{summary}</p>'
        f'<p class="wiki-feature-updated">Updated <time datetime="{updated}">{updated}</time></p>'
        '</article>'
    )
    return detail, card


class VerifyPagesOutputTest(unittest.TestCase):
    def test_pagefind_verifier_requires_current_synthesis_and_rejects_internal_routes(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            write(public / "pagefind/pagefind.en-us.pf_meta", "meta")
            write(public / "pagefind/index/en-us_example.pf_index", "index")
            fragment = public / "pagefind/fragment/en-us_example.pf_fragment"
            fragment.parent.mkdir(parents=True, exist_ok=True)

            fragment.write_bytes(gzip.compress(b"/wiki/current-synthesis/ compact synthesis"))
            errors: list[str] = []
            verifier.validate_pagefind_output(public, errors)
            self.assertEqual([], errors)

            fragment.write_bytes(gzip.compress(b"/wiki/concepts/example/"))
            errors = []
            verifier.validate_pagefind_output(public, errors)
            self.assertIn("Current Synthesis is missing from Pagefind result fragments", errors)

            fragment.write_bytes(
                gzip.compress(b"/wiki/current-synthesis/ /wiki/_generated/synthesis/current/")
            )
            errors = []
            verifier.validate_pagefind_output(public, errors)
            self.assertIn("internal _generated URL found in Pagefind result fragments", errors)

    def test_current_synthesis_verifier_checks_snapshot_metadata_across_landing_and_detail(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            detail, card = synthesis_html_fragments(summary="Example description")
            write(
                public / "wiki/current-synthesis/index.html",
                valid_html("https://podcastatlas.ai/wiki/current-synthesis/", detail),
            )
            write(public / "wiki/index.html", valid_html("https://podcastatlas.ai/wiki/", card))
            errors: list[str] = []
            verifier.validate_current_synthesis(public, errors)
            self.assertEqual([], errors)

            _, mismatched_card = synthesis_html_fragments(
                summary="Different summary", updated="2026-08-22", episodes="11", sources="9"
            )
            write(public / "wiki/index.html", valid_html("https://podcastatlas.ai/wiki/", mismatched_card))
            errors = []
            verifier.validate_current_synthesis(public, errors)

        self.assertIn("Current Synthesis summary differs between landing and detail", errors)
        self.assertIn("Current Synthesis episode-count differs between landing and detail", errors)
        self.assertIn("Current Synthesis update date differs between landing and detail", errors)

    def test_rejects_generic_json_ld_on_semantic_detail_routes(self):
        verifier = load_verifier()
        cases = {
            "episodes/example/index.html": "PodcastEpisode",
            "shows/example/index.html": "PodcastSeries",
            "wiki/concepts/example/index.html": "DefinedTerm",
            "wiki/entities/example/index.html": "Article",
        }
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            errors = []
            for relative, expected_type in cases.items():
                page = public / relative
                write(
                    page,
                    valid_html(
                        f"https://podcastatlas.ai/{relative.removesuffix('index.html')}",
                        schema_type="WebPage",
                    ),
                )
                verifier.validate_metadata_page(page, public, errors)

        for relative, expected_type in cases.items():
            self.assertIn(
                f"invalid JSON-LD type in {relative}: expected {expected_type!r}, found 'WebPage'",
                errors,
            )

    def test_rejects_missing_semantic_json_ld_properties(self):
        verifier = load_verifier()
        cases = {
            "index.html": ("WebSite", "WebSite JSON-LD potentialAction in index.html"),
            "episodes/example/index.html": (
                "PodcastEpisode",
                "PodcastEpisode JSON-LD datePublished in episodes/example/index.html",
            ),
            "shows/example/index.html": (
                "PodcastSeries",
                "PodcastSeries JSON-LD numberOfEpisodes in shows/example/index.html",
            ),
            "wiki/concepts/example/index.html": (
                "DefinedTerm",
                "DefinedTerm JSON-LD inDefinedTermSet in wiki/concepts/example/index.html",
            ),
            "wiki/entities/example/index.html": (
                "Article",
                "Article JSON-LD headline in wiki/entities/example/index.html",
            ),
        }
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            errors = []
            for relative, (schema_type, _) in cases.items():
                url = f"https://podcastatlas.ai/{relative.removesuffix('index.html')}"
                payload = {
                    "@context": "https://schema.org",
                    "@type": schema_type,
                    "name": "Example | Podcast Atlas",
                    "url": url,
                    "description": "Example description",
                }
                page = public / relative
                write(page, valid_html(url, payload=payload))
                verifier.validate_metadata_page(page, public, errors)

        for _, expected_error in cases.values():
            self.assertTrue(
                any(error.startswith(expected_error) for error in errors),
                f"missing error starting with {expected_error!r}: {errors}",
            )

    def test_validates_every_semantic_detail_page(self):
        verifier = load_verifier()
        cases = {
            "episodes/z-wrong/index.html": "PodcastEpisode",
            "shows/z-wrong/index.html": "PodcastSeries",
            "wiki/concepts/z-wrong/index.html": "DefinedTerm",
            "wiki/entities/z-wrong/index.html": "Article",
        }
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            for relative, expected_type in cases.items():
                url = f"https://podcastatlas.ai/{relative.removesuffix('index.html')}"
                write(public / relative, valid_html(url, schema_type="WebPage"))
                if relative.startswith("episodes/"):
                    write(public / "episodes/z-wrong.md", "content")

            report = verifier.validate(public)

        for relative, expected_type in cases.items():
            self.assertIn(
                f"invalid JSON-LD type in {relative}: expected {expected_type!r}, found 'WebPage'",
                report["errors"],
            )

    def test_treats_generated_by_letter_indexes_as_webpages(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            errors = []
            for section in ("concepts", "entities"):
                relative = f"wiki/{section}/by-letter/index.html"
                url = f"https://podcastatlas.ai/wiki/{section}/by-letter/"
                page = public / relative
                write(page, valid_html(url, schema_type="WebPage"))
                verifier.validate_metadata_page(page, public, errors)

        self.assertFalse(
            any("by-letter/index.html" in error and "JSON-LD type" in error for error in errors),
            errors,
        )

    def test_accepts_complete_semantic_json_ld_properties(self):
        verifier = load_verifier()
        cases = (
            "index.html",
            "episodes/example/index.html",
            "shows/example/index.html",
            "wiki/concepts/example/index.html",
            "wiki/entities/example/index.html",
        )
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            errors = []
            for relative in cases:
                url = f"https://podcastatlas.ai/{relative.removesuffix('index.html')}"
                page = public / relative
                write(page, valid_html(url))
                verifier.validate_metadata_page(page, public, errors)

        self.assertEqual([], errors)

    def test_accepts_the_expected_site_output(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            expected_paths = [
                "index.html",
                "episodes/index.html",
                "shows/index.html",
                "tags/index.html",
                "tags/old-tag/index.html",
                "wiki/index.html",
                "wiki/current-synthesis/index.html",
                "topics/index.html",
                *[f"topics/{key}/index.html" for key in verifier.CONTROLLED_TOPIC_KEYS],
                *[f"wiki/concepts/{key}/index.html" for key in verifier.CONTROLLED_TOPIC_KEYS],
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
            (public / "pagefind/fragment/en-us_example.pf_fragment").write_bytes(
                gzip.compress(b"/wiki/current-synthesis/ compact synthesis")
            )
            metadata_pages = (
                "index.html",
                "episodes/index.html",
                "shows/index.html",
                "tags/index.html",
                "tags/old-tag/index.html",
                "wiki/index.html",
                "wiki/current-synthesis/index.html",
                "topics/index.html",
                *[f"topics/{key}/index.html" for key in verifier.CONTROLLED_TOPIC_KEYS],
                *[f"wiki/concepts/{key}/index.html" for key in verifier.CONTROLLED_TOPIC_KEYS],
                "search/index.html",
                "about/index.html",
                "methodology/index.html",
                "episodes/example/index.html",
                "episodes/episode.160/index.html",
                "episodes/中文标题/index.html",
            )
            synthesis_detail, synthesis_card = synthesis_html_fragments(summary="Example description")
            for relative in metadata_pages:
                url = f"https://podcastatlas.ai/{relative.removesuffix('index.html')}"
                if relative == "index.html":
                    body = "A living knowledge atlas synthesized from podcasts."
                elif relative == "episodes/index.html":
                    body = episode_list_body(("example", "episode.160", "中文标题"))
                elif relative.startswith("tags/"):
                    body = '<main class="legacy-tag-page">Legacy tag</main>'
                elif relative == "wiki/index.html":
                    body = synthesis_card + "".join(
                        f'<a class="controlled-topic-link" data-topic-key="{key}" href="/topics/{key}/">{key}</a>'
                        for key in verifier.CONTROLLED_TOPIC_KEYS
                    )
                elif relative == "wiki/current-synthesis/index.html":
                    body = synthesis_detail
                elif relative == "topics/index.html":
                    body = "".join(
                        f'<a class="controlled-topic-link" data-topic-key="{key}" href="/topics/{key}/">{key}</a>'
                        for key in verifier.CONTROLLED_TOPIC_KEYS
                    )
                elif relative.startswith("topics/"):
                    key = Path(relative).parts[1]
                    body = (
                        f'<article class="controlled-topic" data-topic-key="{key}" data-topic-count="1">'
                        f'<a class="controlled-topic-entry" data-topic-kind="concept" href="/wiki/concepts/{key}/">{key}</a>'
                        "</article>"
                    )
                elif relative.startswith("wiki/concepts/"):
                    key = Path(relative).parts[2]
                    body = (
                        f'<a class="wiki-topic-link" data-topic-key="{key}" href="/topics/{key}/">{key}</a>'
                    )
                else:
                    body = ""
                page_html = valid_html(url, body)
                if relative.startswith("tags/"):
                    page_html = page_html.replace(
                        "<head>",
                        '<head><meta name="robots" content="noindex, follow">',
                        1,
                    )
                write(public / relative, page_html)
            write(public / "index.xml", "<rss />")
            write(public / "episodes/index.xml", "<rss />")
            write(
                public / "sitemap.xml",
                "<urlset>"
                "<url><loc>https://podcastatlas.ai/topics/</loc></url>"
                + "".join(
                    f"<url><loc>https://podcastatlas.ai/topics/{key}/</loc></url>"
                    for key in verifier.CONTROLLED_TOPIC_KEYS
                )
                + "</urlset>",
            )

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

    def test_accepts_exactly_six_controlled_topic_artifacts(self):
        verifier = load_verifier()
        keys = ("technology", "economics", "history", "politics", "culture", "science")
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            landing_links = "".join(
                f'<a class="controlled-topic-link" data-topic-key="{key}" href="/topics/{key}/">{key}</a>'
                for key in keys
            )
            write(public / "topics" / "index.html", landing_links)
            write(public / "wiki" / "index.html", landing_links)
            for key in keys:
                write(
                    public / "topics" / key / "index.html",
                    f'<article class="controlled-topic" data-topic-key="{key}" data-topic-count="1">'
                    f'<a class="controlled-topic-entry" data-topic-kind="concept" href="/wiki/concepts/{key}/">{key}</a>'
                    "</article>",
                )
                write(
                    public / "wiki" / "concepts" / key / "index.html",
                    f'<a class="wiki-topic-link" data-topic-key="{key}" href="/topics/{key}/">{key}</a>',
                )
            errors = []
            verifier.validate_controlled_topics(public, errors)
            self.assertEqual([], errors)

            write(public / "wiki" / "concepts" / "technology" / "index.html", "missing reverse link")
            errors = []
            verifier.validate_controlled_topics(public, errors)

        self.assertTrue(any("missing reverse topic link" in error for error in errors))

    def test_rejects_uncontrolled_or_invalid_topics(self):
        verifier = load_verifier()
        keys = ("technology", "economics", "history", "politics", "culture", "science")
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            write(
                public / "topics" / "index.html",
                "".join(
                    f'<a class="controlled-topic-link" data-topic-key="{key}" href="/topics/{key}/">{key}</a>'
                    for key in (*keys, "noise")
                ),
            )
            for key in (*keys, "noise"):
                count = "2" if key == "technology" else "1"
                kind = "entity" if key == "science" else "concept"
                write(
                    public / "topics" / key / "index.html",
                    f'<article class="controlled-topic" data-topic-key="{key}" data-topic-count="{count}">'
                    f'<a class="controlled-topic-entry" data-topic-kind="{kind}" href="/wiki/{kind}s/{key}/">{key}</a>'
                    "</article>",
                )
            errors = []
            verifier.validate_controlled_topics(public, errors)

        self.assertTrue(any("controlled topic routes mismatch" in error for error in errors))
        self.assertTrue(any("entry count mismatch" in error for error in errors))
        self.assertTrue(any("must include at least one concept" in error for error in errors))

    def test_rejects_unsafe_or_misdirected_controlled_topic_links(self):
        verifier = load_verifier()
        keys = ("technology", "economics", "history", "politics", "culture", "science")
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            landing_links = "".join(
                f'<a class="controlled-topic-link" data-topic-key="{key}" '
                f'href="{("https://evil.example/wiki/concepts/technology/" if key == "technology" else f"/topics/{key}/")}">{key}</a>'
                for key in keys
            )
            write(public / "topics" / "index.html", landing_links)
            write(public / "wiki" / "index.html", landing_links)
            for key in keys:
                entry_href = (
                    "https://evil.example/wiki/concepts/technology/"
                    if key == "technology"
                    else f"/wiki/concepts/{key}/"
                )
                write(
                    public / "topics" / key / "index.html",
                    f'<article class="controlled-topic" data-topic-key="{key}" data-topic-count="1">'
                    f'<a class="controlled-topic-entry" data-topic-kind="concept" href="{entry_href}">{key}</a>'
                    "</article>",
                )
                reverse_href = "/topics/science/" if key == "economics" else f"/topics/{key}/"
                write(
                    public / "wiki" / "concepts" / key / "index.html",
                    f'<a class="wiki-topic-link" data-topic-key="{key}" href="{reverse_href}">{key}</a>',
                )
            errors = []
            verifier.validate_controlled_topics(public, errors)

        self.assertTrue(any("invalid landing link" in error for error in errors))
        self.assertTrue(any("invalid Wiki landing link" in error for error in errors))
        self.assertTrue(any("missing knowledge target" in error for error in errors))
        self.assertTrue(any("invalid reverse topic link" in error for error in errors))

    def test_legacy_tag_routes_are_preserved_but_noindexed_and_hidden(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            legacy_html = (
                '<html><head><meta name=robots content="noindex, follow"></head>'
                '<body><main class="legacy-tag-page">Legacy tag</main></body></html>'
            )
            write(public / "tags" / "index.html", legacy_html)
            write(public / "tags" / "old-tag" / "index.html", legacy_html)
            errors = []
            verifier.validate_legacy_tags(public, errors)
            self.assertEqual([], errors)

            write(public / "tags" / "old-tag" / "index.html", "exposed tag page")
            errors = []
            verifier.validate_legacy_tags(public, errors)

        self.assertTrue(any("missing noindex" in error for error in errors))
        self.assertTrue(any("missing compatibility marker" in error for error in errors))

    def test_controlled_topic_sitemap_contract_rejects_tags_and_missing_topics(self):
        verifier = load_verifier()
        valid_urls = [
            "https://podcastatlas.ai/topics/",
            *[
                f"https://podcastatlas.ai/topics/{key}/"
                for key in verifier.CONTROLLED_TOPIC_KEYS
            ],
        ]
        errors = []
        verifier.validate_controlled_topic_sitemap(valid_urls, errors)
        self.assertEqual([], errors)

        errors = []
        verifier.validate_controlled_topic_sitemap(
            [*valid_urls[:-1], "https://podcastatlas.ai/tags/noise/"], errors
        )
        self.assertTrue(any("raw tag URL found in sitemap" in error for error in errors))
        self.assertTrue(any("controlled topic sitemap coverage mismatch" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
