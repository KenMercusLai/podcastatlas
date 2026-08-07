---
title: "Radix Attention"
type: concept
tags: [ai, inference, caching, agents]
sources: [e247-duihua-shengying-xai-infra-de-langman-sglang-kaiyuan-pingquan-yu-zhenhuanchuan-6c9d13b1-ac9a-4a7a-a35b-99bfb8374668]
last_updated: 2026-08-08
---

# Radix Attention

Radix Attention is the [[SGLang]] mechanism [[ShengYing|盛颖]] explains in [[e247-duihua-shengying-xai-infra-de-langman-sglang-kaiyuan-pingquan-yu-zhenhuanchuan-6c9d13b1-ac9a-4a7a-a35b-99bfb8374668]]. It uses a radix-tree structure to manage shared prompt prefixes and reuse already computed KV cache, reducing repeated computation in workloads with overlapping context.

The episode frames the mechanism as especially relevant to multi-turn dialogue and agents. In those settings, many requests share instructions, history, tool context, or retrieved material, so [[PrefixCaching]] becomes a core part of [[AgentInferenceWorkload]] rather than a small serving optimization.

## Key Claims
- Shared prefixes should be treated as cacheable structure, not as unrelated text repeated request by request.
- Prefix reuse matters more when agent or dialogue workloads repeatedly expand from the same context.
- Serving engines need data structures that match model and workflow shape, which links Radix Attention to [[ModelInfraCoDesign]].
- Architecture churn can still force new adaptation work, so Radix Attention sits alongside [[DayZeroModelSupport]] rather than replacing it.

## Connections
- [[SGLang]] and [[ShengYing|盛颖 / Sheng Ying]] - source mechanism and explainer.
- [[PrefixCaching]], [[AgentInferenceWorkload]], and [[InferenceAccelerationStack]] - serving optimization context.
- [[ModelInfraCoDesign]], [[AIInferenceCostStructure]], and [[AIInfrastructureAsProduct]] - broader infrastructure economics and product frame.
- [[RadixARC|Redix ARK]] - company context around the SGLang work.
