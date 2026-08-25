from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
WIKI_LAYOUT = ROOT / "layouts" / "wiki" / "list.html"


class WikiLandingLayoutTest(unittest.TestCase):
    def test_landing_leads_with_the_current_knowledge_state(self):
        layout = WIKI_LAYOUT.read_text()
        homepage = (ROOT / "layouts" / "index.html").read_text()
        current = (ROOT / "layouts" / "partials" / "current-knowledge-section.html").read_text()

        self.assertIn("Explore knowledge synthesized from podcasts", layout)
        self.assertIn('partial "current-knowledge-section.html"', layout)
        self.assertIn('partial "current-knowledge-section.html"', homepage)
        self.assertIn('$site.GetPage "/wiki-projections/current-synthesis"', current)
        self.assertIn('$site.GetPage "/wiki-projections/open-questions"', current)
        self.assertIn("What the atlas currently knows", current)
        self.assertIn("Current Synthesis", current)
        self.assertIn("Open Questions", current)
        self.assertIn("Params.summary", current)
        self.assertIn("Params.last_updated", current)
        self.assertIn("Params.source_count", current)
        self.assertIn("Params.episode_count", current)

    def test_landing_surfaces_recently_updated_concepts_and_entities(self):
        layout = WIKI_LAYOUT.read_text()
        recent = (ROOT / "layouts/partials/recently-updated-data.html").read_text()

        self.assertIn("Recently updated knowledge", layout)
        self.assertIn('partial "recently-updated-data.html"', layout)
        self.assertIn(".Params.last_updated", recent)
        self.assertIn('dict "label" "Concept" "page"', recent)
        self.assertIn('dict "label" "Entity" "page"', recent)
        self.assertIn('sort $recentConcepts "sort_key" "desc"', recent)
        self.assertIn('sort $recentEntities "sort_key" "desc"', recent)
        self.assertIn("first 3 $recentConcepts", recent)
        self.assertIn("first 3 $recentEntities", recent)

    def test_landing_uses_the_shared_five_card_knowledge_collection_section(self):
        layout = WIKI_LAYOUT.read_text()
        homepage = (ROOT / "layouts" / "index.html").read_text()
        collections = (ROOT / "layouts" / "partials" / "knowledge-collection-section.html").read_text()
        base = (ROOT / "layouts" / "_default" / "baseof.html").read_text()

        self.assertIn('partial "knowledge-collection-section.html"', layout)
        self.assertIn('partial "knowledge-collection-section.html"', homepage)
        self.assertEqual(collections.count("Explore the knowledge base"), 1)
        self.assertNotIn("Knowledge coverage", collections)
        self.assertIn('$site.GetPage "/episodes"', collections)
        self.assertIn('$site.GetPage "/show"', collections)

        for label in ("Episodes", "Shows", "Concepts", "Entities", "Source Notes"):
            self.assertIn(f">{label}</a>", collections)

        self.assertIn(".knowledge-collection-grid", base)
        self.assertIn("repeat(3, minmax(0, 1fr))", base)
        self.assertIn("@media (max-width: 760px)", base)
        self.assertIn("@media (max-width: 560px)", base)
        self.assertNotIn("wiki-stat-grid", layout)
        self.assertNotIn("wiki-stat", layout)

        self.assertIn("Browse by topic", layout)
        self.assertIn('.Site.GetPage "/topics"', layout)
        self.assertIn(".Params.topic_pages", layout)
        self.assertNotIn(".Site.Taxonomies.tags", layout)

    def test_landing_keeps_history_and_health_as_supporting_links(self):
        layout = WIKI_LAYOUT.read_text()
        current = (ROOT / "layouts" / "partials" / "current-knowledge-section.html").read_text()

        self.assertIn('$site.GetPage "/wiki-projections/update-history"', current)
        self.assertIn('.Site.GetPage "/wiki/stats"', layout)
        self.assertIn("See how the knowledge base has changed", current)
        self.assertIn("Update History", layout)
        self.assertIn("Wiki Stats", layout)


if __name__ == "__main__":
    unittest.main()
