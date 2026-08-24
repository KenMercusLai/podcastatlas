#!/usr/bin/env python3

from pathlib import Path
from datetime import date, datetime
import argparse
import gzip
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import quote, unquote, urljoin, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SHOW_PROFILES_PATH = ROOT / "data" / "show_profiles.json"


REQUIRED_FILES = (
    "index.html",
    "index.xml",
    "episodes/index.xml",
    "sitemap.xml",
    "episodes/index.html",
    "tags/index.html",
    "shows/index.html",
    "wiki/index.html",
    "wiki/current-synthesis/index.html",
    "topics/index.html",
    "topics/technology/index.html",
    "topics/economics/index.html",
    "topics/history/index.html",
    "topics/politics/index.html",
    "topics/culture/index.html",
    "topics/science/index.html",
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
    "wiki/current-synthesis/index.html",
    "topics/index.html",
    "search/index.html",
)
CONTROLLED_TOPIC_KEYS = (
    "technology",
    "economics",
    "history",
    "politics",
    "culture",
    "science",
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
OG_TITLE_RE = re.compile(
    r'<meta\b(?=[^>]*\bproperty=["\']og:title["\'])[^>]*'
    r'\bcontent=(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+))',
    re.I,
)
DESCRIPTION_RE = re.compile(
    r'<meta\b(?=[^>]*\bname=(?:["\']description["\']|description))[^>]*'
    r'\bcontent=(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+))',
    re.I,
)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.I | re.DOTALL)


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
        self.has_raw_tag_link = False

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
            parsed = urlsplit(normalized)
            hostname = unquote(parsed.hostname or "").lower()
            url_path = unquote(parsed.path)
        except ValueError:
            return
        if re.search(r"(?:^|/)tags(?:/|$)", url_path.lstrip("/")):
            self.has_raw_tag_link = True
        hostname = hostname.translate(
            str.maketrans({"。": ".", "．": ".", "｡": "."})
        ).rstrip(".")
        if hostname == "github.com" or hostname.endswith(".github.com"):
            self.has_github_link = True


class MarkerParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.elements: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = {name: value or "" for name, value in attrs}
        classes = set(attributes.get("class", "").split())
        if classes.intersection(
            {
                "controlled-topic",
                "controlled-topic-link",
                "controlled-topic-entry",
                "wiki-topic-link",
                "legacy-tag-page",
                "show-directory-link",
                "show-identity",
                "show-latest-episode",
                "show-topic-link",
                "show-start-link",
                "show-entity-link",
                "show-archive-link",
            }
        ):
            attributes["_tag"] = tag
            self.elements.append(attributes)


def marked_elements(page_html: str, class_name: str) -> list[dict[str, str]]:
    parser = MarkerParser()
    parser.feed(page_html)
    return [
        attributes
        for attributes in parser.elements
        if class_name in attributes.get("class", "").split()
    ]


class MarkedLinkTextParser(HTMLParser):
    def __init__(self, class_name: str) -> None:
        super().__init__(convert_charrefs=True)
        self.class_name = class_name
        self.current: list[str] | None = None
        self.texts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a" or self.current is not None:
            return
        attributes = {name: value or "" for name, value in attrs}
        if self.class_name in attributes.get("class", "").split():
            self.current = []

    def handle_data(self, data: str) -> None:
        if self.current is not None:
            self.current.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a" and self.current is not None:
            self.texts.append("".join(self.current).strip())
            self.current = None


def marked_link_texts(page_html: str, class_name: str) -> list[str]:
    parser = MarkedLinkTextParser(class_name)
    parser.feed(page_html)
    return parser.texts


class LegacyTagMetadataParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.robots_contents: list[str] = []
        self.in_route_manifest = False
        self.route_manifest_chunks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = {name.lower(): value or "" for name, value in attrs}
        if tag.lower() == "meta" and attributes.get("name", "").casefold() == "robots":
            self.robots_contents.append(attributes.get("content", ""))
        if tag.lower() == "script" and attributes.get("id") == "legacy-tag-route-manifest":
            self.in_route_manifest = True

    def handle_data(self, data: str) -> None:
        if self.in_route_manifest:
            self.route_manifest_chunks.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "script" and self.in_route_manifest:
            self.in_route_manifest = False


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


