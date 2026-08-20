#!/usr/bin/env python3

from pathlib import Path
import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET


REQUIRED_FILES = (
    "index.html",
    "index.xml",
    "episodes/index.xml",
    "sitemap.xml",
    "episodes/index.html",
    "tags/index.html",
    "shows/index.html",
    "wiki/index.html",
    "search/index.html",
    "pagefind/pagefind.js",
    "pagefind/pagefind-component-ui.js",
    "pagefind/pagefind-component-ui.css",
)
WIKI_LINK_RE = re.compile(r"\[\[[^\]\n]+\]\]")


def validate(public_dir: Path) -> dict:
    public_dir = public_dir.resolve()
    files = [path for path in public_dir.rglob("*") if path.is_file()]
    errors = []

    for path in public_dir.rglob("*"):
        if path.is_symlink():
            relative = path.relative_to(public_dir).as_posix()
            errors.append(f"symbolic link not allowed: {relative}")

    for relative in REQUIRED_FILES:
        if not (public_dir / relative).is_file():
            errors.append(f"missing required file: {relative}")

    homepage = public_dir / "index.html"
    if homepage.is_file():
        homepage_html = homepage.read_text(encoding="utf-8")
        if re.search(
            r"http-equiv\s*=\s*(?:[\"']\s*refresh\s*[\"']|refresh\b)",
            homepage_html,
            re.IGNORECASE,
        ):
            errors.append("homepage is still an automatic redirect")
        if "A living knowledge atlas synthesized from podcasts." not in homepage_html:
            errors.append("homepage is missing the discovery introduction")

    pagefind_dir = public_dir / "pagefind"
    if not list(pagefind_dir.glob("*.pf_meta")):
        errors.append("missing Pagefind metadata index")
    if not list((pagefind_dir / "index").glob("*.pf_index")):
        errors.append("missing Pagefind search index")
    if not list((pagefind_dir / "fragment").glob("*.pf_fragment")):
        errors.append("missing Pagefind result fragments")

    for section in ("tags", "shows", "categories"):
        section_dir = public_dir / section
        if section_dir.is_dir():
            for path in section_dir.rglob("index.xml"):
                relative = path.relative_to(public_dir).as_posix()
                errors.append(f"forbidden taxonomy RSS: {relative}")

    wiki_dir = public_dir / "wiki"
    if wiki_dir.is_dir():
        for path in sorted(wiki_dir.rglob("*.html")):
            match = WIKI_LINK_RE.search(path.read_text(encoding="utf-8"))
            if match:
                relative = path.relative_to(public_dir).as_posix()
                errors.append(
                    f"unresolved wiki link in generated HTML: {relative}: {match.group(0)}"
                )
                break

    episode_html = list((public_dir / "episodes").glob("*/index.html"))
    if not episode_html:
        errors.append("no episode detail HTML found")
    elif not any(path.with_suffix(".md").is_file() for path in episode_html):
        errors.append("no episode detail Markdown found")

    for relative in ("index.xml", "episodes/index.xml", "sitemap.xml"):
        path = public_dir / relative
        if path.is_file():
            try:
                ET.parse(path)
            except ET.ParseError as error:
                errors.append(f"invalid XML: {relative}: {error}")

    total_bytes = sum(path.stat().st_size for path in files)
    if total_bytes > 1024 ** 3:
        errors.append("artifact exceeds the GitHub Pages 1 GiB supported limit")

    return {
        "public_dir": str(public_dir),
        "file_count": len(files),
        "total_bytes": total_bytes,
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a GitHub Pages artifact before upload.")
    parser.add_argument("public_dir", type=Path)
    args = parser.parse_args()

    if not args.public_dir.is_dir():
        print(json.dumps({"errors": [f"not a directory: {args.public_dir}"]}, indent=2))
        return 1

    report = validate(args.public_dir)
    print(json.dumps(report, indent=2))
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
