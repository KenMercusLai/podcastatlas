from html.parser import HTMLParser
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "layouts/_default/baseof.html"


class StylesheetParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stylesheets = []
        self.inline_styles = []
        self.in_style = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.stylesheets.append(attrs["href"])
        if tag == "style":
            self.in_style = True

    def handle_endtag(self, tag):
        if tag == "style":
            self.in_style = False

    def handle_data(self, data):
        if self.in_style:
            self.inline_styles.append(data)


class SharedStylesheetTest(unittest.TestCase):
    def test_global_css_is_not_repeated_in_every_html_page(self):
        base = BASE.read_text()
        self.assertNotIn("<style>", base)
        self.assertIn('resources.Get "css/site.css"', base)
        self.assertIn(".RelPermalink", base)
        self.assertTrue((ROOT / "assets/css/site.css").is_file())

    @unittest.skipUnless(shutil.which("hugo"), "Hugo required for rendered fixture")
    def test_shared_css_preserves_prefix_and_cascade_for_all_page_slugs(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            site = Path(temp_dir)
            (site / "hugo.toml").write_text(
                "title = 'Fixture'\n[outputs]\nhome = ['HTML']\nsection = ['HTML']\n"
            )
            layouts = site / "layouts/_default"
            layouts.mkdir(parents=True)
            shutil.copyfile(BASE, layouts / "baseof.html")
            shutil.copytree(ROOT / "layouts/partials", site / "layouts/partials")
            if (ROOT / "assets").is_dir():
                shutil.copytree(ROOT / "assets", site / "assets")
            template = (
                '{{ define "head_extra" }}<style>.fixture { color: red; }</style>{{ end }}'
                '{{ define "main" }}<h1>{{ .Title }}</h1>{{ end }}'
            )
            (site / "layouts/index.html").write_text(template)
            (layouts / "single.html").write_text(template)
            (layouts / "list.html").write_text(template)
            pages = site / "content/pages"
            pages.mkdir(parents=True)
            slugs = ("ordinary", "episode.160", "café-東京")
            for slug in slugs:
                (pages / f"{slug}.md").write_text(f"+++\ntitle = '{slug}'\n+++\nBody.\n")
            for prefix in ("/", "/podcastatlas/"):
                with self.subTest(prefix=prefix):
                    result = subprocess.run(
                        ["hugo", "build", "--source", str(site), "--minify",
                         "--cleanDestinationDir", "--baseURL", f"https://example.test{prefix}"],
                        text=True, capture_output=True,
                    )
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                    public = site / "public"
                    hrefs = set()
                    for relative in ("index.html", *(f"pages/{slug}/index.html" for slug in slugs)):
                        html = (public / relative).read_text()
                        parser = StylesheetParser()
                        parser.feed(html)
                        self.assertEqual(len(parser.stylesheets), 1, relative)
                        href = parser.stylesheets[0]
                        self.assertTrue(href.startswith(prefix + "css/site."), href)
                        self.assertTrue(href.endswith(".css"), href)
                        self.assertNotIn("--bg", "".join(parser.inline_styles))
                        self.assertLess(html.index(".fixture"), html.index(href))
                        hrefs.add(href)
                    self.assertEqual(len(hrefs), 1)
                    css_path = unquote(urlsplit(hrefs.pop()).path.removeprefix(prefix))
                    css = (public / css_path).read_text()
                    for marker in ("--bg", ".pagination", ".knowledge-collection-grid", "max-width:640px"):
                        self.assertIn(marker, css)
                    self.assertEqual(len(list((public / "css").glob("*.css"))), 1)


if __name__ == "__main__":
    unittest.main()
