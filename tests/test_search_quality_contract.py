from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/verify-pagefind-queries.mjs"
FIXTURE = ROOT / "tests/fixtures/pagefind_queries.json"


class SearchQualityContractTest(unittest.TestCase):
    def test_query_suite_covers_languages_aliases_and_all_groups(self):
        payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
        queries = payload["queries"]

        self.assertEqual(1, payload["version"])
        self.assertGreaterEqual(len(queries), 16)
        self.assertEqual({"zh", "en", "mixed"}, {item["locale"] for item in queries})
        self.assertIn("alias", {item["kind"] for item in queries})
        self.assertEqual(
            {
                "Concepts & Topics",
                "People & Organizations",
                "Episodes",
                "Shows",
                "Source Notes",
            },
            {item["expected_group"] for item in queries},
        )

    def test_build_runs_semantic_verifier_after_pagefind(self):
        build_script = (ROOT / "build.sh").read_text(encoding="utf-8")
        pagefind = "./node_modules/.bin/pagefind --site public"
        verifier = (
            "node scripts/verify-pagefind-queries.mjs "
            "public tests/fixtures/pagefind_queries.json"
        )

        self.assertIn(verifier, build_script)
        self.assertGreater(build_script.index(verifier), build_script.index(pagefind))

    def test_build_runs_same_name_fixture_after_production_query_contract(self):
        build_script = (ROOT / "build.sh").read_text(encoding="utf-8")
        production_verifier = (
            "node scripts/verify-pagefind-queries.mjs "
            "public tests/fixtures/pagefind_queries.json"
        )
        fixture_verifier = "scripts/verify-pagefind-same-name.sh"

        self.assertTrue((ROOT / fixture_verifier).is_file())
        self.assertIn(fixture_verifier, build_script)
        self.assertGreater(
            build_script.index(fixture_verifier),
            build_script.index(production_verifier),
        )

    def test_same_name_fixture_proves_a_registry_only_alias(self):
        fixture_root = ROOT / "tests/fixtures/pagefind_same_name"
        queries = json.loads((fixture_root / "queries.json").read_text(encoding="utf-8"))
        alias_query = next(
            item for item in queries["queries"] if item["kind"] == "registry-alias"
        )
        target = fixture_root / "content/wiki/entities/CanonicalIdentity.md"
        script = (ROOT / "scripts/verify-pagefind-same-name.sh").read_text(encoding="utf-8")

        self.assertTrue(target.is_file())
        self.assertNotIn(alias_query["query"].casefold(), target.read_text(encoding="utf-8").casefold())
        self.assertIn("layouts/partials/search-aliases.html", script)

    def test_verifier_uses_the_same_alias_metadata_weight_as_the_browser(self):
        verifier = SCRIPT.read_text(encoding="utf-8")

        self.assertIn("metaWeights: { aliases: 10.0 }", verifier)

    def test_verifier_checks_real_result_rank_type_and_group(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pagefind_dir = root / "public/pagefind"
            pagefind_dir.mkdir(parents=True)
            (pagefind_dir / "pagefind.js").write_text(
                "export function createInstance() { return {"
                "init: async () => {},"
                "search: async (query) => ({ results: query === 'found' ? ["
                "{ data: async () => ({ url: 'https://example.test/project/wiki/entities/target/', meta: { type: 'Entity', group: 'People & Organizations' } }) }"
                "] : [] })"
                "}; }\n",
                encoding="utf-8",
            )
            fixture = root / "queries.json"
            fixture.write_text(
                json.dumps(
                    {
                        "version": 1,
                        "queries": [
                            {
                                "id": "target-alias",
                                "query": "found",
                                "locale": "en",
                                "kind": "alias",
                                "filters": {"group": "People & Organizations"},
                                "expected_url": "/wiki/entities/target/",
                                "expected_type": "Entity",
                                "expected_group": "People & Organizations",
                                "max_rank": 1,
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )

            passed = subprocess.run(
                ["node", str(SCRIPT), str(root / "public"), str(fixture)],
                text=True,
                capture_output=True,
                check=False,
            )
            fixture.write_text(
                fixture.read_text(encoding="utf-8").replace(
                    "/wiki/entities/target/", "/wiki/entities/missing/"
                ),
                encoding="utf-8",
            )
            failed = subprocess.run(
                ["node", str(SCRIPT), str(root / "public"), str(fixture)],
                text=True,
                capture_output=True,
                check=False,
            )

        self.assertEqual(0, passed.returncode, passed.stderr)
        self.assertIn('"passed": 1', passed.stdout)
        self.assertNotEqual(0, failed.returncode)
        self.assertIn("target-alias", failed.stderr)

    def test_verifier_requires_both_same_name_results(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pagefind_dir = root / "public/pagefind"
            pagefind_dir.mkdir(parents=True)
            module_path = pagefind_dir / "pagefind.js"
            module_path.write_text(
                "export function createInstance() { return {"
                "init: async () => {},"
                "search: async () => ({ results: ["
                "{ data: async () => ({ url: '/wiki/concepts/shared/', meta: { type: 'Concept', group: 'Concepts & Topics' } }) }"
                "] })"
                "}; }\n",
                encoding="utf-8",
            )
            fixture = root / "queries.json"
            fixture.write_text(
                json.dumps(
                    {
                        "version": 1,
                        "queries": [
                            {
                                "id": "same-name-unfiltered",
                                "query": "Shared Identity",
                                "locale": "en",
                                "kind": "same-name",
                                "expected_url": "/wiki/concepts/shared/",
                                "expected_type": "Concept",
                                "expected_group": "Concepts & Topics",
                                "max_rank": 2,
                                "also_expected_results": [
                                    {
                                        "url": "/wiki/entities/shared/",
                                        "type": "Entity",
                                        "group": "People & Organizations"
                                    }
                                ],
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )

            missing = subprocess.run(
                ["node", str(SCRIPT), str(root / "public"), str(fixture)],
                text=True,
                capture_output=True,
                check=False,
            )
            module_path.write_text(
                module_path.read_text(encoding="utf-8").replace(
                    "] })",
                    ", { data: async () => ({ url: '/wiki/entities/shared/', meta: { type: 'Entity', group: 'People & Organizations' } }) }] })",
                ),
                encoding="utf-8",
            )
            complete = subprocess.run(
                ["node", str(SCRIPT), str(root / "public"), str(fixture)],
                text=True,
                capture_output=True,
                check=False,
            )

        self.assertNotEqual(0, missing.returncode)
        self.assertIn("same-name-unfiltered", missing.stderr)
        self.assertEqual(0, complete.returncode, complete.stderr)


if __name__ == "__main__":
    unittest.main()
