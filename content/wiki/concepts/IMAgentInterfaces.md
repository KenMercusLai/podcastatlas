---
title: "IM Agent Interfaces"
type: concept
tags: [agents, interfaces, product-design]
sources: [20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto]
last_updated: 2026-07-07
---

# IM Agent Interfaces

IM agent interfaces are chat or messaging surfaces that make agents reachable inside habits users already have. In [[20-ge-wenti-gao-dong-openclaw-baohong-jizhi-benzhi-bianhua-chuangye-jihui-lk6bzkdxti47vehjvs9sgxotrvto]], [[OpenClaw]]'s IM-style entry point is treated as a major reason the product felt more approachable than CLI agents or traditional web tools. The interface does not create the agent's capability by itself, but it changes how users perceive waiting, failure, repeated interaction, and personality.

## Key Claims
- IM lowers the first-use barrier because users already know how to send messages, wait for replies, and return to asynchronous threads.
- Message latency can make long-running agent tasks feel more like waiting for a person than waiting for frozen software.
- IM can increase tolerance for imperfect agents, especially when paired with [[PersistentAgentMemory]] and a product story that feels like onboarding or training a helper.
- IM alone is not enough; without [[LocalAgentExecution]], tools, files, and feedback loops, the agent risks becoming chat-only advice.
- IM also has limits: thread visibility, fork/merge controls, long document review, and task-state inspection can be weaker than purpose-built agent workspaces.
- In China, [[WeChat]] is treated as the high-value but restricted IM entry point; in global markets, WhatsApp, Discord, Telegram, and similar channels are examples of the broader pattern.

## Connections
- [[OpenClaw]] — central product case.
- [[HumanAgentCollaboration]] — IM changes the social and psychological shape of collaboration.
- [[AgentFacingInterfaces]] — IM is the human-facing entry point, while tools and APIs remain the agent-facing side.
- [[AgentHarness]] — the IM surface must connect to runtime, context, memory, tools, and permissions.
- [[LocalAgentExecution]] — complementary mechanism that turns the message interface into executable work.
- [[PersistentAgentMemory]] and [[AISkills]] — features that make repeated message interaction compound.
- [[WeChat]] and [[Tencent]] — Chinese platform context where an IM agent could be powerful but entry is constrained.
