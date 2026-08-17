---
title: "Bioinformatics Domain Gap"
type: concept
tags: [biology, bioinformatics, data-science, ai-for-science]
sources: [data-ai-and-scientific-research-a-coffee-chat, ep-8-implementation-of-ai-in-scientific-research]
last_updated: 2026-08-18
---

# Bioinformatics Domain Gap

Bioinformatics domain gap is the collaboration problem [[EffieDataScienceWithSam|Effie]] describes in [[data-ai-and-scientific-research-a-coffee-chat]]: biologists may need R, Python, statistics, and computational models, while data analysts or bioinformaticians may not know the biological context behind the experiment. She describes this as a wall between biology and bioinformatics.

The concept extends [[DomainExpertAlignment]] into laboratory science. Advanced analysis can surface patterns from RNA-seq, tissue images, or other biological data, but the interpretation still depends on sample context, experimental design, controls, and [[ExperimentalScienceDataQuality]].

[[ep-8-implementation-of-ai-in-scientific-research]] adds a workflow-specific version through [[LucasSimon|Lucas Simon]]. He distinguishes [[Bioinformatics]] as the raw-read-to-[[GeneExpressionMatrix|matrix]] preparation layer from [[ComputationalBiology]] as downstream matrix analysis, while noting this is his own practical definition. The gap therefore includes both collaboration across expertise and handoff quality between [[SequencingDataPipeline|sequencing pipelines]], feature representation, and biological interpretation.

## Key Claims
- Data science skill and biological understanding need to meet inside the same workflow.
- Better tools do not remove the need for scientists who can understand enough code, statistics, and model assumptions to collaborate well.
- Bioinformaticians can miss relevant biology when data is detached from experimental context.
- Biologists can underuse large datasets when the computational layer is too distant from the bench workflow.
- AI adoption in biology is partly a training and communication problem, not only a model-capability problem.
- The raw-data-to-matrix boundary can itself become a collaboration point because representation choices affect what downstream computational biology can discover.

## Connections
- [[EffieDataScienceWithSam]], [[LucasSimon]], and [[DataScienceWithSam]] - source speakers and show context.
- [[DomainExpertAlignment]], [[AIForScience]], and [[HumanDrivenScientificAI]] - broader AI collaboration frame.
- [[ExperimentalScienceDataQuality]], [[AIVerification]], and [[AIExperimentDocumentation]] - adjacent research-practice requirements.
- [[Bioinformatics]], [[ComputationalBiology]], [[GeneExpressionMatrix]], and [[SequencingDataPipeline]] - workflow boundary added by EP8.