def synthesis_article(page_html: str, class_name: str) -> tuple[dict[str, str], str] | None:
    pattern = re.compile(
        rf'<article\b(?=[^>]*\bclass=(?:"[^"]*\b{re.escape(class_name)}\b[^"]*"|\'[^\']*\b{re.escape(class_name)}\b[^\']*\'|[^\s>]*\b{re.escape(class_name)}\b))[^>]*>.*?</article>',
        re.IGNORECASE | re.DOTALL,
    )
    match = pattern.search(page_html)
    if not match:
        return None
    opening = match.group(0).split(">", 1)[0]
    attributes: dict[str, str] = {}
    for name, double, single, bare in re.findall(
        r'([\w:-]+)\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+))', opening
    ):
        attributes[name.lower()] = html.unescape(double or single or bare)
    return attributes, match.group(0)


def validate_current_synthesis(public_dir: Path, errors: list[str]) -> None:
    detail_path = public_dir / "wiki" / "current-synthesis" / "index.html"
    landing_path = public_dir / "wiki" / "index.html"
    if not detail_path.is_file() or not landing_path.is_file():
        return
    detail_html = detail_path.read_text(encoding="utf-8")
    landing_html = landing_path.read_text(encoding="utf-8")
    detail = synthesis_article(detail_html, "current-synthesis")
    card = synthesis_article(landing_html, "current-synthesis-card")
    if detail is None:
        errors.append("Current Synthesis detail is missing its artifact marker")
        return
    if card is None:
        errors.append("Wiki landing is missing its Current Synthesis card marker")
        return
    detail_attrs, detail_block = detail
    card_attrs, card_block = card
    source = detail_attrs.get("data-synthesis-source", "")
    if source not in {"compact", "overview-legacy"}:
        errors.append(f"unsupported Current Synthesis source: {source!r}")
        return
    if card_attrs.get("data-synthesis-source") != source:
        errors.append("Current Synthesis source differs between landing and detail")
    summary = detail_attrs.get("data-summary", "").strip()
    if not summary:
        errors.append("Current Synthesis is missing its summary")
    if card_attrs.get("data-summary", "").strip() != summary:
        errors.append("Current Synthesis summary differs between landing and detail")
    meta_description = extracted_attribute(DESCRIPTION_RE.search(detail_html))
    if summary and meta_description and not (
        summary.startswith(meta_description) or meta_description.startswith(summary)
    ):
        errors.append("Current Synthesis summary does not match its meta description")

    if source == "compact":
        for key in ("episode-count", "source-count"):
            detail_value = detail_attrs.get(f"data-{key}", "")
            card_value = card_attrs.get(f"data-{key}", "")
            if not re.fullmatch(r"[1-9][0-9]*", detail_value):
                errors.append(f"compact Current Synthesis has invalid {key}: {detail_value!r}")
            if card_value != detail_value:
                errors.append(f"Current Synthesis {key} differs between landing and detail")

    def time_in_class(block: str, class_name: str) -> str | None:
        container = re.search(
            rf'<[^>]+\bclass=(?:"[^"]*\b{re.escape(class_name)}\b[^"]*"|\'[^\']*\b{re.escape(class_name)}\b[^\']*\'|[^\s>]*\b{re.escape(class_name)}\b)[^>]*>.*?<time\b[^>]*\bdatetime=(?:"([^"]+)"|\'([^\']+)\'|([^\s>]+))',
            block,
            re.IGNORECASE | re.DOTALL,
        )
        if container is None:
            return None
        return next((value for value in container.groups() if value), None)

    detail_date = time_in_class(detail_block, "synthesis-updated")
    card_date = time_in_class(card_block, "wiki-feature-updated")
    if detail_date is None or card_date is None:
        errors.append("Current Synthesis is missing a visible update date")
    else:
        try:
            parsed = date.fromisoformat(detail_date)
        except ValueError:
            parsed = None
        if parsed is None or parsed.isoformat() != detail_date:
            errors.append(f"compact Current Synthesis has invalid update date: {detail_date!r}")
        if card_date != detail_date:
            errors.append("Current Synthesis update date differs between landing and detail")
    if source == "overview-legacy":
        return
    for heading in ("Executive Summary", "Synthesis by Domain"):
        if heading not in detail_html:
            errors.append(f"compact Current Synthesis is missing {heading}")


