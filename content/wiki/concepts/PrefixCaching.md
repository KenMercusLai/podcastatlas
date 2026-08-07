---
title: "Prefix Caching"
type: concept
tags: [ai, inference, agents, caching]
sources: [e247-duihua-shengying-xai-infra-de-langman-sglang-kaiyuan-pingquan-yu-zhenhuanchuan-6c9d13b1-ac9a-4a7a-a35b-99bfb8374668, xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1, 148-dui-you-kaichao-3-xiaoshi-fangtan-kaiyuan-infra-he-moxing-co-design-ruguo-vllm-shibai-women-hui-houhui-yibeizi-lg-fhgpmq4r-8l-5-yrimxgkims]
last_updated: 2026-08-08
---

# Prefix Caching

[[e247-duihua-shengying-xai-infra-de-langman-sglang-kaiyuan-pingquan-yu-zhenhuanchuan-6c9d13b1-ac9a-4a7a-a35b-99bfb8374668]] adds [[RadixAttention]] as the [[SGLang]]-specific prefix-caching mechanism. [[ShengYing|盛颖]] says a radix tree can track shared prefixes and reuse already computed KV cache, especially in multi-turn dialogue and agent workloads.

[[xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]] adds the [[KimiK3|Kimi K3]] edge case. The source says coding-agent workloads can contain huge reusable prefixes, but [[KimiDeltaAttention|KDA]] makes reuse harder because recurrent state is updated and overwritten rather than simply appended. That turns prefix caching from a prompt-layout optimization into an architecture-specific serving problem.

Prefix caching is the inference reuse pattern highlighted in [[148-dui-you-kaichao-3-xiaoshi-fangtan-kaiyuan-infra-he-moxing-co-design-ruguo-vllm-shibai-women-hui-houhui-yibeizi-lg-fhgpmq4r-8l-5-yrimxgkims]] through coding agents. [[YuKaichao|游凯超]] says coding-agent prompts often contain stable material such as system instructions, repository context, tool descriptions, and policies, making cache reuse valuable when the prefix stays stable.

The source's important twist is that [[AgentHarness]] design can destroy the cache. Dynamic dates, changing tool lists, reordered instructions, or frequently rewritten system prompts can make repeated work look different to the inference engine, increasing [[AIInferenceCostStructure]] even when the user task is similar.

## Key Claims
- Prefix caching connects prompt engineering to serving economics.
- Agent harnesses should treat stable context as an infrastructure asset, not only as model input text.
- Cache-breaking changes can raise cost and latency without improving model quality.
- The pattern becomes more important under [[TestTimeScaling]] because long or repeated agent loops amplify any avoidable prompt recomputation.
- Hybrid attention models may need custom cache lifecycle logic instead of assuming every model state behaves like a standard KV cache.
- Radix-tree cache management shows that the data structure inside the serving engine can be part of the product's cost and latency profile.

## Connections
- [[SGLang]], [[RadixAttention]], [[ShengYing|盛颖 / Sheng Ying]], and [[AIInfrastructureAsProduct]] - source-247 radix-tree cache branch.
- [[AgentHarness]], [[ModelHarnessCoEvolution]], and [[AgenticWorkflow]] — harness and workflow context.
- [[VLLM|vLLM]], [[ContinuousBatching]], and [[AIInferenceCostStructure]] — inference-engine and cost context.
- [[ModelInfraCoDesign]] and [[InferenceAccelerationStack]] — broader co-design and acceleration context.
- [[KimiK3]], [[KimiDeltaAttention]], and [[AgentInferenceWorkload]] — mutable-state serving case added by LateTalk episode 177.
