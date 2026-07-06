---
title: "Agent Self-Evolution"
type: concept
tags: [agents, learning, memory, workflow]
sources: [dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd, vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1]
last_updated: 2026-07-07
---

# Agent Self-Evolution

Agent self-evolution is the episode's practical frame for agents improving through memory, saved workflows, skills, and model-harness feedback loops. In [[dang-women-zai-taolun-harness-de-shihou-women-zai-taolun-shenme-shendu-duitan-minimax-hermes-agent-lvhm1cfno7mqmfv3g0aajmw4zdpd]], [[HermesAgent]] turns successful work traces into reusable [[AISkills]], while [[MiniMax]] describes model plus harness doing most of a model-development pipeline with humans keeping judgment, taste, and direction.

[[vol-161-cong-kaifa-ziji-de-openclaw-liaoqi-1-6626-1]] adds a smaller personal-agent example. [[JustinYan]] lets his [[OpenClaw]]-inspired agent inspect available services and write new skills for itself, which turns self-evolution from a model-training idea into a local product behavior inside an [[AgentHarness]].

## Key Claims
- The source's self-evolution is closer to engineering feedback than fully autonomous self-improvement.
- [[PersistentAgentMemory]] lets agents preserve what worked, what failed, and what the user prefers.
- [[AISkills]] compress repeated successful workflows into reusable procedures.
- [[ModelHarnessCoEvolution]] turns real task execution, tests, deployments, and feedback into signals for both model and harness improvement.
- Human goals, taste, creativity, and value judgment remain part of the loop rather than disappearing.
- Self-written skills increase the need for [[AgentPermissionBoundaries]] because the agent can expand its own action surface.

## Connections
- [[HermesAgent]] and [[Tommy]] — source example of memory becoming skills.
- [[MiniMax]], [[Adao]], and [[Zeying]] — model-company context for model plus harness doing more of the training workflow.
- [[PersistentAgentMemory]], [[AISkills]], and [[AgentHarness]] — mechanisms that make the loop practical.
- [[YouyouAgent]] — adjacent agent-native experiment where an agent pursues a long-running goal.
- [[HumanJudgmentUnderAI]] — boundary condition that humans still set goals and evaluate outputs.
- [[OpenClaw]] and [[AgentNativeSoftware]] — personal-agent case where software can add capability to itself.