def local_route_path(href: str) -> str | None:
    if not href or "\\" in href or "\x00" in href:
        return None
    try:
        parsed = urlsplit(href)
        url_path = unquote(parsed.path)
    except ValueError:
        return None
    if parsed.scheme or parsed.netloc or parsed.query or parsed.fragment:
        return None
    segments = [segment for segment in url_path.split("/") if segment]
    if any(segment in {".", ".."} for segment in segments):
        return None
    return url_path


def controlled_topic_href_matches(href: str, key: str) -> bool:
    url_path = local_route_path(href)
    return bool(url_path and url_path.endswith(f"/topics/{key}/"))


def internal_wiki_target(public_dir: Path, href: str) -> Path | None:
    url_path = local_route_path(href)
    if url_path is None:
        return None
    marker = "/wiki/"
    if url_path.count(marker) != 1:
        return None
    tail = url_path.rsplit(marker, 1)[1].strip("/")
    wiki_root = (public_dir / "wiki").resolve()
    target = (wiki_root / tail / "index.html").resolve() if tail else wiki_root / "index.html"
    if target != wiki_root / "index.html" and wiki_root not in target.parents:
        return None
    return target


def internal_section_target(public_dir: Path, href: str, section: str) -> Path | None:
    url_path = local_route_path(href)
    if url_path is None:
        return None
    marker = f"/{section}/"
    if url_path.count(marker) != 1:
        return None
    tail = url_path.rsplit(marker, 1)[1].strip("/")
    if not tail or "/" in tail:
        return None
    section_root = (public_dir / section).resolve()
    target = (section_root / tail / "index.html").resolve()
    if section_root not in target.parents:
        return None
    return target


def href_matches_project_route(href: str, expected_route: str) -> bool:
    url_path = local_route_path(href)
    return bool(url_path and url_path.endswith(expected_route))


def integer_attribute(attributes: dict[str, str], name: str) -> int | None:
    value = attributes.get(name, "")
    return int(value) if re.fullmatch(r"0|[1-9][0-9]*", value) else None


