---
title: "EP 50: Evolution of Enterprise Data Engineering in Gen AI Era"
type: source
tags: [podcast, data-engineering, enterprise-data, cloud, agentic-ai]
sources: []
date: 2026-09-21
source_file: "/home/ken/repos/podcastatlas/content/episodes/4d1e8e91-dc72-5aa2-a3db-908d1ddbf395 [4d1e8e91-dc72-5aa2-a3db-908d1ddbf395.mp3？session_id=87f4fccf-c92f-53ac-9f91-021c9c.com⧸data-science-with-sam-podcast⧸2026_09_21_02_36_59_3a2d1f18-5e20-4913-8020-e0e857ab626e].md"
source_url: "https://content.rss.com/episodes/401132/3169193/data-science-with-sam-podcast/2026_09_21_02_36_59_3a2d1f18-5e20-4913-8020-e0e857ab626e.mp3"
duration: "1715"
last_updated: 2026-09-24
---

## Summary
This [[DataScienceWithSam]] episode has [[SamDataScienceWithSam|Sam]] interview senior data engineer [[SasankAkkinappoli|Sasank Akkinappoli]] about moving enterprises from overnight ETL toward cloud-based, frequently refreshed data systems without losing business logic or reliability. The discussion compares [[IBMDataStage|IBM DataStage]], [[Databricks]], [[Snowflake]], and [[Dbt|dbt]], then connects [[EnterpriseDataModernization]], [[DataPipelineCICD]], governance, and [[AIReadyDataEngineering]] to supply-chain decisions and future agentic operations. Its central claim is that modernization is not code relocation: trustworthy data, lineage, access control, automated quality checks, and business context determine whether analytics or AI can safely use the result.

## Key Claims
- Enterprises often operate legacy batch ETL and newer cloud platforms at the same time because critical business logic and operational dependencies cannot be replaced in one step.
- [[SasankAkkinappoli|Sasank Akkinappoli]] presents [[Databricks]] as well suited to large-scale Python work and semi-structured or unstructured data, while [[Snowflake]] is framed around SQL, structured warehouse analytics, marts, dashboards, and forecasting.
- [[Dbt|dbt]] can provide reusable transformations, macros, and templating over warehouse data rather than acting as a universal substitute for the other platforms.
- An hourly inventory pipeline can materially improve decisions over an overnight batch even though it is better described as near-real-time than instantaneous streaming.
- Governance must cover data quality, redundancy, least-privilege access, lineage, security, ownership, exposure, and downstream consumers, with controls adapted to domain sensitivity.
- [[DataPipelineCICD]] should automate deployment, standards checks, version history, and rollback, but technical job success does not prove that produced data is logically correct.
- Sasank expects data engineers to move toward data-product engineering and AI-supported operations in which trustworthy historical data helps agents predict failures and recommend actions.
- Current AI use is described mainly as coding, troubleshooting, and SQL optimization; autonomous supply-chain decisions remain prospective rather than a demonstrated mature deployment.
- Future data engineers need Python and PySpark skills alongside data modeling, cloud architecture, integration, transformation-layer knowledge, and business-context judgment.

## Key Quotes
> "modernization is not merely a code migration" - the source summary's boundary between platform movement and reliable operating change.

> "trustworthy data is the foundation" - the episode's recurring link between conventional analytics and agentic AI.

> "logically incorrect data" - the failure mode that can remain even when a pipeline completes successfully.

## Connections
- [[DataScienceWithSam]], [[SamDataScienceWithSam]], and [[SasankAkkinappoli]] - show, host, and guest context.
- [[IBMDataStage]], [[Databricks]], [[Snowflake]], and [[Dbt]] - legacy and cloud-platform comparison.
- [[EnterpriseDataModernization]], [[DataEngineeringForDataScience]], and [[RealTimeOperationalAnalytics]] - migration, data-access, and operational-freshness branch.
- [[DataPipelineCICD]], [[MLCICD]], and [[AIVerification]] - deployment, rollback, and semantic-correctness branch.
- [[AIReadyDataEngineering]], [[AIDataReadiness]], [[AgenticDataEngineeringHarness]], and [[DataAgentGovernance]] - trustworthy-data and agentic-operations branch.

## Contradictions
- No settled contradiction found.
- The hourly inventory example qualifies broad "real-time" language: it demonstrates materially fresher operational data, not instantaneous event streaming.
- The agentic supply-chain and failure-prevention examples are prospective. The guest says his organization is still implementing agentic AI rather than operating a mature autonomous system.
- The product comparison is a practitioner workload-fit heuristic, not a benchmark proving that Databricks, Snowflake, or dbt has a universal advantage.
