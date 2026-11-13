---
title: "Test-Driven Agent Governance"
type: concept
tags: [ai, agents, governance, testing]
sources:
  - default-mp3-ywr3ahjkcgo-6d2e35db114ec311e40e28811db235eb-30651176-default-mp3-ywr3ahjkcgo-6d2e35db114ec311e40e28811db235eb-30651176
last_updated: 2026-11-13
knowledge_schema: synthesis-v1
---

# Test-Driven Agent Governance

## Definition
Test-driven agent governance is a source-described method that defines expected workflow outcomes and risk boundaries before deployment, probes agent behavior against edge cases, and turns observed failures into narrow controls that can be retested.

## Current Synthesis
The method treats governance as an executable assurance loop rather than a static prohibition list. A workflow is decomposed into steps; intended outcomes, malformed states, permissions, and audit requirements are specified; more repeatable inference is used to expose failure cases; and targeted corrections are placed in adapters, smaller models, validators, or other workflow controls. Human attention is then reserved for exceptions whose ambiguity or consequence exceeds those bounded controls.

Its strongest contribution is separation of roles. Model-layer intervention can shape behavior, while deterministic validation, permission boundaries, and audit records constrain what reaches a downstream system. Neither layer alone establishes safety, and a passed test suite does not prove behavior under every model, context, tool, or distribution shift.

## Key Claims
- Expected outcomes and unacceptable states should be specified before an agent receives production authority.
- Edge-case testing should cover model behavior and the composition of outputs across workflow steps.
- Narrow adapters or specialized models can encode targeted corrections without requiring one general model to govern everything.
- Structured validation and permission controls remain necessary even when model behavior has been tuned.
- Human review should focus on consequential exceptions and novel failures rather than repetitive low-value approvals.
- Governance controls need regression testing as models, prompts, tools, data, and workflows change.

## Evidence
- Expected-outcome loop - [[default-mp3-ywr3ahjkcgo-6d2e35db114ec311e40e28811db235eb-30651176-default-mp3-ywr3ahjkcgo-6d2e35db114ec311e40e28811db235eb-30651176]] attributes to [[DustinAllen]] a define, test, correct, distill, and retest process.
- Workflow composition - [[default-mp3-ywr3ahjkcgo-6d2e35db114ec311e40e28811db235eb-30651176-default-mp3-ywr3ahjkcgo-6d2e35db114ec311e40e28811db235eb-30651176]] uses a bank-account-change example to map payroll, APIs, procedures, and audit trails while warning that fabricated but plausible JSON can enter downstream systems.
- Layered enforcement - [[default-mp3-ywr3ahjkcgo-6d2e35db114ec311e40e28811db235eb-30651176-default-mp3-ywr3ahjkcgo-6d2e35db114ec311e40e28811db235eb-30651176]] describes deterministic inference, low-rank adapters, smaller governance models, and output validation as complementary controls.
- Human allocation - [[default-mp3-ywr3ahjkcgo-6d2e35db114ec311e40e28811db235eb-30651176-default-mp3-ywr3ahjkcgo-6d2e35db114ec311e40e28811db235eb-30651176]] argues that routine decisions should be filtered before escalation because excessive review creates fatigue and indiscriminate approval.

## Counterevidence & Qualifications
The source is a founder interview summarized rather than a published evaluation. It gives no test corpus, baseline, error taxonomy, adapter metrics, false-positive rate, adversarial protocol, or independent replication. Deterministic inference may improve repeatability without revealing all failures, and teacher-provided answers or rubrics can encode their own blind spots. Specialized controls can also drift when models, tools, and operating context change.

## What Changed
- Created an assurance-loop concept joining predefined outcomes, edge-case testing, targeted correction, structured validation, and selective escalation.

## Related Concepts
- [[AgentReliabilityVerification]] - broader requirement to prove workflow results through external checks and acceptance criteria.
- [[ProbabilisticSoftware]] - variable execution property that motivates repeatable tests and deterministic subcontrols.
- [[HumanInLoopAgentGovernance]] - exception and approval layer for consequential uncertainty.
- [[AgentPermissionBoundaries]] - authority limits that testing should verify and enforcement should preserve.
- [[LongHorizonAgentReliability]] - multi-step context in which small failures can compound.
- [[EnterpriseAgentGovernance]] - organizational operating layer that can adopt the method.
