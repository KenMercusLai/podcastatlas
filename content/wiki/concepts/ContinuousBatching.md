---
title: "Continuous Batching"
type: concept
tags: [ai, inference, scheduling, infrastructure]
sources: [148-dui-you-kaichao-3-xiaoshi-fangtan-kaiyuan-infra-he-moxing-co-design-ruguo-vllm-shibai-women-hui-houhui-yibeizi-lg-fhgpmq4r-8l-5-yrimxgkims]
last_updated: 2026-08-08
---

# Continuous Batching

Continuous batching is one of the inference first principles [[YuKaichao|游凯超]] says practitioners need in [[148-dui-you-kaichao-3-xiaoshi-fangtan-kaiyuan-infra-he-moxing-co-design-ruguo-vllm-shibai-women-hui-houhui-yibeizi-lg-fhgpmq4r-8l-5-yrimxgkims]]. The episode treats it as part of the basic systems knowledge required to judge whether a large-model serving optimization is real.

In the wiki's terms, continuous batching belongs between [[HighThroughputInferenceBatching]] and product-facing [[AIInferenceCostStructure]]. It is not only a GPU-utilization trick: request arrival patterns, sequence lengths, attention state, and user latency targets all affect whether batching improves actual serving economics.

## Key Claims
- Efficient inference requires scheduling active requests over time, not only choosing a model and counting tokens.
- Batching has to be evaluated with latency, memory pressure, attention-state management, and changing sequence lengths.
- [[VLLM|vLLM]] is important partly because inference engines make these scheduling choices reusable for many users and models.
- Agent workloads complicate batching because long tool loops, variable prompts, and cached prefixes create irregular request shapes.

## Connections
- [[HighThroughputInferenceBatching]], [[AIInferenceCostStructure]], and [[InferenceAccelerationStack]] — serving-efficiency context.
- [[VLLM|vLLM]], [[PagedAttention]], and [[PrefixCaching]] — vLLM and state-management context.
- [[AgentHarness]], [[TestTimeScaling]], and [[ModelInfraCoDesign]] — agent and co-design context.
