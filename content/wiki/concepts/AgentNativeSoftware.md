---
title: "Agent Native Software"
type: concept
tags: [agents, software-design, product]
sources: [vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1]
last_updated: 2026-07-07
---

# Agent Native Software

Agent-native software is software whose core substrate is an agent rather than a traditional app with an AI feature bolted on. In [[vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1]], [[JustinYan]] and [[Zili]] frame [[OpenClaw]] this way: the surrounding code, tools, channels, UI, and [[AISkills]] act as the agent's hands, senses, and work environment, while the agent itself is what makes the product coherent.

## Key Claims
- Agent-native software differs from AI-assisted software because removing the agent would remove the product's reason to exist.
- The design center shifts from screens and static feature menus toward [[AgentHarness]] choices: tools, permissions, channels, triggers, memory, and feedback loops.
- [[AISkills]] become product surface because they define reusable capabilities and can sometimes be created or refined by the agent itself.
- [[OnDemandApps]] are one possible downstream form: the agent assembles or generates capabilities at the moment of need instead of exposing only prebuilt app functions.
- Agent-native software increases the importance of [[AgentPermissionBoundaries]] because broader action capacity also broadens failure and leakage risk.

## Connections
- [[OpenClaw]] — source example of an agent-native product form.
- [[AgentHarness]], [[AgenticWorkflow]], and [[AgentFacingInterfaces]] — infrastructure and interface layer that agent-native software depends on.
- [[AISkills]], [[AgentSelfEvolution]], and [[PersistentAgentMemory]] — mechanisms for durable and self-improving capability.
- [[HeadlessSoftware]] — adjacent thesis that software value should be callable by agents rather than trapped in GUI-first flows.
- [[OnDemandApps]] and [[AgentPermissionBoundaries]] — new concepts added by the same source.
