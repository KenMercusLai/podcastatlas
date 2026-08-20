from pathlib import Path
import re
import tomllib
import unittest


def front_matter(path, delimiter):
    text = path.read_text()
    if not text.startswith(f"{delimiter}\n"):
        raise AssertionError(f"{path} does not start with {delimiter} front matter")
    parts = text.split(delimiter, 2)
    if len(parts) != 3:
        raise AssertionError(f"{path} has unterminated {delimiter} front matter")
    return parts[1]


ROOT = Path(__file__).resolve().parents[1]
SINGLE_LAYOUT = ROOT / "layouts/_default/single.html"
SOURCE_EPISODE_LINK = ROOT / "layouts/partials/wiki-source-episode-link.html"
SOURCE_EPISODE_PAGE = ROOT / "layouts/partials/wiki-source-episode-page.html"
SOURCE_ORIGINAL_AUDIO_LINK = ROOT / "layouts/partials/wiki-source-original-audio-link.html"
EPISODE_SOURCE_NOTE_LINK = ROOT / "layouts/partials/episode-source-note-link.html"
EPISODE_SOURCE_NOTE_PAGE = ROOT / "layouts/partials/episode-source-note-page.html"
EPISODE_SOURCE_RELATIONS = ROOT / "layouts/partials/episode-source-relations.html"


class EpisodeSourcePresentationTest(unittest.TestCase):
    def test_episode_and_source_note_use_reader_facing_names(self):
        single = SINGLE_LAYOUT.read_text()
        source_episode_link = SOURCE_EPISODE_LINK.read_text()

        self.assertIn("Episode guide", single)
        self.assertIn(">Original audio</a>", single)
        self.assertNotIn(">Source</a>", single)
        self.assertIn("Source note", single)
        self.assertIn(">Episode guide</a>", source_episode_link)
        self.assertNotIn(">Episode summary</a>", source_episode_link)

    def test_both_relation_directions_use_one_cached_map(self):
        single = SINGLE_LAYOUT.read_text()

        self.assertTrue(EPISODE_SOURCE_NOTE_LINK.is_file())
        self.assertTrue(EPISODE_SOURCE_NOTE_PAGE.is_file())
        self.assertTrue(EPISODE_SOURCE_RELATIONS.is_file())
        self.assertIn('$sourceNotePage := partial "episode-source-note-page.html" .', single)
        self.assertIn('partial "episode-source-note-link.html" $sourceNotePage', single)

        link = EPISODE_SOURCE_NOTE_LINK.read_text()
        episode_to_source = EPISODE_SOURCE_NOTE_PAGE.read_text()
        source_to_episode = SOURCE_EPISODE_PAGE.read_text()
        relations = EPISODE_SOURCE_RELATIONS.read_text()

        self.assertIn("with .", link)
        self.assertNotIn('partial "episode-source-note-page.html"', link)
        self.assertIn('href="{{ .RelPermalink }}"', link)
        self.assertIn(">Source note</a>", link)
        self.assertIn('partialCached "episode-source-relations.html"', episode_to_source)
        self.assertIn('partialCached "episode-source-relations.html"', source_to_episode)
        self.assertNotIn("range", source_to_episode)
        self.assertIn("$episode.File.LogicalName", episode_to_source)
        self.assertIn("$sourceNote.File.LogicalName", source_to_episode)
        self.assertIn(".Params.source_file", relations)
        self.assertIn('"sourceNotesByEpisode"', relations)
        self.assertIn('"episodesBySourceNote"', relations)
        self.assertIn("multiple source notes reference episode file", relations)
        self.assertIn("source note %s references missing episode file", relations)
        self.assertIn("newScratch", relations)

    def test_source_note_original_audio_comes_from_linked_episode(self):
        single = SINGLE_LAYOUT.read_text()

        self.assertTrue(SOURCE_ORIGINAL_AUDIO_LINK.is_file())
        self.assertIn('partial "wiki-source-original-audio-link.html" .', single)
        self.assertNotIn(".Params.audio_url", single)

        audio_link = SOURCE_ORIGINAL_AUDIO_LINK.read_text()
        self.assertIn('partial "wiki-source-episode-page.html"', audio_link)
        self.assertIn(".Params.source_url", audio_link)
        self.assertIn(">Original audio</a>", audio_link)

    def test_source_note_episode_mapping_is_total_and_one_to_one(self):
        episodes = {
            path.name: tomllib.loads(front_matter(path, "+++"))
            for path in (ROOT / "content/episodes").glob("*.md")
        }
        source_files = {}

        for path in (ROOT / "content/wiki/sources").glob("*.md"):
            if path.name == "_index.md":
                continue

            match = re.search(
                r'^source_file:\s*["\']?(.+?)["\']?\s*$',
                front_matter(path, "---"),
                re.MULTILINE,
            )
            if match is None:
                self.fail(f"{path} has no source_file")
            episode_name = re.split(r"[\\\\/]", match.group(1).strip('"\''))[-1]
            self.assertIn(
                episode_name,
                episodes,
                f"{path} points to missing episode {episode_name}",
            )
            self.assertTrue(
                episodes[episode_name].get("source_url"),
                f"{episode_name} has no source_url for the Original audio link",
            )
            self.assertNotIn(
                episode_name,
                source_files,
                f"{path} and {source_files.get(episode_name)} map to the same episode",
            )
            source_files[episode_name] = path

        self.assertTrue(source_files)


if __name__ == "__main__":
    unittest.main()
