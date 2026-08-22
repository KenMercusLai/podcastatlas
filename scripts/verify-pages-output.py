#!/usr/bin/env python3

from pathlib import Path
from datetime import date, datetime
import argparse
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import unquote, urljoin, urlsplit


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


def expected_schema_type(path: Path, public_dir: Path) -> str:
    parts = path.relative_to(public_dir).parts
    if parts == ("index.html",):
        return "WebSite"
    if len(parts) == 3 and parts[0] == "episodes" and parts[2] == "index.html":
        return "PodcastEpisode"
    if len(parts) == 3 and parts[0] == "shows" and parts[2] == "index.html":
        return "PodcastSeries"
    if (
        len(parts) == 4
        and parts[0] == "wiki"
        and parts[1] in {"concepts", "entities"}
        and parts[2] != "by-letter"
        and parts[3] == "index.html"
    ):
        return "DefinedTerm" if parts[1] == "concepts" else "Article"
    return "WebPage"


def is_absolute_http_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        parsed = urlsplit(value)
    except ValueError:
        return False
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate_semantic_schema(
    payload: dict, schema_type: str, relative: str, canonical_url: str | None, errors: list[str]
) -> None:
    if schema_type == "WebSite":
        action = payload.get("potentialAction")
        if not isinstance(action, dict) or action.get("@type") != "SearchAction":
            errors.append(
                f"WebSite JSON-LD potentialAction in {relative}: expected SearchAction"
            )
            return
        target = action.get("target")
        if not isinstance(target, dict) or target.get("@type") != "EntryPoint":
            errors.append(
                f"WebSite JSON-LD SearchAction target in {relative}: expected EntryPoint"
            )
        else:
            url_template = target.get("urlTemplate")
            expected_template = (
                urljoin(canonical_url, "search/?q={search_term_string}")
                if canonical_url
                else None
            )
            if url_template != expected_template:
                errors.append(
                    f"WebSite JSON-LD SearchAction URL template in {relative}: "
                    f"expected {expected_template!r}, found {url_template!r}"
                )
        if action.get("query-input") != "required name=search_term_string":
            errors.append(
                f"WebSite JSON-LD SearchAction query-input in {relative}: invalid value"
            )
    elif schema_type == "PodcastEpisode":
        published = payload.get("datePublished")
        if not isinstance(published, str):
            errors.append(
                f"PodcastEpisode JSON-LD datePublished in {relative}: invalid value"
            )
        else:
            try:
                datetime.fromisoformat(published.replace("Z", "+00:00"))
            except ValueError:
                errors.append(
                    f"PodcastEpisode JSON-LD datePublished in {relative}: invalid value"
                )
        if not re.fullmatch(r"PT[1-9][0-9]*S", payload.get("duration", "")):
            errors.append(f"PodcastEpisode JSON-LD duration in {relative}: invalid value")
        series = payload.get("partOfSeries")
        if (
            not isinstance(series, dict)
            or series.get("@type") != "PodcastSeries"
            or not series.get("name")
            or not is_absolute_http_url(series.get("url"))
        ):
            errors.append(
                f"PodcastEpisode JSON-LD partOfSeries in {relative}: invalid value"
            )
        if not is_absolute_http_url(payload.get("sameAs")):
            errors.append(f"PodcastEpisode JSON-LD sameAs in {relative}: invalid URL")
    elif schema_type == "PodcastSeries":
        episode_count = payload.get("numberOfEpisodes")
        if not isinstance(episode_count, int) or isinstance(episode_count, bool) or episode_count < 1:
            errors.append(
                f"PodcastSeries JSON-LD numberOfEpisodes in {relative}: invalid value"
            )
    elif schema_type == "DefinedTerm":
        term_set = payload.get("inDefinedTermSet")
        if (
            not isinstance(term_set, dict)
            or term_set.get("@type") != "DefinedTermSet"
            or not term_set.get("name")
            or not is_absolute_http_url(term_set.get("url"))
        ):
            errors.append(
                f"DefinedTerm JSON-LD inDefinedTermSet in {relative}: invalid value"
            )
    elif schema_type == "Article":
        if not isinstance(payload.get("headline"), str) or not payload["headline"].strip():
            errors.append(f"Article JSON-LD headline in {relative}: invalid value")
        modified = payload.get("dateModified")
        if not isinstance(modified, str):
            errors.append(f"Article JSON-LD dateModified in {relative}: invalid value")
        else:
            try:
                date.fromisoformat(modified)
            except ValueError:
                errors.append(f"Article JSON-LD dateModified in {relative}: invalid value")


class PublicLinkParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.has_github_link = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        href = dict(attrs).get("href")
        if not href:
            return
        normalized = f"https:{href}" if href.startswith("//") else href
        normalized = re.sub(r"[\x00-\x20\x7f]", "", normalized)
        normalized = normalized.replace("\\", "/")
        normalized = re.sub(r"^(https?):/*", r"\1://", normalized, flags=re.I)
        try:
            hostname = unquote(urlsplit(normalized).hostname or "").lower()
        except ValueError:
            return
        hostname = hostname.translate(
            str.maketrans({"。": ".", "．": ".", "｡": "."})
        ).rstrip(".")
        if hostname == "github.com" or hostname.endswith(".github.com"):
            self.has_github_link = True


class EpisodeListParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_episode_list = False
        self.in_item = False
        self.current_href: str | None = None
        self.current_date: str | None = None
        self.episode_hrefs: list[str] = []
        self.episode_dates: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        classes = (attributes.get("class") or "").split()
        if tag == "ul" and "episode-list" in classes:
            self.in_episode_list = True
        elif self.in_episode_list and tag == "li":
            self.in_item = True
            self.current_href = None
            self.current_date = None
        elif self.in_item and tag == "a" and self.current_href is None:
            self.current_href = attributes.get("href")
        elif self.in_item and tag == "time" and self.current_date is None:
            self.current_date = attributes.get("datetime")

    def handle_endtag(self, tag: str) -> None:
        if self.in_item and tag == "li":
            if self.current_href:
                self.episode_hrefs.append(self.current_href)
                self.episode_dates.append(self.current_date or "")
            self.in_item = False
            self.current_href = None
            self.current_date = None
        elif self.in_episode_list and tag == "ul":
            self.in_episode_list = False


def episode_list_entries(path: Path) -> list[tuple[str, str]]:
    parser = EpisodeListParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return list(zip(parser.episode_hrefs, parser.episode_dates))


def episode_slug_from_href(href: str) -> str | None:
    try:
        path = unquote(urlsplit(href).path)
    except ValueError:
        return None
    marker = "/episodes/"
    if marker not in path:
        return None
    tail = path.rsplit(marker, 1)[1].strip("/")
    if not tail or "/" in tail or tail.startswith("page/"):
        return None
    return tail


