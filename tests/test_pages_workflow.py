from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "pages.yml"


class PagesWorkflowTest(unittest.TestCase):
    def test_builds_once_and_deploys_the_same_pages_artifact(self):
        workflow = WORKFLOW.read_text()

        self.assertIn("push:", workflow)
        self.assertIn("branches: [master]", workflow)
        self.assertIn("pull_request:", workflow)
        self.assertIn("workflow_dispatch:", workflow)
        self.assertIn("submodules: recursive", workflow)
        self.assertIn("fetch-depth: 0", workflow)
        self.assertIn("persist-credentials: false", workflow)
        self.assertEqual(1, workflow.count("./build.sh"))
        self.assertIn("scripts/verify-pages-output.py public", workflow)
        self.assertIn("path: public", workflow)
        self.assertIn("needs: build", workflow)
        self.assertIn("pages: write", workflow)
        self.assertIn("id-token: write", workflow)
        self.assertIn("environment:", workflow)
        self.assertIn("name: github-pages", workflow)
        self.assertIn("cancel-in-progress: true", workflow)

    def test_uses_pinned_official_pages_actions(self):
        workflow = WORKFLOW.read_text()

        expected_actions = {
            "actions/checkout": "3d3c42e5aac5ba805825da76410c181273ba90b1",  # v7.0.1
            "actions/configure-pages": "45bfe0192ca1faeb007ade9deae92b16b8254a0d",  # v6.0.0
            "actions/upload-pages-artifact": "fc324d3547104276b827a68afc52ff2a11cc49c9",  # v5.0.0
            "actions/deploy-pages": "cd2ce8fcbc39b97be8ca5fce6e763baed58fa128",  # v5.0.0
        }
        for action, revision in expected_actions.items():
            self.assertIn(f"uses: {action}@{revision}", workflow)


if __name__ == "__main__":
    unittest.main()
