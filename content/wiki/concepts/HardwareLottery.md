---
title: "Hardware Lottery"
type: concept
tags: [ai, hardware, infrastructure, model-design]
sources: [148-dui-you-kaichao-3-xiaoshi-fangtan-kaiyuan-infra-he-moxing-co-design-ruguo-vllm-shibai-women-hui-houhui-yibeizi-lg-fhgpmq4r-8l-5-yrimxgkims]
last_updated: 2026-08-08
---

# Hardware Lottery

Hardware lottery is the idea [[YuKaichao|游凯超]] uses in [[148-dui-you-kaichao-3-xiaoshi-fangtan-kaiyuan-infra-he-moxing-co-design-ruguo-vllm-shibai-women-hui-houhui-yibeizi-lg-fhgpmq4r-8l-5-yrimxgkims]] to explain why post-Moore AI progress depends on hardware fit. An algorithm or model structure can be elegant, but if it does not map well to available accelerators, memory systems, and communication patterns, it may not receive the economic benefit of the hardware cycle.

In the source, hardware lottery supports [[ModelInfraCoDesign]]. Efficient inference increasingly depends on whether model architecture, quantization, attention, expert routing, and runtime systems can exploit chip features rather than merely run on them.

## Key Claims
- Hardware support can determine whether a model idea becomes practical infrastructure.
- [[AIChipSpecialization]] increases the importance of choosing architectures that fit real accelerators.
- Inference engines such as [[VLLM|vLLM]] mediate the lottery by translating model behavior into efficient serving.
- The concept explains why [[MixtureOfExperts|MoE]], attention variants, long context, and quantization need systems evaluation, not only model-side benchmarks.

## Connections
- [[ModelInfraCoDesign]], [[AIChipSpecialization]], and [[InferenceAccelerationStack]] — core co-design context.
- [[AIInfrastructureFullStackMoat]], [[GPU]], and [[CUDA]] — platform and ecosystem context.
- [[VLLM|vLLM]], [[PagedAttention]], and [[AIInferenceCostStructure]] — inference engine and cost context.
