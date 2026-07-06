---
title: "Agent Harness"
type: concept
tags: [agents, infrastructure, context, tooling]
sources: [tan-mi-claude-code-gao-dong-agent-harness-dui-tan-lai-xin-lu-lkluk3i7c4gzw4jvxee7odsfgis3]
last_updated: 2026-07-06
---

# Agent Harness

Agent harness is the model-external system that lets an AI agent act in the world. In [[tan-mi-claude-code-gao-dong-agent-harness-dui-tan-lai-xin-lu-lkluk3i7c4gzw4jvxee7odsfgis3]], [[LaiXinlu]] defines it as everything outside the model: tools, files, runtime state, context, memory, compression, handoff, permissions, and multi-agent governance.

## Layers
- Execution ability: CLI tools, file operations, browser use, language interpreters, code-registered tools, and protocol-style extensions.
- Context and environment: system prompt, working directory, dependency state, git state, [[AISkills]], [[PersistentAgentMemory]], context-window management, compression, and task handoff.
- Governance and orchestration: multi-agent roles, permissions, information boundaries, and safeguards against agents mutating the wrong artifacts.

## Key Claims
- Harness matters because a model without tools and environment is an intelligent system without hands, memory, or operating context.
- The model is still the first source of agent intelligence; harness design should amplify the model rather than replace the model's judgment with rigid flow logic.
- Current agents may work better with more context, more action capacity, and less brittle programmatic control.
- CLI/Unix-style interfaces can be more natural for current models than newer abstractions because command-line patterns are deeply represented in training data.
- Good harnesses should align with the model's operating logic and remain useful as models improve; over-managed context or overly restrictive orchestration can become a bottleneck.

## Connections
- [[ClaudeCode]] and [[LearnClaudeCode]] — concrete harness sample analyzed in the source.
- [[AgenticWorkflow]] — task pattern that exposes whether a harness works.
- [[ContextEngineering]], [[PersistentAgentMemory]], and [[AISkills]] — context layer inside the harness.
- [[AgentFacingInterfaces]] and [[HeadlessSoftware]] — product/interface consequences of giving agents callable tools.
- [[SubagentWorkflow]] — orchestration pattern that needs permissions and handoff.
- [[ModelHarnessCoEvolution]] — adjacent concept describing how models and harnesses improve together.
- [[KComputer]] — Share AI implementation of a lightweight Unix-like harness environment.
