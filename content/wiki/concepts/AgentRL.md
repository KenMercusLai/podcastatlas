---
title: "Agent RL"
type: concept
tags: [agents, reinforcement-learning, infrastructure]
sources: [138-dui-luo-fuli-3-5-xiaoshi-fangtan-ai-fanshi-yiran-jubian-openclaw-agent-fanshi-hen-chi-hou-xunlian-ka-de-fenpei-zuzhi-pingquan-lvjthrp5i6nlol64yoj-jddra4wf]
last_updated: 2026-07-08
---

# Agent RL

Agent RL is the reinforcement-learning and rollout problem that appears when a model is trained or adapted inside an [[AgentHarness]] rather than inside a narrow prompt-answer loop. In [[138-dui-luo-fuli-3-5-xiaoshi-fangtan-ai-fanshi-yiran-jubian-openclaw-agent-fanshi-hen-chi-hou-xunlian-ka-de-fenpei-zuzhi-pingquan-lvjthrp5i6nlol64yoj-jddra4wf]], [[LuoFuli]] says agent-era RL infrastructure has to handle agent frameworks, GPU and CPU resources, storage, fault tolerance, compatibility, and train-inference mismatch.

The source treats Agent RL as harder and messier than ordinary post-training because the environment is not just the model inference engine. Tool use, external state, long-running tasks, memory files, simulated users, framework interruptions, and heterogeneous resources all become part of the training loop.

## Key Claims
- Agent RL needs rollout infrastructure that can execute multi-step tasks through tools and frameworks, not only sample text completions.
- The environment may be fuzzy, interruptible, and inconsistent across training and deployment.
- Successful Agent RL depends on [[AIVerification]] and [[AICodingVerification]] because weak evaluations can reward shallow completion or hidden failure.
- Infrastructure must support heterogeneous resources, including GPU inference, CPU work, storage, service calls, timeouts, and recovery after partial failure.
- Agent RL is linked to [[ModelHarnessCoEvolution]]: as the model changes, the framework, reward design, and evaluation tasks may also need to change.

## Connections
- [[AgentPostTraining]] — broader training frame that includes Agent RL.
- [[OpenClaw]], [[OpenCloud]], and [[AgentHarness]] — framework and environment layer.
- [[MemoVR]], [[Xiaomi]], and [[LuoFuli]] — source model-team context.
- [[TrainingComputeAllocation]] — compute pressure created by more parallel experiments and rollout demand.
- [[MultiAgentCollaboration]], [[MLCoding]], and [[LongHorizonAI]] — task classes where agent rollouts become useful and hard to evaluate.
