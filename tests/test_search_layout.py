from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
BASE_LAYOUT = ROOT / "layouts" / "_default" / "baseof.html"


class SearchLayoutTest(unittest.TestCase):
    def test_every_html_page_is_indexed_without_a_page_level_allowlist(self):
        layout = BASE_LAYOUT.read_text()

        self.assertNotIn("data-pagefind-body", layout)
        self.assertIn('<header class="site-header" data-pagefind-ignore="all">', layout)
        self.assertIn('<footer class="site-footer" data-pagefind-ignore="all">', layout)

    def test_every_site_page_links_to_search(self):
        layout = BASE_LAYOUT.read_text()

        self.assertIn('href="{{ "search/" | relURL }}">Search</a>', layout)

    def test_search_page_loads_pagefind_from_the_deployment_base_path(self):
        content = ROOT / "content" / "search" / "_index.md"
        layout = ROOT / "layouts" / "search" / "list.html"

        self.assertTrue(content.is_file())
        self.assertTrue(layout.is_file())
        rendered = layout.read_text()
        self.assertIn('{{ "pagefind/pagefind-component-ui.css" | relURL }}', rendered)
        self.assertIn('{{ "pagefind/pagefind-component-ui.js" | relURL }}', rendered)
        self.assertIn('type="module"', rendered)
        self.assertIn(
            'bundle-path="{{ "pagefind/" | relURL }}"',
            rendered,
        )
        self.assertNotIn("base-url=", rendered)
        self.assertIn("<pagefind-input></pagefind-input>", rendered)
        self.assertIn("<pagefind-summary></pagefind-summary>", rendered)
        self.assertNotIn("<pagefind-filter-pane", rendered)
        self.assertIn("<pagefind-results hide-sub-results>", rendered)
        self.assertNotIn("<pagefind-searchbox", rendered)
        self.assertIn('data-pagefind-ignore="all"', rendered)
        self.assertIn("instance.pagefindOptions.ranking", rendered)
        self.assertIn("metaWeights: { aliases: 10.0 }", rendered)

    def test_search_page_has_fixed_user_facing_groups_and_custom_result_context(self):
        layout = ROOT / "layouts" / "search" / "list.html"
        rendered = layout.read_text()

        groups = [
            "All",
            "Concepts &amp; Topics",
            "People &amp; Organizations",
            "Episodes",
            "Shows",
            "Source Notes",
        ]
        offsets = [rendered.index(f">{group}<") for group in groups]
        self.assertEqual(offsets, sorted(offsets))
        self.assertIn('data-search-group="Concepts &amp; Topics"', rendered)
        self.assertIn('data-search-group="People &amp; Organizations"', rendered)
        self.assertIn('instance.triggerFilter("group", group ? [group] : [])', rendered)
        self.assertIn("{{ meta.type }}", rendered)
        self.assertIn("{{ meta.context }}", rendered)
        self.assertIn('class="search-result-type"', rendered)
        self.assertIn('class="search-result-context"', rendered)

    def test_search_result_link_preserves_pagefind_url_template_through_hugo(self):
        layout = ROOT / "layouts" / "search" / "list.html"
        rendered = layout.read_text()

        self.assertIn(
            '{{ printf `href="{{ meta.url | default(url) | safeUrl }}"` | safeHTMLAttr }}',
            rendered,
        )

    def test_every_page_exposes_searchable_type_group_context_and_alias_metadata(self):
        layout = BASE_LAYOUT.read_text()
        type_partial = ROOT / "layouts" / "partials" / "search-type.html"
        group_partial = ROOT / "layouts" / "partials" / "search-group.html"
        context_partial = ROOT / "layouts" / "partials" / "search-context.html"
        aliases_partial = ROOT / "layouts" / "partials" / "search-aliases.html"

        for path in (type_partial, group_partial, context_partial, aliases_partial):
            self.assertTrue(path.is_file())

        self.assertIn('partial "search-type.html" .', layout)
        self.assertIn('partial "search-group.html" .', layout)
        self.assertIn('partial "search-context.html" .', layout)
        self.assertIn('partial "search-aliases.html" .', layout)
        self.assertIn('data-pagefind-filter="group[content]"', layout)
        self.assertIn('data-pagefind-meta="group[content]"', layout)
        self.assertIn('data-pagefind-meta="type[content]"', layout)
        self.assertIn('data-pagefind-meta="context[content]"', layout)
        self.assertIn('data-pagefind-meta="aliases[content]"', layout)
        self.assertIn('data-pagefind-index-attrs="content"', layout)
        self.assertIn('itemprop="keywords"', layout)
        self.assertGreater(
            layout.index('data-pagefind-meta="aliases[content]"'),
            layout.index("<body"),
        )
        classifier = type_partial.read_text()
        self.assertIn('.Section "episodes"', classifier)
        self.assertIn(".Params.type", classifier)
        self.assertIn('.Data.Singular "show"', classifier)

        groups = group_partial.read_text()
        self.assertIn('slice "concept" "topic"', groups)
        self.assertIn('"Concepts & Topics"', groups)
        self.assertIn('eq $type "entity"', groups)
        self.assertIn('"People & Organizations"', groups)
        self.assertIn('eq $type "source note"', groups)
        self.assertIn('"Source Notes"', groups)

        context = context_partial.read_text()
        self.assertIn("wiki_knowledge_signals.pages", context)
        self.assertIn(".Params.show", context)
        self.assertIn(".Pages.Len", context)

        aliases = aliases_partial.read_text()
        self.assertIn(".Params.search_aliases", aliases)
        self.assertIn("hugo.Data.search_aliases.entries", aliases)
        self.assertIn("errorf", aliases)
        self.assertIn("in $registryAliases $alias", aliases)
        self.assertNotIn(".Site.Data", aliases)
        self.assertIn(".File.Path", aliases)
        self.assertIn(".value", aliases)
        self.assertNotIn(".Params.aliases", aliases)


if __name__ == "__main__":
    unittest.main()
