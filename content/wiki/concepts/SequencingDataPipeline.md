---
title: "Sequencing Data Pipeline"
type: concept
tags: [sequencing, bioinformatics, data-engineering, computational-biology]
sources: [ep-8-implementation-of-ai-in-scientific-research]
last_updated: 2026-08-18
---

# Sequencing Data Pipeline

A sequencing data pipeline is the source's workflow for moving from raw sequencing reads to an analysis-ready [[GeneExpressionMatrix|gene expression matrix]]. In [[ep-8-implementation-of-ai-in-scientific-research]], [[LucasSimon|Lucas Simon]] says standard pipelines exist, but research groups differ in whether they improve those pipelines or accept them and focus on downstream [[ComputationalBiology]].

The pipeline matters because raw sequencing data can be large enough to make storage, compute time, program installation, high-performance computing queues, and IT support part of ordinary biomedical research. The episode therefore links [[Bioinformatics]] to [[DataEngineeringForDataScience]] and [[MachineLearningEngineering]] without reducing the problem to generic software operations.

## Key Claims
- A pipeline translates raw molecular data into a structured matrix that downstream analysis can use.
- Standard pipelines are useful, but they embody choices about how biological signal is summarized.
- Large sequencing files create hardware and operational constraints for academic research teams.
- Some discovery work may happen before the matrix, when researchers change how raw data is summarized.

## Connections
- [[Bioinformatics]], [[GeneExpressionMatrix]], and [[ComputationalBiology]] - pipeline input and output context.
- [[MolecularFeatureEngineering]], [[SingleCellRNASequencing]], and [[BiomedicalDeepLearning]] - representation and modeling consequences.
- [[DataEngineeringForDataScience]], [[MachineLearningEngineering]], and [[IntegratedMLTeams]] - adjacent data/operations concepts from Data Science With Sam.
