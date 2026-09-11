# Wiki Lint Report — 2026-09-11

Scanned 18853 pages.

## Structural Issues

### Orphan Pages (no inbound links)
- `wiki/entities/BobosOatBars.md`

### Broken Wikilinks
- `wiki/concepts/CivilWarThreatRhetoric.md` links to `[[London]]` — not found
- `wiki/sources/trailer-shire-folk-6aa271d1a6e9aef4cc74ef3b.md` links to `[[London]]` — not found
- `wiki/sources/trailer-shire-folk-6aa271d1a6e9aef4cc74ef3b.md` links to `[[London]]` — not found
- `wiki/entities/TommyRobinson.md` links to `[[London]]` — not found
- `wiki/entities/ShireFolk.md` links to `[[London]]` — not found

### Missing Entity Pages (mentioned 3+ times but no page)
> [!warning] Action Required
> Run `python3 tools/heal.py` to automatically materialize these missing entity pages.
- `[[London]]`

## Graph-Aware Issues

### Hub Pages with Insufficient Content (0 pages)
No hub stubs detected — all high-degree nodes have sufficient content.

### Fragile Bridges (1 community pairs)
These community connections rely on a single edge — one broken link isolates them:
- Community 5 ↔ Community 8 via `entities/CatholicChurch` → `concepts/ReligiousControlledSubstanceExemption`

### Isolated Communities (0 communities)
No isolated communities — all clusters have external connections.

---

## Semantic Checks Unavailable

Semantic lint did not complete because the LLM API call failed.

- Error: `BadRequestError: litellm.BadRequestError: LLM Provider NOT provided. Pass in the LLM provider you are trying to call. You passed model=claude-3-5-sonnet-latest Pass model as E.g. For 'Huggingface' inference endpoints pass in `completion(model='huggingface/starcoder',..)` Learn more: https://docs.litellm.ai/docs/providers`
- Deterministic and graph-aware checks above still completed.
- Configure `LLM_MODEL` with a provider-qualified LiteLLM model and required API key, then rerun `python tools/lint.py` for contradiction, stale-content, and data-gap analysis.