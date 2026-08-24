from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "prepare-show-profiles.py"
SPEC = importlib.util.spec_from_file_location("prepare_show_profiles", SCRIPT)
assert SPEC and SPEC.loader
prepare = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = prepare
SPEC.loader.exec_module(prepare)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


class ShowProfilesTest(unittest.TestCase):
    def test_show_profile_generator_exists(self):
        self.assertTrue(SCRIPT.is_file(), "show profile generator is missing")

    def test_committed_projection_matches_the_current_corpus(self):
        expected = prepare.render_payload(prepare.build_show_profiles())
        actual = (ROOT / "data" / "show_profiles.json").read_text(encoding="utf-8")
        self.assertEqual(expected, actual)

    def test_profiles_derive_identity_topics_entities_and_start_here(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            episodes = root / "episodes"
            sources = root / "sources"
            entities = root / "entities"
            write(
                episodes / "a.md",
                "+++\ntitle = 'Episode A'\ndate = 2026-01-01T00:00:00Z\nshow = 'Example Show'\n+++\n",
            )
            write(
                episodes / "b.md",
                "+++\ntitle = 'Episode B'\ndate = 2026-02-01T00:00:00Z\nshow = 'Example Show'\n+++\n",
            )
            write(
                episodes / "c.md",
                "+++\ntitle = 'Episode C'\ndate = 2026-03-01T00:00:00Z\nshow = 'Other Show'\n+++\n",
            )
            write(
                sources / "source-a.md",
                "---\ntitle: Source A\nsource_file: '/canonical/a.md'\n---\n",
            )
            write(
                sources / "source-b.md",
                "---\ntitle: Source B\nsource_file: '/canonical/b.md'\n---\n",
            )
            write(
                entities / "Acme.md",
                "---\ntitle: Acme\ntype: entity\ntags: [company]\nsources: [source-a, source-b]\n---\n",
            )
            write(
                entities / "Alice.md",
                "---\ntitle: Alice\ntype: entity\ntags: [person]\nsources: [source-a, source-b]\n---\n",
            )
            write(
                entities / "OneOff.md",
                "---\ntitle: One Off\ntype: entity\ntags: [person]\nsources: [source-a]\n---\n",
            )
            write(
                entities / "Product.md",
                "---\ntitle: Product\ntype: entity\ntags: [product]\nsources: [source-a, source-b]\n---\n",
            )
            membership = root / "membership.json"
            membership.write_text(
                json.dumps(
                    {
                        "source-a": [
                            {"key": "technology", "label": "Technology", "url": "/topics/technology/"}
                        ],
                        "source-b": [
                            {"key": "technology", "label": "Technology", "url": "/topics/technology/"},
                            {"key": "economics", "label": "Economics", "url": "/topics/economics/"},
                        ],
                    }
                ),
                encoding="utf-8",
            )
            wiki_links = root / "wiki-links.json"
            wiki_links.write_text(
                json.dumps(
                    {
                        "Acme": {"title": "Acme", "url": "/wiki/entities/acme/"},
                        "Alice": {"title": "Alice", "url": "/wiki/entities/alice/"},
                    }
                ),
                encoding="utf-8",
            )

            result = prepare.build_show_profiles(
                episodes,
                sources,
                entities,
                membership,
                wiki_links,
            )

            profile = result["shows"]["Example Show"]
            self.assertEqual(2, profile["episode_count"])
            self.assertNotIn("description", profile)
            self.assertNotIn("language", profile)
            self.assertEqual("2026-01-01", profile["earliest_episode_date"])
            self.assertEqual("2026-02-01", profile["latest_episode_date"])
            self.assertEqual("b.md", profile["latest_episode_file"])
            self.assertEqual(2, profile["source_note_count"])
            self.assertEqual(2, profile["topic_matched_source_note_count"])
            self.assertEqual(
                [
                    {"key": "technology", "label": "Technology", "url": "/topics/technology/", "source_note_count": 2},
                    {"key": "economics", "label": "Economics", "url": "/topics/economics/", "source_note_count": 1},
                ],
                profile["topics"],
            )
            self.assertEqual(
                [
                    {"key": "Acme", "title": "Acme", "url": "/wiki/entities/acme/", "kind": "organization", "episode_count": 2},
                    {"key": "Alice", "title": "Alice", "url": "/wiki/entities/alice/", "kind": "person", "episode_count": 2},
                ],
                profile["entities"],
            )
            self.assertEqual(["b.md", "a.md"], profile["start_here_episode_files"])
            self.assertEqual(["c.md"], result["shows"]["Other Show"]["start_here_episode_files"])

            membership.write_text(
                json.dumps(
                    {
                        "source-a": [
                            {"key": "technology", "label": "Technology", "url": "https://evil.test/topics/technology/"}
                        ]
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "invalid controlled topic route"):
                prepare.build_show_profiles(
                    episodes_dir=episodes,
                    sources_dir=sources,
                    entities_dir=entities,
                    topic_membership_path=membership,
                    wiki_links_path=wiki_links,
                )

    def test_build_pipeline_and_show_taxonomy_render_generated_profile(self):
        build_script = (ROOT / "build.sh").read_text(encoding="utf-8")
        taxonomy = (ROOT / "layouts" / "_default" / "taxonomy.html").read_text(encoding="utf-8")
        self.assertIn("python3 scripts/prepare-show-profiles.py", build_script)
        self.assertIn('partial "show-profile.html" .', taxonomy)
        self.assertNotIn('partial "show-profile.html" .', taxonomy.split("{{ else }}", 1)[0])
        show_profile = ROOT / "layouts" / "partials" / "show-profile.html"
        self.assertTrue(show_profile.is_file())
        rendered = show_profile.read_text(encoding="utf-8")
        for marker in (
            'class="show-identity"',
            'class="show-topic-profile"',
            'class="show-entities"',
            'class="show-start-here"',
            "Complete archive",
        ):
            self.assertIn(marker, rendered)
        self.assertNotIn("/tags/", rendered)
        self.assertIn('partial "canonical-show-name.html"', rendered)
        self.assertIn("$episodePage := .", rendered)
        show_list = (ROOT / "layouts" / "partials" / "show-list.html").read_text(encoding="utf-8")
        self.assertIn('partial "canonical-show-name.html"', show_list)
        self.assertIn('>{{ $sourceTitle }}</a>', show_list)

    def test_show_profile_layout_has_responsive_styles(self):
        base = (ROOT / "layouts" / "_default" / "baseof.html").read_text(encoding="utf-8")
        for selector in (
            ".show-facts",
            ".show-profile-list",
            ".show-identity-header",
            ".show-start-list",
        ):
            self.assertIn(selector, base)
        self.assertRegex(base, r"@media \(max-width: 640px\)[\s\S]*?\.show-facts")

    def test_exact_show_identity_is_shared_by_heading_title_and_schema(self):
        canonical = ROOT / "layouts" / "partials" / "canonical-show-name.html"
        self.assertTrue(canonical.is_file())
        for relative in (
            "layouts/partials/show-profile.html",
            "layouts/partials/show-list.html",
            "layouts/partials/page-title.html",
            "layouts/partials/seo.html",
        ):
            source = (ROOT / relative).read_text(encoding="utf-8")
            self.assertIn('partial "canonical-show-name.html"', source, relative)


if __name__ == "__main__":
    unittest.main()
