from pathlib import Path
import shlex
import unittest


ROOT = Path(__file__).resolve().parents[1]


class BuildScriptTest(unittest.TestCase):
    def test_hugo_build_cleans_stale_destination_files(self):
        build_script = (ROOT / "build.sh").read_text()
        hugo_command = next(
            line.strip()
            for line in build_script.splitlines()
            if line.strip().startswith("hugo build ")
        )

        self.assertIn("--cleanDestinationDir", shlex.split(hugo_command))


if __name__ == "__main__":
    unittest.main()
