---
title: "Governance-First Legal AI"
type: concept
tags: [ai, law, governance, compliance]
sources:
  - ep-40-governance-first-the-architecture-framework-that-makes-ai-auditable-defensible-and-99-cheaper
last_updated: 2026-09-11
knowledge_schema: synthesis-v1
---

# Governance-First Legal AI

## Definition
Governance-first legal AI is the design pattern where legal AI systems encode compliance, auditability, prohibited behavior, deterministic checks, and human review into architecture before broad generation is allowed.

## Current Synthesis
The source's central claim is that legal AI cannot treat governance as a policy PDF or after-the-fact disclaimer. In [[CaseReadyIntakeAI]], governance is implemented as a charter, documented decisions, launch tests, UPL review, deterministic date and scope checks, runtime QA, and human review. The resulting product boundary is defined as much by what the system refuses to do as by what it generates.

## Key Claims
- Legal AI governance should be operational and testable, not only declarative.
- Product charters can make design choices, launch criteria, and revisions auditable.
- Prohibited outputs should be specified as carefully as desired outputs.
- Deterministic checks should handle legal-risk facts such as dates, scope, warnings, and pass/fail decisions when exactness matters.
- Human review remains part of the control system, especially before deployment or high-risk output reliance.

## Evidence
- Architectural charter: [[ep-40-governance-first-the-architecture-framework-that-makes-ai-auditable-defensible-and-99-cheaper]] says [[DanDriver]] uses a 10-page charter to document AI decisions and tests.
- UPL review: [[ep-40-governance-first-the-architecture-framework-that-makes-ai-auditable-defensible-and-99-cheaper]] says an unauthorized-practice-of-law exposure audit delayed launch so the product could remain compliant.
- Deterministic checks: [[ep-40-governance-first-the-architecture-framework-that-makes-ai-auditable-defensible-and-99-cheaper]] says Python performs date, scope, warning, and go/no-go logic before LLM generation.
- Human review: [[ep-40-governance-first-the-architecture-framework-that-makes-ai-auditable-defensible-and-99-cheaper]] says pull requests are manually reviewed as part of an auditable trail.

## Counterevidence & Qualifications
The source presents a founder's architecture account, not an independent legal, security, cost, or product audit. The pattern also does not guarantee legal compliance by itself; UPL, consumer-protection, privacy, bias, and professional-responsibility duties depend on jurisdiction and use context.

## What Changed
- Initial concept created to capture governance as an enforceable legal AI architecture pattern.

## Related Concepts
- [[LegalAIVerificationAuditability]] - audit and verification requirement that governance-first systems try to satisfy.
- [[HumanInTheLoopLegalAI]] - human responsibility layer inside legal AI governance.
- [[DeterministicLegalAIControls]] - implementation pattern for legal-risk checks.
- [[UnauthorizedPracticeOfLawAIBoundary]] - legal boundary that constrains product scope.
- [[AIGovernanceAndCompliance]] - broader institutional AI governance context.
- [[AIWorkflowTriage]] - workflow decomposition principle behind deciding what the LLM should not do.
