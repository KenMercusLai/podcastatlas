---
title: "Data Agent Governance"
type: concept
tags: [ai, agents, governance, data-engineering]
sources:
  - ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack
last_updated: 2026-08-29
knowledge_schema: synthesis-v1
---

# Data Agent Governance

## Definition
Data agent governance is the permission, policy, cost-control, privacy, and audit layer for AI agents that operate across data warehouses, pipelines, BI tools, and analytics workflows.

## Current Synthesis
The EP45 source specializes [[EnterpriseAgentGovernance]] for production data environments. Data agents can query expensive warehouses, touch sensitive data, cross tool boundaries, and generate outputs that influence business decisions, so governance cannot be left to a natural-language prompt.

The current synthesis is that governance has to travel with the agent. Existing RBAC and access policies are often fragmented across data warehouses, pipeline tools, and BI systems; an agent sitting above those tools needs an additional harness layer that can apply enterprise-specific cost, permission, and PII rules.

## Key Claims
- Data-agent governance includes both permission boundaries and warehouse cost controls.
- Sensitive-data and PII access should be constrained before an agent runs or reveals a query result.
- Existing RBAC and access-policy fragmentation becomes harder when agents operate across tools.
- Agents need explicit limits on expensive, long-running, or risky queries.
- A governance layer can sit above warehouses, pipelines, and BI tools while interfacing with their existing controls.
- Enterprise harnesses should let organizations add their own rules, permissions, and guardrails.

## Evidence
- Cost risk: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] discusses a reported expensive Cortex AI query when asking about cost controls.
- Permission scope: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] says governance includes sensitive-data access and PII boundaries.
- RBAC fragmentation: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] says humans already struggle with separate access-policy models across tools and that agents enlarge the problem.
- Query limits: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] argues agents must be told not to run expensive or long-running queries.
- Cross-tool layer: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] says agents sit outside individual tools and can interface with pipeline, warehousing, and BI tools.
- Extensibility: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] says Altimate Code's open-source harness lets enterprises add their own rules, permissions, and guardrails.

## Counterevidence & Qualifications
The source describes governance capabilities at a high level and does not audit how rules are represented, enforced, tested, or integrated with existing warehouse and BI security systems. Governance also cannot repair ambiguous data definitions by itself; it depends on [[AIDataReadiness]] and accountable data ownership.

## What Changed
- Initial concept created to capture data-specific agent governance around query cost, PII, permissions, and cross-tool controls.

## Related Concepts
- [[EnterpriseAgentGovernance]] - broader enterprise-agent governance frame.
- [[AgentPermissionBoundaries]] - permission subproblem that data-agent governance specializes.
- [[AgenticDataEngineeringHarness]] - harness layer where governance is enforced.
- [[AIDataReadiness]] - data ownership and permission foundation governance depends on.
- [[ModelRoutingCostControl]] - adjacent cost-control concept for choosing model and execution paths.
- [[AIInferenceCostStructure]] - broader cost layer affected by long-running agent loops.
- [[HumanJudgmentUnderAI]] - accountability boundary when governance still requires approval or review.
