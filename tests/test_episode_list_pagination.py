from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "hugo.toml"
LIST_LAYOUT = ROOT / "layouts/_default/list.html"
PAGINATION_PARTIAL = ROOT / "layouts/partials/pagination.html"
SEO_PARTIAL = ROOT / "layouts/partials/seo.html"
PAGE_TITLE_PARTIAL = ROOT / "layouts/partials/page-title.html"
BASE_LAYOUT = ROOT / "layouts/_default/baseof.html"


class EpisodeListPaginationTest(unittest.TestCase):
    def test_episode_section_uses_static_pages_of_one_hundred_items(self):
        config = CONFIG.read_text()
        layout = LIST_LAYOUT.read_text()

        self.assertIn("[pagination]", config)
        self.assertIn("pagerSize = 100", config)
        self.assertIn("path = 'page'", config)
        self.assertIn('if eq .Section "episodes"', layout)
        self.assertIn('$episodePages := .Pages.ByDate.Reverse', layout)
        self.assertIn('.Paginate $episodePages', layout)
        self.assertIn('"pages" $paginator.Pages', layout)
        self.assertIn('partial "pagination.html" $paginator', layout)

    def test_pagination_navigation_is_accessible_and_compact(self):
        pagination = PAGINATION_PARTIAL.read_text() if PAGINATION_PARTIAL.exists() else ""
        base = BASE_LAYOUT.read_text()

        self.assertIn('aria-label="Episode pages"', pagination)
        self.assertIn(".HasPrev", pagination)
        self.assertIn(".Prev.URL", pagination)
        self.assertIn("Page {{ .PageNumber }} of {{ .TotalPages }}", pagination)
        self.assertIn(".HasNext", pagination)
        self.assertIn(".Next.URL", pagination)
        self.assertIn('class="pagination"', pagination)
        self.assertIn(".pagination", base)
        self.assertIn("grid-template-columns: 1fr 1fr;", base)
        self.assertIn("grid-column: 1 / -1;", base)
        self.assertIn("overflow-wrap: anywhere;", base)

    def test_paginated_episode_pages_get_unique_metadata_urls(self):
        seo = SEO_PARTIAL.read_text()
        page_title = PAGE_TITLE_PARTIAL.read_text()
        base = BASE_LAYOUT.read_text()

        self.assertIn('and (eq .Kind "section") (eq .Section "episodes")', seo)
        self.assertIn('$episodePaginator := .Paginate $episodePages', seo)
        self.assertIn('$canonicalURL = $episodePaginator.URL | absURL', seo)
        self.assertIn('"url" $canonicalURL', seo)
        self.assertIn('href="{{ $canonicalURL }}"', seo)
        self.assertIn('property="og:url" content="{{ $canonicalURL }}"', seo)
        self.assertIn('partial "page-title.html" .', seo)
        self.assertIn('partial "page-title.html" .', base)
        self.assertIn('Page %d | %s', page_title)

    def test_footer_omits_the_github_repository_link(self):
        base = BASE_LAYOUT.read_text()

        self.assertNotIn("github.com/KenMercusLai/podcastatlas", base)
        self.assertIn('{{ "about/" | relURL }}', base)
        self.assertIn('{{ "methodology/" | relURL }}', base)
        self.assertIn('{{ "wiki/update-history/" | relURL }}', base)


if __name__ == "__main__":
    unittest.main()
