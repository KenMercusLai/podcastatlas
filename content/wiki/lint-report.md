# Wiki Lint Report — 2026-08-22

Scanned 12666 pages.

## Structural Issues

### Orphan Pages (no inbound links)
- `wiki/entities/BobosOatBars.md`

## Graph-Aware Issues

### Hub Pages with Insufficient Content (0 pages)
No hub stubs detected — all high-degree nodes have sufficient content.

### Fragile Bridges (3 community pairs)
These community connections rely on a single edge — one broken link isolates them:
- Community 2 ↔ Community 11 via `concepts/AIForScience` → `entities/LiXiaojie`
- Community 3 ↔ Community 7 via `concepts/AttentionIndustrialization` → `concepts/AttentionAsWeather`
- Community 3 ↔ Community 11 via `concepts/HomeRouterSecurityLifecycle` → `concepts/PersonalSecurityTiering`

### Isolated Communities (0 communities)
No isolated communities — all clusters have external connections.

---

## Semantic Checks Unavailable

Semantic lint did not complete because the LLM API call failed.

- Error: `BadRequestError: litellm.BadRequestError: LLM Provider NOT provided. Pass in the LLM provider you are trying to call. You passed model=claude-3-5-sonnet-latest Pass model as E.g. For 'Huggingface' inference endpoints pass in `completion(model='huggingface/starcoder',..)` Learn more: https://docs.litellm.ai/docs/providers`
- Deterministic and graph-aware checks above still completed.
- Configure `LLM_MODEL` with a provider-qualified LiteLLM model and required API key, then rerun `python tools/lint.py` for contradiction, stale-content, and data-gap analysis.