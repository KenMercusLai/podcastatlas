---
title: "Production Agent Discovery"
type: concept
tags: [ai, agents, discovery, enterprise-ai]
sources:
  - ep-51-building-ai-agents-that-actually-work-in-production
last_updated: 2026-10-12
knowledge_schema: synthesis-v1
---

# Production Agent Discovery

## Definition
Production agent discovery is the pre-implementation process of mapping a real business workflow, its people, rules, systems, data, exceptions, risks, and acceptance criteria before granting an AI agent operational responsibility.

## Current Synthesis
The source frames discovery as paid engineering work rather than a sales prelude. Teams inspect a copy of real client data from the beginning, identify incomplete records and undocumented practices, map systems and APIs, and capture knowledge held in employees' heads. This makes the first deliverable a bounded account of what the agent would need to know, access, and prove—not an impressive demonstration built on cleaned examples.

Discovery connects [[AIDataReadiness]] to workflow design. Data quality matters because missing fields and stale records change what an agent can infer, while organizational context matters because exceptions and decision rules may not exist in a database. The result should define a narrow first capability, human checkpoints, permission limits, tests, and an implementation scope.

## Key Claims
- Discovery should inspect actual workflow data because demonstration data hides operational failure modes.
- Systems, APIs, handoffs, exceptions, and tacit employee knowledge are part of the agent's bounded input.
- A narrow first capability is safer to specify and evaluate than an open-ended automation mandate.
- Paid, fixed-scope discovery can separate evidence gathering from implementation commitment.
- Discovery should produce acceptance, permission, security, and escalation requirements as well as feature requirements.

## Evidence
- Real-data inspection: [[ep-51-building-ai-agents-that-actually-work-in-production]] says HummingAgent works from a copy of client data on day one and commonly encounters incomplete CRM histories and missing fields.
- Workflow mapping: [[ep-51-building-ai-agents-that-actually-work-in-production]] describes identifying systems, APIs, operational rules, and knowledge that exists only in employees' heads.
- Commercial boundary: [[ep-51-building-ai-agents-that-actually-work-in-production]] presents discovery as a paid, fixed-scope engagement before implementation.
- Deployment boundary: [[ep-51-building-ai-agents-that-actually-work-in-production]] recommends one sandboxed capability before expanding access.

## Counterevidence & Qualifications
The source offers a vendor's operating method, not a comparative study proving that paid discovery produces better outcomes. Copies of production data can themselves create privacy, security, freshness, and representativeness risks. Some bounded use cases may need less formal discovery, while regulated or safety-critical work may require substantially more legal, security, and domain review than this episode describes.

## What Changed
- Established real-data, workflow, and tacit-knowledge discovery as a distinct pre-implementation phase for production agents.

## Related Concepts
- [[AIDataReadiness]] - determines whether the workflow's data can support trustworthy agent behavior.
- [[OrganizationalContext]] - captures company-specific state and unwritten operating knowledge.
- [[AgentReliabilityVerification]] - turns discovered acceptance criteria into checks on agent outcomes.
- [[AgentPermissionBoundaries]] - converts workflow risk into enforceable access and action limits.
- [[ProgressiveAgentAutonomy]] - uses discovery to define the narrow first stage of delegated authority.
- [[BusinessLedAITransformation]] - keeps agent work anchored to an operating problem and owner.