def validate_show_profiles(public_dir: Path, payload: dict, errors: list[str]) -> None:
    if not isinstance(payload, dict):
        errors.append("invalid generated show profile projection")
        return
    shows = payload.get("shows")
    if payload.get("version") != 1 or not isinstance(shows, dict) or not shows:
        errors.append("invalid generated show profile projection")
        return

    landing_path = public_dir / "shows" / "index.html"
    if not landing_path.is_file():
        return
    landing_html = landing_path.read_text(encoding="utf-8")
    directory_links = marked_elements(landing_html, "show-directory-link")
    directory_titles = marked_link_texts(landing_html, "show-directory-link")
    if len(directory_titles) != len(directory_links):
        errors.append("Show directory visible title count mismatch")
    routes: dict[str, str] = {}
    for index, link in enumerate(directory_links):
        title = link.get("data-show-title", "")
        href = link.get("href", "")
        if not title or title in routes:
            errors.append(f"duplicate or empty Show directory title: {title!r}")
            continue
        routes[title] = href
        visible_title = directory_titles[index] if index < len(directory_titles) else ""
        if visible_title != title:
            errors.append(f"Show directory visible title mismatch: {title!r}")
    if set(routes) != set(shows):
        errors.append(
            "Show directory/profile set mismatch: "
            f"missing {sorted(set(shows) - set(routes))}, extra {sorted(set(routes) - set(shows))}"
        )

    for title, profile in shows.items():
        href = routes.get(title)
        if href is None:
            continue
        show_path = internal_section_target(public_dir, href, "shows")
        if show_path is None or not show_path.is_file():
            errors.append(f"Show {title} has invalid or missing directory target")
            continue
        page_html = show_path.read_text(encoding="utf-8")
        title_match = TITLE_RE.search(page_html)
        document_title = html.unescape(title_match.group(1)).strip() if title_match else ""
        if not document_title.startswith(f"{title} | "):
            errors.append(f"Show {title} document title does not preserve exact identity")
        open_graph_title = extracted_attribute(OG_TITLE_RE.search(page_html)) or ""
        if not open_graph_title.startswith(f"{title} | "):
            errors.append(f"Show {title} Open Graph title does not preserve exact identity")
        schema_scripts = JSON_LD_RE.findall(page_html)
        try:
            schema = json.loads(html.unescape(schema_scripts[0])) if len(schema_scripts) == 1 else None
        except json.JSONDecodeError:
            schema = None
        if (
            not isinstance(schema, dict)
            or schema.get("@type") != "PodcastSeries"
            or schema.get("name") != title
        ):
            errors.append(f"Show {title} PodcastSeries name does not preserve exact identity")
        markers = marked_elements(page_html, "show-identity")
        if len(markers) != 1:
            errors.append(
                f"Show {title} identity marker count mismatch: expected 1, found {len(markers)}"
            )
            continue
        marker = markers[0]
        if marker.get("data-show-profile") != "controlled":
            errors.append(f"Show {title} has invalid profile provenance marker")
        for attribute, profile_key in (
            ("data-episode-count", "episode_count"),
            ("data-source-note-count", "source_note_count"),
            ("data-topic-matched-source-note-count", "topic_matched_source_note_count"),
        ):
            if integer_attribute(marker, attribute) != profile.get(profile_key):
                errors.append(f"Show {title} {profile_key.replace('_', ' ')} mismatch")
        for attribute, profile_key in (
            ("data-earliest-episode-date", "earliest_episode_date"),
            ("data-latest-episode-date", "latest_episode_date"),
        ):
            if marker.get(attribute) != profile.get(profile_key):
                errors.append(f"Show {title} {profile_key.replace('_', ' ')} mismatch")

        latest_links = marked_elements(page_html, "show-latest-episode")
        if len(latest_links) != 1:
            errors.append(f"Show {title} latest episode marker count mismatch")
        else:
            latest = latest_links[0]
            latest_target = internal_section_target(
                public_dir, latest.get("href", ""), "episodes"
            )
            if latest.get("data-episode-file") != profile.get("latest_episode_file"):
                errors.append(f"Show {title} latest episode file mismatch")
            if latest_target is None or not latest_target.is_file():
                errors.append(f"Show {title} latest episode target is invalid")

        topic_links = marked_elements(page_html, "show-topic-link")
        expected_topics = profile.get("topics", [])
        if [item.get("data-topic-key") for item in topic_links] != [
            item.get("key") for item in expected_topics
        ]:
            errors.append(f"Show {title} controlled topic order mismatch")
        for actual, expected in zip(topic_links, expected_topics):
            key = expected.get("key")
            if integer_attribute(actual, "data-source-note-count") != expected.get(
                "source_note_count"
            ):
                errors.append(f"Show {title} topic {key} source-note count mismatch")
            if not href_matches_project_route(actual.get("href", ""), expected.get("url", "")):
                errors.append(f"Show {title} topic {key} has invalid link")
            topic_target = internal_section_target(
                public_dir, actual.get("href", ""), "topics"
            )
            if topic_target is None or not topic_target.is_file():
                errors.append(f"Show {title} topic {key} target is missing")

        start_links = marked_elements(page_html, "show-start-link")
        expected_start = profile.get("start_here_episode_files", [])
        if [item.get("data-episode-file") for item in start_links] != expected_start:
            errors.append(f"Show {title} Start here episode sequence mismatch")
        for link in start_links:
            target = internal_section_target(public_dir, link.get("href", ""), "episodes")
            if target is None or not target.is_file():
                errors.append(f"Show {title} Start here target is invalid")

        entity_links = marked_elements(page_html, "show-entity-link")
        expected_entities = profile.get("entities", [])
        if [item.get("data-entity-key") for item in entity_links] != [
            item.get("key") for item in expected_entities
        ]:
            errors.append(f"Show {title} entity order mismatch")
        for actual, expected in zip(entity_links, expected_entities):
            key = expected.get("key")
            if actual.get("data-entity-kind") != expected.get("kind"):
                errors.append(f"Show {title} entity {key} kind mismatch")
            if integer_attribute(actual, "data-episode-count") != expected.get(
                "episode_count"
            ):
                errors.append(f"Show {title} entity {key} episode count mismatch")
            if not href_matches_project_route(actual.get("href", ""), expected.get("url", "")):
                errors.append(f"Show {title} entity {key} has invalid link")
            entity_target = internal_wiki_target(public_dir, actual.get("href", ""))
            if entity_target is None or not entity_target.is_file():
                errors.append(f"Show {title} entity {key} target is missing")

        archive_links = marked_elements(page_html, "show-archive-link")
        if len(archive_links) != profile.get("episode_count"):
            errors.append(
                f"Show {title} complete archive count mismatch: "
                f"expected {profile.get('episode_count')}, found {len(archive_links)}"
            )
        archive_hrefs = [item.get("href", "") for item in archive_links]
        if len(archive_hrefs) != len(set(archive_hrefs)):
            errors.append(f"Show {title} complete archive contains duplicate episodes")
        expected_show_path = local_route_path(href)
        for archive_href in archive_hrefs:
            target = internal_section_target(public_dir, archive_href, "episodes")
            if target is None or not target.is_file():
                errors.append(f"Show {title} complete archive target is invalid")
                continue
            episode_html = target.read_text(encoding="utf-8")
            scripts = JSON_LD_RE.findall(episode_html)
            if len(scripts) != 1:
                errors.append(f"Show {title} complete archive episode ownership is unverifiable")
                continue
            try:
                episode_payload = json.loads(html.unescape(scripts[0]))
                series = episode_payload.get("partOfSeries")
                series_url = series.get("url") if isinstance(series, dict) else None
                series_name = series.get("name") if isinstance(series, dict) else None
                series_path = (
                    unquote(urlsplit(series_url).path)
                    if isinstance(series_url, str)
                    else None
                )
            except (TypeError, ValueError, json.JSONDecodeError):
                errors.append(f"Show {title} complete archive episode ownership is unverifiable")
                continue
            if series_path is None:
                errors.append(f"Show {title} complete archive episode ownership is unverifiable")
                continue
            if series_path != expected_show_path:
                errors.append(
                    f"Show {title} complete archive contains an episode owned by another Show"
                )
            if series_name != title:
                errors.append(
                    f"Show {title} complete archive episode does not preserve exact series identity"
                )


