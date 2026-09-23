---
title: "Sasank Akkinappoli"
type: entity
tags: [person, data-engineering, enterprise-data, cloud]
sources:
  - ep-50-evolution-of-enterprise-data-engineering-in-gen-ai-era
last_updated: 2026-09-24
knowledge_schema: synthesis-v1
---

# Sasank Akkinappoli

## Overview
Sasank Akkinappoli is a senior data engineer and [[DataScienceWithSam]] guest whose source-backed experience spans banking, healthcare, and supply-chain systems. He discusses legacy ETL, cloud data platforms, governance, deployment automation, and the future of data engineering in an agentic-AI environment.

## Current Profile
Sasank's profile is that of an enterprise modernization practitioner rather than a general AI forecaster. He treats the movement from [[IBMDataStage|IBM DataStage]] and similar batch systems to [[Databricks]], [[Snowflake]], and [[Dbt|dbt]] as an operating-model change that must preserve business meaning while improving freshness, traceability, quality, and release safety.

His forward-looking view is conditional: data engineers may become data-product builders and stewards of AI-supported operations, but those systems depend on trustworthy data and governance. He explicitly describes his organization's agentic-AI work as still being implemented.

## Key Characteristics
- Bridges legacy batch ETL experience with modern cloud and lakehouse platforms.
- Selects data platforms by workload, data shape, and user workflow rather than treating them as interchangeable.
- Uses inventory freshness to connect pipeline design with concrete operational decisions.
- Treats governance, ownership, lineage, security, and least-privilege access as part of engineering.
- Emphasizes semantic data correctness in addition to successful pipeline execution.
- Expects data engineers to combine programming ability with architecture and business-context judgment.

## Evidence
- Experience and scope: [[ep-50-evolution-of-enterprise-data-engineering-in-gen-ai-era]] introduces Sasank through banking, healthcare, and supply-chain data work across legacy and cloud systems.
- Platform judgment: [[ep-50-evolution-of-enterprise-data-engineering-in-gen-ai-era]] records his workload-based comparison of Databricks, Snowflake, and dbt.
- Operational focus: [[ep-50-evolution-of-enterprise-data-engineering-in-gen-ai-era]] uses an inventory example to show the decision cost of stale batch data.
- Reliability stance: [[ep-50-evolution-of-enterprise-data-engineering-in-gen-ai-era]] has him connect governance and CI/CD to data quality, lineage, access control, rollback, and logical correctness.
- AI outlook: [[ep-50-evolution-of-enterprise-data-engineering-in-gen-ai-era]] attributes to him a future shift toward data products and failure-predicting operations while noting that current agentic work is immature.

## Qualifications
This profile is based on one compact practitioner interview and does not independently verify the guest's employment history, platform outcomes, latency improvements, or production AI deployments. Product-fit recommendations are source-scoped heuristics, and the source provides no reference architecture or comparative benchmark.

## What Changed
- Initial source-scoped profile created from Data Science With Sam EP50.

## Relationships
- [[DataScienceWithSam]] - podcast on which Sasank presents his enterprise data-engineering views.
- [[SamDataScienceWithSam]] - interviewer who elicits the modernization and skills discussion.
- [[EnterpriseDataModernization]] - operating transition Sasank explains.
- [[DataPipelineCICD]] - deployment and correctness discipline he recommends.
- [[AIReadyDataEngineering]] - future-facing data-engineering model he describes.
- [[Databricks]] - platform he associates with large-scale and less-structured workloads.
- [[Snowflake]] - platform he associates with SQL-centric warehouse analytics.
- [[Dbt]] - transformation layer he associates with reusable SQL patterns.
