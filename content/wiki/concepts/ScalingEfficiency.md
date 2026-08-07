---
title: "Scaling Efficiency"
type: concept
tags: [ai, infrastructure, model-architecture]
sources: [e246-hewei-zhengliu-liaoliao-guigu-ruhe-kan-zhongguo-kaifang-moxing-bijin-qianyan-5fd236d7-9a72-4b15-9e84-e83ceadd1b41]
last_updated: 2026-08-08
---

# Scaling Efficiency

Scaling efficiency is the model-development pressure in [[e246-hewei-zhengliu-liaoliao-guigu-ruhe-kan-zhongguo-kaifang-moxing-bijin-qianyan-5fd236d7-9a72-4b15-9e84-e83ceadd1b41]] where teams try to improve capability while lowering training and inference cost. [[WangTiezhen|王铁镇]] says Chinese open-model teams were shaped by compute scarcity, making architecture, data engineering, reinforcement learning, and serving optimization more central than a simple "more compute" story.

The source treats compute constraint as both a limitation and an innovation pressure. If a model team cannot rely on unlimited frontier GPUs, it may pursue attention variants, better utilization, model-infra co-design, and cheaper inference paths that make the resulting model more disruptive to closed API providers.

## Key Claims
- Capability gains should be evaluated per unit of compute, cost, latency, and deployability, not only benchmark score.
- Compute scarcity can push teams toward architecture and inference optimization.
- Efficiency gains can make open models commercially disruptive even when closed frontier models remain stronger at the top end.
- [[KimiK3|Kimi K3]] is source-framed as an efficiency case as well as a capability case.

## Connections
- [[AIInferenceCostStructure]], [[InferenceAccelerationStack]], and [[TokenPerWatt]] - cost and efficiency layers.
- [[ModelInfraCoDesign]], [[OpenSourceAIInfrastructure]], [[VLLM|vLLM]], [[PrefixCaching]], and [[ContinuousBatching]] - serving and architecture context.
- [[DomesticAIChipCatchUp]], [[ComputeFreedom]], and [[AIComputeContinuity]] - hardware and compute-availability pressure.
- [[ModelDistillation]], [[KimiK3]], [[DeepSeek]], and [[Qwen]] - model-progress debate where efficiency should not be ignored.
