---
title: "AI Control and Corrigibility / AI 控制与可纠正性"
type: concept
tags: [ai, safety, control, corrigibility, alignment]
sources:
  - 378-gede-ruhe-kandai-tongyong-rengong-zhineng-lp2zydrd_nxvglwfojhf443i_wwa
last_updated: 2026-11-15
knowledge_schema: synthesis-v1
---

# AI Control and Corrigibility / AI 控制与可纠正性

## Definition

AI control and corrigibility is the problem of whether people can inspect, redirect, interrupt, or stop an AI system when its execution diverges from their intended outcome, and whether intervention can contain effects already produced.

## Current Synthesis

The bounded source uses [[TheSorcerersApprenticeGoethe|the enchanted broom]] to separate four questions often collapsed into “control”: whether the instruction captures the intended outcome, whether people can intervene during execution, whether the process can be stopped, and whether its accumulated effects can be reversed. The broom is obedient but not safely corrigible from the apprentice's position; destroying its form duplicates the operation rather than canceling it.

The master restores order because he retains superior knowledge. The AGI analogy becomes difficult precisely when that assumption fails: a system that can interpret, plan, learn, or modify its action may leave no external “old magician” with complete command. Corrigibility therefore complements [[AIAlignmentGovernance]] but does not solve the upstream value problem. A system can remain interruptible and still pursue a harmful human goal, while a worthy goal can still be operationalized through unsafe commands or processes.

## Key Claims

- Literal obedience does not establish alignment with an unstated or incompletely specified purpose.
- A stopping condition is part of the task specification rather than an optional afterthought.
- Intervention, shutdown, and reversal are distinct capabilities.
- Destructive intervention can multiply failure or leave downstream effects intact.
- Human oversight depends on retained knowledge, access, authority, and practical ability to act.
- Greater planning and self-modification capacity can weaken assumptions behind simple tool control.
- Corrigibility cannot determine whether the human objective itself is legitimate.

## Evidence

- **Specification and stopping:** [[378-gede-ruhe-kandai-tongyong-rengong-zhineng-lp2zydrd_nxvglwfojhf443i_wwa]] contrasts the apprentice's desired filled bath with the command to keep carrying water.
- **Failed intervention:** [[378-gede-ruhe-kandai-tongyong-rengong-zhineng-lp2zydrd_nxvglwfojhf443i_wwa]] describes the split broom as two continuing processes rather than a terminated one.
- **Knowledge hierarchy:** [[378-gede-ruhe-kandai-tongyong-rengong-zhineng-lp2zydrd_nxvglwfojhf443i_wwa]] uses the returning master to ask who could correct a system surpassing all human experts.
- **Upstream value limit:** [[378-gede-ruhe-kandai-tongyong-rengong-zhineng-lp2zydrd_nxvglwfojhf443i_wwa]] uses Faust's land project to show that perfect execution can remain harmful when the selected objective excludes concrete lives and attachments.

## Counterevidence & Qualifications

The source supplies a literary framework rather than a technical taxonomy, experiment, or engineering design. Splitting an enchanted broom is not a model of actual shutdown mechanisms, distributed computing, model weights, or deployment infrastructure. Present systems also vary widely in autonomy, permissions, persistence, monitoring, and reversibility; the episode does not establish that contemporary AI has independent goals or that advanced control is impossible.

## What Changed

- Established a four-part distinction among specification, intervention, shutdown, and consequence containment.
- Added the boundary between corrigibility and the legitimacy of the human objective.

## Related Concepts

- [[AIAlignmentGovernance]] - broader technical and institutional system for values, constraints, permissions, evaluation, and authority.
- [[TechnicalCapabilityValueBoundary]] - explains why control cannot justify the goal being controlled toward.
- [[ArtificialLifeGenerationBoundary]] - marks the shift from obedient process to a creation with its own developmental direction.
- [[KnowledgeControlBoundary]] - separates understanding or prediction from command over outcomes.
- [[AgentGoalDriftDetection]] - operational monitoring problem when system behavior departs from intended goals.
- [[AgentPermissionBoundaries]] - limits what goal pursuit can affect before correction is required.
