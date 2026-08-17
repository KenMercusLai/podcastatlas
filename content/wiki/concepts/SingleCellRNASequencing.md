---
title: "Single-Cell RNA Sequencing"
type: concept
tags: [biology, genomics, sequencing, ai-for-science]
sources: [ep-8-implementation-of-ai-in-scientific-research]
last_updated: 2026-08-18
---

# Single-Cell RNA Sequencing

Single-cell RNA sequencing is the source's key data-shape change for [[BiomedicalDeepLearning]]. In [[ep-8-implementation-of-ai-in-scientific-research]], [[LucasSimon|Lucas Simon]] contrasts it with bulk RNA sequencing: bulk RNA-seq averages expression across many cells, while single-cell RNA sequencing measures gene expression at the level of individual cells.

The episode says a regular single-cell experiment can profile from around 10,000 cells to about 1 million cells. That changes the modeling setting from a small number of samples by many genes into a much wider cell-level dataset, making [[SingleCellAutoencoderRepresentation|autoencoder representations]] and other deep-learning methods more plausible.

## Key Claims
- Single-cell RNA sequencing turns cell identity and heterogeneity into direct data rather than bulk averages.
- The method can create more observations than genes, which is important for deep-learning workflows.
- Cell-level matrices still need biological interpretation; clustering in hidden space matters only if it maps to meaningful cell types or states.
- Single-cell data extends the earlier [[BioinformaticsDomainGap]] because both computational scale and biological context become more demanding.

## Connections
- [[GeneExpressionMatrix]], [[SequencingDataPipeline]], and [[ComputationalBiology]] - data-processing and analysis context.
- [[BiomedicalDeepLearning]], [[SingleCellAutoencoderRepresentation]], and [[Keras]] - modeling branch from the episode.
- [[AIForScience]], [[HumanDrivenScientificAI]], and [[AIVerification]] - broader validation frame.
