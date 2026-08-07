---
title: "Ironwood TPU"
type: entity
tags: [ai, chip, google, tpu, inference]
sources: [e228-guge-tpu-neng-handong-yingweida-ma-qian-tpu-gongchengshi-shouci-jiemi-fd17090c-0d72-4c0d-aa3e-9b00bc062149]
last_updated: 2026-08-07
---

# Ironwood TPU

Ironwood TPU is the TPU generation discussed in [[e228-guge-tpu-neng-handong-yingweida-ma-qian-tpu-gongchengshi-shouci-jiemi-fd17090c-0d72-4c0d-aa3e-9b00bc062149]]. [[HenryTPUEngineer|Henry]] describes Ironwood V7 as having meaningfully improved peak FLOPS and memory bandwidth, and says it is aimed especially at [[HighThroughputInferenceBatching|large-scale inference]] needs such as lower latency, higher throughput, and enough [[HighBandwidthMemory|memory bandwidth]] for LLM decode.

In the source, Ironwood matters less as a standalone chip benchmark than as evidence of [[Google]] shifting [[TPU]] design toward the inference-heavy economics of deployed [[Gemini]] and cloud workloads. Its value still depends on [[XLACompiler|XLA]], [[TPUPodSystemOptimization|TPU Pod]] design, [[AdvancedPackaging]], supply ramp, and integration into [[GoogleCloud]].

## Connections
- [[TPU]], [[Google]], [[Gemini]], and [[GoogleCloud]] — platform context.
- [[MemoryWall]], [[HighBandwidthMemory]], and [[AIInferenceCostStructure]] — inference bottleneck and cost context.
- [[AIChipSpecialization]] and [[ASICWorkloadPredictionRisk]] — specialization and model-churn tradeoff.
