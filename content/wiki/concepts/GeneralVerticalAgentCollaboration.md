---
title: "General–Vertical Agent Collaboration"
type: concept
tags: [ai, agents, product, orchestration]
sources:
  - 7b500b8f-cfde-4da1-9559-8128adcea8f6-7b500b8f-cfde-4da1-9559-8128adcea8f6
last_updated: 2026-11-09
knowledge_schema: synthesis-v1
---

# General–Vertical Agent Collaboration

## Definition
General–vertical agent collaboration is a product and orchestration pattern in which a general agent holds broad user context and manages the main interaction, while a vertical agent contributes domain-specific judgment, tools, workflow, and execution.

## Current Synthesis
The source's “housekeeper and specialist team” analogy separates familiarity from expertise. A general agent may know the user's history, preferences, and immediate objective, then package that context for a specialist. The vertical agent must still resolve domain ambiguity, perform the work, expose a reviewable result, and return consequential decisions to the user. This is not a universal routing rule: frequent users may work directly with a vertical agent, and some people may prefer multiple specialist relationships over one attention-managing entrance.

## Key Claims
- Personal context and domain expertise are separable capabilities that can be passed across an agent boundary.
- Low-frequency tasks favor delegation through a general interface when specialist discovery and briefing would otherwise be costly.
- High-frequency or iterative professional work can justify a direct relationship with the vertical agent.
- Vertical value depends on professional judgment, task completion, and operational follow-through rather than a narrow generated output.
- User attention, authorization, handoff quality, and context fidelity are first-class coordination constraints.

## Evidence
- **Role separation:** [[7b500b8f-cfde-4da1-9559-8128adcea8f6-7b500b8f-cfde-4da1-9559-8128adcea8f6]] compares a context-rich general agent to a long-serving housekeeper and a vertical agent to a specialist team.
- **Frequency-sensitive entry point:** [[7b500b8f-cfde-4da1-9559-8128adcea8f6-7b500b8f-cfde-4da1-9559-8128adcea8f6]] says low-frequency needs may be routed through a general agent, while frequent creative work may pull users into direct specialist interaction.
- **Execution boundary:** [[7b500b8f-cfde-4da1-9559-8128adcea8f6-7b500b8f-cfde-4da1-9559-8128adcea8f6]] uses video and secondhand sales to show that domain judgment, workflow continuity, physical operations, and final approval remain part of the specialist system.

## Counterevidence & Qualifications
The pattern is a practitioner forecast rather than an observed stable market architecture. Context transfer can create privacy, consent, schema, and loss-of-nuance problems, while routing adds latency and accountability ambiguity. Strong general agents may absorb some specialist tasks, and standalone vertical products may fail if their expertise does not cover the user's complete valuable job.

## What Changed
- Established a frequency- and attention-sensitive model for collaboration between general and vertical agents.
- Made context handoff, professional execution, and retained authorization distinct responsibilities.
- Preserved direct specialist use and general-agent capability expansion as live alternatives.

## Related Concepts
- [[VerticalAgentArchitecture]] - supplies the specialist model, harness, context, and tool stack.
- [[PersonalLifeAgent]] - represents the broad context-holding side of the collaboration.
- [[AgentMarketplace]] - possible discovery and routing layer for specialist capabilities.
- [[AgentPermissionBoundaries]] - governs what context and authority can cross the handoff.
- [[HumanInLoopAgentGovernance]] - retains review and authorization at consequential checkpoints.
- [[VerticalAgentSaaSification]] - warns that specialist automation can collapse back into process-heavy software or service work.
