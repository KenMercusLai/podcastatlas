---
title: "Hard Negative Mining"
type: concept
tags: [ai, retrieval, training-data, evaluation]
sources: [xiangliang-moxing-gongchengshi-ai-de-yincang-pingjing-yu-xinshidai-de-xinxi-migong-4b6cf945-d64a-4dd0-95a7-cb8f11963698]
last_updated: 2026-07-09
---

# Hard Negative Mining

Hard negative mining is the practice of constructing training examples that look relevant but should be rejected. In [[xiangliang-moxing-gongchengshi-ai-de-yincang-pingjing-yu-xinshidai-de-xinxi-migong-4b6cf945-d64a-4dd0-95a7-cb8f11963698]], [[NStudent]] describes hard negatives as a central cost in tuning [[VectorModelEngineering]] and [[RerankingModels]] for real enterprise retrieval.

The episode's examples make the problem concrete: industry abbreviations, factory models, part numbers, similar product names, or SEO-stuffed pages may all look close to a generic model while being wrong for the business task. Hard negatives force the model to learn the difference between broad topical similarity and the specific [[SemanticSearchRelevance]] the user needs.

## Key Claims
- Easy negatives teach little because the model can already separate them.
- Hard negatives should be built from the domain's actual failure modes, not only from random unrelated documents.
- Good hard negatives require [[DomainExpertAlignment]] because outsiders may not know which small distinction matters.
- Hard negatives are useful for both first-stage vector models and second-stage rerankers.
- Poor negative design can make a benchmark score improve without making the deployed retrieval system better.

## Connections
- [[VectorModelEngineering]] and [[RerankingModels]] - model layers trained with hard negatives.
- [[RetrievalAugmentedGeneration]] - downstream application harmed by close wrong evidence.
- [[SemanticSearchRelevance]] - standard that decides what should be treated as negative.
- [[AISearchEvaluation]] and [[AIVerification]] - checks that training signals match real usefulness.
- [[HumanJudgmentUnderAI]] - human standard-setting around what counts as wrong.
