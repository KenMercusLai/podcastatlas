---
title: "Synthetic Agent Data"
type: concept
tags: [ai, agents, data, post-training]
sources: [cong-zhengliu-dao-hecheng-shuju-dao-rsi-moxing-jingzheng-de-xiayige-jiaodian-shi-shenme-duitan-evolvent-ai-lianchuang-mengfanqing-lq1xnhp4muc3ividqhvd0ul77qmi]
last_updated: 2026-08-09
---

# Synthetic Agent Data

Synthetic agent data is task-trajectory data generated when a model or agent explores an [[EnvironmentBasedAgentBenchmarks|environment]], receives feedback, and leaves behind usable traces for model training. [[cong-zhengliu-dao-hecheng-shuju-dao-rsi-moxing-jingzheng-de-xiayige-jiaodian-shi-shenme-duitan-evolvent-ai-lianchuang-mengfanqing-lq1xnhp4muc3ividqhvd0ul77qmi]] adds this concept through [[MengFanqing|孟繁青]]'s distinction between synthetic agent trajectories and real human work traces.

The source positions synthetic agent data as a later data phase after ordinary crowd labeling and expert labeling. It can be cleaner than real user traces because the task, environment, and scoring are intentionally constructed, but it still needs strong verification to avoid leakage, benchmark gaming, low-diversity traces, or superficial solutions.

## Key Claims
- Synthetic agent data is more than generated text; it includes environment state, actions, feedback, revisions, and success or failure evidence.
- If an outside stronger model such as [[Claude]] explores the environment and generates trajectories, the result can overlap with [[ModelDistillation]].
- Complex environments and scoring systems make "distilled" synthetic data more skill-dependent than copying a teacher answer in a simple task.
- Synthetic data may be especially valuable for weaker models because they have more learning margin, but leading models can still improve if the environment and verifier surface correct trajectories they did not reliably execute before.
- Real human AI-use traces can be noisy and compliance-heavy; synthetic trajectories are more trainable when the environment and permission structure are controlled.

## Connections
- [[AgentData]], [[AIDataInfrastructure]], and [[DataPricingInAI]] — broader data-value context.
- [[EnvironmentBasedAgentBenchmarks]], [[AgentPostTraining]], and [[AIVerification]] — generation and validation mechanism.
- [[RSIData]] — more specialized data where the trajectory improves a model or training loop.
- [[ModelDistillation]], [[ModelCollapse]], and [[AITrainingDataScarcity]] — adjacent data-quality and risk debates.
- [[EvolventAI]], [[MengFanqing]], and [[RSIBenchData]] — source company, speaker, and project context.
