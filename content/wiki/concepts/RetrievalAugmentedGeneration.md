---
title: "Retrieval-Augmented Generation"
type: concept
tags: [ai, rag, retrieval, knowledge-management]
sources: [xiangliang-moxing-gongchengshi-ai-de-yincang-pingjing-yu-xinshidai-de-xinxi-migong-4b6cf945-d64a-4dd0-95a7-cb8f11963698, weishenme-guigu-kaishi-zhongxin-dingyi-ai-jiyi-s10e20-a70c41aa-41ae-488d-a6e2-63c3de5b9ec3]
last_updated: 2026-07-09
---

# Retrieval-Augmented Generation

Retrieval-augmented generation is the pattern of giving a language model external knowledge so its answer can be grounded in retrieved material rather than only in model weights. In [[xiangliang-moxing-gongchengshi-ai-de-yincang-pingjing-yu-xinshidai-de-xinxi-migong-4b6cf945-d64a-4dd0-95a7-cb8f11963698]], [[NStudent]] separates broad RAG from narrow enterprise RAG: broad RAG means connecting models to external sources, while narrow RAG means cleaning documents, splitting them into chunks, vectorizing them, retrieving candidates, reranking them, and asking the model to answer from the original text.

The source's strongest contribution is that RAG is a system problem rather than a simple upload step. [[DocumentChunking]], [[VectorModelEngineering]], [[SemanticSearchRelevance]], [[RerankingModels]], [[HardNegativeMining]], source-document quality, long-tail knowledge, PDF conversion, industry jargon, and [[AISearchEvaluation]] all influence whether the final answer is useful.

[[weishenme-guigu-kaishi-zhongxin-dingyi-ai-jiyi-s10e20-a70c41aa-41ae-488d-a6e2-63c3de5b9ec3]] adds the memory-layer limitation. [[KangHongwen]] treats RAG as useful but insufficient for personal memory if the system has not first performed [[DataToMemoryTransformation]] across multimodal archives and cannot precisely recover older events, clips, people, or timestamps.

## Key Claims
- RAG reduces hallucination by giving the model external material, but it does not guarantee correct search, ranking, or interpretation.
- Enterprise RAG often fails before generation because documents are messy, fragmented, duplicated, scanned, table-heavy, or full of local business shorthand.
- The language model reads retrieved raw text, not the vectors themselves.
- Long context can cover some single-document reading tasks, but it does not replace retrieval over very large knowledge bases.
- Agent systems still need retrieval tools; better [[AgentHarness]] design can reduce wasteful keyword-search loops.
- RAG quality is inseparable from [[AIVerification]] and [[HumanJudgmentUnderAI]], because users must decide whether the returned evidence really answers the question.
- In personal memory systems, retrieval must sit above multimodal understanding and memory curation; vector search alone does not turn raw data into memory.

## Connections
- [[VectorModelEngineering]] - embedding and recall layer.
- [[DocumentChunking]] - document-unit design problem.
- [[RerankingModels]] - second-stage ranking layer after recall.
- [[SemanticSearchRelevance]] and [[HardNegativeMining]] - relevance definition and training data.
- [[ContextEngineering]], [[DeepResearch]], and [[LongHorizonAI]] - broader context/search/agent threads.
- [[AISearchEvaluation]] - evaluation problem for RAG and research answers.
- [[DataToMemoryTransformation]] and [[MultimodalPersonalMemory]] - memory-layer requirements added by S10E20.
