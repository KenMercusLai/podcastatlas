---
title: "Application Performance Monitoring"
type: concept
tags: [observability, software-operations, application-performance]
sources: [ep-14-what-is-observability]
last_updated: 2026-08-18
---

# Application Performance Monitoring

Application performance monitoring is the predecessor practice from which [[EdFerron]] says modern [[Observability]] grew in [[ep-14-what-is-observability]]. The source treats APM as useful but narrower than observability because classic monitoring can focus on application or component health without tying signals to end-to-end business transactions.

The episode's distinction is practical. APM and monitoring tools may help engineers find fires, but observability asks what customer activity is affected, how widely it is affected, and how the team should engineer around the problem rather than only inspect a dashboard.

## Key Claims
- APM platforms helped mature the observability category.
- Monitoring remains useful for operations and engineering incident response.
- Observability extends APM by adding full-stack, business-facing, and real-time decision context.
- The difference matters more as applications become central to revenue, support, onboarding, and customer experience.
- APM tools can provide insight without always requiring new application code, but teams still need to focus them on business activity.

## Connections
- [[Observability]] and [[FullStackObservability]] - broader successor frame.
- [[EdFerron]] and [[ExigentSolutions]] - source context.
- [[BusinessTransactionObservability]] - business-language extension of application performance.
- [[ProactiveObservability]] - alerting posture beyond reactive monitoring.
- [[MachineLearningEngineering]] and [[MLOps]] - adjacent production engineering disciplines.
