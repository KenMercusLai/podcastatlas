---
title: "E249｜Token经济转点：OpenClaw、Hermes到本地自研的Agent进化之路"
type: source
tags: [podcast, ai, agents, token-economics]
sources: []
date: 2026-08-20
source_file: "/home/ken/repos/podcastatlas/content/episodes/E249｜Token经济转点：OpenClaw、Hermes到本地自研的Agent进化之路 [6242033d-a14a-44e3-a622-cbfc7d3c3817].md"
source_url: "https://www.sv101.net/262"
last_updated: 2026-08-24
---

# E249｜Token经济转点：OpenClaw、Hermes到本地自研的Agent进化之路

## Summary

This [[SiliconValley101|硅谷101]] episode with [[Dongxu|黄东旭]] and [[ZhangHongjiang|张宏江]] frames AI-agent adoption as moving from [[TokenMaxxing|token maxing]] toward [[TokenEfficientAgentWorkflow|token efficient agent workflow]]. The discussion uses [[OpenClaw]], [[HermesAgent]], [[SlockAI|Slock/Raft]], local [[DeepSeek]] models, and frontier models such as [[Fable5]] and [[GLM52|GLM 5.2]] to argue that useful agent systems need model routing, memory, skills, permissions, observability, and human acceptance rather than raw token burn alone.

## Key Claims

- AI infrastructure is still early in the speakers' view: token prices are falling quickly, usage is rising, and [[JevonsParadoxInAI]] may keep total demand growing even as single-task efficiency improves.
- [[Dongxu]] describes earlier [[TokenMaxxing]] as rational for high-value, uncertain software work, citing [[DB9]] as a case where hundreds of dollars per day in model spend could still be cheap if it produced a valuable database system.
- [[OpenClaw]] is framed as an important accessible-agent threshold: open source, local-first deployment, and tool-loop packaging made agents legible to ordinary users, but memory, stability, configuration, and long-term maintainability remained weak.
- [[HermesAgent]] is presented as a more polished middle-use agent whose key contribution is turning successful work traces into reusable [[AISkills]], not magically solving memory.
- [[SlockAI|Slock/Raft]] shows the usefulness and cost of [[MultiAgentCollaboration]]: multiple agents can review software projects more thoroughly than one model pass, but may spend many times more tokens.
- The episode's practical answer is not "always use the strongest model" or "always use local models"; it is [[ModelRoutingCostControl]] across frontier cloud models, cheaper open models, local execution, deterministic tools, and human review.
- Local models can change user behavior by turning marginal model cost into something closer to fixed infrastructure cost, making batch summarization, memory cleaning, and repetitive agent work psychologically easier to attempt.
- Agent workflows naturally consume many tokens because an [[AgentHarness]] repeatedly calls models, tools, context, memory, and verification loops during long tasks.
- The agent-native startup opportunity is strongest where removing the agent would remove the product's reason to exist; infrastructure, memory, search, sandboxing, collaboration harnesses, and "agent cloud" are treated as more timely than many thin end-user apps.
- Granting agents more autonomy requires stronger [[AgentPermissionBoundaries]], [[AgentRuntimeExecutionLayer|runtime execution layers]], backup, sandboxing, logging, and recovery because agents can produce creative surprises and destructive mistakes.

## Key Quotes

> "从 token maxing 到 token efficient" — the episode's opening shift in AI-agent economics.

> "2025 年可被视作 Agent 元年" — the source's framing of agent adoption timing.

> "记忆问题至今仍是 open question" — Dongxu's boundary around current persistent-memory quality.

## Connections

- [[SiliconValley101]] — podcast/show context for the episode.
- [[Dongxu]], [[PingCAP]], [[LamaVentures]], and [[DB9]] — engineering and founder-investor lens behind the token-cost examples.
- [[ZhangHongjiang]] and [[LamaVentures]] — technology-cycle and venture-ecosystem lens.
- [[OpenClaw]], [[HermesAgent]], and [[SlockAI|Slock/Raft]] — product sequence used to compare personal agents, skill-oriented agents, and multi-agent collaboration.
- [[TokenMaxxing]], [[TokenEfficientAgentWorkflow]], [[AIInferenceCostStructure]], and [[ModelRoutingCostControl]] — central economic concepts.
- [[AgentHarness]], [[PersistentAgentMemory]], [[AISkills]], [[AgentSelfEvolution]], [[LocalAgentExecution]], and [[MultiAgentCollaboration]] — agent-engineering stack discussed throughout the episode.
- [[AgentNativeSoftware]], [[AIManagingAI]], [[AIOrganizationDesign]], and [[HumanAgencyUnderAI]] — organizational and human-work implications.
- [[DeepSeek]], [[Fable5]], [[GLM52|GLM 5.2]], [[OpenSourceAIModels]], and [[ClaudeCode]] — model and tool references used in the routing discussion.
- [[AgentPermissionBoundaries]] and [[AgentRuntimeExecutionLayer]] — safety and recoverability requirements raised by agent mistakes and production access.

## Contradictions

- No direct contradiction with prior wiki content found. Some source-mentioned model/product names, especially the transcribed "Fable/Fybe 5" wording and "DeepSeek V4 Flash", remain source-scoped because the episode summary itself flags possible ASR naming uncertainty.
