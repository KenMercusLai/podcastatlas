---
title: "Case Ready Intake AI"
type: entity
tags: [ai, legal-ai, product]
sources:
  - ep-40-governance-first-the-architecture-framework-that-makes-ai-auditable-defensible-and-99-cheaper
last_updated: 2026-09-11
knowledge_schema: synthesis-v1
---

# Case Ready Intake AI

## Overview
Case Ready Intake AI is the legal AI intake product discussed by [[DanDriver]] in [[ep-40-governance-first-the-architecture-framework-that-makes-ai-auditable-defensible-and-99-cheaper]].

## Current Profile
The product is positioned as a bounded legal-intake organizer, not an attorney substitute. It helps users structure a case around narrative, timeline, and evidence while avoiding legal advice and unauthorized practice of law. Its distinctive architecture is that compliance-sensitive decisions are documented and routed through deterministic checks before LLM generation.

## Key Characteristics
- Produces narrative, timeline, and evidence-list outputs for legal intake preparation.
- Avoids legal advice and uses UPL exposure as a central design boundary.
- Uses Python-based checks for dates, scope, warnings, and pass/fail decisions.
- Runs pre-flight checks before spending tokens on full generation.
- Uses runtime QA and human review to keep output aligned with the product charter.

## Evidence
- Output boundary: [[ep-40-governance-first-the-architecture-framework-that-makes-ai-auditable-defensible-and-99-cheaper]] says the product produces narrative, timeline, and evidence list outputs.
- UPL boundary: [[ep-40-governance-first-the-architecture-framework-that-makes-ai-auditable-defensible-and-99-cheaper]] says a UPL exposure audit delayed launch and shaped the product's constraints.
- Deterministic controls: [[ep-40-governance-first-the-architecture-framework-that-makes-ai-auditable-defensible-and-99-cheaper]] says Python handles dates, scope, warnings, and go/no-go decisions.
- Runtime review: [[ep-40-governance-first-the-architecture-framework-that-makes-ai-auditable-defensible-and-99-cheaper]] describes final AI checks against the charter and human review through GitHub pull requests.

## Qualifications
The episode does not provide an external product audit, legal opinion, benchmark, customer outcome study, or cost accounting. Claims about the product's launch, cost reduction, and defensibility remain source-scoped.

## What Changed
- Initial product profile created as the concrete case for governance-first legal AI architecture.

## Relationships
- [[DanDriver]] - founder and architect associated with the product.
- [[DriverAIAgency]] - company behind the product.
- [[GovernanceFirstLegalAI]] - architecture frame the product exemplifies.
- [[DeterministicLegalAIControls]] - technical pattern used in the workflow.
- [[UnauthorizedPracticeOfLawAIBoundary]] - legal boundary the product is designed around.
