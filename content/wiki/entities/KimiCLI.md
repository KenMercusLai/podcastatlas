---
title: "Kimi CLI"
type: entity
tags: [ai-tool, agents, cli, coding]
sources: [yong-agent-donglixue-he-40-ge-agents-yiqi-wei-ren-ai-zuo-chanpin-duitan-slock-ai-chuangshiren-rc-liiv-fkcdolfb06hkoyz0ix3fejy]
last_updated: 2026-07-23
---

# Kimi CLI

Kimi CLI is the command-line agent product [[RC]] discusses in [[yong-agent-donglixue-he-40-ge-agents-yiqi-wei-ren-ai-zuo-chanpin-duitan-slock-ai-chuangshiren-rc-liiv-fkcdolfb06hkoyz0ix3fejy]]. RC describes it as a coding/general agent running in the command line and distinguishes it from the other CLI tools that such an agent may call.

The source frames Kimi CLI as both a product and a design probe. RC says he wanted the CLI form to be only the first layer: underneath it, a local [[AgentHarness]] could be reused and then wrapped into SDK, Web UI, or VS Code extension forms. That makes Kimi CLI relevant to the wiki less as a standalone feature list and more as an example of how [[AgentFacingInterfaces]] and [[AgentOptimizedCLI]] design can expose model capability to real tools.

## Design Lessons
- CLI is useful for agents because language models handle text streams, command output, and terminal conventions well.
- Agent-facing commands need compact inputs, stable and information-dense outputs, clear documentation, and examples the model can reuse.
- A coding agent can begin from a small agent loop and a Bash tool, then gain reliability as missing tools and prompt rules are discovered from failures.
- CLI is not necessarily the final consumer interface; it can be the first accessible harness surface before more human-friendly UI layers appear.

## Connections
- [[Kimi]] — product/company context for Kimi CLI.
- [[RC]] — builder and source speaker.
- [[AgentOptimizedCLI]], [[AgentFacingInterfaces]], and [[AgentHarness]] — core interface and execution concepts the source reinforces.
- [[VibeCoding]], [[ClaudeCode]], [[Codex]], and [[ModelWorkflowFit]] — adjacent coding-agent workflow comparisons.
