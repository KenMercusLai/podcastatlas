---
title: "Local AI Hardware Selection"
type: concept
knowledge_schema: synthesis-v1
tags: [ai, local-ai, hardware]
sources:
  - ep-38-the-local-ai-stack-nobody-talks-about-but-should
last_updated: 2026-09-13
---

# Local AI Hardware Selection

## Definition
Local AI hardware selection is the practice of choosing on-device AI hardware by matching model memory needs, memory bandwidth, accelerator software support, physical constraints, and workload expectations.

## Current Synthesis
The episode turns local AI hardware choice into a memory-first decision. [[TrentRossiter]] treats VRAM or unified memory as the primary constraint because model weights, context, and KV cache must fit before speed matters. The next layer is memory throughput and software-stack compatibility: [[CUDA]], [[ROCm]], and [[AppleMetal|Metal]] shape what tools and models run easily. Form factor, heat, noise, power, and office practicality then decide whether the machine is usable in everyday personal or small-business settings.

## Key Claims
- Memory capacity is the first local AI constraint because models, context, and KV cache must fit in fast accessible memory.
- Memory throughput matters after capacity because equal memory sizes can deliver different inference performance.
- Consumer gaming GPUs can be fast but may be limited by VRAM, heat, power draw, size, and noise.
- Unified-memory machines can make larger local workloads possible, especially when compact ownership matters.
- Software-stack compatibility can outweigh raw specs when the user's clients, tools, or containers expect [[CUDA]], [[ROCm]], or [[AppleMetal|Metal]].
- Hardware selection should be scoped to realistic local use cases rather than assuming a workstation replaces frontier cloud infrastructure.

## Evidence
### Memory-first selection
- [[ep-38-the-local-ai-stack-nobody-talks-about-but-should]] says Rossiter identifies VRAM as the single most important metric because models, context, and KV cache are loaded into memory.

### Consumer GPU limits
- [[ep-38-the-local-ai-stack-nobody-talks-about-but-should]] says gaming GPUs can be fast but expensive, power-hungry, hot, physically large, and often limited to 16 GB or 24 GB of VRAM.

### Unified memory and compatibility
- [[ep-38-the-local-ai-stack-nobody-talks-about-but-should]] describes Apple-style unified memory, AMD integrated architectures, and Rossiter's choice of [[NvidiaDGXSpark]] for 128 GB unified memory plus [[CUDA]] support.

### Practical ownership
- [[ep-38-the-local-ai-stack-nobody-talks-about-but-should]] says compact unified-memory systems can reduce heat, power, noise, and office friction compared with large gaming-style machines.

## Counterevidence & Qualifications
- The source does not provide formal benchmarks, model-by-model memory tables, or price-performance comparisons.
- Hardware recommendations are time-sensitive because model architectures, quantization, framework support, and component prices change quickly.
- More local memory does not solve privacy, permissions, retrieval quality, or agent safety by itself.

## What Changed
- Created a hardware-selection concept for local AI centered on memory capacity, throughput, stack compatibility, and physical practicality.

## Related Concepts
- [[LocalAIWorkstation]] - deployment surface where the hardware choice matters.
- [[LocalAIPrivacyTradeoff]] - adoption reason that can justify buying local hardware.
- [[LocalAIFrameworkStack]] - software layer that must fit the hardware.
- [[AIInferenceCostStructure]] - cost pressure local hardware can address or worsen.
- [[ModelInfraCoDesign]] - broader relationship between models, runtimes, and hardware.
- [[AgentPermissionBoundaries]] - safety layer hardware alone does not solve.
