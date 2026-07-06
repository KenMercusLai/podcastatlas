---
title: "K Computer"
type: entity
tags: [agent-infra, virtual-computer, cli]
sources: [tan-mi-claude-code-gao-dong-agent-harness-dui-tan-lai-xin-lu-lkluk3i7c4gzw4jvxee7odsfgis3]
last_updated: 2026-07-06
---

# K Computer

K Computer is [[ShareAI]]'s lightweight virtual Unix-style computer for agents, described by [[LaiXinlu]] in [[tan-mi-claude-code-gao-dong-agent-harness-dui-tan-lai-xin-lu-lkluk3i7c4gzw4jvxee7odsfgis3]]. It is positioned as part of a broader K-series toolchain with runtime, observation, data export, and reinforcement-learning-oriented tooling.

The design goal is to give agents a small, consistent work environment across many places that can run JavaScript, including browsers and mini-programs. Instead of depending on a full Docker-like sandbox, K Computer represents Unix-like files, shell commands, local networking, and shared disk behavior through data structures, with Rust/WASM used where available and JavaScript fallback elsewhere.

The episode is explicit about the tradeoff: this approach cannot run a real compiler or full browser the way a cloud sandbox can, but it may be much lighter and easier to embed as an [[AgentHarness]] execution environment.

## Connections
- [[ShareAI]] and [[LaiXinlu]] — company and founder behind K Computer.
- [[AgentHarness]] — K Computer's role is mainly in the execution and environment layers.
- [[AgentFacingInterfaces]] — CLI/Unix-style surface that K Computer is designed to expose.
- [[AgenticEconomy]] — future infrastructure context for distributed agents, hybrid networking, and agent-to-agent work.
