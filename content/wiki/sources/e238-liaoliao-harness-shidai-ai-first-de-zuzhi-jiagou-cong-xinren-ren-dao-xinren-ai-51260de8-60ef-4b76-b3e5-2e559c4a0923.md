---
title: "E238｜聊聊Harness时代AI-First的组织架构：从信任人到信任AI"
type: source
tags: [podcast, ai, agents, ai-first, organization-design, software-engineering]
sources: []
date: 2026-05-25
source_file: "/home/ken/repos/podcastatlas/content/episodes/E238｜聊聊Harness时代AI-First的组织架构：从信任人到信任AI [51260de8-60ef-4b76-b3e5-2e559c4a0923].md"
source_url: "https://sv101.fireside.fm/251"
duration: "3921"
last_updated: 2026-07-23
---

# E238｜聊聊Harness时代AI-First的组织架构：从信任人到信任AI

## Summary
This [[SiliconValley101]] episode interviews [[PeterCreo|Peter]], [[ChenKaiCreo|陈凯]], and [[ClarkCreo|Clark]] of [[Creo]] about [[HarnessEngineering]] and [[AIFirstOrganization|AI-first organization design]]. The discussion argues that the next step after prompt and [[ContextEngineering]] is not only better instructions, but an [[AgentHarness]] that lets agents run through real workflows, collect feedback, repair failures, and improve. Its strongest synthesis is organizational: [[Creo]] frames AI-first work as moving from people using AI tools toward AI driving production while humans provide architecture, value definition, judgment, and review.

## Key Claims
- [[PeterCreo|Peter]] defines [[HarnessEngineering]] as a dynamic system problem around tooling, sandbox architecture, host-service interaction, security, startup time, latency, feedback, self-healing, and self-improvement.
- The episode distinguishes [[AIFirstOrganization|AI-first organization design]] from ordinary AI tool adoption: [[ChenKaiCreo|陈凯]] says workflows and organization form have to be rebuilt around AI capability rather than adding AI on top of old handoffs.
- [[Creo]] says its roughly 25-person company has 99% of code written by AI and can move from feature idea to A/B testing and rewrite within a day; this is a source-scoped internal estimate, not a general industry benchmark.
- Faster implementation shifts the bottleneck from engineering delivery toward product choice, testing, quality control, market readiness, and go-to-market narrative.
- [[PeterCreo|Peter]] describes agent-driven CICD, agent-driven bug triage, and low-risk autofixing PRs where different agents identify, assign, and repair frontend, backend, or agent-system issues.
- The episode treats [[AICodingVerification]] as a harness function: Playwright checks, AI-driven integration tests, rollout/fallback decisions, and human proof sit inside the production loop rather than after code generation.
- [[ClarkCreo|Clark]] says go-to-market work is harder to evaluate than engineering because it faces humans and agents, and because market readiness remains a judgment call even when agents generate many candidate outputs.
- The source argues that products may increasingly be consumed by agents, not only by humans, so SaaS value can move toward APIs, MCP-like access, permissions, and data structures that agents can inspect and prioritize.
- [[ChenKaiCreo|陈凯]] frames organization redesign as a trust shift: companies have to decide when they can trust AI to plan, execute, and make recommendations, then build guardrails that make that trust auditable.
- The guests argue that product-manager, engineer, designer, and marketer boundaries blur when AI absorbs implementation and coordination; generalists with architecture, product sense, implementation ability, and market judgment become more valuable.
- The episode keeps humans in the loop at a higher level: architecture, security and latency judgment, value definition, demand direction, final review, and ethical boundaries remain human responsibilities.

## Key Quotes
> "99% 的代码由 AI 写" - Peter's description of Creo's internal engineering workflow.

> "AI drive 公司方向和日常工作方式" - Chen Kai's AI-first organization definition.

> "2026 年自己没有写过一行代码" - Peter's personal coding-role claim.

## Connections
- [[SiliconValley101]] - show context for the episode.
- [[Creo]], [[PeterCreo|Peter]], [[ChenKaiCreo|陈凯]], and [[ClarkCreo|Clark]] - company and guests grounding the organization experiment.
- [[HarnessEngineering]], [[AgentHarness]], [[ContextEngineering]], [[AgenticWorkflow]], and [[ModelHarnessCoEvolution]] - technical frame around moving from prompt/context work to dynamic agent systems.
- [[AIFirstOrganization]], [[AIOrganizationDesign]], [[HumanAgentCollaboration]], [[HumanJudgmentUnderAI]], and [[DigitalEmployees]] - organization and human-role branch.
- [[AICodingVerification]], [[AgentPermissionBoundaries]], [[AgentIdentityAndAuthentication]], and [[EnterpriseAgentGovernance]] - verification, permission, and production-governance branch.
- [[AgentFacingInterfaces]], [[OrganizationalContext]], [[AICoworkers]], and [[GeneratedWorkInterfaces]] - product and workspace implications when agents become users and coworkers.

## Contradictions
- No direct contradiction found.
- The source qualifies [[AgentHarness]] by emphasizing dynamic self-improvement and organization feedback, not only a static wrapper around tools and memory.
- The source qualifies [[AICodingVerification]] by showing a high-AI-code workflow that still depends on architecture, tests, rollout metrics, human proof, and permission boundaries.
- The efficiency claims are [[Creo]] self-reports and should not be generalized to regulated enterprises, large legacy organizations, or nontechnical teams without additional sources.
