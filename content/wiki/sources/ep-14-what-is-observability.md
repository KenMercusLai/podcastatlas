---
title: "EP 14: What is Observability?"
type: source
tags: [podcast, data-science, observability, software-engineering, operations]
sources: []
date: 2023-08-06
source_file: "/home/ken/repos/podcastatlas/content/episodes/93D6BF3DAC1E8E446F94B2892F50C2C3~8584431_2026-08-10-215931-8787-0-0-10.128 [93D6BF3DAC1E8E446F94B2892F50C2C3~8584431_2026-08-10-215931-8787-0-0-10.128.mp3？cdn_id=99&uuid=663bc931-456a-796d-5f73-91aa3fe5563e&wuuid=6a8387d4].md"
source_url: "https://pdcn.co/e/serve.castfire.com/audio/8584431/8584431_2026-08-10-215931.128.mp3?rssID=6736"
duration: "1915"
last_updated: 2026-08-18
---

## Summary
This [[DataScienceWithSam]] episode has [[SamDataScienceWithSam|Sam]] interview [[EdFerron]] of [[ExigentSolutions]] about [[Observability]] as the next operating layer beyond siloed monitoring. The discussion connects [[ApplicationPerformanceMonitoring]], [[FullStackObservability]], [[BusinessTransactionObservability]], [[ObservabilitySecurityTelemetry]], [[AIEnabledObservability]], [[OpenTelemetry]], [[ProactiveObservability]], and [[RealTimeOperationalAnalytics]]. Its core synthesis is that application telemetry becomes more valuable when it explains end-to-end customer experience, business impact, security risk, and infrastructure cost in real time.

## Key Claims
- [[Observability]] is framed as a major jump from monitoring, not just another version of monitoring.
- Traditional logs, infrastructure metrics, database checks, queue metrics, network data, and cloud-service dashboards can stay too siloed to explain end-to-end application behavior.
- [[FullStackObservability]] should let teams move from a business symptom to technical root cause across application, network, database, cloud, security, and other layers.
- [[BusinessTransactionObservability]] translates telemetry into stakeholder language such as order flow, ride-order latency, affected customer percentage, and affected locations.
- The source treats application performance as a revenue and customer-experience issue, including B2B cases where short delays can have large financial consequences.
- [[ObservabilitySecurityTelemetry]] is becoming part of the observability stack because vulnerabilities, bad libraries, bad DLLs, and attacks can interrupt customer onboarding, login, and other business functions.
- [[AIEnabledObservability]] is useful because developers and tools emit too much data for humans to manually correlate across systems.
- Machine-learning methods can help detect anomalous relationships among signals and attach context to alerts.
- [[ProactiveObservability]] matters because customers often retry, restart, abandon a service, or complain on social media before filing a formal support ticket.
- [[OpenTelemetry]] is presented as an important standard for generating, ingesting, querying, modeling, and alerting on observability data.
- For data scientists, metrics, events, traces, logs, and spans can support [[RealTimeOperationalAnalytics]] without replacing enterprise reports or data warehouses.
- Observability can support scaling and cost decisions during demand spikes such as Black Friday, back-to-school periods, and electric-vehicle charging use cases.
- Ed argues that teams often already own strong observability tools but have not tied them to the business activities they need to understand.

## Key Quotes
> "next major jump in monitoring" - Ed's framing of observability's relationship to earlier monitoring.

> "order a ride is slow" - business-language example for customer-visible telemetry.

> "as much data as possible" - Ed's description of the observability data-ingestion posture.

## Connections
- [[DataScienceWithSam]], [[SamDataScienceWithSam]], [[EdFerron]], and [[ExigentSolutions]] - show, host, guest, and organization.
- [[Observability]], [[FullStackObservability]], [[BusinessTransactionObservability]], and [[ApplicationPerformanceMonitoring]] - core monitoring-to-observability frame.
- [[OpenTelemetry]] and [[RealTimeOperationalAnalytics]] - telemetry standard and data-science use case.
- [[AIEnabledObservability]], [[ProactiveObservability]], and [[ProductionMLFeedbackLoops]] - signal-correlation, alerting, and operational feedback branch.
- [[ObservabilitySecurityTelemetry]], [[CybersecurityDataScience]], and [[SecurityDataAccessConstraint]] - security telemetry and risk-management connection.
- [[MLOps]], [[MachineLearningEngineering]], and [[DataEngineeringForDataScience]] - adjacent production-data and model-operations concepts.

## Contradictions
- No direct contradiction found.
- The source extends [[ep-7-data-science-mlops]] by moving from model deployment feedback into whole-application telemetry, business transactions, and cost-aware operations.
- The source qualifies [[CybersecurityDataScience]] by showing that security signals are not only separate threat datasets; they can also be part of business-facing observability when attacks or vulnerable components degrade customer workflows.
