---
title: "存储三巨头破万亿市值，存储超级周期何时能见顶？｜ S10E13"
type: source
tags: [podcast, whats-next, ai, semiconductors, memory, storage]
sources: []
date: 2026-05-29
source_file: "/home/ken/repos/podcastatlas/content/episodes/存储三巨头破万亿市值，存储超级周期何时能见顶？｜ S10E13 [c47ff830-8cb5-4e58-b7d7-1a04e4e5a4c1].md"
source_url: "https://guiguzaozhidao.fireside.fm/20240427"
duration: "2679"
last_updated: 2026-07-12
---

## Summary
This [[WhatsNextKejiZaozhidao]] episode explains why AI infrastructure has pushed memory and storage into an [[AIStorageSupercycle]]. The discussion connects [[HighBandwidthMemory]], DRAM, NAND, advanced packaging, AI inference, and agent workflows into one supply-demand frame: data movement is becoming as important as raw accelerator compute. Its balanced claim is that AI demand, capital discipline, and [[MemoryCapacityLockIn]] can lengthen the upcycle, but [[StorageIndustryCyclicality]] has not disappeared.

## Key Claims
- AI server demand is redirecting memory supply away from consumer electronics, making phone and PC makers more exposed to DRAM and NAND price increases.
- The episode frames AI data-center storage as an [[AIDataCenterMemoryHierarchy]] from on-chip SRAM to [[HighBandwidthMemory]], DRAM, NAND SSDs, and hard drives.
- The core technical bottleneck is the [[MemoryWall]]: accelerator compute can scale faster than data movement, so interconnect, memory bandwidth, and latency shape system throughput.
- Inference can be more memory-hungry than training because long contexts and KV cache raise memory pressure as model use shifts from training runs toward production use.
- HBM scarcity is tied not only to memory dies, but also to [[TSMC]] CoWoS-style advanced packaging capacity and the memory capacity bundled into each [[Nvidia]] accelerator generation.
- [[SKHynix|SK Hynix]], [[Samsung]], and [[MicronTechnology]] are described as the main overseas HBM suppliers, with SK Hynix leading the source's cited HBM3E market and Samsung and Micron contesting later-generation shares.
- [[StorageIndustryCyclicality]] remains rooted in capital intensity, standardized products, lagged capacity, full-utilization incentives, and inventory swings.
- This cycle differs from older PC or smartphone cycles because DRAM, HBM, and NAND demand are rising together while AI server customers can absorb higher component prices than low-margin phone makers.
- Long-term agreements have changed meaning: the episode says some domestic deals lock volume without locking price, while overseas customers may pay deposits or help fund capacity to secure future supply.
- Algorithmic efficiency and memory-compression improvements do not automatically reduce total demand; the source uses a [[JevonsParadoxInAI]] logic where cheaper or more efficient inference can unlock more context and more workloads.
- [[Nvidia]] CMX-style NAND plus DPU designs, [[Google]] CXL memory pooling, and [[Semiconductor3DStacking]] are presented as utilization and hierarchy strategies, not clean replacements for HBM.
- [[Cerebras]] is treated as a differentiated wafer-scale inference route whose SRAM-centric design can fit specific workloads but does not replace general GPU clusters.
- [[AgentEraNANDStorage]] is the episode's distinctive storage claim: long agent workflows need intermediate state saved and recoverable, making NAND part of the inference process rather than only the final-output store.
- [[SanDisk]]'s [[HighBandwidthFlash]] is presented as a promising but limited NAND-derived direction because capacity and cost are attractive, while endurance, heat, and KV-cache latency still constrain substitution for HBM.
- [[ChangXinMemory]] and [[YangtzeMemoryTechnologies]] represent the domestic Chinese memory branch: ChangXin is tied to DRAM and possible HBM work, while Yangtze Memory is tied to NAND.

## Key Quotes
> "AI 抢走内存" - opening shorthand for the consumer-electronics shortage.

> "锁量不锁价" - the domestic long-agreement pattern described by the guest.

> "弱化了存储行业的周期性" - the episode's caveat that AI changes the cycle without abolishing it.

## Connections
- [[WhatsNextKejiZaozhidao]] - show context for the S10E13 AI infrastructure episode.
- [[AIStorageSupercycle]], [[StorageIndustryCyclicality]], and [[MemoryCapacityLockIn]] - market-cycle frame.
- [[AIDataCenterMemoryHierarchy]], [[MemoryWall]], [[HighBandwidthMemory]], [[HighBandwidthFlash]], [[CXLMemoryPooling]], and [[AgentEraNANDStorage]] - technical storage and memory architecture branch.
- [[SKHynix]], [[Samsung]], [[MicronTechnology]], [[SanDisk]], [[ChangXinMemory]], and [[YangtzeMemoryTechnologies]] - supplier branch.
- [[Nvidia]], [[Google]], [[TSMC]], [[Cerebras]], [[Huawei]], [[Alibaba]], [[Apple]], and [[Xiaomi]] - platform, packaging, domestic supply, and customer-allocation context.
- [[AIHardwareSupplyChainPressure]], [[MemoryChipShortage]], [[AIInferenceCostStructure]], [[AIComputeContinuity]], and [[StrategicAIInfrastructureDependence]] - broader AI infrastructure branch.

## Contradictions
- No direct factual contradiction found with existing wiki content.
- The source reinforces [[MemoryChipShortage]] but shifts the explanation from archive and hard-drive scarcity toward DRAM/HBM/NAND allocation inside AI infrastructure.
- The source qualifies [[HighBandwidthMemory]] and [[AIHardwareSupplyChainPressure]] by arguing that NAND, CXL memory pools, SRAM stacking, and wafer-scale designs improve the hierarchy but do not remove HBM demand in the near term.
