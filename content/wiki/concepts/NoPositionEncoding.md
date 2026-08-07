---
title: "NoPE / No Position Encoding"
type: concept
tags: [ai, model-architecture, long-context]
sources: [xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]
last_updated: 2026-08-08
---

# NoPE / No Position Encoding

NoPE / no position encoding is discussed in [[xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]] as part of [[KimiK3|Kimi K3]]'s long-context architecture. [[ZengZhiyuan]] says K3 mostly removes explicit positional encoding and relies on [[KimiDeltaAttention|KDA]] recurrent state, gating, and decay to carry order and recency information implicitly.

The source says NoPE is not new to K3; [[KimiLinear]] had already used it. The significance is that K3 scales the broader design to a much larger model while combining it with hybrid attention, [[AttentionResidues]], and progressive context extension toward million-token contexts.

## Key Claims
- NoPE removes or minimizes explicit position embeddings rather than treating absolute or rotary position as the main order signal.
- KDA's recurrent state and decay can encode sequence order and recency implicitly.
- NoPE's value is tied to the surrounding architecture; it should not be evaluated as an isolated trick.
- Long-context capability still depends on memory capacity, global attention, training curriculum, and serving infrastructure.

## Connections
- [[KimiK3]], [[KimiLinear]], [[KimiDeltaAttention]], and [[AttentionResidues]] — source architecture context.
- [[AgentInferenceWorkload]], [[AIInferenceCostStructure]], and [[LongHorizonAI]] — long-context and agent-workload context.
- [[ModelInfraCoDesign]] and [[InferenceAccelerationStack]] — runtime implications.
