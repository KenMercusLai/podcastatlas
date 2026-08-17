---
title: "Computational Biology"
type: concept
tags: [computational-biology, biology, data-science, ai-for-science]
sources: [ep-8-implementation-of-ai-in-scientific-research]
last_updated: 2026-08-18
---

# Computational Biology

Computational biology is [[LucasSimon|Lucas Simon]]'s source-scoped term in [[ep-8-implementation-of-ai-in-scientific-research]] for downstream analysis once [[Bioinformatics]] has produced an analysis-ready [[GeneExpressionMatrix|gene expression matrix]]. The source gives PCA, modeling, and biological interpretation as examples of what happens after raw sequencing reads have been turned into structured data.

The concept is useful because it separates data preparation from scientific modeling without pretending the boundary is universal. In this episode, [[ComputationalBiology]] is where [[MolecularFeatureEngineering]], [[SingleCellRNASequencing]], [[BiomedicalDeepLearning]], and [[SingleCellAutoencoderRepresentation|autoencoder representations]] become ways to ask biological questions.

## Key Claims
- Computational biology starts after the data matrix exists in Lucas's source-scoped definition.
- The role is not just model fitting; visualization, output analysis, and biological interpretation are part of the workflow.
- It can use standard analysis methods such as PCA as well as deep-learning methods when the data shape supports them.
- In single-cell data, computational biology can connect neural-network hidden spaces to cell-type structure.

## Connections
- [[Bioinformatics]], [[SequencingDataPipeline]], and [[GeneExpressionMatrix]] - upstream workflow layer.
- [[LucasSimon]], [[DataScienceWithSam]], and [[AIForScience]] - source and broader theme.
- [[SingleCellRNASequencing]], [[BiomedicalDeepLearning]], and [[SingleCellAutoencoderRepresentation]] - downstream modeling branch.
