from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class BasePathLinksTest(unittest.TestCase):
    def test_internal_navigation_respects_a_pages_project_base_path(self):
        templates = "\n".join(
            (ROOT / relative).read_text()
            for relative in (
                "layouts/_default/baseof.html",
                "layouts/index.html",
                "layouts/wiki/list.html",
            )
        )

        for path in ("episodes/", "shows/", "wiki/"):
            self.assertIn(f'"{path}" | relURL', templates)
            self.assertNotIn(f'"/{path}" | relURL', templates)
        self.assertNotIn('"/episodes/" | absURL', templates)
        self.assertIn('eq .Path "/wiki"', templates)
        self.assertNotIn('eq .RelPermalink ("/wiki/" | relURL)', templates)


if __name__ == "__main__":
    unittest.main()
