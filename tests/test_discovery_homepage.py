from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
HOME_LAYOUT = ROOT / "layouts/index.html"
BASE_LAYOUT = ROOT / "layouts/_default/baseof.html"


class DiscoveryHomepageLayoutTest(unittest.TestCase):
    def test_homepage_is_a_stable_searchable_landing_page(self):
        homepage = HOME_LAYOUT.read_text()
        base = BASE_LAYOUT.read_text()
        seo = (ROOT / "layouts/partials/seo.html").read_text()

        self.assertNotIn("http-equiv=\"refresh\"", homepage)
        self.assertIn('partial "seo.html" .', base)
        self.assertIn('rel="canonical" href="{{ $canonicalURL }}"', seo)
        self.assertNotIn('rel="canonical"', homepage)
        self.assertIn("A living knowledge atlas synthesized from podcasts.", homepage)
        self.assertIn("<pagefind-searchbox></pagefind-searchbox>", homepage)
        self.assertIn('"pagefind/pagefind-component-ui.css" | relURL', homepage)
        self.assertIn('"pagefind/pagefind-component-ui.js" | relURL', homepage)
        self.assertIn('href="{{ .Site.Home.RelPermalink }}"', base)

    def test_homepage_uses_reader_facing_primary_actions(self):
        homepage = HOME_LAYOUT.read_text()

        self.assertIn(">Explore Knowledge →</a>", homepage)
        self.assertIn(">Browse Episode Guides →</a>", homepage)
        self.assertNotIn(">Explore the Wiki →</a>", homepage)
        self.assertNotIn(">Browse Episodes →</a>", homepage)

    def test_homepage_shows_a_live_update_signal(self):
        homepage = HOME_LAYOUT.read_text()

        self.assertIn('class="home-update-signal"', homepage)
        self.assertIn(
            "Updated daily from {{ len $episodes }} episodes across "
            "{{ len $showSection.Pages }} shows.",
            homepage,
        )
        self.assertEqual(homepage.count("$episodes :="), 1)
        self.assertEqual(homepage.count("$showSection :="), 1)

    def test_homepage_leads_with_current_knowledge_state(self):
        homepage = HOME_LAYOUT.read_text()

        self.assertIn('.Site.GetPage "/wiki-projections/current-synthesis"', homepage)
        self.assertIn('.Site.GetPage "/wiki-projections/open-questions"', homepage)
        self.assertIn("Current Synthesis", homepage)
        self.assertIn("Open Questions", homepage)

    def test_daily_discoveries_use_reader_facing_copy(self):
        homepage = HOME_LAYOUT.read_text()

        self.assertIn(
            "A fresh concept, entity, and source note from across the atlas.",
            homepage,
        )
        self.assertNotIn(
            "Three paths into the atlas, selected deterministically for today.",
            homepage,
        )

    def test_daily_discoveries_are_deterministic_and_canonical(self):
        homepage = HOME_LAYOUT.read_text()

        self.assertIn("Daily discoveries", homepage)
        self.assertIn("now.UTC.Unix", homepage)
        self.assertIn("div", homepage)
        self.assertNotIn("(now.UTC).YearDay", homepage)
        for section in ("concepts", "entities", "sources"):
            self.assertIn(f'.Site.GetPage "/wiki/{section}"', homepage)
        self.assertIn('partial "wiki-content.html" $page', homepage)
        self.assertIn("plainify | htmlUnescape", homepage)
        self.assertIn("strings.TrimPrefix $page.Title", homepage)
        self.assertNotIn("$page.Plain | truncate", homepage)
        self.assertNotIn("shuffle", homepage.lower())
        self.assertNotIn("math.Rand", homepage)

    def test_homepage_resurfaces_historical_episodes_with_a_fallback(self):
        homepage = HOME_LAYOUT.read_text()

        self.assertIn('where .Site.RegularPages "Section" "episodes"', homepage)
        self.assertIn("On this day", homepage)
        self.assertIn("From the archive", homepage)
        self.assertIn(".Date.Month", homepage)
        self.assertIn(".Date.Day", homepage)
        self.assertIn("range $archivePool", homepage)
        self.assertIn('partial "episode-list.html"', homepage)
        self.assertIn("$archivePool := $episodes | after 6", homepage)
        self.assertIn("$windowCount := add (sub (len $archivePool) 3) 1", homepage)
        self.assertIn("first 3", homepage)

    def test_homepage_shows_latest_episodes_and_shared_atlas_entry_points(self):
        homepage = HOME_LAYOUT.read_text()
        episode_card = (ROOT / "layouts/partials/homepage-episode-card.html").read_text()
        collections = (ROOT / "layouts/partials/knowledge-collection-section.html").read_text()

        self.assertIn("Latest episodes", homepage)
        self.assertIn("first 6 $episodes", homepage)
        self.assertIn('partial "homepage-episode-card.html"', homepage)
        self.assertIn("$episode.RenderString $overview", episode_card)
        self.assertIn("plainify | htmlUnescape", episode_card)
        self.assertIn("-webkit-line-clamp", homepage)
        self.assertIn('.Site.GetPage "/show"', homepage)
        self.assertIn('partial "knowledge-collection-section.html"', homepage)
        self.assertIn("Explore the knowledge base", collections)
        for label in ("Episodes", "Shows", "Concepts", "Entities", "Source Notes"):
            self.assertIn(f">{label}</a>", collections)
        self.assertNotIn(">Sources</a>", collections)
        self.assertNotIn("home-stat", homepage)


if __name__ == "__main__":
    unittest.main()
