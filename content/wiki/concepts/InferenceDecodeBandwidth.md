---
title: "Inference Decode Bandwidth"
type: concept
tags: [ai, inference, semiconductors, memory]
knowledge_schema: synthesis-v1
sources:
  - e251-tuili-xinpian-zhi-zhan-liaoliao-groq-cerebras-yu-openai-sanda-lujing-yu-bill-dally-de-sheji-zhexue-786d63c4-d46c-4ff3-80f8-fc895b2a57f0
last_updated: 2026-09-20
---

# Inference Decode Bandwidth

## Definition
Inference decode bandwidth is the constraint created when autoregressive generation produces tokens sequentially and repeatedly moves model weights and state between memory and compute, making usable memory bandwidth and communication efficiency more decisive than peak arithmetic throughput.

## Current Synthesis
[[e251-tuili-xinpian-zhi-zhan-liaoliao-groq-cerebras-yu-openai-sanda-lujing-yu-bill-dally-de-sheji-zhexue-786d63c4-d46c-4ff3-80f8-fc895b2a57f0|E251]] separates compute-rich prefill from bandwidth-sensitive decode. Batching lets general accelerators reuse a weight read across many requests, but it trades individual latency for utilization. SRAM-heavy systems instead bring fixed weights closer to compute, yet their limited capacity forces multi-chip topology, partitioning, and often a separate path for attention and dynamic KV cache. The relevant unit of judgment is therefore the delivered token at system level, not any one chip specification.

## Key Claims
- Autoregressive dependency limits token-level parallelism and can make decode memory-bound even when abundant compute is available.
- Batching amortizes weight movement across requests but can increase queueing and tail latency.
- SRAM improves locality and bandwidth but sacrifices capacity, creating multi-chip communication and model-partitioning costs.
- KV cache and fixed model weights have different growth behavior, so heterogeneous memory and compute placement can be rational.
- Dynamic [[MixtureOfExperts|MoE]] routing makes static communication schedules less efficient because expert selection is known only at runtime.
- Token cost, latency, and power must be evaluated for the complete serving system rather than inferred from FLOPS or memory bandwidth alone.

## Evidence
- Decode mechanism and batching: [[e251-tuili-xinpian-zhi-zhan-liaoliao-groq-cerebras-yu-openai-sanda-lujing-yu-bill-dally-de-sheji-zhexue-786d63c4-d46c-4ff3-80f8-fc895b2a57f0|E251]] contrasts parallel prefill with sequential decode and explains why shared batches improve GPU utilization.
- Memory tradeoff: [[e251-tuili-xinpian-zhi-zhan-liaoliao-groq-cerebras-yu-openai-sanda-lujing-yu-bill-dally-de-sheji-zhexue-786d63c4-d46c-4ff3-80f8-fc895b2a57f0|E251]] compares DRAM, HBM, and six-transistor SRAM across distance, bandwidth, capacity, and cost.
- Architectural responses: [[e251-tuili-xinpian-zhi-zhan-liaoliao-groq-cerebras-yu-openai-sanda-lujing-yu-bill-dally-de-sheji-zhexue-786d63c4-d46c-4ff3-80f8-fc895b2a57f0|E251]] maps deterministic compilation to [[Groq]], wafer-scale locality to [[Cerebras]], and HBM plus on-chip heterogeneity to [[HanaPino]].

## Counterevidence & Qualifications
The episode's numerical bandwidth-per-dollar gaps and model-size estimates are not third-party comparative benchmarks. Workload shape, quantization, batch size, context length, KV-cache compression, interconnect, software maturity, yield, and local electricity economics can all change the result. SRAM is therefore not a universal replacement for HBM, and decode is not the only inference phase that matters.

## What Changed
- Established a decode-specific extension of the wiki's broader memory-wall synthesis.
- Made batching, SRAM capacity, KV cache, MoE routing, and heterogeneous partitioning part of one system-level cost model.

## Related Concepts
- [[MemoryWall]] - broader compute-versus-data-movement bottleneck of which decode bandwidth is a specific case.
- [[AIDataCenterMemoryHierarchy]] - places SRAM, HBM, DRAM, and storage in one distance-capacity-cost hierarchy.
- [[HighBandwidthMemory]] - high-capacity near-compute memory used by general accelerators and HanaPino.
- [[HighThroughputInferenceBatching]] - utilization strategy that amortizes weight reads across concurrent requests.
- [[LowLatencyInferenceChip]] - specialization path that trades generality or capacity for faster token delivery.
- [[AIInferenceCostStructure]] - economic frame that converts architecture, utilization, and energy into token cost.
- [[MixtureOfExperts]] - runtime routing pattern that complicates static scheduling across chips.
