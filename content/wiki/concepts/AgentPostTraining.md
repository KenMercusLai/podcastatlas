---
title: "Agent Post-Training"
type: concept
tags: [agents, model-training, post-training]
sources: [138-dui-luo-fuli-3-5-xiaoshi-fangtan-ai-fanshi-yiran-jubian-openclaw-agent-fanshi-hen-chi-hou-xunlian-ka-de-fenpei-zuzhi-pingquan-lvjthrp5i6nlol64yoj-jddra4wf]
last_updated: 2026-07-08
---

# Agent Post-Training

Agent post-training is [[LuoFuli]]'s frame in [[138-dui-luo-fuli-3-5-xiaoshi-fangtan-ai-fanshi-yiran-jubian-openclaw-agent-fanshi-hen-chi-hou-xunlian-ka-de-fenpei-zuzhi-pingquan-lvjthrp5i6nlol64yoj-jddra4wf]] for moving SFT, RL, evaluation, and model adaptation from chat behavior toward real agent workflows. The source says agent systems such as [[OpenClaw]] and [[OpenCloud]] expose different requirements: memory, tools, long context, active tasks, cost routing, skills, and multi-step recovery.

The concept extends [[ModelHarnessCoEvolution]]. A model trained only for chat may look strong in isolated answers but behave poorly when a framework asks it to plan, call tools, maintain memory, delegate, and verify results. Agent post-training therefore uses simulated user agents, multi-round interaction data, task traces, workflow feedback, and [[AISkills]] to teach the model how to operate inside an [[AgentHarness]].

## Key Claims
- Post-training becomes more important when the product surface is an agent framework rather than a chatbot.
- Agent data must include environment feedback, tool results, memory updates, task persistence, and failure recovery.
- SFT and RL can be built from user-agent simulations and real framework traces, not only preference comparisons over one-turn answers.
- Different frameworks may require different adaptation because memory shape, tool affordances, channel structure, and cost routing differ.
- Agent post-training makes [[AICodingVerification]], [[LongHorizonAI]], and [[ModelWorkflowFit]] part of model training rather than only deployment evaluation.

## Connections
- [[LuoFuli]], [[MemoVR]], and [[Xiaomi]] — source speaker, model series, and team context.
- [[OpenClaw]], [[OpenCloud]], and [[AgentHarness]] — framework layer that changes post-training targets.
- [[AgentRL]], [[TrainingComputeAllocation]], and [[AgentOptimizedModelArchitecture]] — infrastructure, compute, and architecture constraints.
- [[AISkills]], [[PersistentAgentMemory]], and [[AgentSelfEvolution]] — reusable workflow and memory signals for training.
- [[MLCoding]], [[ResearchTaste]], and [[ModelHarnessCoEvolution]] — research-loop and co-evolution context.
