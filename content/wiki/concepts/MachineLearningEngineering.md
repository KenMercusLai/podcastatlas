---
title: "Machine Learning Engineering"
type: concept
tags: [machine-learning, engineering, mlops]
sources: [ep-7-data-science-mlops, ep-8-implementation-of-ai-in-scientific-research]
last_updated: 2026-08-18
---

# Machine Learning Engineering

Machine learning engineering is the role and practice of turning a trained model into a production capability. In [[ep-7-data-science-mlops]], [[AaronBlythe]] explains that a model built by a data scientist often needs to be placed somewhere usable, commonly behind an API, then connected to application behavior and operational feedback.

The source distinguishes this from pure data-science exploration. Data scientists may form hypotheses, analyze data, and build models, while ML engineers make the model reliable and accessible inside real systems. The boundary is not rigid: strong teams cross-train, and data scientists need enough [[DataScientistMLOpsFluency]] to understand the deployment and feedback path.

Machine learning engineering sits between [[DataEngineeringForDataScience]] and [[MLOps]]. The data engineering layer gets data into a usable place; the ML engineering layer operationalizes the model; the MLOps layer adds automation, measurement, CI/CD-style delivery, and feedback loops.

[[ep-8-implementation-of-ai-in-scientific-research]] adds an academic biomedical variant. [[LucasSimon|Lucas Simon]] does not frame his lab as a production-ML team, but the same engineering boundary appears in [[SequencingDataPipeline|sequencing pipelines]], high-performance computing queues, storage, tool installation, and the need to make [[BiomedicalDeepLearning]] outputs analyzable rather than only trainable.

## Key Claims
- ML engineering makes a model usable by other systems, often through APIs.
- ML engineers need some understanding of statistics, model evaluation, confusion matrices, sensitivity, and specificity.
- Data scientists and ML engineers should not be collapsed into one expected super-role by default.
- Cross-training is useful because deployment choices affect model behavior and model assumptions affect production risk.
- The work is continuous when model behavior changes with new data or user behavior.
- In research settings, engineering can mean making large molecular datasets, pipelines, and model outputs usable enough for scientists to interpret.

## Connections
- [[MLOps]] - operating discipline around deployed models.
- [[DataEngineeringForDataScience]] - upstream data foundation.
- [[ProductionMLFeedbackLoops]] - path from production use back into model improvement.
- [[MLCICD]] - CI/CD practice adapted for model delivery.
- [[IntegratedMLTeams]] - team structure combining data engineers, data scientists, and ML engineers.
- [[AaronBlythe]] and [[DataScienceWithSam]] - source context.
- [[LucasSimon]], [[SequencingDataPipeline]], [[GeneExpressionMatrix]], and [[BiomedicalDeepLearning]] - academic biomedical engineering variant added by EP8.
