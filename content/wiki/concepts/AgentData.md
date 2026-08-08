---
title: "Agent Data"
type: concept
tags: [ai, agents, data, workflow]
sources: [cong-zhengliu-dao-hecheng-shuju-dao-rsi-moxing-jingzheng-de-xiayige-jiaodian-shi-shenme-duitan-evolvent-ai-lianchuang-mengfanqing-lq1xnhp4muc3ividqhvd0ul77qmi, tech-20260424-0424-mp-tech-pod-128-tech-20260424-0424-mp-tech-pod-128, tsr-s4-alexandrwang-v3-tsr-s4-alexandrwang-v3]
last_updated: 2026-08-09
---

# Agent Data

[[cong-zhengliu-dao-hecheng-shuju-dao-rsi-moxing-jingzheng-de-xiayige-jiaodian-shi-shenme-duitan-evolvent-ai-lianchuang-mengfanqing-lq1xnhp4muc3ividqhvd0ul77qmi]] adds a synthetic and RSI-oriented version. [[MengFanqing|孟繁青]] distinguishes constructed [[SyntheticAgentData]] from real human AI-use traces: synthetic trajectories can be cleaner and more trainable when the task, environment, and scoring are designed, while ordinary personal usage data is often too noisy and compliance-heavy to sell directly.

Agent data is [[AlexandrWang]]'s term in [[tsr-s4-alexandrwang-v3-tsr-s4-alexandrwang-v3]] for data about how people complete tasks, not just what final answers look like. He describes the needed data as traces of thinking, information gathering, constraint checking, decision-making, and action.

The concept is tied to the shift from chatbots to agents. If AI systems move from talking to doing, then [[AIDataInfrastructure]] must capture how capable people actually perform work such as booking flights, reviewing contracts, building software features, or making product decisions.

[[tech-20260424-0424-mp-tech-pod-128-tech-20260424-0424-mp-tech-pod-128]] adds a contested employee-data version. The episode says [[Meta]] wants real examples of how people use computers so agents can complete everyday computer tasks, turning mouse movements, clicks, and keystrokes into possible [[WorkplaceBehaviorTrainingData]]. This reinforces the value of process data while making labor consent and [[WorkplaceAITransparency]] central.

## Key Claims
- Agent data is process data, not only input-output pairs.
- Many valuable workflows lack good training data because the reasoning, checking, and tool-use steps are not captured.
- Agent data depends on human experts because models still hallucinate, get stuck, and need guidance in real-world domains.
- Capturing agent data could make [[DataAsEducation]] more concrete by turning expert task performance into teachable sequences.
- The data is valuable only if privacy, permissions, task context, and evaluation are handled carefully.
- Workplace process traces may be valuable precisely because they show real tool use, but they also carry stronger employee surveillance risk than public examples.
- Synthetic agent data shifts value toward controllable environments, verifier design, and trace cleaning rather than raw user history.

## Connections
- [[SyntheticAgentData]], [[EnvironmentBasedAgentBenchmarks]], and [[RSIData]] — synthetic and model-improvement data branch.
- [[AlexandrWang]] and [[ScaleAI]] - source person and company.
- [[AIDataInfrastructure]], [[DataAsEducation]], and [[DataEngineLearningLoop]] - data concepts this extends.
- [[AgenticWorkflow]], [[HumanAgentCollaboration]], and [[HumanJudgmentUnderAI]] - workflow and oversight context.
- [[ContextEngineering]] and [[PersistentAgentMemory]] - adjacent context layers agents need while acting.
- [[Meta]], [[Reuters]], [[ComputerUseAgent]], and [[WorkplaceBehaviorTrainingData]] - employee process-data branch added by Marketplace Tech Bytes.
