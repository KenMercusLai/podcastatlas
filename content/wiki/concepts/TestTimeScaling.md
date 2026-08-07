---
title: "Test-Time Scaling"
type: concept
tags: [ai, inference, agents, reasoning]
sources: [148-dui-you-kaichao-3-xiaoshi-fangtan-kaiyuan-infra-he-moxing-co-design-ruguo-vllm-shibai-women-hui-houhui-yibeizi-lg-fhgpmq4r-8l-5-yrimxgkims]
last_updated: 2026-08-08
---

# Test-Time Scaling

Test-time scaling is the pattern of spending more computation during inference to improve output quality. In [[148-dui-you-kaichao-3-xiaoshi-fangtan-kaiyuan-infra-he-moxing-co-design-ruguo-vllm-shibai-women-hui-houhui-yibeizi-lg-fhgpmq4r-8l-5-yrimxgkims]], [[YuKaichao|游凯超]] separates it into several workload shapes: repeated sampling and aggregation, longer thinking-token generation, and multi-turn [[AgentHarness|agent]] interaction with tools and environments.

The distinction matters because each form stresses infrastructure differently. Repeated sampling stresses throughput, long thinking stresses generation length and memory, while agent loops stress prompt stability, [[PrefixCaching]], tool-call latency, and irregular request patterns.

## Key Claims
- Test-time scaling should not be treated as one generic inference workload.
- More inference compute can improve quality, but it also changes cost, latency, batching, cache behavior, and system design.
- Agentic forms of test-time scaling make the harness part of the inference problem.
- Model teams, inference-engine teams, and product teams need shared vocabulary before optimizing these workloads.

## Connections
- [[AgentHarness]], [[PrefixCaching]], and [[ModelHarnessCoEvolution]] — agent and harness side.
- [[AIInferenceCostStructure]], [[ContinuousBatching]], and [[VLLM|vLLM]] — serving cost and scheduling context.
- [[ModelInfraCoDesign]] and [[OpenSourceAIInfrastructure]] — broader system design context.