def validate_controlled_topics(public_dir: Path, errors: list[str]) -> None:
    topics_dir = public_dir / "topics"
    if not topics_dir.is_dir():
        errors.append("missing controlled topics directory")
        return
    actual_routes = tuple(
        sorted(
            child.name
            for child in topics_dir.iterdir()
            if child.is_dir() and (child / "index.html").is_file()
        )
    )
    if set(actual_routes) != set(CONTROLLED_TOPIC_KEYS):
        errors.append(
            "controlled topic routes mismatch: "
            f"expected {list(CONTROLLED_TOPIC_KEYS)}, found {list(actual_routes)}"
        )

    landing_path = topics_dir / "index.html"
    if landing_path.is_file():
        landing_links = marked_elements(
            landing_path.read_text(encoding="utf-8"), "controlled-topic-link"
        )
        landing_keys = tuple(link.get("data-topic-key", "") for link in landing_links)
        if landing_keys != CONTROLLED_TOPIC_KEYS:
            errors.append(
                "controlled topic landing order mismatch: "
                f"expected {list(CONTROLLED_TOPIC_KEYS)}, found {list(landing_keys)}"
            )
        for link in landing_links:
            key = link.get("data-topic-key", "")
            if key in CONTROLLED_TOPIC_KEYS and not controlled_topic_href_matches(
                link.get("href", ""), key
            ):
                errors.append(f"controlled topic {key} has invalid landing link")

    wiki_landing_path = public_dir / "wiki" / "index.html"
    if wiki_landing_path.is_file():
        wiki_landing_links = marked_elements(
            wiki_landing_path.read_text(encoding="utf-8"), "controlled-topic-link"
        )
        wiki_landing_keys = tuple(
            link.get("data-topic-key", "") for link in wiki_landing_links
        )
        if wiki_landing_keys != CONTROLLED_TOPIC_KEYS:
            errors.append(
                "Wiki landing controlled topic order mismatch: "
                f"expected {list(CONTROLLED_TOPIC_KEYS)}, found {list(wiki_landing_keys)}"
            )
        for link in wiki_landing_links:
            key = link.get("data-topic-key", "")
            if key in CONTROLLED_TOPIC_KEYS and not controlled_topic_href_matches(
                link.get("href", ""), key
            ):
                errors.append(f"controlled topic {key} has invalid Wiki landing link")

    for key in CONTROLLED_TOPIC_KEYS:
        path = topics_dir / key / "index.html"
        if not path.is_file():
            continue
        page_html = path.read_text(encoding="utf-8")
        markers = marked_elements(page_html, "controlled-topic")
        if len(markers) != 1:
            errors.append(
                f"controlled topic marker count for {key}: expected 1, found {len(markers)}"
            )
            continue
        marker = markers[0]
        if marker.get("data-topic-key") != key:
            errors.append(f"controlled topic marker key mismatch for {key}")
        count_text = marker.get("data-topic-count", "")
        expected_count = int(count_text) if re.fullmatch(r"[1-9][0-9]*", count_text) else None
        if expected_count is None:
            errors.append(f"controlled topic {key} has invalid page count: {count_text!r}")

        entries = marked_elements(page_html, "controlled-topic-entry")
        if expected_count is not None and len(entries) != expected_count:
            errors.append(
                f"controlled topic {key} entry count mismatch: "
                f"expected {expected_count}, found {len(entries)}"
            )
        hrefs = [entry.get("href", "") for entry in entries]
        if len(set(hrefs)) != len(hrefs):
            errors.append(f"controlled topic {key} contains duplicate knowledge links")
        if not any(entry.get("data-topic-kind") == "concept" for entry in entries):
            errors.append(f"controlled topic {key} must include at least one concept")
        for href in hrefs:
            target = internal_wiki_target(public_dir, href)
            if target is None or not target.is_file():
                errors.append(f"controlled topic {key} has missing knowledge target: {href}")
                continue
            reverse_links = marked_elements(
                target.read_text(encoding="utf-8"), "wiki-topic-link"
            )
            matching_reverse_links = [
                link for link in reverse_links if link.get("data-topic-key", "") == key
            ]
            if not matching_reverse_links:
                errors.append(
                    f"controlled topic {key} knowledge page is missing reverse topic link: {href}"
                )
            elif len(matching_reverse_links) != 1 or not controlled_topic_href_matches(
                matching_reverse_links[0].get("href", ""), key
            ):
                errors.append(
                    f"controlled topic {key} knowledge page has invalid reverse topic link: {href}"
                )


