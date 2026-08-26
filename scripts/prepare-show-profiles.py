#!/usr/bin/env python3
"""Derive deterministic per-show identity data from canonical site content."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EPISODES_DIR = ROOT / "content" / "episodes"
SOURCES_DIR = ROOT / "content" / "wiki" / "sources"
ENTITIES_DIR = ROOT / "content" / "wiki" / "entities"
TOPIC_MEMBERSHIP_PATH = ROOT / "data" / "wiki_topic_membership.json"
WIKI_LINKS_PATH = ROOT / "data" / "wiki_links.json"
OUTPUT_PATH = ROOT / "data" / "show_profiles.json"
TOPIC_ORDER = ("technology", "economics", "history", "politics", "culture", "science")
PERSON_TAGS = frozenset({"person"})
ORGANIZATION_TAGS = frozenset(
    {
        "agency",
        "company",
        "foundation",
        "government",
        "institution",
        "investment-firm",
        "ngo",
        "nonprofit",
        "organization",
        "research-firm",
        "university",
    }
)


@dataclass(frozen=True)
class Episode:
    file_name: str
    title: str
    show: str
    published: str


def split_front_matter(text: str) -> tuple[str, list[str]]:
    lines = text.splitlines()
    if not lines or lines[0] not in {"+++", "---"}:
        raise ValueError("missing front matter")
    delimiter = lines[0]
    for index, line in enumerate(lines[1:], start=1):
        if line == delimiter:
            return delimiter, lines[1:index]
    raise ValueError("unterminated front matter")


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def scalar(lines: list[str], key: str, delimiter: str) -> str:
    separator = "=" if delimiter == "+++" else ":"
    prefix = f"{key} {separator}" if delimiter == "+++" else f"{key}:"
    for raw_line in lines:
        line = raw_line.strip()
        if line.startswith(prefix):
            return strip_quotes(line.split(separator, 1)[1])
    return ""


def front_matter_list(lines: list[str], key: str) -> tuple[str, ...]:
    prefix = f"{key}:"
    for index, raw_line in enumerate(lines):
        line = raw_line.strip()
        if not line.startswith(prefix):
            continue
        value = line.split(":", 1)[1].strip()
        if value:
            if not value.startswith("[") or not value.endswith("]"):
                raise ValueError(f"{key} must be a list")
            return tuple(
                strip_quotes(item.strip())
                for item in value[1:-1].split(",")
                if item.strip()
            )

        key_indent = len(raw_line) - len(raw_line.lstrip())
        items: list[str] = []
        for item_line in lines[index + 1 :]:
            stripped = item_line.strip()
            if not stripped:
                continue
            item_indent = len(item_line) - len(item_line.lstrip())
            if item_indent <= key_indent:
                break
            if not stripped.startswith("- "):
                raise ValueError(f"{key} must be a list")
            item = strip_quotes(stripped[2:].strip())
            if not item:
                raise ValueError(f"{key} contains an empty item")
            items.append(item)
        if not items:
            raise ValueError(f"{key} must be a list")
        return tuple(items)
    return ()


def normalize_date(raw_value: str) -> str:
    value = raw_value.strip()
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return parsed.date().isoformat()
    except ValueError:
        try:
            return date.fromisoformat(value).isoformat()
        except ValueError as error:
            raise ValueError(f"invalid episode date: {raw_value!r}") from error


def load_episodes(path: Path) -> dict[str, Episode]:
    episodes: dict[str, Episode] = {}
    for episode_path in sorted(path.glob("*.md")):
        delimiter, front_matter = split_front_matter(episode_path.read_text(encoding="utf-8"))
        title = scalar(front_matter, "title", delimiter)
        show = scalar(front_matter, "show", delimiter)
        published = scalar(front_matter, "date", delimiter)
        if not title or not show or not published:
            raise ValueError(f"{episode_path}: title, show, and date are required")
        file_name = unicodedata.normalize("NFC", episode_path.name)
        if file_name in episodes:
            raise ValueError(f"duplicate normalized episode filename: {file_name}")
        episodes[file_name] = Episode(file_name, title, show, normalize_date(published))
    if not episodes:
        raise ValueError("episode corpus is empty")
    return episodes


def load_source_episode_map(path: Path, episodes: dict[str, Episode]) -> dict[str, str]:
    source_to_episode: dict[str, str] = {}
    episode_owner: dict[str, str] = {}
    for source_path in sorted(path.glob("*.md")):
        if source_path.name.startswith("_"):
            continue
        delimiter, front_matter = split_front_matter(source_path.read_text(encoding="utf-8"))
        source_file = scalar(front_matter, "source_file", delimiter)
        if not source_file:
            raise ValueError(f"{source_path}: source_file is required")
        episode_file = unicodedata.normalize("NFC", Path(source_file).name)
        if episode_file not in episodes:
            raise ValueError(f"{source_path}: source_file does not match an episode: {episode_file}")
        source_key = unicodedata.normalize("NFC", source_path.stem)
        if source_key in source_to_episode:
            raise ValueError(f"duplicate normalized source key: {source_key}")
        previous = episode_owner.get(episode_file)
        if previous:
            raise ValueError(
                f"multiple source notes map to episode {episode_file}: {previous}, {source_key}"
            )
        source_to_episode[source_key] = episode_file
        episode_owner[episode_file] = source_key
    return source_to_episode


def load_json_object(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"invalid JSON object: {path}") from error
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def entity_kind(tags: set[str]) -> str | None:
    if tags.intersection(PERSON_TAGS):
        return "person"
    if tags.intersection(ORGANIZATION_TAGS):
        return "organization"
    return None


def load_entity_support(
    path: Path,
    source_to_episode: dict[str, str],
    wiki_links: dict,
) -> list[dict]:
    entities: list[dict] = []
    for entity_path in sorted(path.glob("*.md")):
        if entity_path.name.startswith("_"):
            continue
        delimiter, front_matter = split_front_matter(entity_path.read_text(encoding="utf-8"))
        tags = {value.casefold() for value in front_matter_list(front_matter, "tags")}
        kind = entity_kind(tags)
        if kind is None:
            continue
        sources = front_matter_list(front_matter, "sources")
        episode_files = sorted(
            {source_to_episode[source] for source in sources if source in source_to_episode}
        )
        if len(episode_files) < 2:
            continue
        key = unicodedata.normalize("NFC", entity_path.stem)
        link = wiki_links.get(key)
        if not isinstance(link, dict):
            raise ValueError(f"selected entity is missing wiki link data: {key}")
        title = link.get("title")
        url = link.get("url")
        if not isinstance(title, str) or not title.strip():
            raise ValueError(f"selected entity has invalid title: {key}")
        if not isinstance(url, str) or not url.startswith("/wiki/entities/") or not url.endswith("/"):
            raise ValueError(f"selected entity has invalid URL: {key}")
        entities.append(
            {
                "key": key,
                "title": title,
                "url": url,
                "kind": kind,
                "episode_files": episode_files,
            }
        )
    return entities


def build_show_profiles(
    episodes_dir: Path = EPISODES_DIR,
    sources_dir: Path = SOURCES_DIR,
    entities_dir: Path = ENTITIES_DIR,
    topic_membership_path: Path = TOPIC_MEMBERSHIP_PATH,
    wiki_links_path: Path = WIKI_LINKS_PATH,
) -> dict:
    episodes = load_episodes(episodes_dir)
    source_to_episode = load_source_episode_map(sources_dir, episodes)
    topic_membership = load_json_object(topic_membership_path)
    wiki_links = load_json_object(wiki_links_path)
    entity_support = load_entity_support(entities_dir, source_to_episode, wiki_links)

    episodes_by_show: dict[str, list[Episode]] = defaultdict(list)
    for episode in episodes.values():
        episodes_by_show[episode.show].append(episode)
    for values in episodes_by_show.values():
        values.sort(key=lambda item: (item.published, item.file_name), reverse=True)

    source_keys_by_show: dict[str, list[str]] = defaultdict(list)
    source_key_by_episode: dict[str, str] = {}
    for source_key, episode_file in source_to_episode.items():
        show = episodes[episode_file].show
        source_keys_by_show[show].append(source_key)
        source_key_by_episode[episode_file] = source_key

    topic_rank = {key: index for index, key in enumerate(TOPIC_ORDER)}
    shows: dict[str, dict] = {}
    for show in sorted(episodes_by_show, key=str.casefold):
        show_episodes = episodes_by_show[show]
        show_source_keys = sorted(source_keys_by_show.get(show, []))
        topic_counts: Counter[str] = Counter()
        topic_records: dict[str, dict] = {}
        matched_source_count = 0
        for source_key in show_source_keys:
            raw_topics = topic_membership.get(source_key, [])
            if not isinstance(raw_topics, list):
                raise ValueError(f"invalid topic membership for source: {source_key}")
            seen_for_source: set[str] = set()
            for topic in raw_topics:
                if not isinstance(topic, dict):
                    raise ValueError(f"invalid topic record for source: {source_key}")
                key = topic.get("key")
                label = topic.get("label")
                url = topic.get("url")
                if key not in topic_rank:
                    raise ValueError(f"unknown controlled topic for source {source_key}: {key}")
                if not isinstance(label, str) or not isinstance(url, str):
                    raise ValueError(f"invalid controlled topic metadata for source: {source_key}")
                if url != f"/topics/{key}/":
                    raise ValueError(f"invalid controlled topic route for source {source_key}: {url!r}")
                if label != key.title():
                    raise ValueError(f"invalid controlled topic label for source {source_key}: {label!r}")
                if key in seen_for_source:
                    raise ValueError(f"duplicate topic {key} for source: {source_key}")
                seen_for_source.add(key)
                topic_counts[key] += 1
                topic_records[key] = {"key": key, "label": label, "url": url}
            if seen_for_source:
                matched_source_count += 1

        ranked_topic_keys = sorted(
            topic_counts,
            key=lambda key: (-topic_counts[key], topic_rank[key]),
        )[:4]
        topics = [
            {
                **topic_records[key],
                "source_note_count": topic_counts[key],
            }
            for key in ranked_topic_keys
        ]

        show_episode_files = {episode.file_name for episode in show_episodes}
        entities = []
        for entity in entity_support:
            support_count = len(show_episode_files.intersection(entity["episode_files"]))
            if support_count >= 2:
                entities.append(
                    {
                        "key": entity["key"],
                        "title": entity["title"],
                        "url": entity["url"],
                        "kind": entity["kind"],
                        "episode_count": support_count,
                    }
                )
        entities.sort(key=lambda item: (-item["episode_count"], item["title"].casefold(), item["key"].casefold()))
        entities = entities[:8]

        start_here: list[str] = []
        for topic_key in ranked_topic_keys:
            for episode in show_episodes:
                source_key = source_key_by_episode.get(episode.file_name)
                source_topics = topic_membership.get(source_key, []) if source_key else []
                if any(record.get("key") == topic_key for record in source_topics):
                    if episode.file_name not in start_here:
                        start_here.append(episode.file_name)
                    break
            if len(start_here) == 4:
                break
        for episode in show_episodes:
            if len(start_here) == 4:
                break
            if episode.file_name not in start_here:
                start_here.append(episode.file_name)

        shows[show] = {
            "episode_count": len(show_episodes),
            "earliest_episode_date": show_episodes[-1].published,
            "latest_episode_date": show_episodes[0].published,
            "latest_episode_file": show_episodes[0].file_name,
            "source_note_count": len(show_source_keys),
            "topic_matched_source_note_count": matched_source_count,
            "topics": topics,
            "entities": entities,
            "start_here_episode_files": start_here,
        }

    return {"version": 1, "shows": shows}


def render_payload(payload: dict) -> str:
    return json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail when committed projection is stale")
    args = parser.parse_args()

    rendered = render_payload(build_show_profiles())
    if args.check:
        if not OUTPUT_PATH.exists() or OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
            print(f"stale show profile projection: {OUTPUT_PATH}", flush=True)
            return 1
        return 0
    OUTPUT_PATH.write_text(rendered, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
