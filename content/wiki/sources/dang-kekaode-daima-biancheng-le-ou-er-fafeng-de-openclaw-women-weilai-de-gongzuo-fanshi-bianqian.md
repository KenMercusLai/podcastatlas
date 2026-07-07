---
title: "当可靠的代码变成了偶尔发疯的OpenClaw，我们未来的工作范式变迁"
type: source
tags: [podcast, ai, agents, openclaw, safety, workflow]
sources: []
date: 2026-02-12
source_file: "/home/ken/repos/podcastatlas/content/episodes/当可靠的代码变成了偶尔发疯的OpenClaw，我们未来的工作范式变迁 ｜ 科技乱炖⧸急中生智⧸拼娃时代⧸其他 (1) [当可靠的代码变成了偶尔发疯的openclaw，我们未来的工-1].md"
source_url: "https://hosting.wavpub.cn/dao-sub/2026/02/12/%e5%bd%93%e5%8f%af%e9%9d%a0%e7%9a%84%e4%bb%a3%e7%a0%81%e5%8f%98%e6%88%90%e4%ba%86%e5%81%b6%e5%b0%94%e5%8f%91%e7%96%af%e7%9a%84openclaw%ef%bc%8c%e6%88%91%e4%bb%ac%e6%9c%aa%e6%9d%a5%e7%9a%84%e5%b7%a5/"
last_updated: 2026-07-08
---

## Summary
This [[KejiLuandun]] episode uses hands-on [[OpenClaw]] deployment to argue that AI agents change software from a predictable command executor into a probabilistic coworker with local files, accounts, browsers, memory, skills, and unsafe edge cases. The hosts connect Mac mini deployment, high remote-model cost, [[Kimi]] routing, scheduled-task drift, prompt injection, memory lock-in, MCP-style platform access, and AI coding into a broader shift from "by you" computer use toward "with you" agent management. Its main wiki contribution is [[ProbabilisticSoftware]]: useful agent systems need bounded permissions, recoverable harnesses, deterministic subtools, verification, and human judgment because local autonomy amplifies both capability and failure.

## Key Claims
- [[OpenClaw]] is useful for low-risk, one-off, human-reviewed tasks such as checking flights or sorting information, but the episode is skeptical of letting it run unattended deterministic routines after seeing scheduled workflows and configuration files drift.
- [[LocalAgentExecution]] is the attraction and the danger: the agent can use local browser state, logged-in accounts, files, iCloud-like data, and password-manager plugins in ways cloud agents usually cannot.
- Open source does not remove the core risk because the underlying model can still misunderstand, hallucinate, mutate its own environment, or follow injected instructions from a webpage or third-party skill.
- Docker or a virtualized environment is only a partial boundary if the user mounts important directories, tokens, accounts, or outbound network access into the agent's workspace.
- The work pattern shifts from reliable software operated "by you" to uncertain collaboration "with you": the user writes clearer tasks, maintains memory and [[AISkills]], gives feedback, reviews output, and manages agents like digital employees.
- [[ClaudeCode]]-style memory files and reusable skills show how advanced users may "train" agents through project norms, testing methods, product-design routines, and post-task experience updates.
- Enterprise agents will likely remain closer to fixed, auditable processes with selected skills than to fully autonomous personal agents because companies need reproducibility and control.
- MCP-like access could become an AI-era service interface: if platforms such as [[Meituan]] expose callable ordering or local-service actions, assistants such as [[Doubao]] or [[Yuanbao]] can route demand to them; if they do not, they may become less visible in AI workflows.
- AI service entry can reduce browsing and shift choice power to the assistant, as in the hosts' milk-tea example where the user sees fewer options than in the traditional app interface.
- Good AI interaction should include clarification and triage, not only execution; the hosts contrast a medical-style assistant that asks follow-up questions with tools that mechanically complete a vague request.
- Persistent memory can become user lock-in because accumulated conversations, preferences, and task habits make switching agents costly; the hosts also speculate about a third-party "one memory" layer.
- AI coding makes one-off utilities easier, such as a Markdown-to-Word HTML tool, but debugging, answer checking, context loss, and repeated bug regressions keep [[AICodingVerification]] and engineering structure central.
- The hosts warn of skill discontinuity: if future code is generated from scratch by agents, fewer people may develop the architecture, reading, and low-level practice that later expert review requires.
- Practical safety advice is to experiment on an isolated device, grant only narrow directories, avoid credit cards and high-risk accounts, and stop exposed services after use.

## Key Quotes
> "可靠的代码变成了偶尔发疯的OpenClaw" — the episode's core metaphor for AI-driven software.

> "by you" / "with you" — the hosts' contrast between tool operation and agent collaboration.

> "基模、应用、技能、数据" — the product stack the hosts use to describe future AI competition.

## Connections
- [[OpenClaw]] — central local-agent case.
- [[ProbabilisticSoftware]] — concept added by this source for uncertain agent-mediated software behavior.
- [[LocalAgentExecution]] and [[AgentPermissionBoundaries]] — local data access, password-manager exposure, Docker limits, and least-permission guidance.
- [[AgentHarness]], [[PersistentAgentMemory]], and [[AISkills]] — memory files, skills, task feedback, and recoverable execution loops.
- [[HumanAgentCollaboration]] and [[HumanJudgmentUnderAI]] — "with you" agent management, clarification, and final responsibility.
- [[AICodingVerification]], [[VibeCoding]], and [[AIEngineeringThinking]] — temporary tool building, context loss, debugging, and skill-transfer concerns.
- [[ModelRoutingCostControl]], [[ModelWorkflowFit]], and [[Kimi]] — high remote-model cost and cheaper model routing in hands-on OpenClaw use.
- [[ModelContextProtocol]], [[AgentFacingInterfaces]], and [[AIAssistantServiceEntry]] — platform visibility and service-fulfillment interfaces.
- [[AgenticCommerce]], [[Meituan]], [[Doubao]], and [[Yuanbao]] — milk-tea ordering, AI recommendation power, and platform incentive questions.
- [[MiniMax]] — low-friction HTML deployment example where platform safety checks modified generated scripts.

## Contradictions
- No direct contradiction with prior wiki content. The source reinforces existing [[OpenClaw]], [[AgentPermissionBoundaries]], [[LocalAgentExecution]], [[PersistentAgentMemory]], [[AISkills]], and [[AICodingVerification]] themes.
- It qualifies optimistic OpenClaw readings by stressing that local autonomy is still poorly suited to unattended, high-impact, or enterprise-deterministic work unless the surrounding harness, permissions, testing, and audit surfaces improve.
- It also adds tension to agentic-commerce enthusiasm: assistant-led ordering can lower friction, but it may also reduce user choice visibility and shift distribution power toward whichever assistant or platform controls recommendations.
