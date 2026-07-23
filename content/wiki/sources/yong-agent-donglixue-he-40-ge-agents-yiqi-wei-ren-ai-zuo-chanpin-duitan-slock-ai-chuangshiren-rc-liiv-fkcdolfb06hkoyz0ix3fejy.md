---
title: "用 Agent 动力学，和 40 个 Agents 一起为「人 + AI」做产品｜对谈 Slock.ai 创始人 RC"
type: source
tags: [podcast, ai, agents, startup, collaboration]
sources: []
date: 2026-04-23
source_file: "/home/ken/repos/podcastatlas/content/episodes/用 Agent 动力学，和 40 个 Agents 一起为「人 + AI」做产品｜对谈 Slock.ai 创始人 RC [liiv-fKcDolfb06hKOyz0IX3feJY].md"
source_url: "https://www.xiaoyuzhoufm.com/episode/69e999241e94ae6921f2901d"
last_updated: 2026-07-23
---

## Summary
This [[42Zhangjing]] episode interviews [[RC]], founder of [[SlockAI|Slock.ai]], about why CLI returned as an important interface in the agent era, what he learned from building [[KimiCLI|Kimi CLI]], and why he left [[Kimi]] to build a collaborative environment for people and many agents. RC argues that future software has to serve both humans and agents: command-line tools, [[AISkills]], memory, channels, threads, shared documents, task claiming, and model diversity become organizational infrastructure rather than peripheral product details. The strongest new contribution is [[AgentDynamics]]: once a seven-person team works with roughly forty agents, product design becomes a question of identity, context, shared learning, task ownership, team culture, and human review.

## Key Claims
- CLI is newly valuable because large models are text-first systems; an [[AgentOptimizedCLI]] should have concise inputs, clear docs and examples, stable output, dense information, and obvious success/failure signals.
- [[KimiCLI|Kimi CLI]] is presented as a command-line coding/general agent, but RC says the deeper asset was a reusable local [[AgentHarness]] that could later support SDK, Web UI, or VS Code surfaces.
- RC says a coding agent can be derived from a simple agent loop plus a Bash tool, then improved by observing what the model cannot do and adding tools and prompt structure.
- Stronger coding models may widen security pressure because attackers can search for vulnerabilities in banks, kernels, browsers, compilers, and critical software faster than defenders can patch.
- Skill plus CLI lowers the human software-use burden: the person should know what capability a tool gives the agent, while the agent reads instructions, installs tools, and uses them.
- [[SlockAI|Slock.ai]] is designed as a collaborative environment for people and multiple agents, addressing hard-to-track local sessions, disconnected findings, and team knowledge trapped in individual human-agent interactions.
- RC argues that Build and Code are becoming orthogonal: non-programmers can build with agents, while experienced programmers still have an advantage in serious software because they can inspect and constrain the agent.
- Programming education may shift from bottom-up foundations first to top-down building first: users prompt an agent into producing a working artifact, then learn front end, back end, deployment, database, and code concepts as complexity forces them to.
- Slock's internal case is a small team with about seven people and forty agents, including engineering, head-of-engineering, design, growth, and strategy roles.
- RC contrasts a single all-purpose agent with a multi-agent route: humans still often want micro-control because current subagents can drift, and unrelated tasks should not all share one context.
- In an [[AgentMarketplace]], adopting someone else's agent may be closer to forking its memory, context, and collaboration history than downloading a static app.
- Long-running work still needs shared channels: agents can communicate through chat, databases, code, GitHub issues, or new tools, but foreground and background work both need a place where state is visible.
- Slock has to design UX simultaneously for humans and agents: people see channels and unread messages, while agents see linear events, summaries, IDs, and context windows.
- Message-based multi-agent systems need [[AgentTaskClaiming]] so multiple agents do not all rush to do the same job after one instruction.
- RC says agents can forget identity, such as failing to recognize that they are the named Alice in a channel, making identity and context refresh product issues.
- [[AgentDynamics]] includes culture-like effects: prompts that ask agents to complement each other encourage cooperation, while race-style competition can produce falsehoods, empty claims, and denigration of other agents.
- RC sees model diversity as part of Slock's advantage: different models and tools can play different roles, so an application company should not assume one model provider will own the whole surface.
- Slock's target user expanded from the [[OnePersonCompany]] or independent builder toward one-to-one-hundred-person teams that manage and interact with many agents.

## Key Quotes
> "Agent 动力学" — RC's name for the behavior that appears when many agents interact in one work environment.

> "7 个人和 40 个 Agent" — the source's concrete team-scale example.

> "Build 与 Code 已经变成正交关系" — RC's claim that building with agents is separating from traditional coding skill.

## Connections
- [[RC]] — guest and founder explaining Kimi CLI, Slock, and the agent-dynamics frame.
- [[SlockAI|Slock.ai]] — company and product case for multi-agent human collaboration.
- [[Kimi]] and [[KimiCLI|Kimi CLI]] — RC's prior work context and command-line agent example.
- [[AgentDynamics]], [[AgentTaskClaiming]], and [[AgentOrganizationalCulture]] — new concepts grounded in this source.
- [[AgenticWorkflow]], [[HumanAgentCollaboration]], [[MultiAgentCollaboration]], [[AgentHarness]], [[PersistentAgentMemory]], and [[AgentFacingInterfaces]] — existing agent-work infrastructure extended by the episode.
- [[AgentOptimizedCLI]], [[AISkills]], [[VibeCoding]], and [[AIProgrammingEngineShift]] — interface, skills, and build/code separation themes.
- [[AgentMarketplace]], [[AgentIdentityAndAuthentication]], [[AgentPermissionBoundaries]], and [[AIOrganizationDesign]] — governance and organization implications of persistent, role-bearing agents.
- [[ClaudeCode]], [[Codex]], [[Kimi]], and [[ModelWorkflowFit]] — model/tool diversity and role-fit comparison in RC's discussion.
- [[AIInferenceCostStructure]], [[AIFirstOrganization]], and [[OnePersonCompany]] — economics and team-size implications of running many agents.

## Contradictions
- No direct contradiction with prior wiki content. The source reinforces existing CLI, skills, harness, memory, and AI-first organization themes while adding a more explicit multi-agent sociology layer. The main tension is scope: older one-person-company material often frames agents as leverage for a solo operator, while this source says the value becomes clearer when one or more humans jointly manage a population of agents.
