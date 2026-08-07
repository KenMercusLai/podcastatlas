---
title: "Model-Infra Co-Design"
type: concept
tags: [ai, infrastructure, models, hardware]
sources: [148-dui-you-kaichao-3-xiaoshi-fangtan-kaiyuan-infra-he-moxing-co-design-ruguo-vllm-shibai-women-hui-houhui-yibeizi-lg-fhgpmq4r-8l-5-yrimxgkims]
last_updated: 2026-08-08
---

# Model-Infra Co-Design

Model-infra co-design is [[YuKaichao|游凯超]]'s core technical frame in [[148-dui-you-kaichao-3-xiaoshi-fangtan-kaiyuan-infra-he-moxing-co-design-ruguo-vllm-shibai-women-hui-houhui-yibeizi-lg-fhgpmq4r-8l-5-yrimxgkims]]. The episode uses an electricity analogy: hardware is the natural resource, the model is the generator, and the inference engine is the power system that determines whether tokens can be produced efficiently.

The concept says model architecture, serving engine, hardware, and agent workload should be designed together. After easy general-purpose compute gains slow down, efficiency depends on whether attention design, cache behavior, quantization, routing, batching, chip features, and [[AgentHarness|agent harnesses]] line up.

## Key Claims
- Model teams and infrastructure teams cannot optimize independently once inference cost, latency, memory, and power become first-order constraints.
- [[HardwareLottery]] makes some algorithms more durable than others because hardware support determines whether they can be run efficiently.
- [[VLLM|vLLM]] is a co-design layer because inference engines translate model design into deployable serving behavior.
- [[MixtureOfExperts|MoE]], long context, test-time compute, and coding-agent loops create different serving bottlenecks.
- Good co-design begins at model-design time, not after a trained model is thrown over the wall to an infrastructure team.

## Connections
- [[VLLM|vLLM]], [[PagedAttention]], [[ContinuousBatching]], and [[PrefixCaching]] — inference-engine examples.
- [[AIInferenceCostStructure]], [[InferenceAccelerationStack]], and [[HighThroughputInferenceBatching]] — serving economics and runtime optimization.
- [[AIChipSpecialization]], [[AIInfrastructureFullStackMoat]], and [[HardwareLottery]] — hardware and platform fit.
- [[DeepSeek]], [[OpenSourceAIModels]], and [[OpenSourceAIInfrastructure]] — open-model and infrastructure ecosystem case.
- [[AgentHarness]], [[TestTimeScaling]], and [[ModelHarnessCoEvolution]] — workload and harness side of co-design.
