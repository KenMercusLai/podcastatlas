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

    def test_hugo_build_forwards_cli_arguments(self):
        build_script = (ROOT / "build.sh").read_text()
        hugo_command = next(
            line.strip()
            for line in build_script.splitlines()
            if line.strip().startswith("hugo build ")
        )

        self.assertTrue(hugo_command.endswith('"$@"'))

    def test_pagefind_indexes_the_complete_hugo_output_after_the_build(self):
        build_script = (ROOT / "build.sh").read_text()
        hugo_position = build_script.index(
            'hugo build --gc --minify --cleanDestinationDir "$@"'
        )
        pagefind_command = "./node_modules/.bin/pagefind --site public"

        self.assertIn(pagefind_command, build_script)
        pagefind_position = build_script.index(pagefind_command)
        pagefind_args = shlex.split(pagefind_command)
        self.assertGreater(pagefind_position, hugo_position)
        self.assertNotIn("--glob", pagefind_args)
        self.assertNotIn("--exclude-selectors", pagefind_args)


if __name__ == "__main__":
    unittest.main()
