import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "prepare-on-this-day.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("prepare_on_this_day", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class OnThisDayProjectionTest(unittest.TestCase):
    def test_generates_a_stable_route_for_every_calendar_date(self):
        generator = load_generator()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            generator.generate(root)

            generated = root / "content" / "on-this-day"
            date_pages = sorted(generated.glob("??-??/_index.md"))
            self.assertEqual(366, len(date_pages))
            self.assertTrue((generated / "02-29" / "_index.md").is_file())
            self.assertIn('month_day: "02-29"', (generated / "02-29" / "_index.md").read_text())
            self.assertIn("On This Day", (generated / "_index.md").read_text())

    def test_generation_is_idempotent_and_checkable(self):
        generator = load_generator()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)

            self.assertEqual(367, len(generator.generate(root)))
            self.assertEqual([], generator.generate(root))
            self.assertEqual([], generator.generate(root, check=True))

    def test_stale_owned_files_are_removed_but_unowned_files_fail_closed(self):
        generator = load_generator()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            generator.generate(root)
            generated = root / "content" / "on-this-day"
            stale = generated / "retired" / "_index.md"
            stale.parent.mkdir()
            stale.write_text(f"{generator.GENERATED_NOTICE}\n")

            generator.generate(root)
            self.assertFalse(stale.exists())

            unowned = generated / "manual.md"
            unowned.write_text("manual content\n")
            with self.assertRaisesRegex(ValueError, "Refusing to remove unowned file"):
                generator.generate(root)

    def test_existing_expected_path_must_already_be_generator_owned(self):
        generator = load_generator()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manual = root / "content" / "on-this-day" / "01-01" / "_index.md"
            manual.parent.mkdir(parents=True)
            manual.write_text("manual content\n")

            with self.assertRaisesRegex(ValueError, "Refusing to overwrite unowned file"):
                generator.generate(root)

    def test_symlinked_output_ancestor_cannot_escape_the_repository(self):
        generator = load_generator()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "repo"
            outside = Path(directory) / "outside"
            root.mkdir()
            outside.mkdir()
            (root / "content").symlink_to(outside, target_is_directory=True)

            with self.assertRaisesRegex(ValueError, "outside repository"):
                generator.generate(root)

            self.assertEqual([], list(outside.iterdir()))

    def test_nested_symlink_in_generated_tree_is_rejected(self):
        generator = load_generator()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "repo"
            outside = Path(directory) / "outside"
            root.mkdir()
            outside.mkdir()
            generator.generate(root)
            nested = root / "content" / "on-this-day" / "linked"
            nested.symlink_to(outside, target_is_directory=True)

            with self.assertRaisesRegex(ValueError, "must not contain symlinks"):
                generator.generate(root)

            self.assertEqual([], list(outside.iterdir()))


class UpdatesCenterLayoutTest(unittest.TestCase):
    def test_build_prepares_route_pages_before_hugo(self):
        build_script = (ROOT / "build.sh").read_text()
        generator = "python3 scripts/prepare-on-this-day.py"
        hugo = 'hugo build --gc --minify --cleanDestinationDir "$@"'

        self.assertIn(generator, build_script)
        self.assertLess(build_script.index(generator), build_script.index(hugo))
        self.assertIn("/content/on-this-day/", (ROOT / ".gitignore").read_text())

    def test_updates_center_unifies_the_three_update_views(self):
        layout = (ROOT / "layouts" / "updates" / "list.html").read_text()
        base = (ROOT / "layouts" / "_default" / "baseof.html").read_text()

        self.assertIn("Recently Updated", layout)
        self.assertIn("On This Day", layout)
        self.assertIn("Full Update History", layout)
        self.assertIn('"/wiki-projections/update-history"', layout)
        self.assertIn('"updates/" | relURL', base)

    def test_on_this_day_uses_melbourne_and_an_explicit_around_date_fallback(self):
        data_partial = (
            ROOT / "layouts" / "partials" / "on-this-day-data.html"
        ).read_text()
        archive = (ROOT / "layouts" / "on-this-day" / "list.html").read_text()
        episode_list = (
            ROOT / "layouts" / "partials" / "on-this-day-episode-list.html"
        ).read_text()

        self.assertIn('time.In "Australia/Melbourne"', data_partial)
        self.assertIn('.Date | time.In "Australia/Melbourne"', data_partial)
        self.assertIn('"published" $published', data_partial)
        self.assertIn('"displayDate"', data_partial)
        self.assertIn('"intro"', data_partial)
        self.assertIn('"archivePage"', data_partial)
        self.assertIn("Around this date", data_partial)
        self.assertIn('first 5', data_partial)
        self.assertIn('where $onThisDay.entries "year"', archive)
        self.assertIn('.published.Format "2006-01-02"', episode_list)

    def test_homepage_uses_the_shared_date_selection_and_links_the_archive(self):
        homepage = (ROOT / "layouts" / "index.html").read_text()

        self.assertIn('partial "on-this-day-data.html"', homepage)
        self.assertIn("archivePage.RelPermalink", homepage)
        self.assertNotIn("$today := now.UTC", homepage)
        self.assertNotIn("eq .Date.Month", homepage)


if __name__ == "__main__":
    unittest.main()
