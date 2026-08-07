---
title: "Agent Inference Workload"
type: concept
tags: [ai, agents, inference, infrastructure]
sources: [e247-duihua-shengying-xai-infra-de-langman-sglang-kaiyuan-pingquan-yu-zhenhuanchuan-6c9d13b1-ac9a-4a7a-a35b-99bfb8374668, xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1, e246-hewei-zhengliu-liaoliao-guigu-ruhe-kan-zhongguo-kaifang-moxing-bijin-qianyan-5fd236d7-9a72-4b15-9e84-e83ceadd1b41]
last_updated: 2026-08-08
---

# Agent Inference Workload

[[e247-duihua-shengying-xai-infra-de-langman-sglang-kaiyuan-pingquan-yu-zhenhuanchuan-6c9d13b1-ac9a-4a7a-a35b-99bfb8374668]] adds the [[SGLang]] implementation angle. [[ShengYing|盛颖]] explains [[RadixAttention]] as a way to reuse shared prefixes and KV cache in multi-turn and agent-like settings, making the agent workload a concrete serving-engine problem.

[[xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]] adds a K3-specific version of the workload. [[ZhaoChenyang]] says a coding task may reuse a very large stable prefix while adding a much smaller increment, making prefix reuse central to latency and cost. The complication is that [[KimiDeltaAttention|KDA]] carries mutable recurrent state, so prefix caching and speculative-sampling rollback are harder than with append-only KV cache.

Agent inference workload is the serving pattern described in [[e246-hewei-zhengliu-liaoliao-guigu-ruhe-kan-zhongguo-kaifang-moxing-bijin-qianyan-5fd236d7-9a72-4b15-9e84-e83ceadd1b41]] where agent systems differ from ordinary chatbots or simple RAG. [[WangTiezhen|王铁镇]] says agent work often has long input, short output, and high prefix/KV-cache reuse, making cache lifetime, scheduling, and hardware/software co-design central to cost.

The concept explains why open-model competition creates infrastructure opportunity. If many agent tasks reuse long context or tool state, the provider that manages [[PrefixCaching]], routing, batching, memory, and model fit can reduce cost even when it does not own the strongest base model.

## Key Claims
- Agent workloads can be dominated by context reuse and intermediate steps rather than only final output length.
- KV-cache lifecycle and prefix reuse become product and infrastructure variables.
- Routing across models can matter more when agents decompose work into planning, tool use, retrieval, execution, and review.
- Hardware/software co-design remains a major cost-reduction opportunity for agent-heavy inference.
- Mutable attention state can make agent serving harder even when it reduces memory growth.
- Radix Attention adds that tree-structured prefix reuse can be a first-class serving mechanism when many conversations or agent steps share context.

## Connections
- [[SGLang]], [[RadixAttention]], [[ShengYing|盛颖 / Sheng Ying]], and [[DayZeroModelSupport]] - source-247 SGLang serving branch.
- [[AIInferenceCostStructure]], [[ModelRoutingCostControl]], and [[MaaSInfrastructure]] - cost and routing context.
- [[AgentHarness]], [[ModelHarnessCoEvolution]], and [[ModelInfraCoDesign]] - agent workflow and serving-engine co-design.
- [[PrefixCaching]], [[ContinuousBatching]], [[HighThroughputInferenceBatching]], and [[InferenceAccelerationStack]] - infrastructure mechanisms.
- [[OpenRouter]], [[NeoCloud]], [[KimiK3]], and [[OpenSourceAIModels]] - ecosystem players and model diversity that make workload optimization valuable.
- [[KimiDeltaAttention]], [[AgentIn]], [[KernelDevelopmentAgents]], and [[ModelInfraCoDesign]] - K3 architecture and environment branch added by LateTalk episode 177.
