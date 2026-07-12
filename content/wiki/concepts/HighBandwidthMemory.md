---
title: "High Bandwidth Memory"
type: concept
tags: [ai, semiconductors, memory, infrastructure]
sources: [tech-20251219-1219-mp-tech-pod-128-tech-20251219-1219-mp-tech-pod-128, cunchu-sanjutou-po-wanyi-shizhi-cunchu-chaoji-zhouqi-heshi-neng-jianding-s10e13-c47ff830-8cb5-4e58-b7d7-1a04e4e5a4c1]
last_updated: 2026-07-12
---

# High Bandwidth Memory

High bandwidth memory is the fast memory category discussed in [[tech-20251219-1219-mp-tech-pod-128-tech-20251219-1219-mp-tech-pod-128]] as a critical companion to AI processors. [[AnitaRamaswamy]] uses [[MicronTechnology]] to explain that AI workloads need memory close to accelerators, making HBM a less visible but important part of the AI data-center stack.

The source's concrete comparison is scale: it describes Nvidia's GB200 as having 192 gigabytes of memory per chip, versus roughly 16 to 20 gigabytes in many consumer laptops. That makes [[HighBandwidthMemory]] part of [[AIHardwareSupplyChainPressure]] rather than merely a component specification.

[[cunchu-sanjutou-po-wanyi-shizhi-cunchu-chaoji-zhouqi-heshi-neng-jianding-s10e13-c47ff830-8cb5-4e58-b7d7-1a04e4e5a4c1]] adds the architecture and market-cycle detail. The source places HBM inside an [[AIDataCenterMemoryHierarchy]], says HBM scarcity is tied to [[Nvidia]] accelerator demand and [[TSMC]] advanced packaging capacity, and contrasts HBM with [[HighBandwidthFlash]], [[CXLMemoryPooling]], and NAND+DPU prefetching routes that improve utilization without replacing HBM.

## Key Claims
- AI acceleration depends on fast memory as well as GPUs or model software.
- HBM demand can lift memory suppliers such as [[MicronTechnology]], [[SKHynix]], and [[Samsung]] when AI data-center buildout accelerates.
- Memory capacity and bandwidth can become bottlenecks for training and inference economics.
- AI demand can spill into consumer markets by changing storage supply, product focus, and pricing.
- HBM demand is intensified by inference and long-context KV cache, not only training.
- Alternative memory architectures can reduce pressure at the margins but do not remove HBM from the hottest low-latency layer in the source's view.

## Connections
- [[MicronTechnology]] - main company case in the source.
- [[Nvidia]] - AI chip platform used for the GB200 memory comparison.
- [[SKHynix]] and [[Samsung]] - peer suppliers named in the episode.
- [[AIHardwareSupplyChainPressure]] - broader supply-chain implication.
- [[AIComputeContinuity]] and [[MaaSInfrastructure]] - infrastructure branches that depend on available hardware.
- [[AIDataCenterMemoryHierarchy]], [[MemoryWall]], [[HighBandwidthFlash]], and [[CXLMemoryPooling]] - architecture branches added by the What's Next source.
- [[AIStorageSupercycle]], [[StorageIndustryCyclicality]], and [[MemoryCapacityLockIn]] - market-cycle branches added by the What's Next source.
