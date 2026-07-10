---
title: "Model Collapse"
type: concept
tags: [ai, training-data, model-quality]
sources: [tech-20251219-1219-mp-tech-pod-128-tech-20251219-1219-mp-tech-pod-128, kate-crawford-mapping-empires]
last_updated: 2026-07-10
---

# Model Collapse

Model collapse is the failure mode in [[kate-crawford-mapping-empires]] where models trained repeatedly on synthetic outputs lose diversity, flatten minority patterns, erase outliers, and degrade toward lower-quality or noisier distributions. [[KateCrawford]] also links the idea to model autophagy, where AI systems effectively consume their own outputs.

The concept turns synthetic data from a simple scaling solution into a risk that must be evaluated. It connects [[FrontierModelScaling]] to [[DataRecipeCoCreation]]: more data is not automatically better if the data is recursively generated, homogeneous, hallucinated, or detached from the human and physical variation the model needs to preserve.

[[tech-20251219-1219-mp-tech-pod-128-tech-20251219-1219-mp-tech-pod-128]] adds a consumer-platform route into the same risk. The [[MarketplaceTech]] episode discusses whether large volumes of [[AISlop]] could create feedback loops for future AI training, making platform quality and training-data quality part of the same problem.

## Key Claims
- Repeated training on generated outputs can narrow the distribution a model learns.
- Minority patterns, rare cases, edge cases, and unusual styles are especially exposed when synthetic averages dominate.
- Synthetic data may still be useful, but it needs grounding, filtering, evaluation, and diversity controls.
- Media-scale [[AISlop]] can become a data-quality problem if it enters future crawls.
- Model collapse matters beyond aesthetics because high-stakes systems may depend on rare or outlier cases.
- Public platforms can become part of the model-collapse risk surface if AI-generated material is published at scale and later recrawled as training data.

## Connections
- [[KateCrawford]] - source speaker.
- [[AISlop]] - synthetic media supply that can contaminate future training data.
- [[FrontierModelScaling]] - broader scaling debate around data quantity and quality.
- [[DataRecipeCoCreation]] - need to discover which data mixtures improve systems.
- [[AIRecognitionBias]] - related problem where model confidence can hide skewed or sparse training data.
- [[HumanJudgmentUnderAI]] - review and evaluation remain necessary when generated outputs look plausible.
- [[MarketplaceTech]] and [[MerriamWebster]] - mainstream slop discussion that reinforces the training-data feedback concern.
