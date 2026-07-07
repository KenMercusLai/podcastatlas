---
title: "Vol. 160 一年多以后，再聊AI写代码Vibe Coding"
type: source
tags: [podcast, ai, ai-coding, vibe-coding, agents]
sources: []
date: 2026-02-01
source_file: "/home/ken/repos/podcastatlas/content/episodes/Vol. 160 一年多以后，再聊AI写代码Vibe Coding (1) [6623-1].md"
source_url: "https://justinyan.me/post/6623"
last_updated: 2026-07-07
---

## Summary
This [[FengyanFengyu]] episode by [[JustinYan]] and [[Zili]] revisits [[VibeCoding]] roughly a year after the hosts first discussed AI-assisted programming. It uses [[NewSpot]], Justin's AI-assisted tech-news product, to show how coding agents moved from supervised [[Cursor]]-style workflows toward [[ClaudeCode]], [[Codex]], [[Gemini]], YOLO execution, long task loops, and multi-agent supervision. The main synthesis is that AI now deeply changes coding, search, content production, and solo product building, but it remains a tool that amplifies judgment rather than a wish-granting substitute for product taste, tests, debugging, permissions, or final acceptance.

## Key Claims
- The year-over-year shift in [[VibeCoding]] is from strong human supervision toward command-line [[AgenticWorkflow]] patterns where agents can execute commands, loop over failures, and run in parallel windows.
- YOLO-style coding-agent permissions raise the value of [[AgentPermissionBoundaries]] because the risk is no longer only bad code; agents may touch local files, cloud services, email, servers, payment accounts, or financial accounts.
- The hosts define an agent pragmatically as an LLM repeatedly using tools to achieve a goal, making [[AgentHarness]], tool feedback, and verification loops more important than a fixed UI.
- [[ClaudeCode]] is presented as the practical breakthrough that made command-line coding agents feel useful, while [[Cursor]], [[Codex]], [[Gemini]], and open or domestic models still differ by [[ModelWorkflowFit]].
- AI search is becoming a default entry point for many users, but the episode warns that one synthesized answer can be wrong and that AI-answer surfaces invite new [[GenerativeEngineOptimization]], [[AIDiscoverySEO]], and content-pollution behavior.
- [[NewSpot]] crawls technology news, lets models score items, and turns filtered stories into a public product, but Justin argues that "99.99% AI-written code" is not itself a customer-facing value proposition.
- The productization boundary is [[AIEngineeringThinking]]: useful AI coding depends on plan review, architecture judgment, tests, final workflow acceptance, and knowing when to rewrite or debug a core module.
- [[AICodingVerification]] matters more as code generation becomes cheap; the source emphasizes test plans, TDD-like workflows, code review, final online tests, and watching for AI that changes tests merely to pass.
- Non-programmers can now build useful small tools through [[VibeCoding]], but beginners are also more exposed because they may not recognize plausible but broken architecture, security, or edge-case behavior.
- The episode frames AI as an ability amplifier: a stronger programmer, product thinker, or creator can use it to do more, while weak problem definition and weak judgment still produce weak results.
- AI-generated content is becoming easier to recognize and discount, so [[HumanJudgmentUnderAI]], personal bias, editorial voice, and deliberate human-written pieces become part of product value.
- Natural language becomes a production interface; [[AICommunicationAbility]], voice input, English practice, and clear acceptance criteria become part of the user's effective toolchain.
- Heavy subscriptions, open-source models such as [[Qwen]], [[MiniMax]], [[GLM52]], and [[DeepSeek]], and long-running agents make [[AIInferenceCostStructure]] and [[ModelRoutingCostControl]] everyday workflow issues.
- The closing caution is behavioral: AI's speed and quota pressure can pull users into overwork, so the human still has to choose when to slow down and decide what is actually worth building.

## Key Quotes
> "99.99% AI 写代码" — context for [[NewSpot]], but not treated as the product's real selling point.

> "不是许愿池" — the episode's boundary between using natural language as input and treating AI as magic.

> "慢下来" — the closing reminder that faster agents do not decide what deserves attention.

## Connections
- [[FengyanFengyu]], [[JustinYan]], and [[Zili]] — show and host context.
- [[NewSpot]] — concrete product case for AI-assisted news screening, AI-coded implementation, final tests, and human editorial bias.
- [[VibeCoding]], [[AIEngineeringThinking]], and [[AICodingVerification]] — central coding workflow and productization boundary.
- [[ClaudeCode]], [[Cursor]], [[Codex]], [[Gemini]], [[Qwen]], [[MiniMax]], [[GLM52]], and [[DeepSeek]] — model and tool landscape discussed through practical fit, cost, and adoption.
- [[AgentPermissionBoundaries]], [[AgenticWorkflow]], [[AgentHarness]], and [[RoutineAgentAutomation]] — long-running, multi-window, remote, and scheduled agent work patterns.
- [[GenerativeEngineOptimization]], [[AIDiscoverySEO]], and [[AIContentDevaluation]] — AI search, content manipulation, and human-authored content value.
- [[HumanJudgmentUnderAI]], [[AICommunicationAbility]], and [[ModelWorkflowFit]] — human-side capabilities that decide whether model progress becomes useful work.

## Contradictions
- No direct contradiction with existing wiki content. The source reinforces earlier [[VibeCoding]], [[AgentPermissionBoundaries]], [[AIEngineeringThinking]], [[AICodingVerification]], [[AICommunicationAbility]], and [[HumanJudgmentUnderAI]] pages while adding a more mature 2025-era workflow snapshot centered on [[NewSpot]], YOLO permissions, AI search pollution, and the need to slow down.
