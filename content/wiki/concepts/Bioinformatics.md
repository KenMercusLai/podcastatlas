---
title: "Bioinformatics"
type: concept
tags: [bioinformatics, biology, data-science, sequencing]
sources: [ep-8-implementation-of-ai-in-scientific-research]
last_updated: 2026-08-18
---

# Bioinformatics

Bioinformatics is [[LucasSimon|Lucas Simon]]'s source-scoped name in [[ep-8-implementation-of-ai-in-scientific-research]] for the preparation layer that turns raw sequencing data into an analysis-ready [[GeneExpressionMatrix|gene expression matrix]]. In his distinction, this includes the work before downstream modeling: raw reads, alignment or counting-style processing, and standardized [[SequencingDataPipeline|sequencing pipelines]].

The concept complements [[BioinformaticsDomainGap]]. The earlier gap page describes a collaboration wall between biology and computational analysis; this episode adds a workflow boundary, where bioinformatics creates the matrix that [[ComputationalBiology]] then analyzes through PCA, clustering, neural networks, or other models.

## Key Claims
- Bioinformatics can be the data-engineering and preprocessing layer for molecular biology.
- Standard pipelines reduce repeated work, but they do not remove storage, compute, and setup challenges.
- Raw sequencing files can be large enough that hardware and high-performance computing support become part of the research workflow.
- The boundary with [[ComputationalBiology]] is source-scoped rather than universal; Lucas explicitly presents it as his own distinction.

## Connections
- [[LucasSimon]], [[BaylorCollegeOfMedicine]], and [[TherapeuticInnovationCenter]] - source context.
- [[BioinformaticsDomainGap]], [[DomainExpertAlignment]], and [[ExperimentalScienceDataQuality]] - collaboration and data-quality context.
- [[SequencingDataPipeline]], [[GeneExpressionMatrix]], and [[ComputationalBiology]] - workflow sequence in the source.
