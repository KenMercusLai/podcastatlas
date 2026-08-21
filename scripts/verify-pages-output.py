#!/usr/bin/env python3

from pathlib import Path
import argparse
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from urllib.parse import urlsplit


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
    "about/index.html",
    "about/index.md",
    "methodology/index.html",
    "methodology/index.md",
    "robots.txt",
    "images/podcast-atlas-social.png",
    "pagefind/pagefind.js",
    "pagefind/pagefind-component-ui.js",
    "pagefind/pagefind-component-ui.css",
)
WIKI_LINK_RE = re.compile(r"\[\[[^\]\n]+\]\]")
JSON_LD_RE = re.compile(
    r'<script\b[^>]*\btype=(?:["\']application/ld\+json["\']|application/ld\+json)'
    r"[^>]*>(.*?)</script>",
    re.IGNORECASE | re.DOTALL,
)
METADATA_PAGE_FILES = (
    "index.html",
    "about/index.html",
    "methodology/index.html",
    "episodes/index.html",
    "shows/index.html",
    "tags/index.html",
    "wiki/index.html",
    "search/index.html",
)
METADATA_PATTERNS = {
    "canonical link": re.compile(r'<link\b[^>]*\brel=(?:["\']canonical["\']|canonical)', re.I),
    "description": re.compile(r'<meta\b[^>]*\bname=(?:["\']description["\']|description)', re.I),
    "Open Graph title": re.compile(r'<meta\b[^>]*\bproperty=["\']og:title["\']', re.I),
    "Open Graph URL": re.compile(r'<meta\b[^>]*\bproperty=["\']og:url["\']', re.I),
    "Open Graph image": re.compile(r'<meta\b[^>]*\bproperty=["\']og:image["\']', re.I),
    "Twitter card": re.compile(r'<meta\b[^>]*\bname=(?:["\']twitter:card["\']|twitter:card)', re.I),
}
CANONICAL_URL_RE = re.compile(
    r'<link\b(?=[^>]*\brel=(?:["\']canonical["\']|canonical))[^>]*'
    r'\bhref=(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+))',
    re.I,
)
OG_URL_RE = re.compile(
    r'<meta\b(?=[^>]*\bproperty=["\']og:url["\'])[^>]*'
    r'\bcontent=(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+))',
    re.I,
)
DESCRIPTION_RE = re.compile(
    r'<meta\b(?=[^>]*\bname=(?:["\']description["\']|description))[^>]*'
    r'\bcontent=(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+))',
    re.I,
)


def extracted_attribute(match: re.Match | None) -> str | None:
    if match is None:
        return None
    return html.unescape(next(value for value in match.groups() if value is not None))


