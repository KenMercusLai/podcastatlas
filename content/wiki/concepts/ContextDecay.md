---
title: "Context Decay"
type: concept
tags: [ai, context, agents, rag]
sources: [xiangliang-moxing-gongchengshi-ai-de-yincang-pingjing-yu-xinshidai-de-xinxi-migong-4b6cf945-d64a-4dd0-95a7-cb8f11963698]
last_updated: 2026-07-09
---

# Context Decay

Context decay is the failure mode where long conversations or long-running AI workflows lose, blur, or misapply earlier information. In [[xiangliang-moxing-gongchengshi-ai-de-yincang-pingjing-yu-xinshidai-de-xinxi-migong-4b6cf945-d64a-4dd0-95a7-cb8f11963698]], [[HanYang]] and [[NStudent]] discuss this as "context rot": as multi-turn interaction grows, early state can become vague even when it technically remains in the window.

The concept qualifies simple long-context optimism. Longer windows help with some single-document tasks, but they do not automatically solve [[RetrievalAugmentedGeneration]], [[DeepResearch]], or agent work. Useful systems still need [[ContextEngineering]], retrieval, summaries, tests, source links, and [[HumanJudgmentUnderAI]] to decide which information remains active.

## Key Claims
- More context is not the same as better use of context.
- Long conversations can preserve tokens while losing operational clarity.
- Context decay can make an agent repeat work, forget constraints, undo earlier fixes, or answer from stale assumptions.
- [[LongHorizonAI]] requires active state management: retrieve, summarize, forget, and re-check.
- RAG and knowledge graphs can be viewed as structured responses to context decay, but they need evaluation and upkeep.

## Connections
- [[ContextEngineering]] - practices for preserving useful context.
- [[LongHorizonAI]] - model and harness direction that tries to handle extended tasks.
- [[RetrievalAugmentedGeneration]] and [[DocumentChunking]] - retrieval-based alternative to dumping everything into one prompt.
- [[AgentHarness]] and [[PersistentAgentMemory]] - system layers that decide what state survives.
- [[AICodingVerification]] - catches regressions when coding agents lose prior context.
