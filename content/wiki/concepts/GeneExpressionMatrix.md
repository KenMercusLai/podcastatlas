---
title: "Gene Expression Matrix"
type: concept
tags: [biology, genomics, sequencing, data-science]
sources: [ep-8-implementation-of-ai-in-scientific-research]
last_updated: 2026-08-18
---

# Gene Expression Matrix

A gene expression matrix is the central molecular-data object in [[ep-8-implementation-of-ai-in-scientific-research]]. [[LucasSimon|Lucas Simon]] explains that sequencing technology can measure expression across roughly 20,000 genes, producing matrices across samples or cells that are too large to interpret by inspection.

The matrix is the hinge between [[Bioinformatics]] and [[ComputationalBiology]]. [[SequencingDataPipeline|Sequencing pipelines]] turn raw reads into counts or related measurements; downstream analysis then uses the matrix for PCA, clustering, [[MolecularFeatureEngineering]], or [[BiomedicalDeepLearning]].

## Key Claims
- The matrix makes high-dimensional molecular data analyzable, but also hides biological interpretation inside representation choices.
- Bulk RNA-seq and [[SingleCellRNASequencing]] create different matrix shapes, which changes which models are practical.
- A clean matrix is not the end of the workflow; biological questions, visualization, and validation still determine whether analysis is useful.
- Nontraditional summaries of raw molecular data can create new feature spaces beyond ordinary count matrices.

## Connections
- [[Bioinformatics]], [[SequencingDataPipeline]], and [[ComputationalBiology]] - workflow boundary around the matrix.
- [[LucasSimon]], [[BaylorCollegeOfMedicine]], and [[TherapeuticInnovationCenter]] - source context.
- [[SingleCellRNASequencing]], [[MolecularFeatureEngineering]], and [[BiomedicalDeepLearning]] - downstream analysis branches.
