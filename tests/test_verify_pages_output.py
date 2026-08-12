import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "verify-pages-output.py"


def load_verifier():
    spec = importlib.util.spec_from_file_location("verify_pages_output", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write(path, content=""):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


class VerifyPagesOutputTest(unittest.TestCase):
    def test_accepts_the_expected_site_output(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            for relative in [
                "episodes/index.html",
                "tags/index.html",
                "shows/index.html",
                "wiki/index.html",
                "episodes/example/index.html",
                "episodes/example/index.md",
            ]:
                write(public / relative, "content")
            write(public / "index.xml", "<rss />")
            write(public / "episodes/index.xml", "<rss />")
            write(public / "sitemap.xml", "<urlset />")

            report = verifier.validate(public)

        self.assertEqual([], report["errors"])
        self.assertEqual(9, report["file_count"])

    def test_rejects_taxonomy_rss(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            write(public / "tags" / "example" / "index.xml", "<rss />")

            report = verifier.validate(public)

        self.assertIn(
            "forbidden taxonomy RSS: tags/example/index.xml",
            report["errors"],
        )

    def test_rejects_symbolic_links(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            write(public / "target.txt", "content")
            (public / "linked.txt").symlink_to(public / "target.txt")

            report = verifier.validate(public)

        self.assertIn("symbolic link not allowed: linked.txt", report["errors"])

    def test_rejects_artifacts_larger_than_one_gibibyte(self):
        verifier = load_verifier()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            oversized = public / "oversized.bin"
            with oversized.open("wb") as output:
                output.truncate((1024 ** 3) + 1)

            report = verifier.validate(public)

        self.assertIn(
            "artifact exceeds the GitHub Pages 1 GiB supported limit",
            report["errors"],
        )


if __name__ == "__main__":
    unittest.main()
