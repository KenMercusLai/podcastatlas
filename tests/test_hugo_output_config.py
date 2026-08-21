from pathlib import Path
import tomllib
import unittest


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


if __name__ == "__main__":
    unittest.main()
