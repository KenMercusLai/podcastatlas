---
title: "Agentic Software"
type: concept
tags: [agents, software-design, product]
sources: [vol-164-cong-pingguo-liaodao-ruanjian-weilai-agentic-software-zhende-yaolaile-1-6639-1]
last_updated: 2026-07-07
---

# Agentic Software

Agentic software is the Vol. 164 [[FengyanFengyu]] frame for software designed around agents interpreting goals, selecting capabilities, and generating or reshaping the work surface, rather than users pressing fixed buttons in a static application. In [[vol-164-cong-pingguo-liaodao-ruanjian-weilai-agentic-software-zhende-yaolaile-1-6639-1]], [[JustinYan]] and [[Zili]] argue that adding an AI assistant, skills, or tool calls to a traditional product is only an intermediate step.

The concept overlaps with [[AgentNativeSoftware]], but is slightly broader. Agent-native software describes products whose core substrate is the agent; agentic software also covers the transition path where existing SaaS products, operating systems, and platforms expose [[AtomicCapabilityServices]] and [[AgentFacingInterfaces]] so agents can assemble task-specific behavior.

## Key Claims
- The interaction model shifts from clear input-output buttons toward ambiguous goals, tool choice, generated interfaces, and iterative human review.
- Traditional GUI still matters for inspection, trust, and presentation, but the core capability should become callable and recombinable by agents.
- Platform review systems such as [[AppStore]] can become bottlenecks if they assume every app behavior is fixed before review.
- The pattern depends on [[ContextEngineering]], [[PersistentAgentMemory]], permissions, and bounded verification; otherwise the agent can confidently assemble the wrong workflow.
- Mature agentic software may serve small groups, personal habits, and vertical workflows that fixed maximum-common-denominator software would not support economically.

## Connections
- [[AgentNativeSoftware]] — adjacent product frame where the agent is the product substrate.
- [[AtomicCapabilityServices]] — architectural pattern for decomposing software into recombinable abilities.
- [[TencentMeeting]] — source example used to imagine a meeting product rebuilt as capability atoms.
- [[HeadlessSoftware]] and [[AgentFacingInterfaces]] — interface and callable-surface requirements.
- [[OnDemandApps]], [[GeneratedWorkInterfaces]], and [[TokenDrivenSoftware]] — downstream forms of dynamic software behavior.
- [[AICodingVerification]], [[HumanJudgmentUnderAI]], and [[AICommunicationAbility]] — disciplines needed when agents generate software behavior and code.
