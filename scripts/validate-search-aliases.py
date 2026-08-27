#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / "data" / "search_aliases.json"


def _load_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"alias registry does not exist: {path}")
    except json.JSONDecodeError as exc:
        errors.append(f"alias registry is not valid JSON: {exc}")
    return None


def _contains_symbolic_link(path: Path, anchor: Path) -> bool:
    anchor = anchor.resolve()
    path = path.parent.resolve() / path.name
    try:
        relative_path = path.relative_to(anchor)
    except ValueError:
        return True
    current = anchor
    for part in relative_path.parts:
        current = current / part
        if current.is_symlink():
            return True
    return False


def _canonical_title(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        for line in text.splitlines()[1:]:
            if line == "---":
                break
            if line.startswith("title:"):
                return line.split(":", 1)[1].strip().strip("\"'")
    return path.stem


def validate_registry(root: Path, registry_path: Path) -> list[str]:
    errors: list[str] = []
    payload = _load_json(registry_path, errors)
    if payload is None:
        return errors
    if not isinstance(payload, dict):
        return ["alias registry root must be an object"]
    if payload.get("version") != 1:
        errors.append("alias registry version must be 1")
    entries = payload.get("entries")
    if not isinstance(entries, dict) or not entries:
        errors.append("alias registry entries must be a non-empty object")
        return errors

    alias_claims: dict[str, set[str]] = {}
    for target_path, record in entries.items():
        if not isinstance(target_path, str) or not isinstance(record, dict):
            errors.append("each alias entry must map a string target path to an object")
            continue
        target_rel = Path(target_path)
        target_parts = target_rel.parts
        if (
            target_rel.is_absolute()
            or ".." in target_parts
            or len(target_parts) != 3
            or target_parts[0] != "wiki"
            or target_parts[1] not in {"concepts", "entities", "sources"}
            or target_rel.suffix != ".md"
            or target_rel.name == "_index.md"
        ):
            errors.append(f"alias target must be a canonical content path: {target_path}")
            continue
        content_root = (root / "content").resolve()
        target = content_root / target_rel
        if _contains_symbolic_link(target, content_root):
            errors.append(f"alias target contains a symbolic link: content/{target_path}")
            continue
        try:
            target.resolve().relative_to(content_root)
        except ValueError:
            errors.append(f"alias target escapes the content root: {target_path}")
            continue
        if not target.is_file():
            errors.append(f"alias target does not exist: content/{target_path}")
            continue
        aliases = record.get("aliases")
        if not isinstance(aliases, list) or not aliases:
            errors.append(f"alias target has no aliases: content/{target_path}")
            continue
        target_key = target.stem
        target_title = _canonical_title(target)
        seen_aliases: set[str] = set()
        for alias_record in aliases:
            if not isinstance(alias_record, dict):
                errors.append(f"alias record must be an object: content/{target_path}")
                continue
            value = alias_record.get("value")
            evidence = alias_record.get("evidence")
            if not isinstance(value, str) or not value.strip():
                errors.append(f"alias value must be a non-empty string: content/{target_path}")
                continue
            value = value.strip()
            if len(value) > 100:
                errors.append(
                    f"alias must be at most 100 characters: {value!r} for content/{target_path}"
                )
            folded_value = value.casefold()
            if folded_value in {target_key.casefold(), target_title.casefold()}:
                errors.append(
                    f"alias does not add a new search term: {value!r} for content/{target_path}"
                )
            if folded_value in seen_aliases:
                errors.append(f"duplicate alias for content/{target_path}: {value!r}")
            seen_aliases.add(folded_value)
            alias_claims.setdefault(folded_value, set()).add(target_path)
            if not isinstance(evidence, list) or not evidence:
                errors.append(f"alias has no evidence: {value!r} for content/{target_path}")
                continue
            expected_wikilink = f"[[{target_key}|{value}]]"
            for item in evidence:
                if not isinstance(item, dict):
                    errors.append(f"alias evidence must be an object: {value!r}")
                    continue
                evidence_path = item.get("path")
                wikilink = item.get("wikilink")
                if wikilink != expected_wikilink:
                    errors.append(
                        f"alias evidence wikilink must equal {expected_wikilink!r}: {wikilink!r}"
                    )
                    continue
                if not isinstance(evidence_path, str):
                    errors.append(f"alias evidence path must be a string: {value!r}")
                    continue
                evidence_rel = Path(evidence_path)
                canonical_parts = evidence_rel.parts
                if (
                    evidence_rel.is_absolute()
                    or ".." in canonical_parts
                    or canonical_parts[:2] != ("content", "wiki")
                    or evidence_rel.name in {"overview.md", "stats.md", "_index.md"}
                    or any(part in {"_generated", "by-letter", "by-key"} for part in canonical_parts)
                ):
                    errors.append(
                        f"alias evidence must be a canonical wiki page: {evidence_path}"
                    )
                    continue
                source = root / evidence_rel
                wiki_root = (root / "content/wiki").resolve()
                if _contains_symbolic_link(source, wiki_root):
                    errors.append(
                        f"alias evidence contains a symbolic link: {evidence_path}"
                    )
                    continue
                try:
                    source.resolve().relative_to(wiki_root)
                except ValueError:
                    errors.append(f"alias evidence escapes the wiki root: {evidence_path}")
                    continue
                if not source.is_file():
                    errors.append(f"alias evidence file does not exist: {evidence_path}")
                    continue
                if expected_wikilink not in source.read_text(encoding="utf-8"):
                    errors.append(
                        f"alias evidence not found in {evidence_path}: {expected_wikilink}"
                    )
    for folded_alias, targets in sorted(alias_claims.items()):
        if len(targets) > 1:
            errors.append(
                f"alias {folded_alias!r} is claimed by multiple targets: "
                + ", ".join(sorted(targets))
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate canonical Pagefind aliases.")
    parser.add_argument("registry", nargs="?", type=Path, default=DEFAULT_REGISTRY)
    args = parser.parse_args()
    errors = validate_registry(ROOT, args.registry)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Search aliases valid: {args.registry.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
