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


if __name__ == "__main__":
    unittest.main()
