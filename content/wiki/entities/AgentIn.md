---
title: "AgentIn"
type: entity
tags: [ai, agents, open-source, infrastructure]
sources: [xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]
last_updated: 2026-08-08
---

# AgentIn

AgentIn is the agent environment that [[KimiK3|Kimi K3]] opened according to [[xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]]. The source treats it as part of K3's open infrastructure bundle alongside weights and low-level kernels, while still emphasizing that the full IO environment, task system, and raw expert checkpoints were not fully released.

The source-specific lesson is that agent capability and isolation are coupled. [[ZhaoChenyang]] argues that Kimi's approach is not simply to lock the model down, but to improve [[AgentEnvironmentIsolation]] so the model can run with more useful permissions while failures remain contained.

AgentIn also connects training and deployment. The episode says K3 uses partial rollout so completed trajectories can be used for training before every long-running sample finishes, making [[AgentRL]] infrastructure more consistent with real agent execution.

## Connections
- [[KimiK3]], [[MoonshotAI]], and [[OpenWeightReleaseBoundary]] — model and release context.
- [[AgentEnvironmentIsolation]], [[AgentRL]], [[AgentPostTraining]], and [[ModelHarnessCoEvolution]] — agent-training and execution context.
- [[AIModelSandboxEscape]], [[FrontierModelCyberMisuse]], and [[AICyberDefenseUtility]] — adjacent sandbox and safety context.
