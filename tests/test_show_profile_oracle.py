from __future__ import annotations

import json
import subprocess
import tomllib
import unicodedata
import unittest
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOPIC_ORDER = ("technology", "economics", "history", "politics", "culture", "science")
PERSON_TAGS = {"person"}
ORGANIZATION_TAGS = {
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


def nfc(value: str) -> str:
    return unicodedata.normalize("NFC", value)


def tracked_files(prefix: str) -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z", "--", prefix],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [ROOT / path.decode("utf-8") for path in result.stdout.split(b"\0") if path]


def toml_front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("+++\n"):
        raise AssertionError(f"Expected TOML front matter: {path}")
    closing = text.find("\n+++\n", 4)
    if closing < 0:
        raise AssertionError(f"Unclosed TOML front matter: {path}")
    return tomllib.loads(text[4:closing])


def yaml_front_matter(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise AssertionError(f"Expected YAML front matter: {path}")
    closing = text.find("\n---\n", 4)
    if closing < 0:
        raise AssertionError(f"Unclosed YAML front matter: {path}")
    return text[4:closing].splitlines()


def yaml_scalar(lines: list[str], key: str) -> str | None:
    prefix = f"{key}:"
    for line in lines:
        if line.startswith(prefix):
            value = line[len(prefix) :].strip()
            if not value:
                return None
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            return value
    return None


def yaml_list(lines: list[str], key: str) -> list[str]:
    prefix = f"{key}:"
    for index, line in enumerate(lines):
        if not line.startswith(prefix):
            continue
        value = line[len(prefix) :].strip()
        if value.startswith("[") and value.endswith("]"):
            return [
                item.strip().strip("\"'")
                for item in value[1:-1].split(",")
                if item.strip()
            ]
        values: list[str] = []
        for following in lines[index + 1 :]:
            stripped = following.strip()
            if not stripped:
                continue
            if not following.startswith((" ", "\t")):
                break
            if not stripped.startswith("-"):
                break
            values.append(stripped[1:].strip().strip("\"'"))
        return values
    return []


def iso_date(value: date | datetime | str) -> str:
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, date):
        return value.isoformat()
    return str(value)[:10]


def independent_show_profiles() -> dict:
    episodes: dict[str, dict] = {}
    shows: dict[str, list[dict]] = defaultdict(list)
    for path in tracked_files("content/episodes"):
        if path.suffix != ".md" or path.name.startswith("_"):
            continue
        metadata = toml_front_matter(path)
        show_value = metadata["show"]
        show = str(show_value[0] if isinstance(show_value, list) else show_value)
        item = {
            "file": nfc(path.name),
            "show": nfc(show),
            "date": iso_date(metadata["date"]),
        }
        if item["file"] in episodes:
            raise AssertionError(f"Duplicate normalized episode filename: {item['file']}")
        episodes[item["file"]] = item
        shows[item["show"]].append(item)

    source_to_episode: dict[str, dict] = {}
    for path in tracked_files("content/wiki/sources"):
        if path.suffix != ".md" or path.name.startswith("_"):
            continue
        lines = yaml_front_matter(path)
        source_file = yaml_scalar(lines, "source_file")
        if not source_file:
            raise AssertionError(f"Missing source_file: {path}")
        episode_file = nfc(Path(source_file).name)
        if episode_file not in episodes:
            raise AssertionError(f"Source Note points to missing Episode: {path}")
        source_key = nfc(path.stem)
        if source_key in source_to_episode:
            raise AssertionError(f"Duplicate normalized Source Note key: {source_key}")
        source_to_episode[source_key] = episodes[episode_file]

    memberships = json.loads((ROOT / "data/wiki_topic_membership.json").read_text(encoding="utf-8"))
    topic_by_source: dict[str, set[str]] = {}
    topic_metadata: dict[str, tuple[str, str]] = {}
    for source_key in source_to_episode:
        keys: set[str] = set()
        for topic in memberships.get(source_key, []):
            key = topic["key"]
            if key not in TOPIC_ORDER:
                raise AssertionError(f"Unknown controlled topic: {key}")
            keys.add(key)
            topic_metadata[key] = (topic["label"], topic["url"])
        topic_by_source[source_key] = keys

    wiki_links = json.loads((ROOT / "data/wiki_links.json").read_text(encoding="utf-8"))
    entity_support: dict[str, list[dict]] = defaultdict(list)
    for path in tracked_files("content/wiki/entities"):
        if path.suffix != ".md" or path.name.startswith("_"):
            continue
        lines = yaml_front_matter(path)
        tags = {tag.casefold() for tag in yaml_list(lines, "tags")}
        if tags & PERSON_TAGS:
            kind = "person"
        elif tags & ORGANIZATION_TAGS:
            kind = "organization"
        else:
            continue
        key = nfc(path.stem)
        link = wiki_links.get(key)
        if not isinstance(link, dict):
            continue
        support_by_show: dict[str, set[str]] = defaultdict(set)
        for source_key in {nfc(value) for value in yaml_list(lines, "sources")}:
            episode = source_to_episode.get(source_key)
            if episode:
                support_by_show[episode["show"]].add(episode["file"])
        for show, episode_files in support_by_show.items():
            if len(episode_files) >= 2:
                entity_support[show].append(
                    {
                        "key": key,
                        "title": link["title"],
                        "url": link["url"],
                        "kind": kind,
                        "episode_count": len(episode_files),
                    }
                )

    result: dict[str, dict] = {}
    for show in sorted(shows, key=str.casefold):
        newest = sorted(shows[show], key=lambda item: (item["date"], item["file"]), reverse=True)
        source_keys = sorted(key for key, episode in source_to_episode.items() if episode["show"] == show)
        topic_counts: Counter[str] = Counter()
        for source_key in source_keys:
            topic_counts.update(topic_by_source[source_key])
        ranked_topics = sorted(
            topic_counts,
            key=lambda key: (-topic_counts[key], TOPIC_ORDER.index(key)),
        )[:4]
        topics = [
            {
                "key": key,
                "label": topic_metadata[key][0],
                "url": topic_metadata[key][1],
                "source_note_count": topic_counts[key],
            }
            for key in ranked_topics
        ]

        start_files: list[str] = []
        for topic_key in ranked_topics:
            candidates = [
                source_to_episode[source_key]
                for source_key in source_keys
                if topic_key in topic_by_source[source_key]
            ]
            candidate = max(candidates, key=lambda item: (item["date"], item["file"]))
            if candidate["file"] not in start_files:
                start_files.append(candidate["file"])
            if len(start_files) == 4:
                break
        for episode in newest:
            if len(start_files) == 4:
                break
            if episode["file"] not in start_files:
                start_files.append(episode["file"])

        entities = sorted(
            entity_support.get(show, []),
            key=lambda item: (-item["episode_count"], item["title"].casefold(), item["key"]),
        )[:8]
        result[show] = {
            "episode_count": len(newest),
            "earliest_episode_date": min(item["date"] for item in newest),
            "latest_episode_date": newest[0]["date"],
            "latest_episode_file": newest[0]["file"],
            "source_note_count": len(source_keys),
            "topic_matched_source_note_count": sum(bool(topic_by_source[key]) for key in source_keys),
            "topics": topics,
            "entities": entities,
            "start_here_episode_files": start_files,
        }
    return {"version": 1, "shows": result}


class IndependentShowProfileOracleTest(unittest.TestCase):
    def test_committed_projection_matches_an_independent_source_oracle(self):
        actual = json.loads((ROOT / "data/show_profiles.json").read_text(encoding="utf-8"))
        self.assertEqual(independent_show_profiles(), actual)


if __name__ == "__main__":
    unittest.main()
