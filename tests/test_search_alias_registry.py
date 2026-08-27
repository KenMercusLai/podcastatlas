from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate-search-aliases.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_search_aliases", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


class SearchAliasRegistryTest(unittest.TestCase):
    def test_repository_registry_contains_evidenced_aliases(self):
        validator = load_validator()
        registry = ROOT / "data/search_aliases.json"

        payload = json.loads(registry.read_text(encoding="utf-8"))

        self.assertGreaterEqual(len(payload["entries"]), 10)
        self.assertEqual([], validator.validate_registry(ROOT, registry))

    def test_accepts_an_alias_with_canonical_wikilink_evidence(self):
        validator = load_validator()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write(
                root / "content/wiki/entities/FoodAndDrugAdministration.md",
                '---\ntitle: "Food and Drug Administration"\ntype: entity\n---\n',
            )
            write(
                root / "content/wiki/concepts/FoodSafety.md",
                "---\ntitle: Food Safety\ntype: concept\n---\n\n"
                "The regulator is [[FoodAndDrugAdministration|FDA]].\n",
            )
            registry = root / "data/search_aliases.json"
            write(
                registry,
                json.dumps(
                    {
                        "version": 1,
                        "entries": {
                            "wiki/entities/FoodAndDrugAdministration.md": {
                                "aliases": [
                                    {
                                        "value": "FDA",
                                        "evidence": [
                                            {
                                                "path": "content/wiki/concepts/FoodSafety.md",
                                                "wikilink": "[[FoodAndDrugAdministration|FDA]]",
                                            }
                                        ],
                                    }
                                ]
                            }
                        },
                    }
                ),
            )

            self.assertEqual([], validator.validate_registry(root, registry))

    def test_rejects_generated_overview_as_alias_evidence(self):
        validator = load_validator()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write(
                root / "content/wiki/entities/FoodAndDrugAdministration.md",
                '---\ntitle: "Food and Drug Administration"\n---\n',
            )
            write(
                root / "content/wiki/overview.md",
                "[[FoodAndDrugAdministration|FDA]]\n",
            )
            registry = root / "data/search_aliases.json"
            write(
                registry,
                json.dumps(
                    {
                        "version": 1,
                        "entries": {
                            "wiki/entities/FoodAndDrugAdministration.md": {
                                "aliases": [
                                    {
                                        "value": "FDA",
                                        "evidence": [
                                            {
                                                "path": "content/wiki/overview.md",
                                                "wikilink": "[[FoodAndDrugAdministration|FDA]]",
                                            }
                                        ],
                                    }
                                ]
                            }
                        },
                    }
                ),
            )

            errors = validator.validate_registry(root, registry)

        self.assertTrue(any("canonical wiki page" in error for error in errors), errors)

    def test_rejects_target_path_traversal(self):
        validator = load_validator()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write(root / "outside.md", "---\ntitle: Outside\n---\n")
            write(
                root / "content/wiki/concepts/Evidence.md",
                "[[outside|Alias]]\n",
            )
            registry = root / "data/search_aliases.json"
            write(
                registry,
                json.dumps(
                    {
                        "version": 1,
                        "entries": {
                            "../outside.md": {
                                "aliases": [
                                    {
                                        "value": "Alias",
                                        "evidence": [
                                            {
                                                "path": "content/wiki/concepts/Evidence.md",
                                                "wikilink": "[[outside|Alias]]",
                                            }
                                        ],
                                    }
                                ]
                            }
                        },
                    }
                ),
            )

            errors = validator.validate_registry(root, registry)

        self.assertTrue(any("canonical content path" in error for error in errors), errors)

    def test_rejects_one_alias_claimed_by_multiple_targets(self):
        validator = load_validator()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for key in ("One", "Two"):
                write(
                    root / f"content/wiki/entities/{key}.md",
                    f"---\ntitle: {key}\n---\n",
                )
                write(
                    root / f"content/wiki/concepts/{key}Evidence.md",
                    f"[[{key}|Shared Alias]]\n",
                )
            entries = {}
            for key in ("One", "Two"):
                entries[f"wiki/entities/{key}.md"] = {
                    "aliases": [
                        {
                            "value": "Shared Alias",
                            "evidence": [
                                {
                                    "path": f"content/wiki/concepts/{key}Evidence.md",
                                    "wikilink": f"[[{key}|Shared Alias]]",
                                }
                            ],
                        }
                    ]
                }
            registry = root / "data/search_aliases.json"
            write(registry, json.dumps({"version": 1, "entries": entries}))

            errors = validator.validate_registry(root, registry)

        self.assertTrue(any("claimed by multiple targets" in error for error in errors), errors)

    def test_rejects_self_aliases_and_casefolded_duplicates(self):
        validator = load_validator()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write(
                root / "content/wiki/entities/One.md",
                "---\ntitle: One\n---\n",
            )
            evidence = root / "content/wiki/concepts/Evidence.md"
            write(
                evidence,
                "[[One|One]] [[One|Duplicate]] [[One|duplicate]]\n",
            )
            registry = root / "data/search_aliases.json"
            write(
                registry,
                json.dumps(
                    {
                        "version": 1,
                        "entries": {
                            "wiki/entities/One.md": {
                                "aliases": [
                                    {
                                        "value": value,
                                        "evidence": [
                                            {
                                                "path": "content/wiki/concepts/Evidence.md",
                                                "wikilink": f"[[One|{value}]]",
                                            }
                                        ],
                                    }
                                    for value in ("One", "Duplicate", "duplicate")
                                ]
                            }
                        },
                    }
                ),
            )

            errors = validator.validate_registry(root, registry)

        self.assertTrue(any("does not add a new search term" in error for error in errors), errors)
        self.assertTrue(any("duplicate alias" in error for error in errors), errors)

    def test_rejects_aliases_longer_than_one_hundred_characters(self):
        validator = load_validator()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            value = "x" * 101
            write(root / "content/wiki/entities/One.md", "---\ntitle: One\n---\n")
            write(
                root / "content/wiki/concepts/Evidence.md",
                f"[[One|{value}]]\n",
            )
            registry = root / "data/search_aliases.json"
            write(
                registry,
                json.dumps(
                    {
                        "version": 1,
                        "entries": {
                            "wiki/entities/One.md": {
                                "aliases": [
                                    {
                                        "value": value,
                                        "evidence": [
                                            {
                                                "path": "content/wiki/concepts/Evidence.md",
                                                "wikilink": f"[[One|{value}]]",
                                            }
                                        ],
                                    }
                                ]
                            }
                        },
                    }
                ),
            )

            errors = validator.validate_registry(root, registry)

        self.assertTrue(any("at most 100 characters" in error for error in errors), errors)

    def test_rejects_symlinked_alias_targets_and_evidence(self):
        validator = load_validator()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            actual_target = root / "content/wiki/entities/Actual.md"
            actual_evidence = root / "content/wiki/concepts/ActualEvidence.md"
            write(actual_target, "---\ntitle: One\n---\n")
            write(actual_evidence, "[[One|Alias]]\n")

            target = root / "content/wiki/entities/One.md"
            target.symlink_to(actual_target)
            evidence = root / "content/wiki/concepts/Evidence.md"
            evidence.symlink_to(actual_evidence)
            registry = root / "data/search_aliases.json"
            write(
                registry,
                json.dumps(
                    {
                        "version": 1,
                        "entries": {
                            "wiki/entities/One.md": {
                                "aliases": [
                                    {
                                        "value": "Alias",
                                        "evidence": [
                                            {
                                                "path": "content/wiki/concepts/Evidence.md",
                                                "wikilink": "[[One|Alias]]",
                                            }
                                        ],
                                    }
                                ]
                            }
                        },
                    }
                ),
            )

            errors = validator.validate_registry(root, registry)

        self.assertTrue(any("symbolic link" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