def validate_metadata_page(path: Path, public_dir: Path, errors: list[str]) -> None:
    relative = path.relative_to(public_dir).as_posix()
    page_html = path.read_text(encoding="utf-8")

    for label, pattern in METADATA_PATTERNS.items():
        count = len(pattern.findall(page_html))
        if count != 1:
            errors.append(f"{label} count in {relative}: expected 1, found {count}")

    canonical_url = extracted_attribute(CANONICAL_URL_RE.search(page_html))
    og_url = extracted_attribute(OG_URL_RE.search(page_html))
    meta_description = extracted_attribute(DESCRIPTION_RE.search(page_html))
    if canonical_url is not None:
        try:
            parsed_canonical = urlsplit(canonical_url)
        except (TypeError, ValueError) as error:
            errors.append(f"invalid canonical URL in {relative}: {error}")
        else:
            if parsed_canonical.scheme not in {"http", "https"} or not parsed_canonical.netloc:
                errors.append(f"invalid canonical URL in {relative}: {canonical_url!r}")
    if canonical_url is not None and og_url is not None and canonical_url != og_url:
        errors.append(f"canonical URL does not match Open Graph URL in {relative}")

    scripts = JSON_LD_RE.findall(page_html)
    if len(scripts) != 1:
        errors.append(f"JSON-LD count in {relative}: expected 1, found {len(scripts)}")
        return

    try:
        payload = json.loads(html.unescape(scripts[0]))
    except (json.JSONDecodeError, TypeError) as error:
        errors.append(f"invalid JSON-LD in {relative}: {error}")
        return

    if not isinstance(payload, dict):
        errors.append(f"invalid JSON-LD in {relative}: root must be an object")
        return
    if payload.get("@context") != "https://schema.org":
        errors.append(f"invalid JSON-LD context in {relative}: {payload.get('@context')!r}")
    if payload.get("@type") not in {"WebSite", "WebPage"}:
        errors.append(f"invalid JSON-LD type in {relative}: {payload.get('@type')!r}")
    if canonical_url is not None and payload.get("url") != canonical_url:
        errors.append(f"canonical URL does not match JSON-LD URL in {relative}")
    if meta_description is not None and payload.get("description") != meta_description:
        errors.append(f"JSON-LD description does not match meta description in {relative}")
    try:
        parsed_url = urlsplit(payload.get("url", ""))
    except (TypeError, ValueError) as error:
        errors.append(f"invalid JSON-LD URL in {relative}: {error}")
    else:
        if parsed_url.scheme not in {"http", "https"} or not parsed_url.netloc:
            errors.append(f"invalid JSON-LD URL in {relative}: {payload.get('url')!r}")


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

    for relative in METADATA_PAGE_FILES:
        path = public_dir / relative
        if path.is_file():
            validate_metadata_page(path, public_dir, errors)

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
    else:
        validate_metadata_page(sorted(episode_html)[0], public_dir, errors)
        for html_path in episode_html:
            markdown_path = html_path.parent.parent / f"{html_path.parent.name}.md"
            if not markdown_path.is_file():
                relative = markdown_path.relative_to(public_dir).as_posix()
                errors.append(f"missing episode detail Markdown: {relative}")

    concept_html = sorted((public_dir / "wiki" / "concepts").glob("*/index.html"))
    if concept_html:
        validate_metadata_page(concept_html[0], public_dir, errors)

    for nested_markdown_path in sorted((public_dir / "episodes").glob("*/index.md")):
        relative = nested_markdown_path.relative_to(public_dir).as_posix()
        errors.append(f"nested episode Markdown URL is forbidden: {relative}")

    for flat_html_path in sorted((public_dir / "episodes").glob("*.html")):
        if flat_html_path.name == "index.html":
            continue
        relative = flat_html_path.relative_to(public_dir).as_posix()
        errors.append(f"flat episode HTML URL is forbidden: {relative}")

    for relative in ("index.xml", "episodes/index.xml", "sitemap.xml"):
        path = public_dir / relative
        if path.is_file():
            try:
                tree = ET.parse(path)
            except ET.ParseError as error:
                errors.append(f"invalid XML: {relative}: {error}")
                continue

            if relative == "sitemap.xml":
                urls = [
                    element.text.strip()
                    for element in tree.getroot().iter()
                    if element.tag.rsplit("}", 1)[-1] == "loc" and element.text
                ]
                sitemap_entries = []
                for url in urls:
                    try:
                        url_path = urlsplit(url).path
                    except ValueError as error:
                        errors.append(f"invalid URL in sitemap: {url}: {error}")
                        continue
                    sitemap_entries.append((url, url_path))

                episode_root_candidates = [
                    url_path
                    for _, url_path in sitemap_entries
                    if url_path.endswith("/episodes/")
                ]
                episode_root = min(
                    episode_root_candidates,
                    key=lambda path: (path.count("/"), len(path)),
                    default=None,
                )
                for url, url_path in sitemap_entries:
                    is_episode_url = bool(
                        episode_root and url_path.startswith(episode_root)
                    )
                    if is_episode_url and not url_path.endswith("/"):
                        errors.append(f"noncanonical Episode URL in sitemap: {url}")

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
