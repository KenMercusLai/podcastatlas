---
title: "Slock.ai / Slock AI"
type: entity
tags: [ai-tool, startup, agents, collaboration]
sources: [e249-token-jingji-zhuandian-openclaw-hermes-dao-bendi-ziyan-de-agent-jinhua-zhi-lu-6242033d-a14a-44e3-a622-cbfc7d3c3817, yong-agent-donglixue-he-40-ge-agents-yiqi-wei-ren-ai-zuo-chanpin-duitan-slock-ai-chuangshiren-rc-liiv-fkcdolfb06hkoyz0ix3fejy]
last_updated: 2026-08-24
---

# Slock.ai / Slock AI

Slock.ai is the multi-agent collaboration product founded by [[RC]] and discussed in [[yong-agent-donglixue-he-40-ge-agents-yiqi-wei-ren-ai-zuo-chanpin-duitan-slock-ai-chuangshiren-rc-liiv-fkcdolfb06hkoyz0ix3fejy]]. RC describes it as an environment where people and many agents can work together through channels, threads, shared documents, tasks, memory, and role-specific agent sessions.

[[e249-token-jingji-zhuandian-openclaw-hermes-dao-bendi-ziyan-de-agent-jinhua-zhi-lu-6242033d-a14a-44e3-a622-cbfc7d3c3817]] adds that Slock later appears in the source under the name Raft. [[Dongxu]] uses it for complex software-project review by putting multiple agents into a shared discussion so they can challenge and supplement one another, which strengthens the page's [[MultiAgentCollaboration]] theme while adding a cost boundary: the review can reveal issues a one-shot model pass misses, but may consume many times more tokens.

The product starts from a practical workflow pain: local agent sessions are hard to manage when many are running at once, progress is hard to inspect, and useful conclusions from one session do not automatically transfer to another. Slock's answer is not only more automation; it tries to make the workspace itself legible to humans and to agents, so a user or team can see what is happening while agents see enough context, event history, and summaries to continue work.

The source also presents Slock as its own operating case. RC says the company runs financing, research, growth, and development inside Slock, with about seven people and forty agents. That makes Slock a concrete example of [[AIOrganizationDesign]] where headcount, token budget, agent roles, human review, and culture-like multi-agent behavior all have to be managed together.

## Product Position
- Slock targets people or teams managing multiple agents, not only a single assistant session.
- Its intended audience expanded from [[OnePersonCompany]] and independent builders toward one-to-one-hundred-person teams.
- It treats model diversity as a feature: different agents and models can play different roles, and an application layer can support many providers rather than collapse into one model vendor's interface.
- Its hard design problem is dual UX: humans need channels, tasks, progress, unread states, and review surfaces; agents need linear events, IDs, summaries, memory, and actionable context.

## Connections
- [[RC]] — founder and source speaker.
- [[AgentDynamics]] — term RC uses for emergent multi-agent behavior.
- [[AgentTaskClaiming]] — task ownership mechanism Slock needs in message-based multi-agent work.
- [[AgentOrganizationalCulture]] — culture-like behavior that can emerge from prompt norms and agent interaction.
- [[MultiAgentCollaboration]], [[HumanAgentCollaboration]], [[AgenticWorkflow]], and [[PersistentAgentMemory]] — work patterns Slock tries to make operational.
- [[AgentHarness]], [[AgentFacingInterfaces]], [[AgentMarketplace]], and [[AgentIdentityAndAuthentication]] — infrastructure and governance layers implied by the product.
- [[KimiCLI]], [[Kimi]], [[ClaudeCode]], and [[Codex]] — prior work and model/tool references in the episode.
- [[Dongxu]], [[TokenEfficientAgentWorkflow]], and [[AIInferenceCostStructure]] — E249's Slock/Raft review workflow and token-cost boundary.
