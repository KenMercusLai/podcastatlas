---
title: "Long-Horizon Agent Reliability / 长期智能体可靠性"
type: concept
tags: [ai, agents, reliability, memory, infrastructure]
sources:
  - cong-mianfei-pisa-dao-dingcuo-jipiao-guigu-chuangyezhe-zhengzai-jiejue-agent-de-naxie-mafan-s10e33-039d9703-e999-454e-b6f4-f3d42ff195be
  - default-mp3-ywr3ahjkcgo-6d2e35db114ec311e40e28811db235eb-30651176-default-mp3-ywr3ahjkcgo-6d2e35db114ec311e40e28811db235eb-30651176
last_updated: 2026-11-13
knowledge_schema: synthesis-v1
---

# Long-Horizon Agent Reliability / 长期智能体可靠性

## Definition
Long-horizon agent reliability is the ability of an agent system to preserve goals, constraints, evidence, progress, and recoverability across many steps, tool calls, context compressions, interruptions, and days of execution.

## Current Synthesis
Long tasks turn small weaknesses into accumulated operational risk. A model may call tools and make plausible plans yet forget the original goal after compaction, drop a privacy constraint, repeat work, fabricate structurally plausible output, or commit an irreversible mistake such as a wrong booking. The newest source sharpens composition risk: even a low per-step error rate can become material when outputs flow through many APIs and decisions without validation.

Reliability therefore belongs to the whole system: external state, selective memory, checkpoints, observability, schema and outcome validation, retry and rollback rules, permission gates, and a channel for timely human escalation. Testing needs to cover handoffs and downstream state, not only whether each isolated model response appears reasonable.

The governing distinction is between continuing and recovering. Persistence alone can let an error run longer; a reliable agent must detect uncertainty or divergence, stop safely, reconstruct what happened, ask for help when needed, and resume from a known state.

## Key Claims
- Step count, duration, cross-platform action, and repeated context compaction create failure modes not captured by short-answer quality.
- Durable state must preserve goals, constraints, completed work, evidence, and outstanding decisions outside fragile conversational context.
- Checkpoints, verification, retry, rollback, cancellation, and compensation paths are part of task completion when actions affect the real world.
- High-impact ambiguity should trigger human escalation through a reachable channel rather than silent continuation.
- Reliability is a systems property spanning models, harnesses, runtimes, tools, permissions, identities, and external services.
- Efficiency and concurrency matter because excessive steps, latency, and overload widen both failure probability and recovery cost.
- Step-level success does not establish workflow success when malformed state or plausible fabrication can propagate across interfaces.

## Evidence
- Compaction and goal loss: [[cong-mianfei-pisa-dao-dingcuo-jipiao-guigu-chuangyezhe-zhengzai-jiejue-agent-de-naxie-mafan-s10e33-039d9703-e999-454e-b6f4-f3d42ff195be]] says tasks with hundreds or thousands of steps can lose information or forget the original objective after repeated compression.
- Real-world recovery: [[cong-mianfei-pisa-dao-dingcuo-jipiao-guigu-chuangyezhe-zhengzai-jiejue-agent-de-naxie-mafan-s10e33-039d9703-e999-454e-b6f4-f3d42ff195be]] uses a wrong-airport booking to show that correction may require cancellation, extra work, and fees rather than a simple undo.
- Privacy constraint decay: [[cong-mianfei-pisa-dao-dingcuo-jipiao-guigu-chuangyezhe-zhengzai-jiejue-agent-de-naxie-mafan-s10e33-039d9703-e999-454e-b6f4-f3d42ff195be]] warns that an agent working for days may forget restrictions and disclose addresses, names, or banking information.
- Human escalation and concurrency: [[cong-mianfei-pisa-dao-dingcuo-jipiao-guigu-chuangyezhe-zhengzai-jiejue-agent-de-naxie-mafan-s10e33-039d9703-e999-454e-b6f4-f3d42ff195be]] presents messaging or calls as an uncertainty path and Hark's promotion as an overload case.
- Composed workflow error: [[default-mp3-ywr3ahjkcgo-6d2e35db114ec311e40e28811db235eb-30651176-default-mp3-ywr3ahjkcgo-6d2e35db114ec311e40e28811db235eb-30651176]] uses an employee bank-account-change workflow and fabricated JSON from empty input to show how a plausible local output can corrupt downstream action.
- Repeatable edge-case testing: [[default-mp3-ywr3ahjkcgo-6d2e35db114ec311e40e28811db235eb-30651176-default-mp3-ywr3ahjkcgo-6d2e35db114ec311e40e28811db235eb-30651176]] proposes deterministic inference and expected-outcome tests to expose failures before targeted correction and retesting.

## Counterevidence & Qualifications
The sources offer practitioner interpretation and anecdotes rather than controlled failure rates or a comparative architecture study. More stored state can preserve stale or sensitive data; frequent checkpoints can increase cost; retries can duplicate consequential actions; validators can accept semantically wrong but well-formed output; and human escalation can fail through delay or approval fatigue. The newest source does not publish the claimed error rates, deterministic-test methods, or adapter results. No single memory, context-window, validator, or rollback mechanism makes arbitrary long tasks reliable.

## What Changed
- Added explicit error compounding across model, API, and workflow handoffs.
- Distinguished syntactic plausibility from validated downstream state and intended outcome.
- Added repeatable edge-case testing as a complement to runtime recovery.

## Related Concepts
- [[AgentRuntimeExecutionLayer]] - execution substrate for state, isolation, observability, and recovery.
- [[PersistentAgentMemory]] - continuity mechanism that must preserve relevant facts without uncontrolled accumulation.
- [[DataAgentContextCompaction]] - domain-specific example of information loss during compaction.
- [[HumanInLoopAgentGovernance]] - escalation and approval relationship at consequential uncertainty.
- [[AgentGoalDriftDetection]] - monitoring relationship for divergence from the assigned objective.
- [[AgentReliabilityVerification]] - evidence relationship for testing sustained execution rather than isolated output.
- [[AgentPermissionBoundaries]] - constraint relationship that must survive the full task horizon.
- [[TestDrivenAgentGovernance]] - predeployment testing relationship for composed workflow failure.
