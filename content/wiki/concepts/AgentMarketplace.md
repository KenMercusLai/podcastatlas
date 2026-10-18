---
title: "Agent Marketplace"
type: concept
knowledge_schema: synthesis-v1
tags: [agents, marketplace, infrastructure]
sources:
  - 142-yusen-de-chuangtou-guancha-di-2-ji-harness-xia-yige-zijie-2026-da-jihui-he-stanley-druckenmiller-lg4sphlaunrjuulqraxs-1gc5ufz
  - yong-agent-donglixue-he-40-ge-agents-yiqi-wei-ren-ai-zuo-chanpin-duitan-slock-ai-chuangshiren-rc-liiv-fkcdolfb06hkoyz0ix3fejy
  - xin-de-chuangye-jihui-zhengzai-claude-code-he-codex-zhouwei-zhang-chulai-duitan-treg-lsjeudluybigsxwwu9v-u2kurpsm
last_updated: 2026-10-19
---

# Agent Marketplace

## Definition

An agent marketplace is infrastructure through which agents can discover, invoke, compare, pay for, or exchange differentiated capabilities, including other agents, accumulated memory, skills, real-time data, and professional APIs.

## Current Synthesis

The bounded evidence now contains two related market forms. [[DaiYusen]] and [[RC]] describe a future agent-to-agent market where persistent agents have differentiated context, experience, memory, and work style that can be hired, invoked, or forked. [[Trigg]] supplies an early agent-to-service form: many general agents access the same external data and tools through one key, metered billing, provider selection, and reusable integrations.

Both forms depend on more than a catalog. Identity, permission, payment, verification, reputation, task fit, sandboxing, and portable state determine whether an agent can safely buy or use anything. The practical near-term market may therefore resemble API and tool aggregation before autonomous agents trade rich identities or memories with one another.

## Key Claims

- Marketplace value comes from differentiated context, data, skills, tools, workflow history, or provider quality rather than access to the same base model alone.
- Agent-to-service aggregation is a nearer-term form than fully autonomous agent-to-agent commerce.
- A useful market needs identity, permission, payment, observability, verification, reputation, and sandbox boundaries for nonhuman operators.
- Cross-harness portability can reduce integration and switching costs when users move between general agents.
- Usage-based billing fits heterogeneous tool demand but exposes customers and intermediaries to cost, quality, and abuse-management problems.
- Agent feedback can improve routing only if task labels, evaluation signals, privacy protections, and resistance to manipulation are adequate.
- Marketplace network effects remain hypothetical until agents complete valuable work often enough for selection data, reputation, or accumulated context to compound.

## Evidence

### Agent-to-agent exchange
- [[142-yusen-de-chuangtou-guancha-di-2-ji-harness-xia-yige-zijie-2026-da-jihui-he-stanley-druckenmiller-lg4sphlaunrjuulqraxs-1gc5ufz]] proposes agents hiring or assisting one another because their context, skills, and experience differ.
- [[yong-agent-donglixue-he-40-ge-agents-yiqi-wei-ren-ai-zuo-chanpin-duitan-slock-ai-chuangshiren-rc-liiv-fkcdolfb06hkoyz0ix3fejy]] frames adoption as potentially forking an agent's memory and collaboration history rather than downloading a static app.

### Agent-facing tool and data aggregation
- [[xin-de-chuangye-jihui-zhengzai-claude-code-he-codex-zhouwei-zhang-chulai-duitan-treg-lsjeudluybigsxwwu9v-u2kurpsm]] describes Trigg's one-key, usage-metered access to multiple data suppliers, APIs, and media models across harnesses.

### Selection and governance
- [[xin-de-chuangye-jihui-zhengzai-claude-code-he-codex-zhouwei-zhang-chulai-duitan-treg-lsjeudluybigsxwwu9v-u2kurpsm]] proposes agent feedback and task-level provider scoring.
- [[142-yusen-de-chuangtou-guancha-di-2-ji-harness-xia-yige-zijie-2026-da-jihui-he-stanley-druckenmiller-lg4sphlaunrjuulqraxs-1gc5ufz]] and [[yong-agent-donglixue-he-40-ge-agents-yiqi-wei-ren-ai-zuo-chanpin-duitan-slock-ai-chuangshiren-rc-liiv-fkcdolfb06hkoyz0ix3fejy]] make persistent identity, permission, shared state, and task ownership prerequisites for richer exchange.

## Counterevidence & Qualifications

The agent-to-agent market remains speculative, and Trigg's tool market was only weeks old in the source. No bounded evidence establishes liquidity, durable network effects, neutral routing, supplier quality, switching-cost reduction, or favorable unit economics. Aggregators may be bypassed by model providers or suppliers, while shared credentials and cross-platform access enlarge the security surface. Feedback from agents is not automatically ground truth: models can share failure modes, optimize for the wrong proxy, or be influenced by provider output.

## What Changed

- Expanded the concept from agent-to-agent exchange to include agent-facing data, API, and tool aggregation.
- Distinguished a near-term service marketplace from a richer market in forkable agent context and memory.
- Added portability, metered billing, routing feedback, and supplier-neutrality qualifications.
- Migrated the full three-source synthesis to `synthesis-v1`.

## Related Concepts

- [[AgenticEconomy]] - broader economic system in which agents transact and perform work.
- [[AgentHarness]] - supplies persistent state, tools, permissions, and execution context.
- [[AgentFacingInterfaces]] - exposes services in forms agents can discover and call.
- [[AgentIdentityAndAuthentication]] - attributes marketplace action to an accountable operator.
- [[AgentPermissionBoundaries]] - limits what an agent may buy, disclose, or execute.
- [[AgenticCommerce]] - transaction layer for agent-mediated purchasing.
- [[ModelWorkflowFit]] - routes tasks toward tools or models suited to the work.
