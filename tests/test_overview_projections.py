from __future__ import annotations

import hashlib
import importlib.util
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "prepare-overview-projections.py"
SPEC = importlib.util.spec_from_file_location("prepare_overview_projections", SCRIPT)
assert SPEC and SPEC.loader
prepare = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = prepare
SPEC.loader.exec_module(prepare)


def overview(update_paragraphs: list[str], synthesis: str, questions: list[str]) -> str:
    return (
        "---\ntitle: Overview\ntype: synthesis\n---\n\n"
        "# Overview\n\n"
        + "\n\n".join(update_paragraphs)
        + "\n\n## Current Synthesis\n\n"
        + synthesis
        + "\n\n## Open Questions\n\n"
        + "\n".join(f"- {question}" for question in questions)
        + "\n"
    )


class GitFixture:
    def __init__(self, root: Path):
        self.root = root
        self.overview_path = root / "content" / "wiki" / "overview.md"
        self.overview_path.parent.mkdir(parents=True)
        self.run("init", "-q")
        self.run("config", "user.name", "Test Author")
        self.run("config", "user.email", "test@example.com")

    def run(self, *args: str, env: dict[str, str] | None = None) -> str:
        result = subprocess.run(
            ["git", "-C", str(self.root), *args],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env,
        )
        return result.stdout

    def commit(self, message: str, timestamp: str) -> str:
        self.run("add", "content/wiki/overview.md")
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = timestamp
        env["GIT_COMMITTER_DATE"] = timestamp
        self.run("commit", "-q", "-m", message, env=env)
        return self.run("rev-parse", "HEAD").strip()


class OverviewSectionTest(unittest.TestCase):
    def test_extracts_explicit_current_sections_without_guessing_question_text(self):
        text = overview(
            ["The latest addition is [[SourceA]]."],
            "Current synthesis with a question mark? It remains synthesis.",
            ["Question one?", "Question two without punctuation"],
        )

        sections = prepare.split_overview_sections(text)

        self.assertEqual("Current synthesis with a question mark? It remains synthesis.", sections.current_synthesis)
        self.assertEqual("- Question one?\n- Question two without punctuation", sections.open_questions)

    def test_rejects_missing_or_duplicate_structural_headings(self):
        valid = overview(["Update."], "Synthesis.", ["Question?"])
        with self.assertRaisesRegex(ValueError, "exactly one"):
            prepare.split_overview_sections(valid.replace("## Open Questions", "## Questions"))
        with self.assertRaisesRegex(ValueError, "exactly one"):
            prepare.split_overview_sections(valid + "\n## Open Questions\n\n- Duplicate?\n")


