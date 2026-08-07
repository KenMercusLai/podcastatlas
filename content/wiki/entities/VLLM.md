---
title: "vLLM"
type: entity
tags: [project, open-source, ai-infrastructure, inference]
sources: [148-dui-you-kaichao-3-xiaoshi-fangtan-kaiyuan-infra-he-moxing-co-design-ruguo-vllm-shibai-women-hui-houhui-yibeizi-lg-fhgpmq4r-8l-5-yrimxgkims]
last_updated: 2026-08-08
---

# vLLM

vLLM is the open-source large-model inference engine at the center of [[148-dui-you-kaichao-3-xiaoshi-fangtan-kaiyuan-infra-he-moxing-co-design-ruguo-vllm-shibai-women-hui-houhui-yibeizi-lg-fhgpmq4r-8l-5-yrimxgkims]]. [[YuKaichao|游凯超]] traces it from the [[PagedAttention]] paper and Berkeley open-source culture into a production infrastructure project supported by [[Infract]] and governed through the [[PyTorchFoundation|PyTorch Foundation]].

The episode frames vLLM's moat less as one clever trick than as the accumulated work of maintaining compatibility with rapidly changing model structures, attention variants, hardware constraints, and user workloads. Its 2024 V0-to-V1 rewrite is presented as a response to growing system complexity while preserving user-facing stability where possible.

For the wiki, vLLM is a concrete case of [[OpenSourceAIInfrastructure]]. It sits inside [[AIInferenceCostStructure]] because serving tokens cheaply and reliably depends on scheduling, cache management, model support, hardware fit, and community maintenance. It also sits inside [[ModelInfraCoDesign]] because inference engines increasingly influence how model teams think about attention, [[MixtureOfExperts|MoE]], context length, and deployment efficiency.

## Key Claims
- vLLM began from [[PagedAttention]] but became valuable as a full inference engine and community-maintained system.
- The project was donated to the [[PyTorchFoundation|PyTorch Foundation]] to keep the trademark and governance community-owned.
- [[Infract]] supplies company-level labor, customer collaboration, and infrastructure resources around the open project.
- vLLM must support many model architectures while also deleting features that no longer fit mainstream inference workloads.
- Coding agents create more low-quality pull requests, increasing the importance of maintainer judgment and real user feedback.
- Its long-term ambition in the source is to become Linux-like infrastructure for AI inference.

## Connections
- [[PagedAttention]], [[ContinuousBatching]], and [[PrefixCaching]] — state and scheduling concepts around efficient inference.
- [[AIInferenceCostStructure]], [[HighThroughputInferenceBatching]], and [[InferenceAccelerationStack]] — serving economics and optimization context.
- [[ModelInfraCoDesign]], [[HardwareLottery]], and [[AIChipSpecialization]] — model/hardware/system fit.
- [[DeepSeek]], [[Kimi]], and [[OpenSourceAIModels]] — model ecosystem that creates pressure on engine support.
- [[PyTorchFoundation|PyTorch Foundation]], [[Infract]], and [[OpenSourceAIInfrastructure]] — governance and sustainability context.
