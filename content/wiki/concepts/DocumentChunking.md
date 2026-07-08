---
title: "Document Chunking"
type: concept
tags: [rag, documents, retrieval, context]
sources: [xiangliang-moxing-gongchengshi-ai-de-yincang-pingjing-yu-xinshidai-de-xinxi-migong-4b6cf945-d64a-4dd0-95a7-cb8f11963698]
last_updated: 2026-07-09
---

# Document Chunking

Document chunking is the process of turning source material into retrieval units. In [[xiangliang-moxing-gongchengshi-ai-de-yincang-pingjing-yu-xinshidai-de-xinxi-migong-4b6cf945-d64a-4dd0-95a7-cb8f11963698]], it is one of the main bottlenecks in [[RetrievalAugmentedGeneration]] because naive splitting by token count, punctuation, or page boundaries can destroy the structure that makes a text meaningful.

The episode treats chunking as a semantic and product decision. A short chunk may answer a parameter question but fail to preserve a book's argument; a long chunk may preserve context but hurt recall precision; a PDF page may contain columns, figures, captions, tables, and layout clues that ordinary text extraction mangles. Good chunking therefore sits between [[ContextEngineering]], [[VectorModelEngineering]], and [[SemanticSearchRelevance]].

## Key Claims
- Chunk size trades off local precision against global structure.
- Books, reports, tables, scanned PDFs, and multi-column layouts often require different chunking strategies.
- The right chunk depends on the question: a parameter lookup and "what is this book about" need different retrieval units.
- Multi-modal page embeddings can bypass some OCR problems but do not remove the need to define useful evidence.
- Bad chunking can make a RAG system look like a weak language model even when the generation step is not the primary failure.

## Connections
- [[RetrievalAugmentedGeneration]] - pipeline that consumes chunks.
- [[VectorModelEngineering]] - converts chunks into searchable vectors.
- [[SemanticSearchRelevance]] - defines whether a chunk answers the user's need.
- [[ContextEngineering]] and [[ContextDecay]] - context preservation and loss around long documents and conversations.
- [[PersonalKnowledgeEcology]] - adjacent personal-archive problem where source structure matters.
