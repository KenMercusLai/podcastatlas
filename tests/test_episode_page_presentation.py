from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SINGLE_LAYOUT = ROOT / "layouts/_default/single.html"
BASE_LAYOUT = ROOT / "layouts/_default/baseof.html"
EPISODE_PRESENTATION = ROOT / "layouts/partials/episode-presentation.html"
EPISODE_DURATION = ROOT / "layouts/partials/episode-duration.html"
EPISODE_SOURCE_NOTE_LINK = ROOT / "layouts/partials/episode-source-note-link.html"


class EpisodePagePresentationTest(unittest.TestCase):
    def test_episode_has_one_h1_and_only_distinct_generated_titles_become_subtitles(self):
        single = SINGLE_LAYOUT.read_text()
        base = BASE_LAYOUT.read_text()

        self.assertTrue(EPISODE_PRESENTATION.is_file())
        presentation = EPISODE_PRESENTATION.read_text()

        self.assertIn('<h1>{{ .Title }}</h1>', single)
        self.assertIn('partial "episode-presentation.html" .', single)
        self.assertNotIn('{{ .Content }}', single)
        self.assertNotIn(".RawContent", presentation)
        self.assertIn("findRESubmatch", presentation)
        self.assertIn("$content 1", presentation)
        self.assertIn("if gt (len $headingMatches) 0", presentation)
        self.assertLess(
            presentation.index("if gt (len $headingMatches) 0"),
            presentation.index("index $headingMatches 0"),
        )
        self.assertNotIn(".RenderString", presentation)
        self.assertIn("plainify", presentation)
        self.assertIn("htmlUnescape", presentation)
        self.assertIn("ne $subtitle $page.Title", presentation)
        self.assertIn("replaceRE", presentation)
        self.assertIn("<h1", presentation)
        self.assertIn('"<h2$1>"', presentation)
        self.assertIn('"</h2>"', presentation)
        self.assertIn("safeHTML", single)
        self.assertIn('class="episode-subtitle"', single)
        self.assertIn(".episode-subtitle", base)

    def test_episode_metadata_is_labeled_grouped_and_human_readable(self):
        single = SINGLE_LAYOUT.read_text()
        base = BASE_LAYOUT.read_text()

        self.assertTrue(EPISODE_DURATION.is_file())
        duration = EPISODE_DURATION.read_text()
        source_note_link = EPISODE_SOURCE_NOTE_LINK.read_text()

        self.assertIn('class="meta episode-meta-primary"', single)
        self.assertIn('class="episode-actions"', single)
        self.assertIn('$sourceNotePage := partial "episode-source-note-page.html" .', single)
        self.assertIn("if or .Params.source_url $sourceNotePage", single)
        self.assertIn('partial "episode-source-note-link.html" $sourceNotePage', single)
        self.assertIn('Published {{ partial "episode-publication-date.html" . }}', single)
        self.assertIn('partial "episode-duration.html" .Params.duration', single)
        self.assertNotIn("Show:", single)
        self.assertNotIn("{{ . }}s", single)
        self.assertNotIn(" · ", source_note_link)
        self.assertIn("div", duration)
        self.assertIn("mod", duration)
        self.assertIn(" hr", duration)
        self.assertIn(" min", duration)
        self.assertIn(" sec", duration)
        self.assertIn(".episode-meta-primary", base)
        self.assertIn(".episode-actions", base)


if __name__ == "__main__":
    unittest.main()
