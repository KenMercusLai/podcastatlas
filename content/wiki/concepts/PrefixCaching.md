---
title: "Prefix Caching"
type: concept
tags: [ai, inference, agents, caching]
sources: [148-dui-you-kaichao-3-xiaoshi-fangtan-kaiyuan-infra-he-moxing-co-design-ruguo-vllm-shibai-women-hui-houhui-yibeizi-lg-fhgpmq4r-8l-5-yrimxgkims]
last_updated: 2026-08-08
---

# Prefix Caching

Prefix caching is the inference reuse pattern highlighted in [[148-dui-you-kaichao-3-xiaoshi-fangtan-kaiyuan-infra-he-moxing-co-design-ruguo-vllm-shibai-women-hui-houhui-yibeizi-lg-fhgpmq4r-8l-5-yrimxgkims]] through coding agents. [[YuKaichao|游凯超]] says coding-agent prompts often contain stable material such as system instructions, repository context, tool descriptions, and policies, making cache reuse valuable when the prefix stays stable.

The source's important twist is that [[AgentHarness]] design can destroy the cache. Dynamic dates, changing tool lists, reordered instructions, or frequently rewritten system prompts can make repeated work look different to the inference engine, increasing [[AIInferenceCostStructure]] even when the user task is similar.

## Key Claims
- Prefix caching connects prompt engineering to serving economics.
- Agent harnesses should treat stable context as an infrastructure asset, not only as model input text.
- Cache-breaking changes can raise cost and latency without improving model quality.
- The pattern becomes more important under [[TestTimeScaling]] because long or repeated agent loops amplify any avoidable prompt recomputation.

## Connections
- [[AgentHarness]], [[ModelHarnessCoEvolution]], and [[AgenticWorkflow]] — harness and workflow context.
- [[VLLM|vLLM]], [[ContinuousBatching]], and [[AIInferenceCostStructure]] — inference-engine and cost context.
- [[ModelInfraCoDesign]] and [[InferenceAccelerationStack]] — broader co-design and acceleration context.
