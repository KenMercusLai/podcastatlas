---
title: "Subagent Workflow"
type: concept
tags: [agents, workflow, skills]
sources: [ali-qianwen-lizhi-yuzhen-zai-jiwanren-de-tieqiu-li-ruhe-timian-shengcun-keji-luandun, tan-mi-claude-code-gao-dong-agent-harness-dui-tan-lai-xin-lu-lkluk3i7c4gzw4jvxee7odsfgis3, dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd]
last_updated: 2026-07-06
---

# Subagent Workflow

Subagent workflow is an agentic pattern where a foreground assistant delegates complex, long-running, or adversarial tasks to background agents and later integrates their outputs. In [[ali-qianwen-lizhi-yuzhen-zai-jiwanren-de-tieqiu-li-ruhe-timian-shengcun-keji-luandun]], the host describes one skill that sends tool-heavy or high-token tasks to a background subagent and another that has pro and con agents debate a question before synthesis.

[[tan-mi-claude-code-gao-dong-agent-harness-dui-tan-lai-xin-lu-lkluk3i7c4gzw4jvxee7odsfgis3]] adds the governance side of subagent work. [[LaiXinlu]] argues that multi-agent systems need role-specific permissions, information boundaries, and handoff documents, such as giving a code-exploration agent read-only powers while preventing a test agent from changing production code just to make tests pass.

[[dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd]] adds the cross-checking side through [[MiniMax]]. The source says multiple agents can exchange much larger context than human feedback usually provides and can correct a single agent when long-context work starts drifting.

## Key Patterns
- Background execution for tasks too large or disruptive for the foreground thread.
- Reference IDs for later retrieval, pausing, or management.
- Adversarial analysis by assigning different agents opposing roles before a synthesizer reviews them.
- Role-specific tool permissions and information access.
- Context compression and handoff documents when a new agent continues work from a prior agent.
- Peer review or cross-checking between agents when a long task needs another context window or viewpoint.

## Connections
- [[AISkills]] — subagent behavior can be packaged as reusable skills.
- [[AgenticWorkflow]] — broader workflow pattern that subagents extend.
- [[ContextEngineering]] — subagents still need task context and integration standards.
- [[AgentHarness]] — governance and orchestration layer for safe multi-agent work.
- [[MultiAgentCollaboration]] — broader collaboration frame added by the Hermes Agent source.
