---
title: "Agent Permission Boundaries"
type: concept
tags: [agents, security, governance]
sources: [vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1]
last_updated: 2026-07-07
---

# Agent Permission Boundaries

Agent permission boundaries are the practical limits that decide which tools, accounts, data, and actions an agent can use automatically, which require explicit human instruction, and which should remain out of scope. In [[vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1]], the issue appears through [[OpenClaw]] and [[JustinYan]]'s personal agent: he uses a virtual machine, separate accounts, and trusted versus agent-written skill categories because the agent may otherwise expose personal information or misuse powerful services.

## Key Claims
- Permission design is part of the [[AgentHarness]], not an afterthought, because tool access defines what the agent can actually do.
- Personal agents need tiered skill policies: some skills can run automatically, while others should require explicit human invocation.
- Separate browser profiles, cheap or disposable accounts, and virtual machines can reduce damage when experimenting with agentic systems.
- High-impact resources such as main accounts, private repositories, payment systems, banking, passwords, and tokens require stronger controls than calendar or reminder data.
- Permission boundaries connect local safety with [[AgentIdentityAndAuthentication]] because external services need to know which actor is taking an action and under whose authority.

## Connections
- [[OpenClaw]], [[JustinYan]], and [[Zili]] — source context for personal-agent safety.
- [[AgentHarness]] and [[AgentFacingInterfaces]] — places where permissions are configured and enforced.
- [[AgentIdentityAndAuthentication]] — adjacent infrastructure problem for attribution and account access.
- [[AIGovernanceAndCompliance]] — broader governance context when agents touch regulated or sensitive workflows.
- [[DataPortabilityAndSustainableTools]] — trust pattern for personal tools that should preserve user control over data.