def validate_legacy_tags(public_dir: Path, errors: list[str]) -> None:
    tags_dir = public_dir / "tags"
    if not tags_dir.is_dir():
        errors.append("missing legacy tag compatibility directory")
        return
    pages = sorted(tags_dir.rglob("index.html"))
    root_path = tags_dir / "index.html"
    if not root_path.is_file():
        errors.append("missing legacy tag compatibility root")
        return

    root_html = root_path.read_text(encoding="utf-8")
    root_parser = LegacyTagMetadataParser()
    root_parser.feed(root_html)
    manifest_text = "".join(root_parser.route_manifest_chunks).strip()
    expected_pages = {root_path.relative_to(public_dir).as_posix()}
    try:
        manifest_routes = json.loads(html.unescape(manifest_text))
    except (json.JSONDecodeError, TypeError) as error:
        errors.append(f"invalid legacy tag route manifest: {error}")
        manifest_routes = []
    if not isinstance(manifest_routes, list) or not all(
        isinstance(route, str) for route in manifest_routes
    ):
        errors.append("legacy tag route manifest must be a list of URLs")
        manifest_routes = []
    if len(set(manifest_routes)) != len(manifest_routes):
        errors.append("legacy tag route manifest contains duplicate URLs")

    for route in manifest_routes:
        url_path = local_route_path(route)
        marker = "/tags/"
        if url_path is None or url_path.count(marker) != 1:
            errors.append(f"invalid legacy tag route manifest URL: {route}")
            continue
        tail = url_path.rsplit(marker, 1)[1].strip("/")
        if not tail or "/" in tail:
            errors.append(f"invalid legacy tag term route: {route}")
            continue
        expected_pages.add(
            (Path("tags") / unquote(tail) / "index.html").as_posix()
        )

    actual_pages = {
        path.relative_to(public_dir).as_posix()
        for path in pages
    }
    if actual_pages != expected_pages:
        missing = sorted(expected_pages - actual_pages)
        unexpected = sorted(actual_pages - expected_pages)
        errors.append(
            "legacy tag route coverage mismatch: "
            f"missing {len(missing)} {missing[:3]}, "
            f"unexpected {len(unexpected)} {unexpected[:3]}"
        )

    root_canonical = extracted_attribute(CANONICAL_URL_RE.search(root_html))
    for path in pages:
        page_html = path.read_text(encoding="utf-8")
        relative = path.relative_to(public_dir).as_posix()
        parser = LegacyTagMetadataParser()
        parser.feed(page_html)
        if len(parser.robots_contents) != 1:
            errors.append(
                f"legacy tag robots directive count in {relative}: "
                f"expected 1, found {len(parser.robots_contents)}"
            )
        else:
            directives = {
                directive
                for directive in re.split(r"[\s,]+", parser.robots_contents[0].casefold())
                if directive
            }
            if not {"noindex", "follow"}.issubset(directives):
                errors.append(f"legacy tag page must be noindex, follow: {relative}")
        markers = marked_elements(page_html, "legacy-tag-page")
        if len(markers) != 1:
            errors.append(
                f"legacy tag page is missing compatibility marker: {relative}"
            )
        validate_metadata_page(path, public_dir, errors)
        canonical = extracted_attribute(CANONICAL_URL_RE.search(page_html))
        if root_canonical is not None and canonical is not None:
            if path == root_path:
                expected_canonical = root_canonical
            else:
                term = path.parent.relative_to(tags_dir).as_posix()
                expected_canonical = urljoin(root_canonical, f"{quote(term, safe='/')}/")
            if canonical != expected_canonical:
                errors.append(
                    f"legacy tag canonical mismatch in {relative}: "
                    f"expected {expected_canonical}, found {canonical}"
                )


