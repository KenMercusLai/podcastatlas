from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/benchmark-pagefind.mjs"


class SearchBenchmarkTest(unittest.TestCase):
    def make_fixture(self, root: Path, *, include_expected: bool = True) -> tuple[Path, Path, Path]:
        pagefind = root / "public/pagefind"
        pagefind.mkdir(parents=True)
        result = (
            "[{ data: async () => ({ url: '/wiki/entities/target/', "
            "meta: { type: 'Entity', group: 'People & Organizations' } }) }]"
            if include_expected
            else "[]"
        )
        (pagefind / "pagefind.js").write_text(
            "export function createInstance() { return {"
            "init: async () => {},"
            f"search: async () => ({{ results: {result} }}),"
            "destroy: async () => {}"
            "}; }\n",
            encoding="utf-8",
        )
        (pagefind / "pagefind-entry.json").write_text(
            json.dumps(
                {
                    "version": "1.5.2",
                    "languages": {"en-us": {"hash": "fixture", "wasm": "en-us", "page_count": 1}},
                }
            ),
            encoding="utf-8",
        )
        (pagefind / "fixture.pf_index").write_bytes(b"index bytes")
        fixture = root / "queries.json"
        fixture.write_text(
            json.dumps(
                {
                    "version": 1,
                    "queries": [
                        {
                            "id": "target",
                            "query": "target",
                            "locale": "en",
                            "kind": "entity",
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
        thresholds = root / "thresholds.json"
        thresholds.write_text(
            json.dumps(
                {
                    "version": 1,
                    "minimums": {
                        "page_count": 1,
                        "pages_per_second": 0,
                        "recall_at_5": 1,
                        "mrr": 1,
                    },
                    "maximums": {
                        "index_bytes": 1_000_000,
                        "hugo_ms": 10_000,
                        "pagefind_ms": 10_000,
                        "end_to_end_ms": 10_000,
                        "cold_query_p50_ms": 10_000,
                        "cold_query_p95_ms": 10_000,
                        "warm_query_p50_ms": 10_000,
                        "warm_query_p95_ms": 10_000,
                    },
                }
            ),
            encoding="utf-8",
        )
        return root / "public", fixture, thresholds

    def run_benchmark(
        self,
        public: Path,
        fixture: Path,
        thresholds: Path,
        report: Path,
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                "node",
                str(SCRIPT),
                str(public),
                str(fixture),
                str(thresholds),
                "--hugo-ms",
                "100",
                "--pagefind-ms",
                "50",
                "--prebenchmark-ms",
                "200",
                "--cold-rounds",
                "3",
                "--warm-rounds",
                "3",
                "--report",
                str(report),
            ],
            text=True,
            capture_output=True,
            check=False,
        )

    def test_benchmark_writes_reproducible_quality_size_and_latency_report(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            public, fixture, thresholds = self.make_fixture(root)
            report = root / "report.json"

            result = self.run_benchmark(public, fixture, thresholds, report)

            self.assertEqual(0, result.returncode, result.stderr)
            payload = json.loads(report.read_text(encoding="utf-8"))
            self.assertEqual(1, payload["version"])
            self.assertEqual("1.5.2", payload["pagefind_version"])
            self.assertEqual(1, payload["metrics"]["page_count"])
            self.assertGreater(payload["metrics"]["index_bytes"], len(b"index bytes"))
            self.assertEqual(100, payload["metrics"]["hugo_ms"])
            self.assertEqual(50, payload["metrics"]["pagefind_ms"])
            self.assertGreaterEqual(payload["metrics"]["end_to_end_ms"], 200)
            self.assertEqual(1, payload["metrics"]["recall_at_5"])
            self.assertEqual(1, payload["metrics"]["mrr"])
            self.assertEqual(3, payload["samples"]["cold_queries"])
            self.assertEqual(3, payload["samples"]["warm_queries"])
            self.assertEqual([], payload["threshold_failures"])

    def test_benchmark_fails_when_recall_regresses(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            public, fixture, thresholds = self.make_fixture(root, include_expected=False)
            report = root / "report.json"

            result = self.run_benchmark(public, fixture, thresholds, report)

            self.assertNotEqual(0, result.returncode)
            payload = json.loads(report.read_text(encoding="utf-8"))
            self.assertIn("recall_at_5", "\n".join(payload["threshold_failures"]))
            self.assertIn("mrr", "\n".join(payload["threshold_failures"]))

    def test_benchmark_fails_closed_on_index_and_latency_thresholds(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            public, fixture, thresholds = self.make_fixture(root)
            threshold_payload = json.loads(thresholds.read_text(encoding="utf-8"))
            threshold_payload["minimums"]["page_count"] = 2
            threshold_payload["minimums"]["pages_per_second"] = 1_000_000
            threshold_payload["maximums"].update(
                {
                    "index_bytes": 1,
                    "hugo_ms": 99,
                    "pagefind_ms": 49,
                    "end_to_end_ms": 199,
                    "cold_query_p50_ms": 0,
                    "cold_query_p95_ms": 0,
                    "warm_query_p50_ms": 0,
                    "warm_query_p95_ms": 0,
                }
            )
            thresholds.write_text(json.dumps(threshold_payload), encoding="utf-8")
            report = root / "report.json"

            result = self.run_benchmark(public, fixture, thresholds, report)

            self.assertNotEqual(0, result.returncode)
            payload = json.loads(report.read_text(encoding="utf-8"))
            failures = "\n".join(payload["threshold_failures"])
            for metric in (
                "page_count",
                "pages_per_second",
                "index_bytes",
                "hugo_ms",
                "pagefind_ms",
                "end_to_end_ms",
                "cold_query_p50_ms",
                "cold_query_p95_ms",
                "warm_query_p50_ms",
                "warm_query_p95_ms",
            ):
                self.assertIn(metric, failures)

    def test_build_runs_benchmark_after_semantic_checks(self):
        build_script = (ROOT / "build.sh").read_text(encoding="utf-8")
        benchmark = "node scripts/benchmark-pagefind.mjs"

        self.assertIn(benchmark, build_script)
        self.assertGreater(
            build_script.index(benchmark),
            build_script.index("scripts/verify-pagefind-same-name.sh"),
        )
        self.assertIn("SEARCH_BENCHMARK_REPORT", build_script)

    def test_ci_publishes_benchmark_report_to_job_summary(self):
        workflow = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")

        self.assertIn(".artifacts/search-benchmark.json", workflow)
        self.assertIn("GITHUB_STEP_SUMMARY", workflow)


if __name__ == "__main__":
    unittest.main()
