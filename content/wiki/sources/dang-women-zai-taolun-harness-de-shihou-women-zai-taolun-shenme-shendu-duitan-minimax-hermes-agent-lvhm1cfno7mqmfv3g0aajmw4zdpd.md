---
title: "当我们在讨论 Harness 的时候，我们在讨论什么 | 深度对谈: MiniMax × Hermes Agent"
type: source
tags: [podcast, ai, agents, harness, memory]
sources: []
date: 2026-04-28
source_file: "/home/ken/repos/podcastatlas/content/episodes/当我们在讨论 Harness 的时候，我们在讨论什么 ｜ 深度对谈： Minimax × Hermes Agent [lvHm1cFno7MQMFV3g0aajmW4zdPd].md"
source_url: "https://www.xiaoyuzhoufm.com/episode/69e96b5b1e94ae6921ee3c2b"
last_updated: 2026-07-06
---

## Summary
This [[ShizilukouCrossing]] episode, hosted by [[Koji]], brings together [[MiniMax]] guests [[Adao]] and [[Zeying]] with [[HermesAgent]] business lead [[Tommy]] to discuss what agent harnesses actually do. The discussion argues that [[AgentHarness]] is not a prompt wrapper or UI shell, but the system that gives models tools, memory, environment, permissions, feedback, and enough freedom to complete real work. It connects the domestic [[OpenCloud]] and [[OpenClaw]] agent wave to [[PersistentAgentMemory]], [[AISkills]], [[MultiAgentCollaboration]], [[InterleavedThinking]], [[AgentSelfEvolution]], and the open question of [[AgentIdentityAndAuthentication]].

## Key Claims
- [[OpenCloud]] and [[OpenClaw]] became hot in China because domestic users were suddenly able to experience agents that could keep working through familiar, low-friction interfaces.
- [[HermesAgent]] is framed as an open-source agent framework where the language model is the brain and the framework supplies the hands: tool orchestration, main-loop control, state, errors, and memory.
- The source defines [[AgentHarness]] as the work environment that lets an agent act: tools, environment, constraints, feedback, permissions, and sometimes other agents.
- [[PersistentAgentMemory]] is treated as a decisive product capability because users expect agents to remember prior work, learn preferences, and convert successful workflows into reusable [[AISkills]].
- Human operators can become the bottleneck once they supervise many local and cloud agents; stronger harnesses let agents test, deploy, check results, and preserve experience without constant user intervention.
- [[MultiAgentCollaboration]] is useful because agents can exchange large context quickly, cross-check each other, and recover when one long-context agent drifts off path.
- [[MiniMax]] practice is used as evidence for [[ModelHarnessCoEvolution]]: the source says an M2.7 R1 pipeline already had most work done by model plus harness, with humans keeping direction, taste, creativity, and judgment.
- [[InterleavedThinking]] distinguishes agentic models from chatbots: the model must re-plan after tool calls and environment feedback instead of only following an initial plan.
- Skill plus CLI is presented as easier for ordinary users to author and share than heavier protocol-first approaches, while Claude Code's memory, IM, scheduled task, and mobile-control direction is described as becoming more OpenCloud-like.
- [[AgentIdentityAndAuthentication]] becomes more important as agents gain real-world powers, but the episode also warns that excessive real-name or safety framing can become a route to closed ecosystems.

## Key Quotes
> "大语言模型是大脑，智能体框架就是双手" — [[Tommy]] on the role of an agent framework.

> "给同事约定边界、配备电脑、电话、邮箱和权限" — the human-work analogy for [[AgentHarness]].

> "人反而成为效率瓶颈" — the problem that appears when users coordinate many agents manually.

> "旧模型帮助训练新模型" — the engineering-loop version of [[AgentSelfEvolution]].

> "intelligence with everyone" — the open-intelligence principle raised in the safety and real-name discussion.

## Connections
- [[Koji]] — host of the episode and moderator of the agent harness discussion.
- [[Adao]] and [[Zeying]] — [[MiniMax]] guests discussing harness design, multi-agent checks, and model-agent feedback.
- [[Tommy]] and [[HermesAgent]] — guest and open-source agent framework centered on memory, tools, and self-improving workflows.
- [[OpenCloud]] and [[OpenClaw]] — domestic agent-wave context that made memory and harness problems visible.
- [[AgentHarness]], [[AgenticWorkflow]], and [[ModelHarnessCoEvolution]] — core system-design concepts reinforced by the source.
- [[PersistentAgentMemory]], [[AISkills]], and [[AgentSelfEvolution]] — memory-to-skill loop emphasized through Hermes Agent and Claude Code-style systems.
- [[MultiAgentCollaboration]], [[SubagentWorkflow]], and [[InterleavedThinking]] — technical patterns for cross-checking, long-horizon tasks, and environment-aware reasoning.
- [[ClaudeCode]], [[Anthropic]], [[Codex]], and [[Manus]] — agent products used as comparison points for harness design, constraints, source leakage, and product life cycles.
- [[AgentFacingInterfaces]], [[HeadlessSoftware]], and [[AgenticEconomy]] — broader infrastructure direction around CLI, skills, payments, identities, and agent-native work.
- [[YouyouAgent]] and [[AIInteractiveEntertainment]] — examples of agent-native experiments and simulated worlds where agents may act continuously.

## Contradictions
- No direct contradiction with prior wiki content. The source reinforces the existing [[AgentHarness]], [[PersistentAgentMemory]], [[AgentFacingInterfaces]], and [[ModelHarnessCoEvolution]] threads while adding more emphasis on Hermes-style memory, multi-agent cross-checking, interleaved thinking, and identity/authentication pressure.
