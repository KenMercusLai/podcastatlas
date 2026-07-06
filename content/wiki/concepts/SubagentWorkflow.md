---
title: "Subagent Workflow"
type: concept
tags: [agents, workflow, skills]
sources: [ali-qianwen-lizhi-yuzhen-zai-jiwanren-de-tieqiu-li-ruhe-timian-shengcun-keji-luandun]
last_updated: 2026-07-06
---

# Subagent Workflow

Subagent workflow is an agentic pattern where a foreground assistant delegates complex, long-running, or adversarial tasks to background agents and later integrates their outputs. In [[ali-qianwen-lizhi-yuzhen-zai-jiwanren-de-tieqiu-li-ruhe-timian-shengcun-keji-luandun]], the host describes one skill that sends tool-heavy or high-token tasks to a background subagent and another that has pro and con agents debate a question before synthesis.

## Key Patterns
- Background execution for tasks too large or disruptive for the foreground thread.
- Reference IDs for later retrieval, pausing, or management.
- Adversarial analysis by assigning different agents opposing roles before a synthesizer reviews them.

## Connections
- [[AISkills]] — subagent behavior can be packaged as reusable skills.
- [[AgenticWorkflow]] — broader workflow pattern that subagents extend.
- [[ContextEngineering]] — subagents still need task context and integration standards.
