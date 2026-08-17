---
title: "EP 8: Implementation of AI in scientific research"
type: source
tags: [podcast, data-science, ai-for-science, computational-biology, biomedical-research]
sources: []
date: 2022-12-27
source_file: "/home/ken/repos/podcastatlas/content/episodes/965A022265C6C461D9BB2BB98171C1A8~8584438_2026-08-10-210438-8787-0-0-10.128 [965A022265C6C461D9BB2BB98171C1A8~8584438_2026-08-10-210438-8787-0-0-10.128.mp3？cdn_id=99&uuid=67e34be6-5b48-d742-2140-006d01478122&wuuid=6a83842b].md"
source_url: "https://pdcn.co/e/serve.castfire.com/audio/8584438/8584438_2026-08-10-210438.128.mp3?rssID=6736"
duration: "1734"
last_updated: 2026-08-18
---

## Summary
This [[DataScienceWithSam]] episode has [[SamDataScienceWithSam|Sam]] interview [[LucasSimon|Lucas Simon]] about applying AI, machine learning, and data science to biomedical research at [[BaylorCollegeOfMedicine]]'s [[TherapeuticInnovationCenter]]. The source turns the wiki's existing [[AIForScience]] and [[BioinformaticsDomainGap]] themes into a concrete molecular-data workflow: [[SequencingDataPipeline|sequencing pipelines]] create [[GeneExpressionMatrix|gene expression matrices]], [[ComputationalBiology]] analyzes them, and [[SingleCellRNASequencing]] creates data shapes where [[BiomedicalDeepLearning]] and [[SingleCellAutoencoderRepresentation|autoencoder representations]] become more useful. Its core synthesis is that biomedical AI depends on the representation layer as much as on models: raw reads, count matrices, feature engineering, high-performance computing, team IT support, and biological interpretation all shape whether deep learning reveals real cell structure.

## Key Claims
- [[LucasSimon|Lucas Simon]] leads a small data-science group at the [[TherapeuticInnovationCenter]] at [[BaylorCollegeOfMedicine]], where the group applies data science to molecular data for early cancer therapeutics.
- The source says biomedical research has changed because sequencing and related technologies make large molecular datasets routine rather than exceptional.
- [[GeneExpressionMatrix|Gene expression matrices]] are presented as a central data object: roughly 20,000 expressed genes can be measured across samples or cells, producing matrices that are hard to interpret by inspection.
- Lucas makes a source-scoped distinction between [[Bioinformatics]] and [[ComputationalBiology]]: bioinformatics turns raw sequencing reads into analysis-ready matrices, while computational biology asks downstream biological questions from those matrices.
- [[SequencingDataPipeline|Sequencing pipelines]] create storage and compute pressure because raw sequencing samples can contain tens of millions of reads and very large intermediate files.
- [[MolecularFeatureEngineering]] is framed as a discovery opportunity, because researchers can summarize raw molecular signals in nontraditional ways rather than accepting only standard count-matrix representations.
- [[SingleCellRNASequencing]] changes the deep-learning setting by moving from bulk RNA-seq experiments with perhaps hundreds of samples to cell-level datasets that can contain tens of thousands to around a million cells.
- [[BiomedicalDeepLearning]] becomes more plausible in this data shape because there can be many more cell-level observations than genes.
- [[SingleCellAutoencoderRepresentation|Autoencoders]] are used as an example of biological meaning emerging from a neural network: compressed hidden-space clusters can correspond to different cell types.
- The source emphasizes that model optimization alone is not the endpoint; visualization, output analysis, and biological interpretation are needed to turn learned structure into scientific insight.
- Tool choice is presented pragmatically: Lucas's team uses a mix of R and Python, and commonly uses [[Keras]], which sits on [[TensorFlow]] and has both Python and R interfaces.

## Key Quotes
> "bioinformatics" - Lucas's term for the raw-read-to-matrix preparation layer.

> "computational biology" - Lucas's term for downstream analysis of analysis-ready molecular matrices.

> "profiling means measuring" - Lucas's clarification that gene-expression profiling is measurement, not prediction.

## Connections
- [[DataScienceWithSam]], [[SamDataScienceWithSam]], [[LucasSimon]], [[BaylorCollegeOfMedicine]], and [[TherapeuticInnovationCenter]] - show, host, guest, institution, and research-center context.
- [[AIForScience]], [[HumanDrivenScientificAI]], [[BioinformaticsDomainGap]], [[DomainExpertAlignment]], and [[AIVerification]] - broader scientific-AI and expert-interpretation frame.
- [[Bioinformatics]], [[ComputationalBiology]], [[SequencingDataPipeline]], [[GeneExpressionMatrix]], and [[MolecularFeatureEngineering]] - source's molecular-data workflow branch.
- [[SingleCellRNASequencing]], [[BiomedicalDeepLearning]], and [[SingleCellAutoencoderRepresentation]] - deep-learning branch enabled by cell-level sequencing data.
- [[Keras]], [[TensorFlow]], and [[MachineLearningEngineering]] - practical modeling and software-tool context.
- [[AIDrugDiscoveryPlatform]], [[AIClinicalValidationInDrugDiscovery]], [[GenerativeBiology]], and [[AIProteinDesign]] - adjacent wiki branch for AI in molecular biology and drug discovery.

## Contradictions
- No direct contradiction found.
- The source extends [[data-ai-and-scientific-research-a-coffee-chat]] by making the biology/bioinformatics boundary more operational: raw-read processing, matrix construction, feature representation, hardware, and cell-level data volume decide which AI methods are credible before biological interpretation begins.
