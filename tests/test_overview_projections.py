from __future__ import annotations

import hashlib
import importlib.util
import json
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
    def test_prefers_valid_compact_synthesis_without_modifying_automatic_overview(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            compact = root / "content" / "wiki" / "_generated" / "synthesis" / "current.md"
            compact.parent.mkdir(parents=True)
            compact_text = (
                "<!-- Generated by tools.synthesis; do not edit manually. -->\n"
                "---\n"
                "schema_version: 1\n"
                "generated: true\n"
                "synthesis_source: compact\n"
                "last_updated: 2026-08-23\n"
                "as_of_overview_commit: abc123\n"
                "summary: A compact cross-source knowledge map.\n"
                "episode_count: 10\n"
                "source_count: 9\n"
                "topic_count: 8\n"
                "---\n\n"
                "# Current Synthesis\n\n"
                "## Executive Summary\n\nCompact body.\n\n"
                "## Synthesis by Domain\n\nDomain body.\n"
            )
            compact.write_text(compact_text, encoding="utf-8")
            topics = {}
            paragraphs = [{"id": "paragraph-1"}]
            for index in range(8):
                topic_id = f"topic-{index}"
                topic_text = f"# Topic {index}\n"
                claims = {"topic_id": topic_id, "summary": f"Topic {index} summary.", "claims": []}
                topic_path = compact.parent / "topics" / f"{topic_id}.md"
                claims_path = compact.parent / "claims" / f"{topic_id}.json"
                topic_path.parent.mkdir(parents=True, exist_ok=True)
                claims_path.parent.mkdir(parents=True, exist_ok=True)
                topic_path.write_text(topic_text, encoding="utf-8")
                claims_path.write_text(json.dumps(claims), encoding="utf-8")
                topics[topic_id] = {
                    "output_digest": hashlib.sha256(topic_text.encode()).hexdigest(),
                    "claim_digest": prepare._digest_json(claims),
                }
            (compact.parent / "paragraph-ledger.json").write_text(
                json.dumps(
                    {
                        "overview_digest": "overview-digest",
                        "paragraphs": paragraphs,
                        "coverage": {"paragraph_count": 1},
                    }
                ),
                encoding="utf-8",
            )
            (compact.parent / "manifest.json").write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "generated": True,
                        "overview_digest": "overview-digest",
                        "overview_commit": "newer-root-commit",
                        "paragraph_count": 1,
                        "corpus": {"episode_count": 11, "source_count": 10},
                        "topics": topics,
                        "global": {
                            "output_digest": hashlib.sha256(compact_text.encode()).hexdigest(),
                            "overview_commit": "abc123",
                            "content_date": "2026-08-23",
                            "corpus": {"episode_count": 10, "source_count": 9},
                        },
                    }
                ),
                encoding="utf-8",
            )
            sections = prepare.OverviewSections("history", "Automatic raw synthesis.", "questions")

            source = prepare.load_current_synthesis(root, sections)

            self.assertIn("## Executive Summary\n\nCompact body.", source.body)
            self.assertIn("## Synthesis by Domain\n\nDomain body.", source.body)
            self.assertEqual("2026-08-23", source.last_updated)
            self.assertEqual("abc123", source.as_of_overview_commit)
            self.assertEqual("A compact cross-source knowledge map.", source.summary)
            self.assertEqual("compact", source.synthesis_source)
            self.assertEqual(10, source.episode_count)
            self.assertEqual(9, source.source_count)
            self.assertEqual(8, source.topic_count)
            self.assertNotIn("Automatic raw synthesis.", source.body)

            claims_path = compact.parent / "claims" / "topic-7.json"
            original_claims = claims_path.read_text(encoding="utf-8")
            claims_path.write_text(json.dumps({"topic_id": "tampered"}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "claims .* digest differs"):
                prepare.load_current_synthesis(root, sections)
            claims_path.write_text(original_claims, encoding="utf-8")

            outside = root / "outside-current.md"
            outside.write_text(compact_text, encoding="utf-8")
            compact.unlink()
            compact.symlink_to(outside)
            with self.assertRaisesRegex(ValueError, "symbolic link"):
                prepare.load_current_synthesis(root, sections)
            compact.unlink()
            compact.write_text(compact_text, encoding="utf-8")

            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.name", "Test"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=root, check=True)
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            subprocess.run(["git", "commit", "-qm", "compact"], cwd=root, check=True)
            compact.write_text(compact_text + "Tampered.\n", encoding="utf-8")

            historical = prepare.load_current_synthesis(root, sections)

            self.assertEqual("compact", historical.synthesis_source)
            self.assertNotIn("Tampered", historical.body)

    def test_missing_compact_synthesis_keeps_automatic_overview_as_compatibility_fallback(self):
        sections = prepare.OverviewSections("history", "Automatic raw synthesis.", "questions")

        with tempfile.TemporaryDirectory() as temp_dir:
            source = prepare.load_current_synthesis(Path(temp_dir), sections)

        self.assertEqual("Automatic raw synthesis.", source.body)
        self.assertEqual("", source.last_updated)
        self.assertEqual("Automatic raw synthesis.", source.summary)

    def test_existing_invalid_compact_synthesis_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            compact = root / "content" / "wiki" / "_generated" / "synthesis" / "current.md"
            compact.parent.mkdir(parents=True)
            compact.write_text("# Current Synthesis\n\nUnmarked output.\n", encoding="utf-8")
            sections = prepare.OverviewSections("history", "Automatic raw synthesis.", "questions")

            with self.assertRaisesRegex(ValueError, "generated compact synthesis"):
                prepare.load_current_synthesis(root, sections)

    def test_projection_exposes_compact_summary_and_update_metadata(self):
        source = prepare.CurrentSynthesisSource(
            body="## Executive Summary\n\nCompact body.\n\n## Synthesis by Domain\n\nDomain body.",
            summary="A compact cross-source knowledge map.",
            last_updated="2026-08-23",
            as_of_overview_commit="abc123",
            synthesis_source="compact",
            episode_count=10,
            source_count=9,
            topic_count=8,
        )

        page = prepare.current_synthesis_page(source)

        self.assertIn('summary: "A compact cross-source knowledge map."', page)
        self.assertIn('description: "A compact cross-source knowledge map."', page)
        self.assertIn('synthesis_source: "compact"', page)
        self.assertIn("episode_count: 10", page)
        self.assertIn("source_count: 9", page)
        self.assertIn("topic_count: 8", page)
        self.assertIn('last_updated: "2026-08-23"', page)
        self.assertIn('as_of_overview_commit: "abc123"', page)
        self.assertIn('<time datetime="2026-08-23">August 23, 2026</time>', page)
        self.assertIn("## Executive Summary", page)

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
        self.assertIn(r"content/wiki/_generated/", hugo_config)
        gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
        self.assertIn("/content/wiki-projections/", gitignore.splitlines())


    def test_generated_wiki_pages_use_wiki_rendering_for_single_and_list_routes(self):
        single = (ROOT / "layouts" / "_default" / "single.html").read_text(encoding="utf-8")
        wiki_list = (ROOT / "layouts" / "wiki" / "list.html").read_text(encoding="utf-8")
        current_knowledge = (
            ROOT / "layouts" / "partials" / "current-knowledge-section.html"
        ).read_text(encoding="utf-8")
        wiki_content = (ROOT / "layouts" / "partials" / "wiki-content.html").read_text(encoding="utf-8")
        self.assertIn('(eq .Type "wiki")', single)
        self.assertIn('class="current-synthesis"', single)
        self.assertIn(".Params.synthesis_source", single)
        self.assertIn(".Params.summary", single)
        self.assertIn(".Params.episode_count", single)
        self.assertIn(".Params.source_count", single)
        self.assertIn("synthesis-updated", single)
        self.assertIn("Coverage snapshot:", single)
        self.assertIn(".Params.wiki_projection", wiki_list)
        self.assertIn('eq .Path "/wiki"', wiki_list)
        self.assertNotIn('eq .RelPermalink ("/wiki/" | relURL)', wiki_list)
        self.assertIn('partial "wiki-content.html" .', wiki_list)
        self.assertIn('partial "current-knowledge-section.html"', wiki_list)
        self.assertIn('$site.GetPage "/wiki-projections/current-synthesis"', current_knowledge)
        self.assertIn("Params.summary", current_knowledge)
        self.assertIn("Params.last_updated", current_knowledge)
        self.assertIn("Params.episode_count", current_knowledge)
        self.assertIn("Params.source_count", current_knowledge)
        self.assertIn("wiki-feature-coverage", current_knowledge)
        self.assertNotIn("The atlas's evolving account of ideas and claims across all processed podcast sources.", current_knowledge)
        self.assertNotIn('.Site.GetPage "/wiki-projections/overview"', wiki_list)
        self.assertIn('.Site.GetPage "/wiki-projections/update-history"', wiki_list)
        self.assertIn('$site.GetPage "/wiki-projections/open-questions"', current_knowledge)
        self.assertIn("$page.Params.wiki_projection", wiki_content)
        self.assertIn("$escapedLabel", wiki_content)
        self.assertIn('strings.TrimPrefix "/" $targetPage.url | relURL', wiki_content)


if __name__ == "__main__":
    unittest.main()
