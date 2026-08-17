---
title: "MLOps"
type: concept
tags: [mlops, machine-learning, operations]
sources: [ep-7-data-science-mlops]
last_updated: 2026-08-18
---

# MLOps

MLOps is the operating discipline for taking machine-learning models from data-science work into production systems, then keeping those models measured, updated, and useful. In [[ep-7-data-science-mlops]], [[AaronBlythe]] explains it as a model-operations layer that borrows heavily from DevOps while adding production ML needs such as APIs, feedback loops, model improvement, and collaboration with data scientists.

The source treats MLOps as broader than deployment. A model may need to be placed behind a REST API, wired into application behavior, measured in production, retrained or improved when user behavior reveals missing features, and connected back to the data scientist who understands the model's assumptions. That makes [[ProductionMLFeedbackLoops]] and [[MLCICD]] central rather than optional process garnish.

MLOps also clarifies role boundaries. [[DataScientistMLOpsFluency]] says data scientists should understand what MLOps is for, but [[MachineLearningEngineering]] and operations specialists may own much of the hands-on deployment work inside [[IntegratedMLTeams]].

## Key Claims
- MLOps adapts DevOps ideas to model deployment and operation.
- Production ML needs automation, measurement, feedback, and shared ownership.
- Putting a model behind an API is only the beginning; behavior and model quality need to keep flowing back into improvement work.
- MLOps is still partly experimental because organizations have not fully standardized best practice.
- Data scientists benefit from understanding MLOps even when they do not perform all MLOps tasks.

## Connections
- [[AaronBlythe]], [[DataScienceWithSam]], and [[SamDataScienceWithSam]] - source context.
- [[MachineLearningEngineering]] - adjacent role that gets models into production systems.
- [[DataEngineeringForDataScience]] - upstream data layer that makes model work possible.
- [[DevOpsCALMS]] and [[MLCICD]] - DevOps-derived practice base.
- [[ProductionMLFeedbackLoops]] and [[FastFeedbackLoops]] - measurement and learning loops after deployment.
- [[IntegratedMLTeams]] and [[DataScientistMLOpsFluency]] - team design and role-boundary frame.
