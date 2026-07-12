---
title: "High Bandwidth Flash"
type: concept
tags: [ai, storage, nand, semiconductors]
sources: [cunchu-sanjutou-po-wanyi-shizhi-cunchu-chaoji-zhouqi-heshi-neng-jianding-s10e13-c47ff830-8cb5-4e58-b7d7-1a04e4e5a4c1]
last_updated: 2026-07-12
---

# High Bandwidth Flash

High Bandwidth Flash is the NAND-derived memory direction discussed in [[cunchu-sanjutou-po-wanyi-shizhi-cunchu-chaoji-zhouqi-heshi-neng-jianding-s10e13-c47ff830-8cb5-4e58-b7d7-1a04e4e5a4c1]] through [[SanDisk]]. The source frames it as an attempt to bring much larger and cheaper capacity closer to AI systems while offering higher bandwidth and lower latency than ordinary NAND storage.

The source's strongest distinction is between model parameters and active inference state. HBF may be useful for holding large model parameters or datasets, but the guest argues that KV cache and hottest computation still need [[HighBandwidthMemory]] because NAND endurance, heat tolerance, and latency limits remain material.

## Key Claims
- HBF may offer much larger capacity than HBM at lower cost.
- Its appeal grows when AI systems need larger datasets, bigger models, and longer contexts.
- HBF does not remove HBM demand because active low-latency inference and KV cache remain demanding.
- NAND erase endurance and AI board thermal constraints are central limitations.

## Connections
- [[SanDisk]] - company tied to HBF in the source.
- [[AgentEraNANDStorage]] - broader NAND role in agent-era inference.
- [[HighBandwidthMemory]], [[AIDataCenterMemoryHierarchy]], and [[MemoryWall]] - comparison and bottleneck context.
- [[AIStorageSupercycle]] - market demand frame.
