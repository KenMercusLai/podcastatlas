---
title: "Integrated ML Teams"
type: concept
tags: [machine-learning, organization-design, mlops]
sources: [ep-7-data-science-mlops]
last_updated: 2026-08-18
---

# Integrated ML Teams

Integrated ML teams are cross-functional groups that combine data engineering, data science, and ML engineering around a business function or product outcome. In [[ep-7-data-science-mlops]], [[AaronBlythe]] describes a recommendation-team pattern with a data engineer, data scientist, and ML engineer working together rather than passing work across isolated silos.

The source connects this to data mesh thinking and DevOps ownership. The point is organizational: the team that understands the business function should have the data, model, deployment, and feedback responsibilities close enough together to improve the system. That makes [[DataEngineeringForDataScience]], [[MachineLearningEngineering]], [[MLOps]], and [[ProductionMLFeedbackLoops]] mutually dependent.

Integrated teams also prevent a hiring anti-pattern. Sam argues data-science managers should hire both data scientists and ML engineers rather than expecting one person to cover both jobs by default. Aaron allows that some people can span roles, but frames cross-training and bidirectional mentorship as the healthier team pattern.

## Key Claims
- Production ML works better when data engineers, data scientists, and ML engineers collaborate around the same business function.
- Data mesh thinking appears as a way to organize teams around domain responsibility.
- Cross-training helps each role understand the others' constraints.
- Bidirectional mentorship is stronger than one-way handoff.
- Managers should avoid treating the data scientist as automatically responsible for every deployment and operations task.

## Connections
- [[MLOps]], [[MachineLearningEngineering]], and [[DataEngineeringForDataScience]] - core role stack.
- [[ProductionMLFeedbackLoops]] and [[MLCICD]] - operating practices the team has to support.
- [[DataScientistMLOpsFluency]] - role-boundary skill that enables collaboration.
- [[DomainExpertAlignment]] and [[BusinessLedAITransformation]] - broader organizational context for applied AI work.
- [[AaronBlythe]] and [[DataScienceWithSam]] - source context.