class UpdateHistoryTest(unittest.TestCase):
    def test_groups_real_git_history_by_author_day_and_omits_days_without_updates(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture = GitFixture(Path(temp_dir))
            source_a_latest = "The latest addition is [[SourceA]], adding Alpha."
            maintenance_note = "*This page is maintained by the LLM. It is updated on every ingest to reflect the current synthesis across all sources.*"
            fixture.overview_path.write_text(
                overview([source_a_latest, maintenance_note], "Synthesis one.", ["Question one?"]),
                encoding="utf-8",
            )
            first = fixture.commit("add source A", "2026-08-01T23:30:00+10:00")

            source_a_previous = "The previous addition is [[SourceA]], adding Alpha."
            source_b_latest = "The latest addition is [[SourceB]], adding Beta."
            fixture.overview_path.write_text(
                overview([source_b_latest, source_a_previous], "Synthesis two.", ["Question one?"]),
                encoding="utf-8",
            )
            second = fixture.commit("add source B", "2026-08-01T23:45:00+10:00")

            fixture.overview_path.write_text(
                overview([source_b_latest, source_a_previous], "Synthesis only changed.", ["Question two?"]),
                encoding="utf-8",
            )
            fixture.commit("synthesis only", "2026-08-02T08:00:00+10:00")

            source_b_updated = "The latest addition is [[SourceB]], adding Beta and Gamma."
            fixture.overview_path.write_text(
                overview([source_b_updated, source_a_previous], "Synthesis only changed.", ["Question two?"]),
                encoding="utf-8",
            )
            fourth = fixture.commit("update source B summary", "2026-08-03T08:00:00+10:00")

            history = prepare.collect_update_history(
                fixture.root,
                Path("content/wiki/overview.md"),
                "Australia/Melbourne",
            )

            self.assertEqual(["2026-08-03", "2026-08-01"], list(history))
            self.assertEqual([fourth], [event.commit for event in history["2026-08-03"]])
            self.assertEqual(source_b_updated, history["2026-08-03"][0].markdown)
            self.assertEqual([first, second], [event.commit for event in history["2026-08-01"]])
            self.assertEqual([source_a_latest, source_b_latest], [event.markdown for event in history["2026-08-01"]])
            self.assertNotIn(maintenance_note, [event.markdown for events in history.values() for event in events])

    def test_rejects_shallow_history_instead_of_publishing_an_empty_archive(self):
        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as clone_parent:
            fixture = GitFixture(Path(source_dir))
            fixture.overview_path.write_text(overview(["Update one."], "Synthesis.", ["Question?"]), encoding="utf-8")
            fixture.commit("one", "2026-08-01T10:00:00+10:00")
            fixture.overview_path.write_text(overview(["Update two.", "Update one."], "Synthesis.", ["Question?"]), encoding="utf-8")
            fixture.commit("two", "2026-08-02T10:00:00+10:00")
            clone = Path(clone_parent) / "shallow"
            subprocess.run(
                ["git", "clone", "-q", "--depth", "1", f"file://{fixture.root}", str(clone)],
                check=True,
            )

            with self.assertRaisesRegex(RuntimeError, "full Git history"):
                prepare.collect_update_history(
                    clone,
                    Path("content/wiki/overview.md"),
                    "Australia/Melbourne",
                )


class ProjectionLifecycleTest(unittest.TestCase):
    def test_builds_independent_current_synthesis_history_and_questions_pages(self):
        sections = prepare.OverviewSections(
            update_history="ignored canonical history",
            current_synthesis="Current synthesis body.",
            open_questions="- Open one?\n- Open two?",
        )
        history = {
            "2026-08-03": [prepare.UpdateEvent("b" * 40, "Updated Gamma.")],
            "2026-08-01": [
                prepare.UpdateEvent("a" * 40, "Added Alpha."),
                prepare.UpdateEvent("c" * 40, "Added Beta."),
            ],
        }

        generated = prepare.expected_projection_files(Path("/repo"), sections, history)
        relative = {path.relative_to(Path("/repo")).as_posix(): body for path, body in generated.items()}

        self.assertEqual(
            {
                "content/wiki-projections/current-synthesis/index.md",
                "content/wiki-projections/open-questions/index.md",
                "content/wiki-projections/update-history/_index.md",
                "content/wiki-projections/update-history/2026-08-01/index.md",
                "content/wiki-projections/update-history/2026-08-03/index.md",
            },
            set(relative),
        )
        index = relative["content/wiki-projections/update-history/_index.md"]
        self.assertLess(index.index("2026-08-03"), index.index("2026-08-01"))
        self.assertNotIn("2026-08-02", index)
        self.assertIn("[2026-08-03](2026-08-03/)", index)
        synthesis = relative["content/wiki-projections/current-synthesis/index.md"]
        self.assertIn('title: "Current Synthesis"', synthesis)
        self.assertIn('url: "/wiki/current-synthesis/"', synthesis)
        self.assertIn('  - "/wiki/overview/"', synthesis)
        self.assertIn("# Current Synthesis", synthesis)
        self.assertIn("Current synthesis body.", synthesis)
        self.assertNotIn("## Update History", synthesis)
        self.assertNotIn("## Open Questions", synthesis)
        self.assertNotIn("../update-history/", synthesis)
        self.assertNotIn("../open-questions/", synthesis)
        self.assertIn("- Open one?", relative["content/wiki-projections/open-questions/index.md"])
        self.assertNotIn("ignored canonical history", "".join(relative.values()))

    def test_repeated_write_is_idempotent_removes_stale_generated_dates_and_preserves_source(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            canonical = root / "content" / "wiki" / "overview.md"
            canonical.parent.mkdir(parents=True)
            canonical.write_text(overview(["Update."], "Synthesis.", ["Question?"]), encoding="utf-8")
            before = hashlib.sha256(canonical.read_bytes()).hexdigest()
            sections = prepare.split_overview_sections(canonical.read_text(encoding="utf-8"))
            expected = prepare.expected_projection_files(
                root,
                sections,
                {"2026-08-03": [prepare.UpdateEvent("a" * 40, "Update.")]},
            )

            first = prepare.sync_projection_files(root, expected)
            second = prepare.sync_projection_files(root, expected)
            stale = root / "content" / "wiki-projections" / "update-history" / "2026-08-02" / "index.md"
            stale.parent.mkdir(parents=True)
            stale.write_text(prepare.GENERATED_NOTICE + "\n", encoding="utf-8")
            third = prepare.sync_projection_files(root, expected)

            self.assertTrue(first)
            self.assertEqual([], second)
            self.assertIn(stale.resolve(), [path.resolve() for path in third])
            self.assertFalse(stale.exists())
            self.assertEqual(before, hashlib.sha256(canonical.read_bytes()).hexdigest())

    def test_rejects_a_generated_output_symlink_that_escapes_the_repository(self):
        with tempfile.TemporaryDirectory() as temp_dir, tempfile.TemporaryDirectory() as outside_dir:
            root = Path(temp_dir)
            output = root / "content" / "wiki-projections"
            output.parent.mkdir(parents=True)
            output.symlink_to(Path(outside_dir), target_is_directory=True)
            expected = {
                output / "overview" / "index.md": prepare.GENERATED_NOTICE + "\n",
            }

            with self.assertRaisesRegex(RuntimeError, "generated directory"):
                prepare.sync_projection_files(root, expected)

    def test_refuses_to_delete_an_unmarked_file_from_the_generated_tree(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            output = root / "content" / "wiki-projections"
            manual = output / "update-history" / "manual.md"
            manual.parent.mkdir(parents=True)
            manual.write_text("Manual content.\n", encoding="utf-8")
            expected = {
                output / "overview" / "index.md": prepare.GENERATED_NOTICE + "\n",
            }

            with self.assertRaisesRegex(RuntimeError, "unmarked projection file"):
                prepare.sync_projection_files(root, expected)
            self.assertEqual("Manual content.\n", manual.read_text(encoding="utf-8"))


class RepositoryIntegrationTest(unittest.TestCase):
    def test_build_generates_projections_before_hugo_and_ignores_canonical_overview(self):
        build_script = (ROOT / "build.sh").read_text(encoding="utf-8")
        projection_command = "python3 scripts/prepare-overview-projections.py"
        wiki_command = "python3 scripts/prepare-wiki-content.py"
        hugo_command = "hugo build "
        self.assertIn(projection_command, build_script)
        self.assertLess(build_script.index(projection_command), build_script.index(wiki_command))
        self.assertLess(build_script.index(projection_command), build_script.index(hugo_command))

        hugo_config = (ROOT / "hugo.toml").read_text(encoding="utf-8")
        self.assertIn(r"content/wiki/overview\.md$", hugo_config)
        gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
        self.assertIn("/content/wiki-projections/", gitignore.splitlines())

    def test_generated_wiki_pages_use_wiki_rendering_for_single_and_list_routes(self):
        single = (ROOT / "layouts" / "_default" / "single.html").read_text(encoding="utf-8")
        wiki_list = (ROOT / "layouts" / "wiki" / "list.html").read_text(encoding="utf-8")
        wiki_content = (ROOT / "layouts" / "partials" / "wiki-content.html").read_text(encoding="utf-8")
        self.assertIn('(eq .Type "wiki")', single)
        self.assertIn(".Params.wiki_projection", wiki_list)
        self.assertIn('eq .Path "/wiki"', wiki_list)
        self.assertNotIn('eq .RelPermalink ("/wiki/" | relURL)', wiki_list)
        self.assertIn('partial "wiki-content.html" .', wiki_list)
        self.assertIn('.Site.GetPage "/wiki-projections/current-synthesis"', wiki_list)
        self.assertNotIn('.Site.GetPage "/wiki-projections/overview"', wiki_list)
        self.assertIn('.Site.GetPage "/wiki-projections/update-history"', wiki_list)
        self.assertIn('.Site.GetPage "/wiki-projections/open-questions"', wiki_list)
        self.assertIn("$page.Params.wiki_projection", wiki_content)
        self.assertIn("$escapedLabel", wiki_content)
        self.assertIn('strings.TrimPrefix "/" $targetPage.url | relURL', wiki_content)


if __name__ == "__main__":
    unittest.main()
