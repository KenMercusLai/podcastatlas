---
title: "Snowflake"
type: entity
tags: [company, data, cloud, enterprise-software]
sources:
  - tsr-ycoffsite-kasishgupta-v1-audioonly-tsr-ycoffsite-kasishgupta-v1-audioonly
  - ep-50-evolution-of-enterprise-data-engineering-in-gen-ai-era
last_updated: 2026-09-24
knowledge_schema: synthesis-v1
---

# Snowflake

## Overview
Snowflake is an enterprise data platform represented in the wiki as both a governed customer-data foundation and a SQL-centered warehouse environment for structured analytics.

## Current Profile
The Hightouch source presents Snowflake as a system in which enterprises already hold customer data and from which they want to activate advertising, lifecycle-marketing, and sales workflows without copying ownership into another platform. EP50 adds a workload-fit view: Snowflake is associated with SQL, structured data, data marts, dashboards, warehouse analytics, and forecasting, with [[Dbt|dbt]] as a reusable transformation layer.

Together, the sources position Snowflake around governed warehouse data and downstream analytical or operational use. They do not establish that it is limited to these workloads or universally preferable to [[Databricks]].

## Key Characteristics
- Acts as an enterprise-controlled customer-data foundation in the Hightouch account.
- Supports SQL-centered and structured-data workflows in EP50's platform comparison.
- Is associated with marts, dashboards, warehouse analytics, and forecasting.
- Can pair with dbt for reusable transformation logic.
- Enables downstream activation without requiring the activation layer to own the source data.

## Evidence
- Data foundation: [[tsr-ycoffsite-kasishgupta-v1-audioonly-tsr-ycoffsite-kasishgupta-v1-audioonly]] says Hightouch customers already stored customer data in systems such as Snowflake.
- Activation boundary: [[tsr-ycoffsite-kasishgupta-v1-audioonly-tsr-ycoffsite-kasishgupta-v1-audioonly]] explains that enterprises wanted to use warehouse data in production marketing while retaining control of it.
- Workload fit: [[ep-50-evolution-of-enterprise-data-engineering-in-gen-ai-era]] associates Snowflake with SQL, structured data, data marts, dashboards, analytics, and forecasting.
- Transformation pairing: [[ep-50-evolution-of-enterprise-data-engineering-in-gen-ai-era]] presents dbt as a reusable transformation layer for Snowflake workflows.

## Qualifications
Both sources are practitioner or founder interviews rather than independent product evaluations. EP50's comparison is a workload-selection heuristic, not a benchmark or claim that platform boundaries are absolute.

## What Changed
- Added the EP50 workload-fit and dbt-transformation view.
- Migrated the page to the synthesis-first entity schema while preserving prior evidence.

## Relationships
- [[Databricks]] - adjacent platform contrasted by workload shape and programming style.
- [[Dbt]] - reusable SQL transformation layer paired with Snowflake in EP50.
- [[Hightouch]] - downstream platform activating customer data from Snowflake.
- [[EnterpriseDataActivation]] - operational use pattern supported by warehouse-held data.
- [[EnterpriseDataModernization]] - broader transition in which Snowflake can serve structured analytics workloads.
- [[SasankAkkinappoli]] - practitioner providing the EP50 workload comparison.
