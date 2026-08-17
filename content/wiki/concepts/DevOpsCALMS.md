---
title: "DevOps CALMS"
type: concept
tags: [devops, mlops, software-engineering]
sources: [ep-7-data-science-mlops]
last_updated: 2026-08-18
---

# DevOps CALMS

DevOps CALMS is the source's shorthand for the DevOps ingredients that [[MLOps]] borrows: culture, automation, lean or learning, measurement, and sharing. In [[ep-7-data-science-mlops]], [[AaronBlythe]] uses DevOps history to explain why old developer-operations handoffs created friction and why production ML should be designed around ownership, automation, and feedback.

The concept matters because the episode does not define MLOps as only a toolchain. Automation is central, but Aaron also emphasizes communication, measurement, shared responsibility, and learning loops. Those cultural and organizational pieces connect [[MLCICD]] and [[ProductionMLFeedbackLoops]] to [[IntegratedMLTeams]].

The source also invokes the DevOps idea "if you write it, you run it" as an ownership pattern. For ML systems, the point is not that data scientists personally run all infrastructure; it is that teams should not create a brittle wall between model creation and model operation.

## Key Claims
- DevOps responds to slow handoffs between people who write code and people who operate it.
- Automation is necessary but not sufficient; culture, learning, measurement, and sharing matter too.
- MLOps borrows DevOps ideas but applies them to model deployment and feedback.
- Shared ownership reduces the chance that model builders ignore production behavior.
- The source treats DevOps principles as a team design lesson, not merely a set of tools.

## Connections
- [[MLOps]] - ML-specific adaptation of DevOps principles.
- [[MLCICD]] - CI/CD practice connected to automation and measurement.
- [[ProductionMLFeedbackLoops]] - learning and measurement loop in deployed ML.
- [[IntegratedMLTeams]] - organizational pattern that makes sharing and ownership practical.
- [[AIEngineeringThinking]] - broader engineering discipline around requirements, tests, logs, and handoffs.
