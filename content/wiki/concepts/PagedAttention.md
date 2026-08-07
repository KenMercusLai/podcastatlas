---
title: "PagedAttention"
type: concept
tags: [ai, inference, memory, systems]
sources: [148-dui-you-kaichao-3-xiaoshi-fangtan-kaiyuan-infra-he-moxing-co-design-ruguo-vllm-shibai-women-hui-houhui-yibeizi-lg-fhgpmq4r-8l-5-yrimxgkims]
last_updated: 2026-08-08
---

# PagedAttention

PagedAttention is the inference-memory idea that [[148-dui-you-kaichao-3-xiaoshi-fangtan-kaiyuan-infra-he-moxing-co-design-ruguo-vllm-shibai-women-hui-houhui-yibeizi-lg-fhgpmq4r-8l-5-yrimxgkims]] identifies as the technical origin of [[VLLM|vLLM]]. [[YuKaichao|游凯超]] says the idea itself was not necessarily complicated in hindsight, but it arrived early, was experimentally solid, and became valuable because it was turned into a usable open-source inference engine.

The source's durable lesson is that an inference optimization becomes important only when it survives contact with production. PagedAttention matters less as an isolated paper result than as the first proof that attention state, memory layout, request scheduling, and user-facing serving needs belong in one systems problem.

## Key Claims
- PagedAttention helped make vLLM possible by treating attention-state management as an inference-system problem.
- Its impact came from implementation timing, experiments, and open-source packaging, not only from algorithmic novelty.
- It links memory management to [[AIInferenceCostStructure]] because inefficient state handling raises serving cost and lowers throughput.
- It is an early example of [[ModelInfraCoDesign]] because model attention behavior and inference runtime behavior cannot be fully separated.

## Connections
- [[VLLM|vLLM]] — project that grew from the PagedAttention work.
- [[ContinuousBatching]], [[HighThroughputInferenceBatching]], and [[PrefixCaching]] — adjacent serving-efficiency concepts.
- [[AIInferenceCostStructure]], [[InferenceAccelerationStack]], and [[ModelInfraCoDesign]] — broader system context.
