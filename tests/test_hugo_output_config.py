import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import tomllib
import unittest
from urllib.parse import unquote
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]


class HugoOutputConfigTest(unittest.TestCase):
    def test_taxonomy_and_term_pages_only_emit_html(self):
        with (ROOT / "hugo.toml").open("rb") as config_file:
            config = tomllib.load(config_file)

        outputs = config["outputs"]
        self.assertEqual(["html"], outputs.get("taxonomy"))
        self.assertEqual(["html"], outputs.get("term"))
        self.assertEqual(["html", "markdown"], outputs.get("page"))

    def test_episode_pages_keep_pretty_html_and_use_flat_markdown_urls(self):
        with (ROOT / "hugo.toml").open("rb") as config_file:
            config = tomllib.load(config_file)

        self.assertTrue(config["uglyURLs"]["episodes"])
        self.assertTrue(config["outputFormats"]["html"]["noUgly"])

    def test_content_dates_are_metadata_not_release_schedules(self):
        with (ROOT / "hugo.toml").open("rb") as config_file:
            config = tomllib.load(config_file)
        self.assertIs(config.get("buildFuture"), True)

    @unittest.skipUnless(shutil.which("hugo"), "Hugo required for rendered fixture")
    def test_future_latest_episode_renders_at_frozen_clock(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            site = Path(temp_dir)
            (site / "hugo.toml").write_bytes((ROOT / "hugo.toml").read_bytes())
            (site / "themes/hugo-xmin").mkdir(parents=True)
            partials = site / "layouts/partials"
            partials.mkdir(parents=True)
            for name in (
                "show-profile.html", "canonical-show-name.html",
                "episode-list.html", "episode-publication-date.html",
            ):
                shutil.copyfile(ROOT / "layouts/partials" / name, partials / name)
            layouts = site / "layouts/_default"
            layouts.mkdir()
            (layouts / "single.html").write_text("<h1>{{ .Title }}</h1>")
            (layouts / "single.md").write_text("{{ .RawContent }}")
            (layouts / "list.html").write_text(
                '{{ if and (eq .Kind "term") (eq .Data.Singular "show") }}'
                '{{ partial "show-profile.html" . }}{{ end }}'
            )
            episodes = site / "content/episodes"
            episodes.mkdir(parents=True)
            profiles = {}
            slugs = ("ordinary", "episode.160", "café-東京")
            for index, slug in enumerate(slugs):
                show = f"Show {index}"
                (episodes / f"{slug}.md").write_text(
                    f"+++\ntitle = '{slug}'\nshow = '{show}'\n"
                    "date = 2026-10-27T00:00:00Z\ndraft = false\n+++\nPublished episode.\n"
                )
                (episodes / f"past-{index}.md").write_text(
                    f"+++\ntitle = 'Past episode'\nshow = '{show}'\n"
                    "date = 2026-10-25T00:00:00Z\n+++\nPast episode.\n"
                )
                profiles[show] = {
                    "episode_count": 2, "earliest_episode_date": "2026-10-25",
                    "latest_episode_date": "2026-10-27",
                    "latest_episode_file": f"{slug}.md", "source_note_count": 0,
                    "topic_matched_source_note_count": 0, "topics": [], "entities": [],
                    "start_here_episode_files": [f"{slug}.md"],
                }
            (episodes / "unpublished.md").write_text(
                "+++\ntitle = 'Unpublished'\ndate = 2026-10-27T00:00:00Z\n"
                "draft = true\n+++\nDraft.\n"
            )
            (site / "data").mkdir()
            (site / "data/show_profiles.json").write_text(json.dumps({"shows": profiles}))
            for prefix in ("/", "/podcastatlas/"):
                with self.subTest(prefix=prefix):
                    result = subprocess.run(
                        ["hugo", "build", "--source", str(site), "--cleanDestinationDir",
                         "--clock", "2026-10-26T20:35:19Z", "--baseURL", f"https://example.test{prefix}"],
                        capture_output=True, text=True,
                    )
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                    public = site / "public"
                    sitemap = ET.parse(public / "sitemap.xml")
                    locations = {unquote(node.text or "") for node in sitemap.iter()
                                 if node.tag.endswith("}loc")}
                    for index, slug in enumerate(slugs):
                        self.assertTrue((public / "episodes" / slug / "index.html").is_file())
                        self.assertTrue((public / "episodes" / f"{slug}.md").is_file())
                        route = f"{prefix}episodes/{slug}/"
                        self.assertIn(f"https://example.test{route}", locations)
                        show_html = (public / "shows" / f"show-{index}" / "index.html").read_text()
                        self.assertIn(f'href="{route}"', unquote(show_html))
                        self.assertIn('class="show-latest-episode"', show_html)
                    self.assertFalse((public / "episodes/unpublished/index.html").exists())
                    self.assertFalse((public / "episodes/unpublished.md").exists())


if __name__ == "__main__":
    unittest.main()
