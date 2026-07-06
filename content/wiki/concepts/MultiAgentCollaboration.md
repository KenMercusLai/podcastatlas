---
title: "Multi-Agent Collaboration"
type: concept
tags: [agents, collaboration, verification]
sources: [dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd]
last_updated: 2026-07-06
---

# Multi-Agent Collaboration

Multi-agent collaboration is the use of multiple agents to exchange context, review each other, explore alternatives, and recover from drift in long tasks. In [[dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd]], the [[MiniMax]] guests argue that two models can exchange far more context than a human normally provides and can cross-check each other when a single long-context agent starts moving down a wrong path.

## Key Claims
- Multi-agent work is not only role-play; it can be review, adversarial checking, parallel exploration, and handoff.
- It helps with long-horizon tasks where one agent's context window grows stale or overcommitted to a bad plan.
- It requires [[AgentHarness]] governance so each agent has appropriate tools, permissions, information boundaries, and goals.
- It overlaps with [[SubagentWorkflow]], but the source emphasizes peer checking and high-bandwidth model-to-model context exchange.

## Connections
- [[SubagentWorkflow]] — related pattern for background delegation and synthesis.
- [[AgenticWorkflow]] — broader task-completion pattern where multiple agents may be useful.
- [[AgentHarness]] — orchestration and permission layer needed for safe collaboration.
- [[MiniMax]], [[Adao]], and [[Zeying]] — source context for the cross-checking claim.
- [[AICodingVerification]] — adjacent area where independent review agents may reduce unchecked generation risk.
