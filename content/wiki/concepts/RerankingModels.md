---
title: "Reranking Models"
type: concept
tags: [ai, retrieval, ranking, rag]
sources: [xiangliang-moxing-gongchengshi-ai-de-yincang-pingjing-yu-xinshidai-de-xinxi-migong-4b6cf945-d64a-4dd0-95a7-cb8f11963698]
last_updated: 2026-07-09
---

# Reranking Models

Reranking models are second-stage retrieval models that rescore candidate results after a cheaper recall step. In [[xiangliang-moxing-gongchengshi-ai-de-yincang-pingjing-yu-xinshidai-de-xinxi-migong-4b6cf945-d64a-4dd0-95a7-cb8f11963698]], [[NStudent]] describes a common [[RetrievalAugmentedGeneration]] flow: use [[VectorModelEngineering]] to recall a batch of candidates, then use a more specialized reranker to choose the passages most relevant to the user question.

The reason is practical. First-stage recall must search many items quickly, so it can return plausible but weak matches. A reranker can inspect query-document pairs more directly, use a narrower [[SemanticSearchRelevance]] definition, and improve the evidence passed to the final language model.

## Key Claims
- Reranking separates fast recall from more precise relevance scoring.
- A reranker is only useful when the candidate pool contains the right answer often enough.
- Reranking quality depends on labels, hard negatives, task definition, and evaluation metrics.
- In RAG, reranking affects generation quality because the final model can only answer from what it receives.
- Agent search could benefit from better reranking because agents otherwise waste steps on mechanical keyword searches.

## Connections
- [[RetrievalAugmentedGeneration]] - downstream pipeline where reranking is commonly used.
- [[VectorModelEngineering]] - first-stage recall layer that rerankers refine.
- [[HardNegativeMining]] - training mechanism for making rerankers distinguish close wrong answers.
- [[SemanticSearchRelevance]] and [[AISearchEvaluation]] - standards used to judge ranking quality.
- [[DeepResearch]] and [[AgentHarness]] - agentic search contexts where ranking determines useful evidence.
