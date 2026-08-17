---
title: "Synthetic Agent Data"
type: concept
tags: [ai, agents, data, post-training]
sources: [zhengliu-fengbao-yichang-wuren-gongkai-tanlun-de-jishu-jingsai-1-179-1, cong-zhengliu-dao-hecheng-shuju-dao-rsi-moxing-jingzheng-de-xiayige-jiaodian-shi-shenme-duitan-evolvent-ai-lianchuang-mengfanqing-lq1xnhp4muc3ividqhvd0ul77qmi]
last_updated: 2026-08-17
---

# Synthetic Agent Data

[[zhengliu-fengbao-yichang-wuren-gongkai-tanlun-de-jishu-jingsai-1-179-1]] adds the distillation-sensitive version. The source says a stronger model can generate tasks, create environments, produce full agent trajectories, and evaluate student-model behavior, making synthetic agent data overlap with [[AgentTrajectoryDistillation]] when the student learns from the teacher's behavior rather than only from neutral feedback.

Synthetic agent data is task-trajectory data generated when a model or agent explores an [[EnvironmentBasedAgentBenchmarks|environment]], receives feedback, and leaves behind usable traces for model training. [[cong-zhengliu-dao-hecheng-shuju-dao-rsi-moxing-jingzheng-de-xiayige-jiaodian-shi-shenme-duitan-evolvent-ai-lianchuang-mengfanqing-lq1xnhp4muc3ividqhvd0ul77qmi]] adds this concept through [[MengFanqing|孟繁青]]'s distinction between synthetic agent trajectories and real human work traces.

The source positions synthetic agent data as a later data phase after ordinary crowd labeling and expert labeling. It can be cleaner than real user traces because the task, environment, and scoring are intentionally constructed, but it still needs strong verification to avoid leakage, benchmark gaming, low-diversity traces, or superficial solutions.

## Key Claims
- Synthetic agent data is more than generated text; it includes environment state, actions, feedback, revisions, and success or failure evidence.
- If an outside stronger model such as [[Claude]] explores the environment and generates trajectories, the result can overlap with [[ModelDistillation]].
- Complex environments and scoring systems make "distilled" synthetic data more skill-dependent than copying a teacher answer in a simple task.
- Synthetic data may be especially valuable for weaker models because they have more learning margin, but leading models can still improve if the environment and verifier surface correct trajectories they did not reliably execute before.
- Real human AI-use traces can be noisy and compliance-heavy; synthetic trajectories are more trainable when the environment and permission structure are controlled.
- LateTalk episode 179 adds that teacher-generated trajectories can be more legally and strategically sensitive when the teacher is a closed frontier model governed by restrictive terms of service.

## Connections
- [[AgentData]], [[AIDataInfrastructure]], and [[DataPricingInAI]] — broader data-value context.
- [[EnvironmentBasedAgentBenchmarks]], [[AgentPostTraining]], and [[AIVerification]] — generation and validation mechanism.
- [[RSIData]] — more specialized data where the trajectory improves a model or training loop.
- [[ModelDistillation]], [[ModelCollapse]], and [[AITrainingDataScarcity]] — adjacent data-quality and risk debates.
- [[EvolventAI]], [[MengFanqing]], and [[RSIBenchData]] — source company, speaker, and project context.
- [[AgentTrajectoryDistillation]], [[ModelDistillationEvidence]], and [[AIModelDistillationGovernance]] — distillation and provenance branch added by LateTalk episode 179.
