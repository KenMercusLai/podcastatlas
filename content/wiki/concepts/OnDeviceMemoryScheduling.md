---
title: "On-Device Memory Scheduling"
type: concept
tags: [ai, edge-ai, systems, memory]
sources: [weishenme-guigu-kaishi-zhongxin-dingyi-ai-jiyi-s10e20-a70c41aa-41ae-488d-a6e2-63c3de5b9ec3]
last_updated: 2026-07-09
---

# On-Device Memory Scheduling

On-device memory scheduling is the systems problem [[KangHongwen]] emphasizes in [[weishenme-guigu-kaishi-zhongxin-dingyi-ai-jiyi-s10e20-a70c41aa-41ae-488d-a6e2-63c3de5b9ec3]]. A local AI memory system cannot assume a dedicated cloud server. It must share CPU, GPU, NPU, memory, storage, and thermal budget with the user's active applications.

The source treats this as a major reason local memory is harder than a simple local-model demo. The system needs to detect device configuration, foreground app state, available compute, current user experience, model/task priority, and whether work should happen locally, pause, or fall back to cloud assistance.

## Key Claims
- Local memory products must schedule perception, indexing, retrieval, summarization, and agent tasks without making the user's computer feel slow or unstable.
- Device heterogeneity makes edge AI harder than server-side AI: different Macs, Windows PCs, chips, memory sizes, drivers, and workloads create different constraints.
- Model optimization, operator-level tuning, and chip-specific adaptation can become product requirements when local AI is not yet mature.
- [[EdgeCloudAIBoundary]] decisions are dynamic: local first does not mean local only when the device lacks enough compute for a task.

## Connections
- [[CliptoAI]] and [[KangHongwen]] — product and speaker case.
- [[OnDeviceAI]] and [[EdgeCloudAIBoundary]] — broader device/cloud systems frame.
- [[LocalFirstMemoryLayer]] and [[MultimodalPersonalMemory]] — memory architecture that creates the scheduling need.
- [[AIInferenceCostStructure]] — cloud cost pressure that can make local scheduling valuable.
- [[AgentPermissionBoundaries]] — adjacent issue because local memory systems may have broad file and device access.
