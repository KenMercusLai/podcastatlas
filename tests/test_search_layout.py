from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
BASE_LAYOUT = ROOT / "layouts" / "_default" / "baseof.html"


class SearchLayoutTest(unittest.TestCase):
    def test_every_html_page_is_indexed_without_a_page_level_allowlist(self):
        layout = BASE_LAYOUT.read_text()

        self.assertNotIn("data-pagefind-body", layout)
        self.assertIn('<header class="site-header" data-pagefind-ignore="all">', layout)
        self.assertIn('<footer class="site-footer" data-pagefind-ignore="all">', layout)

    def test_every_site_page_links_to_search(self):
        layout = BASE_LAYOUT.read_text()

        self.assertIn('href="{{ "search/" | relURL }}">Search</a>', layout)

    def test_search_page_loads_pagefind_from_the_deployment_base_path(self):
        content = ROOT / "content" / "search" / "_index.md"
        layout = ROOT / "layouts" / "search" / "list.html"

        self.assertTrue(content.is_file())
        self.assertTrue(layout.is_file())
        rendered = layout.read_text()
        self.assertIn('{{ "pagefind/pagefind-component-ui.css" | relURL }}', rendered)
        self.assertIn('{{ "pagefind/pagefind-component-ui.js" | relURL }}', rendered)
        self.assertIn('type="module"', rendered)
        self.assertIn(
            'bundle-path="{{ "pagefind/" | relURL }}"',
            rendered,
        )
        self.assertNotIn("base-url=", rendered)
        self.assertIn("<pagefind-input></pagefind-input>", rendered)
        self.assertIn("<pagefind-summary></pagefind-summary>", rendered)
        self.assertIn("<pagefind-filter-pane></pagefind-filter-pane>", rendered)
        self.assertIn("<pagefind-results></pagefind-results>", rendered)
        self.assertNotIn("<pagefind-searchbox", rendered)
        self.assertIn('data-pagefind-ignore="all"', rendered)

    def test_every_page_exposes_searchable_type_metadata(self):
        layout = BASE_LAYOUT.read_text()
        type_partial = ROOT / "layouts" / "partials" / "search-type.html"

        self.assertTrue(type_partial.is_file())
        self.assertIn('partial "search-type.html" .', layout)
        self.assertIn('data-pagefind-filter="type[content]"', layout)
        self.assertIn('data-pagefind-meta="type[content]"', layout)

        classifier = type_partial.read_text()
        self.assertIn('.Section "episodes"', classifier)
        self.assertIn(".Params.type", classifier)
        self.assertIn('.Data.Singular "show"', classifier)
        self.assertIn('.Data.Singular "tag"', classifier)
        self.assertIn('.Data.Singular "category"', classifier)


if __name__ == "__main__":
    unittest.main()