def validate_controlled_topic_sitemap(
    urls: list[str], site_root_url: str | None, errors: list[str]
) -> None:
    if not site_root_url:
        errors.append("missing site root canonical for sitemap validation")
        return
    expected_urls = {
        urljoin(site_root_url, "topics/"),
        *(
            urljoin(site_root_url, f"topics/{key}/")
            for key in CONTROLLED_TOPIC_KEYS
        ),
    }
    found_urls = set(urls).intersection(expected_urls)
    if found_urls != expected_urls:
        errors.append(
            "controlled topic sitemap coverage mismatch: "
            f"missing {sorted(expected_urls - found_urls)}"
        )

    tag_root = urljoin(site_root_url, "tags/")
    try:
        parsed_tag_root = urlsplit(tag_root)
    except ValueError:
        errors.append(f"invalid expected tag root URL: {tag_root}")
        return
    for url in urls:
        try:
            parsed = urlsplit(url)
        except ValueError:
            continue
        if (
            parsed.scheme == parsed_tag_root.scheme
            and parsed.netloc == parsed_tag_root.netloc
            and (
                parsed.path == parsed_tag_root.path.rstrip("/")
                or parsed.path.startswith(parsed_tag_root.path)
            )
        ):
            errors.append(f"raw tag URL found in sitemap: {parsed.path}")


