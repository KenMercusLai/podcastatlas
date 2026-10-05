---
title: "Agentic Software"
type: concept
knowledge_schema: synthesis-v1
tags: [agents, software-design, product]
sources:
  - vol-164-cong-pingguo-liaodao-ruanjian-weilai-agentic-software-zhende-yaolaile-1-6639-1
  - e155-sihu-meishenme-ren-zai-ti-ai-paomolun-le-lkon87vgpkdkq9ll-fg0eabnuubf
  - all-in-with-chamath-jason-sacks-friedberg-jensen-huang-live-nvidias-future-physical-ai-rise-of-the-agent-inference-explosion-ai-pr-crisis-40545520
last_updated: 2026-10-05
---

# Agentic Software

## Definition
Agentic software is software organized around agents that interpret goals, select tools and capabilities, maintain working context, execute multi-step actions, and expose results for human review. It differs from a conventional application with a chatbot attached because the agent participates in deciding how work is performed.

## Current Synthesis
The software boundary is shifting from fixed screens and button sequences toward callable capabilities, generated work surfaces, and agents that operate across tools. Existing SaaS does not necessarily disappear: databases, design systems, and specialist applications may become heavily used by agents when their functions are exposed through reliable interfaces. The durable product problem is therefore not “chat versus apps,” but how memory, permissions, context, evaluation, security, and deterministic services constrain probabilistic action.

## Key Claims
- Agentic software turns an ambiguous goal into tool selection, intermediate work, evaluation, and an inspectable result.
- Core product capabilities become more valuable when agents can call and recombine them through stable interfaces.
- Existing specialist software can gain machine users even as graphical entry points and learned UI workflows lose some moat value.
- Persistent memory, context engineering, identity, permissions, and review boundaries are product requirements rather than optional features.
- Agentic workloads can multiply model calls and tool use, making inference cost, latency, reliability, and security part of application design.
- Human-facing interfaces remain important for inspection, correction, trust, and presentation even when the agent performs the underlying workflow.

## Evidence
### Agent-oriented product architecture
- [[vol-164-cong-pingguo-liaodao-ruanjian-weilai-agentic-software-zhende-yaolaile-1-6639-1]] distinguishes an AI feature added to traditional software from products rebuilt around atomic capabilities, agent-facing interfaces, generated work surfaces, context, and review.

### Market structure and machine users
- [[e155-sihu-meishenme-ren-zai-ti-ai-paomolun-le-lkon87vgpkdkq9ll-fg0eabnuubf]] argues that language interfaces, connectors, and skills can weaken GUI entry value and make embedded workflow knowledge more portable.
- [[all-in-with-chamath-jason-sacks-friedberg-jensen-huang-live-nvidias-future-physical-ai-rise-of-the-agent-inference-explosion-ai-pr-crisis-40545520]] says agents may increase use of SQL systems, vector databases, Blender, Photoshop, Synopsys, Cadence, and other tools rather than simply replacing them.

### Workload and control requirements
- [[all-in-with-chamath-jason-sacks-friedberg-jensen-huang-live-nvidias-future-physical-ai-rise-of-the-agent-inference-explosion-ai-pr-crisis-40545520]] frames agentic systems as memory-, tool-, storage-, and model-intensive and says governance is required when agents can access sensitive information, execute code, schedule work, and communicate externally.

## Counterevidence & Qualifications
- The sources describe an emerging architecture, not a settled replacement for conventional applications or graphical interfaces.
- Increased agent use of incumbent tools depends on those tools exposing reliable, economical, permission-aware interfaces; products built mainly around GUI friction remain vulnerable.
- Generated workflows can confidently implement the wrong objective, so autonomy without evaluation and bounded authority can increase rather than reduce operational risk.
- Huang's orders-of-magnitude compute estimates are directional executive claims and should not be generalized to every agent workload.

## What Changed
- Migrated the page to the synthesis-v1 concept schema.
- Added the coexistence thesis that agents can become major users of specialist software rather than only substitutes for it.
- Made heterogeneous workload cost and agent governance part of the core product definition.

## Related Concepts
- [[AgentNativeSoftware]] - narrower product frame in which the agent is the primary substrate.
- [[AtomicCapabilityServices]] - callable building blocks agents can recombine into workflows.
- [[AgentFacingInterfaces]] - machine-oriented surfaces through which agents operate software.
- [[PersistentAgentMemory]] - continuity mechanism that supports long-running and personalized work.
- [[AgentPermissionBoundaries]] - authority limits required when software can act on data and external systems.
- [[AIInferenceCostStructure]] - economic constraint created by repeated model calls and long-running agent loops.
- [[HumanJudgmentUnderAI]] - review and evaluation boundary for probabilistic work.
