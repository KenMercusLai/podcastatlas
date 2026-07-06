---
title: "探秘 Claude Code，搞懂 Agent Harness｜对谈来新璐"
type: source
tags: [podcast, ai, agents, infrastructure, coding]
sources: []
date: 2026-05-05
source_file: "/home/ken/repos/podcastatlas/content/episodes/探秘 Claude Code，搞懂 Agent Harness｜对谈来新璐 [lklUK3i7C4Gzw4jvxeE7ODSFGiS3].md"
source_url: "https://www.xiaoyuzhoufm.com/episode/69f2e83fbb3ffa11e59dec82"
last_updated: 2026-07-06
---

## Summary
This [[ShizilukouCrossing]] episode interviews [[LaiXinlu]] of [[ShareAI]] about [[AgentHarness]] design, using [[ClaudeCode]] and [[LearnClaudeCode]] as the main teaching sample. Lai defines harness as the model-external system that gives an agent execution ability, context, state, memory, permissions, and orchestration. The discussion argues for model-aligned harness design: stronger models should get more context and action capacity with less brittle programmatic control, and CLI/Unix-like interfaces may be more agent-native than prompt-node or flow-graph frameworks.

## Key Claims
- [[AgentHarness]] can be understood as "everything outside the model": tools, runtime environment, context, state, memory, permissions, and multi-agent governance.
- Lai breaks harness design into three layers: execution ability, context/environment, and governance/orchestration.
- The execution layer includes files, search, browser operation, language interpreters, CLI tools, code-registered tools, and MCP-like extensions, but the episode argues that CLI often outperforms newer abstractions because models have more pretraining exposure to Unix and shell patterns.
- The context/environment layer includes system prompts, [[AISkills]], [[PersistentAgentMemory]], context-window management, compression, and cross-agent handoff documents.
- The governance/orchestration layer controls multi-agent roles, information access, and permissions, such as giving exploration agents read-only capabilities so they cannot mutate code or tests.
- [[ClaudeCode]] is presented as an especially instructive harness because of its memory update hooks, AutoDream-like consolidation, markdown memory files, context compression, and task handoff mechanisms.
- Good harnesses should fit the model's operating logic and remain orthogonal to model improvement; a harness that over-controls the model may become a bottleneck as models improve.
- [[KComputer]] represents [[ShareAI]]'s lightweight Unix-style approach: a virtual computer built as data structures rather than a traditional Docker-like sandbox.
- The entrepreneurial direction extends beyond coding tools into hybrid agent networking, agent payment, personalized model training, and agent-native organizations such as "zero-person companies."

## Key Quotes
> "模型以外都是 Harness" — Lai's compact definition of agent harness.

> "模型才是 Agent" — the reason the episode emphasizes model capability before harness cleverness.

> "更多 context、更少 control、更多 action 能力" — the preferred direction for Claude Code-style harness design.

> "CLI is all you need" — the Unix/CLI-oriented interface thesis.

> "最好的管理就是不要做管理" — the warning against context management that fights the model's own operating pattern.

## Connections
- [[LaiXinlu]] — guest explaining harness layers, Claude Code lessons, and Share AI's infrastructure thesis.
- [[ShareAI]] — company behind [[LearnClaudeCode]] and the K-series agent infrastructure tools.
- [[ClaudeCode]] and [[LearnClaudeCode]] — central sample used to study memory, skills, tools, compression, and handoff design.
- [[AgentHarness]] — core concept added by this source.
- [[KComputer]] — concrete Share AI implementation of a lightweight Unix-style agent work environment.
- [[AgentFacingInterfaces]], [[HeadlessSoftware]], and [[AgenticWorkflow]] — existing wiki concepts sharpened by the CLI/Unix-first argument.
- [[ContextEngineering]], [[PersistentAgentMemory]], and [[AISkills]] — context and self-improvement layer inside the harness.
- [[SubagentWorkflow]] and [[ModelHarnessCoEvolution]] — multi-agent and model-harness design frames extended by the episode.
- [[Anthropic]], [[Manus]], [[MiniMax]], and [[YouyouAgent]] — reference points used to compare models, agent products, memory/sandbox approaches, and future agent-native experiments.
- [[AgenticEconomy]] — future-facing infrastructure frame for agent payment, hybrid networking, personalized training, and agent economic actors.

## Contradictions
- No direct contradiction with prior wiki content. The source reinforces the existing [[HeadlessSoftware]], [[AgentFacingInterfaces]], [[PersistentAgentMemory]], and [[ModelHarnessCoEvolution]] threads while making a stronger claim that CLI/Unix-style surfaces may be more natural for current agents than newer protocol or flow-graph abstractions.
