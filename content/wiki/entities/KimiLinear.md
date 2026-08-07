---
title: "Kimi Linear"
type: entity
tags: [ai, model, architecture]
sources: [xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]
last_updated: 2026-08-08
---

# Kimi Linear

Kimi Linear appears in [[xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]] as the smaller-model predecessor whose experiments informed [[KimiK3|Kimi K3]]'s hybrid attention design. The source says the three-to-one pattern of KDA layers to Gated MLA layers came mainly from Kimi Linear-scale experiments rather than from a full search at K3's reported 3T scale.

The page matters because Kimi Linear turns K3 from an isolated release into a scaling case. [[KimiDeltaAttention|KDA]], [[NoPositionEncoding|NoPE]], and long-context efficiency are presented as ideas tested at smaller scale, then carried into a much larger open-weight model with new serving and training challenges.

## Connections
- [[Kimi]], [[KimiK3]], and [[MoonshotAI]] — model family and company context.
- [[KimiDeltaAttention]], [[NoPositionEncoding]], and [[ModelInfraCoDesign]] — architecture and scale-up branch.
- [[AIInferenceCostStructure]], [[AgentInferenceWorkload]], and [[InferenceAccelerationStack]] — long-context serving context.
