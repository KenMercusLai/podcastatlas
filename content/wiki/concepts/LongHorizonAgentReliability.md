---
title: "Long-Horizon Agent Reliability / 长期智能体可靠性"
type: concept
tags: [ai, agents, reliability, memory, infrastructure]
sources:
  - cong-mianfei-pisa-dao-dingcuo-jipiao-guigu-chuangyezhe-zhengzai-jiejue-agent-de-naxie-mafan-s10e33-039d9703-e999-454e-b6f4-f3d42ff195be
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

# Long-Horizon Agent Reliability / 长期智能体可靠性

## Definition
Long-horizon agent reliability is the ability of an agent system to preserve goals, constraints, evidence, progress, and recoverability across many steps, tool calls, context compressions, interruptions, and days of execution.

## Current Synthesis
Long tasks turn small weaknesses into accumulated operational risk. A model may call tools and make plausible plans yet forget the original goal after compaction, drop a privacy constraint, repeat work, or commit an irreversible mistake such as a wrong booking. Reliability therefore belongs to the whole system: external state, selective memory, checkpoints, observability, verification, retry and rollback rules, permission gates, and a channel for timely human escalation.

The governing distinction is between continuing and recovering. Persistence alone can let an error run longer; a reliable agent must detect uncertainty or divergence, stop safely, reconstruct what happened, ask for help when needed, and resume from a known state.

## Key Claims
- Step count, duration, cross-platform action, and repeated context compaction create failure modes not captured by short-answer quality.
- Durable state must preserve goals, constraints, completed work, evidence, and outstanding decisions outside fragile conversational context.
- Checkpoints, verification, retry, rollback, cancellation, and compensation paths are part of task completion when actions affect the real world.
- High-impact ambiguity should trigger human escalation through a reachable channel rather than silent continuation.
- Reliability is a systems property spanning models, harnesses, runtimes, tools, permissions, identities, and external services.
- Efficiency and concurrency matter because excessive steps, latency, and overload widen both failure probability and recovery cost.

## Evidence
- Compaction and goal loss: [[cong-mianfei-pisa-dao-dingcuo-jipiao-guigu-chuangyezhe-zhengzai-jiejue-agent-de-naxie-mafan-s10e33-039d9703-e999-454e-b6f4-f3d42ff195be]] says tasks with hundreds or thousands of steps can lose information or forget the original objective after repeated compression.
- Real-world recovery: [[cong-mianfei-pisa-dao-dingcuo-jipiao-guigu-chuangyezhe-zhengzai-jiejue-agent-de-naxie-mafan-s10e33-039d9703-e999-454e-b6f4-f3d42ff195be]] uses a wrong-airport booking to show that correction may require cancellation, extra work, and fees rather than a simple undo.
- Privacy constraint decay: [[cong-mianfei-pisa-dao-dingcuo-jipiao-guigu-chuangyezhe-zhengzai-jiejue-agent-de-naxie-mafan-s10e33-039d9703-e999-454e-b6f4-f3d42ff195be]] warns that an agent working for days may forget restrictions and disclose addresses, names, or banking information.
- Human escalation and concurrency: [[cong-mianfei-pisa-dao-dingcuo-jipiao-guigu-chuangyezhe-zhengzai-jiejue-agent-de-naxie-mafan-s10e33-039d9703-e999-454e-b6f4-f3d42ff195be]] presents messaging or calls as an uncertainty path and Hark's promotion as an overload case.

## Counterevidence & Qualifications
The source offers practitioner interpretation and anecdotes rather than controlled failure rates or a comparative architecture study. More stored state can preserve stale or sensitive data; frequent checkpoints can increase cost; retries can duplicate consequential actions; and human escalation can fail through delay or approval fatigue. No single memory, context-window, or rollback mechanism makes arbitrary long tasks reliable.

## What Changed
- Created a systems-level reliability concept joining memory, state, recovery, permission, escalation, and concurrency.

## Related Concepts
- [[AgentRuntimeExecutionLayer]] - execution substrate for state, isolation, observability, and recovery.
- [[PersistentAgentMemory]] - continuity mechanism that must preserve relevant facts without uncontrolled accumulation.
- [[DataAgentContextCompaction]] - domain-specific example of information loss during compaction.
- [[HumanInLoopAgentGovernance]] - escalation and approval relationship at consequential uncertainty.
- [[AgentGoalDriftDetection]] - monitoring relationship for divergence from the assigned objective.
- [[AgentReliabilityVerification]] - evidence relationship for testing sustained execution rather than isolated output.
- [[AgentPermissionBoundaries]] - constraint relationship that must survive the full task horizon.
