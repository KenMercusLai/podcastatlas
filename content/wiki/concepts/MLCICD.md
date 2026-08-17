---
title: "ML CI/CD"
type: concept
tags: [mlops, ci-cd, machine-learning]
sources: [ep-7-data-science-mlops]
last_updated: 2026-08-18
---

# ML CI/CD

ML CI/CD is the adaptation of continuous integration and continuous delivery or deployment to machine-learning work. In [[ep-7-data-science-mlops]], [[AaronBlythe]] references the State of DevOps report and describes high-performing software organizations as using practices such as CI/CD, then says [[MLOps]] is moving toward similar practices.

The source distinguishes continuous integration, continuous delivery, and continuous deployment. CI tests code when it is checked in; continuous delivery keeps tested work ready for production release; continuous deployment automatically pushes through the pipeline. Aaron notes that most teams use continuous delivery language, and that he has not seen MLOps fully perfected in the same way mature DevOps aspires to.

For ML systems, CI/CD cannot be only code movement. It has to account for model artifacts, data changes, evaluation, feedback, and production behavior, which connects this concept to [[ProductionMLFeedbackLoops]] and [[MachineLearningEngineering]].

## Key Claims
- CI/CD is a mature DevOps reference point for MLOps.
- Continuous integration means testing changes as they enter the shared codebase.
- Continuous delivery means tested work is ready for production release.
- Continuous deployment means the pipeline automatically deploys after passing checks.
- ML CI/CD is still an emerging practice because model behavior depends on data, evaluation, and feedback, not only code.

## Connections
- [[MLOps]] and [[DevOpsCALMS]] - operating discipline and DevOps principle base.
- [[MachineLearningEngineering]] - role that turns model artifacts into deployed systems.
- [[ProductionMLFeedbackLoops]] - production evidence that should affect later releases.
- [[DataEngineeringForDataScience]] - data layer that makes repeatable model delivery possible.
- [[AIEngineeringThinking]] and [[AIVerification]] - broader testing and verification context.