def validate_pagefind_output(public_dir: Path, errors: list[str]) -> None:
    pagefind_dir = public_dir / "pagefind"
    if not list(pagefind_dir.glob("*.pf_meta")):
        errors.append("missing Pagefind metadata index")
    if not list((pagefind_dir / "index").glob("*.pf_index")):
        errors.append("missing Pagefind search index")

    fragments = list((pagefind_dir / "fragment").glob("*.pf_fragment"))
    if not fragments:
        errors.append("missing Pagefind result fragments")
        return

    decoded_fragments = []
    for fragment in fragments:
        try:
            decoded_fragments.append(gzip.decompress(fragment.read_bytes()))
        except (OSError, EOFError) as exc:
            relative = fragment.relative_to(public_dir).as_posix()
            errors.append(f"invalid Pagefind result fragment: {relative}: {exc}")
            return

    if not any(b"/wiki/current-synthesis/" in fragment for fragment in decoded_fragments):
        errors.append("Current Synthesis is missing from Pagefind result fragments")
    if any(b"/_generated/" in fragment for fragment in decoded_fragments):
        errors.append("internal _generated URL found in Pagefind result fragments")
    if any(b"/tags/" in fragment for fragment in decoded_fragments):
        errors.append("legacy raw tag URL found in Pagefind result fragments")


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
        if link_parser.has_raw_tag_link:
            relative = path.relative_to(public_dir).as_posix()
            errors.append(f"raw tag navigation link is forbidden: {relative}")

    for relative in REQUIRED_FILES:
        if not (public_dir / relative).is_file():
            errors.append(f"missing required file: {relative}")

    for relative in METADATA_PAGE_FILES:
        path = public_dir / relative
        if path.is_file():
            validate_metadata_page(path, public_dir, errors)

    validate_current_synthesis(public_dir, errors)
    validate_controlled_topics(public_dir, errors)
    validate_legacy_tags(public_dir, errors)
    try:
        show_profiles = json.loads(SHOW_PROFILES_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"invalid generated show profile projection: {error}")
    else:
        validate_show_profiles(public_dir, show_profiles, errors)

    homepage = public_dir / "index.html"
    homepage_canonical = None
    if homepage.is_file():
        homepage_html = homepage.read_text(encoding="utf-8")
        homepage_canonical = extracted_attribute(CANONICAL_URL_RE.search(homepage_html))
        if re.search(
            r"http-equiv\s*=\s*(?:[\"']\s*refresh\s*[\"']|refresh\b)",
            homepage_html,
            re.IGNORECASE,
        ):
            errors.append("homepage is still an automatic redirect")
        if "A living knowledge atlas synthesized from podcasts." not in homepage_html:
            errors.append("homepage is missing the discovery introduction")

    validate_pagefind_output(public_dir, errors)

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
        public_dir / "topics",
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

                validate_controlled_topic_sitemap(urls, homepage_canonical, errors)

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
