---
title: "Agent Trajectory Distillation"
type: concept
tags: [ai, agents, model-training, distillation]
sources: [zhengliu-fengbao-yichang-wuren-gongkai-tanlun-de-jishu-jingsai-1-179-1]
last_updated: 2026-08-17
---

# Agent Trajectory Distillation

Agent trajectory distillation is the agent-era form of [[ModelDistillation]] described in [[zhengliu-fengbao-yichang-wuren-gongkai-tanlun-de-jishu-jingsai-1-179-1]]. Instead of only asking a teacher model for answers or reasoning chains, a model team can use a stronger model to create tasks, operate inside an [[EnvironmentBasedAgentBenchmarks|environment]], generate action traces, and leave behind trajectories that train a student model.

The source defines "environment" concretely: a codebase, terminal, editor, compiler, test runner, unit tests, and other task conditions that let an [[AgentHarness]] actually execute work. This overlaps with [[SyntheticAgentData]], but the distillation frame matters when the student is trained to imitate, compress, or internalize behavior from a stronger teacher model rather than only learning from neutral task feedback.

## Key Claims
- Agent distillation can include task design, environment setup, intermediate actions, tool calls, failures, corrections, final answers, and evaluator scores.
- A stronger model can be used as question maker, environment builder, trajectory generator, or evaluator; not every evaluator-only use is typical distillation.
- Trajectory distillation makes [[AIVerification]] and [[AgentEnvironmentIsolation]] more important because the training signal depends on whether the environment exposes real success or benchmark shortcuts.
- The technique can help weaker models acquire task behavior faster, but it can also transfer teacher-model mistakes, habits, refusal styles, or shallow shortcuts.
- The practical moat is the data pipeline: stable access, realistic questions, filtering, rewriting, correction, data mixing, and checking whether training actually improves the student.

## Connections
- [[ModelDistillation]] — parent technical category.
- [[SyntheticAgentData]] and [[EnvironmentBasedAgentBenchmarks]] — adjacent data and benchmark infrastructure.
- [[AgentPostTraining]], [[AgentRL]], and [[OnPolicyDistillation]] — post-training methods that can use trajectory data.
- [[AgentHarness]], [[AgentEnvironmentIsolation]], and [[AIVerification]] — runtime and validation layers.
- [[ModelDistillationEvidence]] and [[AIModelDistillationGovernance]] — evidence and governance concerns when trajectories come from closed teacher models.
