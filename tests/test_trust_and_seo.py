from pathlib import Path
import struct
import unittest


ROOT = Path(__file__).resolve().parents[1]
BASE_LAYOUT = ROOT / "layouts/_default/baseof.html"
SEO_PARTIAL = ROOT / "layouts/partials/seo.html"
HOME_LAYOUT = ROOT / "layouts/index.html"


class TrustAndSeoTest(unittest.TestCase):
    def test_every_html_page_gets_canonical_social_and_structured_metadata(self):
        base = BASE_LAYOUT.read_text()
        seo = SEO_PARTIAL.read_text() if SEO_PARTIAL.exists() else ""
        home = HOME_LAYOUT.read_text()

        self.assertIn('partial "seo.html" .', base)
        self.assertIn('<link rel="canonical" href="{{ .Permalink }}">', seo)
        self.assertIn('name="description"', seo)
        self.assertIn('property="og:title"', seo)
        self.assertIn('property="og:description"', seo)
        self.assertIn('property="og:url"', seo)
        self.assertIn('property="og:image"', seo)
        self.assertIn('name="twitter:card" content="summary_large_image"', seo)
        self.assertIn('type="application/ld+json"', seo)
        self.assertIn('$schemaJSON | safeJS', seo)
        self.assertIn('replace $schemaJSON "https://schema.org" `https:\\/\\/schema.org`', seo)
        self.assertIn('"@context" "https://schema.org"', seo)
        self.assertIn("hugo.Data.wiki_links", seo)
        self.assertIn('findRE `\\[\\[[^\\]\\n]+\\]\\]` $summary', seo)
        self.assertIn('replaceRE `\\s+` " " $description', seo)
        self.assertIn('replaceRE `(?i)^(?:概览|overview|摘要|summary)', seo)
        self.assertIn('property="og:image:alt"', seo)
        self.assertIn('name="twitter:image:alt"', seo)
        self.assertNotIn('<link rel="canonical"', home)

    def test_about_and_methodology_explain_scope_provenance_and_limits(self):
        about_path = ROOT / "content/about.md"
        methodology_path = ROOT / "content/methodology.md"
        about = about_path.read_text() if about_path.exists() else ""
        methodology = methodology_path.read_text() if methodology_path.exists() else ""

        self.assertIn('title: "About"', about)
        self.assertIn("a living knowledge atlas synthesized from podcasts", about)
        self.assertIn("not a podcast directory", about)
        self.assertIn('relref "/methodology.md"', about)

        self.assertIn('title: "Methodology"', methodology)
        self.assertIn("## How the atlas is built", methodology)
        self.assertIn("## Evidence and provenance", methodology)
        self.assertIn("## Limitations and corrections", methodology)
        self.assertIn("AI-assisted", methodology)
        self.assertIn("original audio", methodology)
        self.assertIn("Source Note", methodology)
        self.assertIn("not independent fact-checking", methodology)
        self.assertIn("GitHub", methodology)

    def test_trust_pages_use_a_general_page_rendering_branch(self):
        single = (ROOT / "layouts/_default/single.html").read_text()

        self.assertIn('{{ else if eq .Section "episodes" }}', single)
        self.assertIn('<article class="informational-page">', single)
        self.assertIn('partial "informational-content.html" .', single)
        informational = (ROOT / "layouts/partials/informational-content.html").read_text()
        self.assertIn('<div class="content">{{ .Content }}</div>', informational)

    def test_footer_exposes_trust_and_project_navigation(self):
        base = BASE_LAYOUT.read_text()

        self.assertIn('aria-label="Footer"', base)
        self.assertIn('{{ "about/" | relURL }}', base)
        self.assertIn('{{ "methodology/" | relURL }}', base)
        self.assertIn('{{ "wiki/update-history/" | relURL }}', base)
        self.assertIn("A living knowledge atlas synthesized from podcasts.", base)
        self.assertIn("github.com/KenMercusLai/podcastatlas", base)
        self.assertIn("footer-links", base)

    def test_robots_and_social_card_are_publishable(self):
        config = (ROOT / "hugo.toml").read_text()
        robots_path = ROOT / "layouts/robots.txt"
        robots = robots_path.read_text() if robots_path.exists() else ""
        image_path = ROOT / "static/images/podcast-atlas-social.png"

        self.assertIn("enableRobotsTXT = true", config)
        self.assertIn("User-agent: *", robots)
        self.assertIn("Allow: /", robots)
        self.assertIn('{{ "sitemap.xml" | absURL }}', robots)
        self.assertTrue(image_path.exists())

        image = image_path.read_bytes() if image_path.exists() else b""
        self.assertEqual(b"\x89PNG\r\n\x1a\n", image[:8])
        self.assertEqual((1200, 630), struct.unpack(">II", image[16:24]))


if __name__ == "__main__":
    unittest.main()
