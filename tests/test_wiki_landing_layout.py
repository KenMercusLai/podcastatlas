from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
WIKI_LAYOUT = ROOT / "layouts" / "wiki" / "list.html"


class WikiLandingLayoutTest(unittest.TestCase):
    def test_landing_leads_with_the_current_knowledge_state(self):
        layout = WIKI_LAYOUT.read_text()

        self.assertIn("Explore knowledge synthesized from podcasts", layout)
        self.assertIn('.Site.GetPage "/wiki-projections/current-synthesis"', layout)
        self.assertIn('.Site.GetPage "/wiki-projections/open-questions"', layout)
        self.assertIn("What the atlas currently knows", layout)
        self.assertIn("Current Synthesis", layout)
        self.assertIn("Open Questions", layout)

    def test_landing_surfaces_recently_updated_concepts_and_entities(self):
        layout = WIKI_LAYOUT.read_text()

        self.assertIn("Recently updated knowledge", layout)
        self.assertIn(".Params.last_updated", layout)
        self.assertIn('dict "label" "Concept" "page"', layout)
        self.assertIn('dict "label" "Entity" "page"', layout)
        self.assertIn('sort $recentConcepts "sort_key" "desc"', layout)
        self.assertIn('sort $recentEntities "sort_key" "desc"', layout)
        self.assertIn("first 3 $recentConcepts", layout)
        self.assertIn("first 3 $recentEntities", layout)

    def test_landing_unifies_coverage_into_five_linked_collection_cards(self):
        layout = WIKI_LAYOUT.read_text()

        self.assertEqual(layout.count("Explore the knowledge base"), 1)
        self.assertNotIn("Knowledge coverage", layout)
        self.assertIn('.Site.GetPage "/episodes"', layout)
        self.assertIn('.Site.GetPage "/show"', layout)

        for label in ("Episodes", "Shows", "Concepts", "Entities", "Source Notes"):
            self.assertIn(f">{label}</a>", layout)

        self.assertNotIn("wiki-stat-grid", layout)
        self.assertNotIn("wiki-stat", layout)

        self.assertIn("Browse by topic", layout)
        self.assertIn('.Site.GetPage "/topics"', layout)
        self.assertIn(".Params.topic_pages", layout)
        self.assertNotIn(".Site.Taxonomies.tags", layout)

    def test_landing_keeps_history_and_health_as_supporting_links(self):
        layout = WIKI_LAYOUT.read_text()

        self.assertIn('.Site.GetPage "/wiki-projections/update-history"', layout)
        self.assertIn('.Site.GetPage "/wiki/stats"', layout)
        self.assertIn("Update History", layout)
        self.assertIn("Wiki Stats", layout)


if __name__ == "__main__":
    unittest.main()
