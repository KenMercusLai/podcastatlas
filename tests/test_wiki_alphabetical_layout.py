from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class WikiAlphabeticalLayoutTest(unittest.TestCase):
    def test_renders_only_the_selected_static_bucket_with_accessible_tabs(self):
        layout = (ROOT / "layouts" / "wiki" / "list.html").read_text()
        partial = (ROOT / "layouts" / "partials" / "wiki-alphabetical-list.html").read_text()

        self.assertIn(".Params.wiki_alphabetical", layout)
        self.assertIn('partial "wiki-alphabetical-list.html" .', layout)
        self.assertIn(".Params.wiki_pages", partial)
        self.assertIn('class="wiki-letter-tabs"', partial)
        self.assertIn('aria-label="Browse by first character"', partial)
        self.assertIn('aria-current="page"', partial)
        self.assertIn('slice "#" "0-9" "a"', partial)
        self.assertIn('cond (eq $bucket "#") "symbols" $bucket', partial)
        self.assertIn('strings.TrimPrefix "/" $page.url | relURL', partial)
        self.assertNotIn("<script", partial)
        self.assertNotIn(".RegularPages", partial)

    def test_build_generates_indexes_before_hugo(self):
        build_script = (ROOT / "build.sh").read_text()
        prepare_command = "python3 scripts/prepare-wiki-content.py"
        hugo_command = "hugo build "

        self.assertIn(prepare_command, build_script)
        self.assertLess(build_script.index(prepare_command), build_script.index(hugo_command))

    def test_tabs_wrap_without_changing_the_single_column_page_list(self):
        base_layout = (ROOT / "layouts" / "_default" / "baseof.html").read_text()

        self.assertIn(".wiki-letter-tabs", base_layout)
        self.assertIn("flex-wrap: wrap", base_layout)
        self.assertIn(".wiki-letter-tab.is-active", base_layout)
        self.assertIn(".page-list li", base_layout)


if __name__ == "__main__":
    unittest.main()
