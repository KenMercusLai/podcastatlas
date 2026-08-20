from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def read_template(relative_path: str) -> str:
    path = ROOT / relative_path
    return path.read_text() if path.is_file() else ""


class EpisodePublicationDatesTest(unittest.TestCase):
    def test_every_episode_surface_uses_the_shared_publication_date_partial(self):
        episode_list = read_template("layouts/partials/episode-list.html")
        page_list = read_template("layouts/partials/page-list.html")
        single = read_template("layouts/_default/single.html")

        self.assertIn('partial "episode-publication-date.html" .', episode_list)
        self.assertIn('if eq .Params.type "source"', page_list)
        self.assertIn('partial "episode-publication-date.html" .', page_list)
        self.assertIn('if eq .Params.type "source"', single)
        self.assertGreaterEqual(
            single.count('partial "episode-publication-date.html" .'),
            2,
        )

    def test_wiki_sources_resolve_the_linked_episode_as_the_canonical_date_source(self):
        resolver = read_template("layouts/partials/wiki-source-episode-page.html")
        relations = read_template("layouts/partials/episode-source-relations.html")
        date_partial = read_template("layouts/partials/episode-publication-date.html")
        source_link = read_template("layouts/partials/wiki-source-episode-link.html")

        self.assertIn('.Params.source_file', relations)
        self.assertIn('partialCached "episode-source-relations.html"', resolver)
        self.assertIn('File.LogicalName', resolver)
        self.assertIn('return $episode', resolver)
        self.assertIn('partial "wiki-source-episode-page.html" $page', date_partial)
        self.assertIn(".Date", date_partial)
        self.assertNotIn("last_updated", date_partial)
        self.assertIn('partial "wiki-source-episode-page.html" $page', source_link)

    def test_update_dates_remain_only_for_non_source_wiki_pages(self):
        page_list = read_template("layouts/partials/page-list.html")
        single = read_template("layouts/_default/single.html")

        self.assertIn('if ne .Params.type "source"', page_list)
        self.assertLess(
            page_list.index('if ne .Params.type "source"'),
            page_list.index("last_updated"),
        )

        source_branch = single.index('if eq .Params.type "source"')
        update_branch = single.index("last_updated", source_branch)
        self.assertIn("else", single[source_branch:update_branch])


if __name__ == "__main__":
    unittest.main()
