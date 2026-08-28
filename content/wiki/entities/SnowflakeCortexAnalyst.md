---
title: "Snowflake Cortex Analyst"
type: entity
tags: [product, ai, analytics, data-warehouse]
sources:
  - ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack
last_updated: 2026-08-29
knowledge_schema: synthesis-v1
---

# Snowflake Cortex Analyst

## Overview
Snowflake Cortex Analyst is the Snowflake AI analytics product used in EP45 of [[DataScienceWithSam]] as an example of why production data agents need validation beyond successful SQL execution. The source cites an independent evaluation where many generated queries were wrong even though they compiled and ran.

## Current Profile
In this wiki branch, Cortex Analyst functions as a source-scoped failure example rather than a full product review. The episode uses it to show that [[SilentSQLFailure|silent SQL failure]] can be more dangerous than syntax errors: a query can execute cleanly, return data, and still answer the wrong question.

The source connects the product example to the broader [[Snowflake]] data-platform context and to the need for [[AgenticDataEngineeringHarness|agentic data engineering harnesses]] that include semantic checks, table context, cost controls, and permissions.

## Key Characteristics
- Serves as the episode's opening example of AI-generated SQL that can run while being semantically wrong.
- Illustrates the gap between query compilation and query correctness in warehouse-backed AI analytics.
- Connects hallucinated tables, wrong joins, and incomplete schema context to data-agent reliability risk.
- Raises cost-control concerns through a source-scoped discussion of expensive Cortex AI queries.
- Grounds the episode's argument that data-agent systems need validation and governance layers around model output.

## Evidence
- Wrong-query example: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] cites an evaluation where six in ten Cortex Analyst AI-generated queries were wrong while still compiling and running.
- Silent-failure framing: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] uses the example to argue that execution success does not prove semantic correctness.
- Data-context need: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] says data agents need table, relationship, and lineage context to avoid hallucinated or partial answers.
- Cost-control context: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] discusses a reported expensive Cortex AI query when motivating governance guardrails.
- Governance implication: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] connects the product example to permissions, PII limits, and query-cost controls.

## Qualifications
The page does not independently evaluate Snowflake Cortex Analyst or Snowflake's current product behavior. The error rate and expensive-query example are episode-level claims without methodology details in the ingested summary. The source also does not separate every Cortex AI service from Cortex Analyst, so cost claims should remain attached to the episode's broader Cortex discussion.

## What Changed
- Initial source-scoped product page created to capture the executable-but-wrong SQL example.

## Relationships
- [[Snowflake]] - parent data-platform context already present in the wiki.
- [[SilentSQLFailure]] - failure mode Cortex Analyst is used to illustrate.
- [[AgenticDataEngineeringHarness]] - infrastructure response the episode argues for.
- [[DeterministicDataAgentValidation]] - correctness layer needed beyond compilation.
- [[AIDataReadiness]] - data-context and permission foundation implicated by the example.
- [[DataAgentGovernance]] - cost and access-control response to warehouse-backed agents.
- [[DataScienceWithSam]] - podcast source context for the example.
