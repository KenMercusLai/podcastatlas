---
title: "Deterministic Legal AI Controls"
type: concept
tags: [ai, law, verification, governance]
sources:
  - ep-40-governance-first-the-architecture-framework-that-makes-ai-auditable-defensible-and-99-cheaper
last_updated: 2026-09-11
knowledge_schema: synthesis-v1
---

# Deterministic Legal AI Controls

## Definition
Deterministic legal AI controls are non-generative checks that decide legally sensitive facts, gates, warnings, or workflow eligibility before or alongside LLM output.

## Current Synthesis
The episode makes deterministic controls a practical legal AI safety and cost pattern. [[CaseReadyIntakeAI]] uses Python for dates, scope, warnings, and pass/fail decisions so the LLM does not calculate legally sensitive thresholds or decide whether a user request is inside the product's permitted role. The control layer also reduces cost by stopping or warning on out-of-scope submissions before the full LLM workflow runs.

## Key Claims
- Date calculations and limitation-like thresholds should not be left to LLM generation when deterministic logic can check them.
- Pre-flight controls can reduce token spend by filtering unsuitable or out-of-scope matters early.
- Deterministic gates make the system's refusal and warning behavior more auditable than prompt-only guardrails.
- Runtime QA can compare user input, generated output, and charter requirements before release.
- Deterministic controls are most useful when paired with human review and a documented product boundary.

## Evidence
- Date and scope checks: [[ep-40-governance-first-the-architecture-framework-that-makes-ai-auditable-defensible-and-99-cheaper]] says the system never asks the LLM to calculate dates and uses Python to detect out-of-scope situations.
- Cost effect: [[ep-40-governance-first-the-architecture-framework-that-makes-ai-auditable-defensible-and-99-cheaper]] says front-door date checks prevented unnecessary full LLM runs.
- Prompt-injection and legal-advice boundary: [[ep-40-governance-first-the-architecture-framework-that-makes-ai-auditable-defensible-and-99-cheaper]] says the workflow fails when a user tries to push it into legal advice.
- Charter comparison: [[ep-40-governance-first-the-architecture-framework-that-makes-ai-auditable-defensible-and-99-cheaper]] describes a final check that output still fits the intended narrative, timeline, and evidence-list role.

## Counterevidence & Qualifications
Deterministic checks are only as good as their encoded rules and input parsing. They may miss ambiguous facts, jurisdiction-specific legal differences, misleading user descriptions, or procedural exceptions. The episode does not provide benchmark data proving a 99% cost reduction or legal-risk reduction.

## What Changed
- Initial concept created for the legal AI version of deterministic verification and workflow gating.

## Related Concepts
- [[DeterministicAIVerification]] - broader deterministic-checking frame.
- [[LegalAIVerificationAuditability]] - auditability layer supported by deterministic logs and gates.
- [[GovernanceFirstLegalAI]] - architecture pattern that uses deterministic controls.
- [[AIWorkflowTriage]] - workflow-allocation principle separating code, LLMs, and humans.
- [[LegalAIHallucination]] - failure mode reduced when sensitive checks are not delegated to generation.
- [[HumanJudgmentUnderAI]] - human review remains necessary around deterministic gates.