def validate_episode_pagination(
    public_dir: Path, episode_html: list[Path], errors: list[str]
) -> None:
    episodes_dir = public_dir / "episodes"
    list_pages = [episodes_dir / "index.html"]
    list_pages.extend(
        sorted(
            (
                path
                for path in episodes_dir.glob("page/*/index.html")
                if path.parent.name.isdigit() and int(path.parent.name) > 1
            ),
            key=lambda path: int(path.parent.name),
        )
    )
    list_pages = [path for path in list_pages if path.is_file()]

    expected_page_count = max(1, (len(episode_html) + 99) // 100)
    if len(list_pages) != expected_page_count:
        errors.append(
            "episode pagination page count mismatch: "
            f"expected {expected_page_count}, found {len(list_pages)}"
        )

    found_page_numbers = [
        1 if page == episodes_dir / "index.html" else int(page.parent.name)
        for page in list_pages
    ]
    expected_page_numbers = list(range(1, expected_page_count + 1))
    if found_page_numbers != expected_page_numbers:
        errors.append(
            "episode pagination page sequence mismatch: "
            f"expected {expected_page_numbers}, found {found_page_numbers}"
        )

    all_hrefs: list[str] = []
    all_dates: list[str] = []
    root_canonical_url = extracted_attribute(
        CANONICAL_URL_RE.search((episodes_dir / "index.html").read_text(encoding="utf-8"))
    ) if (episodes_dir / "index.html").is_file() else None
    for page_index, page in enumerate(list_pages):
        if page != episodes_dir / "index.html":
            validate_metadata_page(page, public_dir, errors)
        entries = episode_list_entries(page)
        hrefs = [href for href, _ in entries]
        all_dates.extend(date for _, date in entries)
        relative = page.relative_to(public_dir).as_posix()
        canonical_url = extracted_attribute(
            CANONICAL_URL_RE.search(page.read_text(encoding="utf-8"))
        )
        if root_canonical_url is not None and canonical_url is not None:
            page_number = 1 if page == episodes_dir / "index.html" else int(page.parent.name)
            expected_canonical_url = (
                root_canonical_url
                if page_number == 1
                else f"{root_canonical_url.rstrip('/')}/page/{page_number}/"
            )
            if canonical_url != expected_canonical_url:
                errors.append(
                    f"episode pagination canonical mismatch: {relative}: "
                    f"expected {expected_canonical_url}, found {canonical_url}"
                )
        expected_item_count = min(100, max(0, len(episode_html) - (page_index * 100)))
        if len(hrefs) != expected_item_count:
            errors.append(
                f"episode pagination page size mismatch: {relative}: "
                f"expected {expected_item_count}, found {len(hrefs)}"
            )
        all_hrefs.extend(hrefs)

    if any(not publication_date for publication_date in all_dates):
        errors.append("episode list item missing publication date")
    for publication_date in sorted(set(all_dates) - {""}):
        try:
            parsed_date = date.fromisoformat(publication_date)
        except ValueError:
            parsed_date = None
        if parsed_date is None or parsed_date.isoformat() != publication_date:
            errors.append(
                f"episode list item has invalid publication date: {publication_date}"
            )

    if all_dates != sorted(all_dates, reverse=True):
        errors.append("episode list is not ordered newest first")

    unique_hrefs = set(all_hrefs)
    if len(unique_hrefs) != len(all_hrefs):
        errors.append("episode pagination contains duplicate episode links")
    if len(unique_hrefs) != len(episode_html):
        errors.append(
            "episode list coverage mismatch: "
            f"expected {len(episode_html)} unique episodes, found {len(unique_hrefs)}"
        )

    expected_slugs = {path.parent.name for path in episode_html}
    actual_slugs = {
        slug if (slug := episode_slug_from_href(href)) is not None else f"invalid:{href}"
        for href in unique_hrefs
    }
    missing_slugs = expected_slugs - actual_slugs
    unexpected_slugs = actual_slugs - expected_slugs
    if missing_slugs or unexpected_slugs:
        errors.append(
            "episode list/detail mismatch: "
            f"missing {len(missing_slugs)}, unexpected {len(unexpected_slugs)}"
        )

    if root_canonical_url is not None:
        expected_episode_urls = {
            canonical_url
            for path in episode_html
            if (
                canonical_url := extracted_attribute(
                    CANONICAL_URL_RE.search(path.read_text(encoding="utf-8"))
                )
            )
            is not None
        }
        actual_episode_urls = {
            urljoin(root_canonical_url, href) for href in unique_hrefs
        }
        missing_urls = expected_episode_urls - actual_episode_urls
        unexpected_urls = actual_episode_urls - expected_episode_urls
        if missing_urls or unexpected_urls:
            errors.append(
                "episode list/detail URL mismatch: "
                f"missing {len(missing_urls)}, unexpected {len(unexpected_urls)}"
            )


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
    schema_type = expected_schema_type(path, public_dir)
    if payload.get("@type") != schema_type:
        errors.append(
            f"invalid JSON-LD type in {relative}: "
            f"expected {schema_type!r}, found {payload.get('@type')!r}"
        )
    else:
        validate_semantic_schema(payload, schema_type, relative, canonical_url, errors)
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

    for path in files:
        if path.suffix.lower() != ".html":
            continue
        page_html = path.read_text(encoding="utf-8")
        link_parser = PublicLinkParser()
        link_parser.feed(page_html)
        if link_parser.has_github_link:
            relative = path.relative_to(public_dir).as_posix()
            errors.append(f"public GitHub link found: {relative}")

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
        for html_path in sorted(episode_html):
            validate_metadata_page(html_path, public_dir, errors)
            markdown_path = html_path.parent.parent / f"{html_path.parent.name}.md"
            if not markdown_path.is_file():
                relative = markdown_path.relative_to(public_dir).as_posix()
                errors.append(f"missing episode detail Markdown: {relative}")
        validate_episode_pagination(public_dir, episode_html, errors)

    for semantic_dir in (
        public_dir / "shows",
        public_dir / "wiki" / "concepts",
        public_dir / "wiki" / "entities",
    ):
        for html_path in sorted(semantic_dir.glob("*/index.html")):
            validate_metadata_page(html_path, public_dir, errors)

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
