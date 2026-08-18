---
title: "Computational Biology"
type: concept
tags: [computational-biology, biology, data-science, ai-for-science]
sources: [ep-8-implementation-of-ai-in-scientific-research]
last_updated: 2026-08-18
---

# Computational Biology

[[all-in-with-chamath-jason-sacks-friedberg-bill-maris-how-google-could-crush-ai-competitors-why-small-funds-win-and-ais-atari-stage-41586010]] adds [[BillMaris|Bill Maris]]'s investor and founder perspective through [[Calico]] and [[Section32|Section 32]]. Maris is optimistic about computation in biology, but he cautions that discovering a promising compound is only a small part of the path because titration, safety, human biology, clinical evidence, and regulation remain hard constraints.

Computational biology is [[LucasSimon|Lucas Simon]]'s source-scoped term in [[ep-8-implementation-of-ai-in-scientific-research]] for downstream analysis once [[Bioinformatics]] has produced an analysis-ready [[GeneExpressionMatrix|gene expression matrix]]. The source gives PCA, modeling, and biological interpretation as examples of what happens after raw sequencing reads have been turned into structured data.

The concept is useful because it separates data preparation from scientific modeling without pretending the boundary is universal. In this episode, [[ComputationalBiology]] is where [[MolecularFeatureEngineering]], [[SingleCellRNASequencing]], [[BiomedicalDeepLearning]], and [[SingleCellAutoencoderRepresentation|autoencoder representations]] become ways to ask biological questions.

## Key Claims
- Computational biology starts after the data matrix exists in Lucas's source-scoped definition.
- The role is not just model fitting; visualization, output analysis, and biological interpretation are part of the workflow.
- It can use standard analysis methods such as PCA as well as deep-learning methods when the data shape supports them.
- In single-cell data, computational biology can connect neural-network hidden spaces to cell-type structure.
- Maris's All-In source adds that realistic in-silico cell simulation would be a major accelerator, but the episode treats it as an unsolved bottleneck rather than a current replacement for biological validation.

## Connections
- [[Bioinformatics]], [[SequencingDataPipeline]], and [[GeneExpressionMatrix]] - upstream workflow layer.
- [[LucasSimon]], [[DataScienceWithSam]], and [[AIForScience]] - source and broader theme.
- [[SingleCellRNASequencing]], [[BiomedicalDeepLearning]], and [[SingleCellAutoencoderRepresentation]] - downstream modeling branch.
- [[BillMaris|Bill Maris]], [[Calico]], [[Section32|Section 32]], [[AIForScience]], and [[AIClinicalValidationInDrugDiscovery]] - Maris interview branch around computational biology and validation limits.
