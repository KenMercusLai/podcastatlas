# Wiki Lint Report — 2026-08-23

Scanned 13168 pages.

## Structural Issues

### Orphan Pages (no inbound links)
- `wiki/entities/BobosOatBars.md`

## Graph-Aware Issues

### Hub Pages with Insufficient Content (0 pages)
No hub stubs detected — all high-degree nodes have sufficient content.

### Fragile Bridges (5 community pairs)
These community connections rely on a single edge — one broken link isolates them:
- Community 0 ↔ Community 2 via `concepts/SocialEngineeringFraud` → `entities/Cambodia`
- Community 2 ↔ Community 8 via `concepts/FangshiFraudAndAuthority` → `concepts/SocialEngineeringFraud`
- Community 4 ↔ Community 12 via `entities/LongNow` → `concepts/CriticalMineralsGeopolitics`
- Community 8 ↔ Community 15 via `concepts/ValuesFirstTalent` → `concepts/TalentVirtueDistinction`
- Community 13 ↔ Community 15 via `concepts/EconomicWayOfThinking` → `concepts/ComparativeAdvantage`

### Isolated Communities (0 communities)
No isolated communities — all clusters have external connections.

---

## Semantic Checks Unavailable

Semantic lint did not complete because the LLM API call failed.

- Error: `BadRequestError: litellm.BadRequestError: LLM Provider NOT provided. Pass in the LLM provider you are trying to call. You passed model=claude-3-5-sonnet-latest Pass model as E.g. For 'Huggingface' inference endpoints pass in `completion(model='huggingface/starcoder',..)` Learn more: https://docs.litellm.ai/docs/providers`
- Deterministic and graph-aware checks above still completed.
- Configure `LLM_MODEL` with a provider-qualified LiteLLM model and required API key, then rerun `python tools/lint.py` for contradiction, stale-content, and data-gap analysis.