---
title: "Tiered On-Device Sensing / 分层端侧感知"
type: concept
tags: [ai, edge-ai, sensors, wearables, hardware]
sources:
  - no-221-leiniao-ceo-xinjishu-yuelaiyueduo-women-weishenme-hai-xuyao-yifu-zhineng-yanjing-gkwridon6uwmaoosszqset9vd
last_updated: 2026-09-10
knowledge_schema: synthesis-v1
---

# Tiered On-Device Sensing / 分层端侧感知

## Definition
Tiered on-device sensing is a low-power architecture where small sensors and chips continuously monitor for simple signals, then wake larger local or cloud compute only when a scene requires richer perception, recording, or reasoning.

## Current Synthesis
The RayNeo source uses always-on camera as the concrete case. [[LiHongwei|李鸿伟]] says a small camera-side CNN can sample frames at low frequency, a simpler chip can recognize notable scenes, and a larger chip can wake for video or complex processing only when needed.

The concept matters because AI glasses have less battery, space, thermal headroom, and social tolerance than phones. It links [[EdgeCloudAIBoundary]] to product fit: without local filtering and wake-up logic, [[FirstPersonAIMemory]] becomes either too power-hungry, too cloud-dependent, or too privacy-invasive for daily wear.

## Key Claims
- Always-on wearable AI requires local filtering before heavy model calls.
- The architecture separates low-frequency perception, simple scene detection, and expensive recording or reasoning.
- Power, heat, and battery constraints make sensing hierarchy a product requirement, not only an engineering optimization.
- Trigger design shapes privacy and data minimization because not every moment should become stored or cloud-processed data.
- The concept is source-scoped to RayNeo's described architecture until supported by additional implementations.

## Evidence
- Three-layer scheme - [[no-221-leiniao-ceo-xinjishu-yuelaiyueduo-women-weishenme-hai-xuyao-yifu-zhineng-yanjing-gkwridon6uwmaoosszqset9vd]] describes camera-side CNN sampling, simple-chip scene recognition, and larger-chip escalation.
- Battery constraint - [[no-221-leiniao-ceo-xinjishu-yuelaiyueduo-women-weishenme-hai-xuyao-yifu-zhineng-yanjing-gkwridon6uwmaoosszqset9vd]] presents the design as a way to support Live Log despite small glasses batteries.
- Chip logic - [[no-221-leiniao-ceo-xinjishu-yuelaiyueduo-women-weishenme-hai-xuyao-yifu-zhineng-yanjing-gkwridon6uwmaoosszqset9vd]] later links glasses chips to extreme low power, small/large core design, RTOS, and possible low-power islands.

## Counterevidence & Qualifications
The source gives an architectural description but not measured battery life, false-positive rates, privacy safeguards, or external verification of RayNeo's implementation.

## What Changed
- Created the concept from the No.221 RayNeo interview.

## Related Concepts
- [[EdgeCloudAIBoundary]] - broader split between local and cloud AI work.
- [[OnDeviceAI]] - local execution layer used by tiered sensing.
- [[FirstPersonAIMemory]] - memory use case that depends on sensing hierarchy.
- [[AIGlassesProductFit]] - product-fit question shaped by battery and latency.
- [[AIHardwarePrivacyExchange]] - privacy tradeoff affected by local filtering.
