---
title: "Kimi Delta Attention / KDA"
type: concept
tags: [ai, model-architecture, inference, long-context]
sources:
  - xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1
  - 152-lingdu-kimi-k3-jishu-baogao-cong-jiagou-chuangxin-liaoqi-zhuyili-meixue-duojiaoshi-zhengliu-he-kaiyuan-moe-lrvngxoafcz7vzh8hywulkwnb6n6
last_updated: 2026-08-26
knowledge_schema: synthesis-v1
---

# Kimi Delta Attention / KDA

## Definition
Kimi Delta Attention / KDA is the Kimi-family linear-attention mechanism used in [[KimiK3|Kimi K3]] as part of a hybrid attention architecture that alternates recurrent linear-attention state with periodic global attention.

## Current Synthesis
KDA's current wiki role is to show that long-context efficiency is becoming an architecture-and-kernel problem. The earlier LateTalk source frames KDA as a way to reduce KV-cache and memory movement for long contexts while complicating prefix reuse, rollback, and serving implementation. The newer Zhang Xiaojun technical reading gives the mechanism a more explicit lineage: RetNet-like decay, DeltaNet capacity, Gated DeltaNet, then KDA's channelized decay. KDA is therefore not only "linear attention at scale"; it is a constrained design where stronger recurrence, numerical range control, chunk/tile kernels, global-attention retention, and inference-engine state management have to work together.

## Key Claims
- KDA lowers long-context memory pressure by compressing much of the sequence history into recurrent state rather than a conventional full KV cache.
- K3 remains hybrid: retained global attention is important because fixed or compressed recurrent state alone can lose detail.
- Channelized decay gives KDA more expressive control over how different channels remember or forget context.
- KDA's kernel feasibility depends on numerical and tiling constraints, including decay bounds that keep computation inside practical low-precision ranges.
- Mutable recurrent state makes [[PrefixCaching]], speculative decoding rollback, and serving-engine support harder than append-only KV-cache handling.
- KDA raises the value of [[ModelInfraCoDesign]] because the mathematical form, kernel, cache lifecycle, and inference stack cannot be optimized separately.

## Evidence
- Hybrid long-context design: [[xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]] describes KDA plus periodic global attention as K3's long-context architecture and explicitly ties it to prefix caching and rollback challenges.
- Lineage and channelized decay: [[152-lingdu-kimi-k3-jishu-baogao-cong-jiagou-chuangxin-liaoqi-zhuyili-meixue-duojiaoshi-zhengliu-he-kaiyuan-moe-lrvngxoafcz7vzh8hywulkwnb6n6]] traces KDA through RetNet, DeltaNet, Gated DeltaNet, and channelized decay.
- Kernel co-design: [[152-lingdu-kimi-k3-jishu-baogao-cong-jiagou-chuangxin-liaoqi-zhuyili-meixue-duojiaoshi-zhengliu-he-kaiyuan-moe-lrvngxoafcz7vzh8hywulkwnb6n6]] emphasizes lower-bound decay, tile/chunk ranges, BF16 practicality, and context-parallel chunking as part of why KDA is implementable.

## Counterevidence & Qualifications
KDA does not eliminate all long-context problems. The sources preserve a hybrid design because global attention still helps retrieve older detail, and they treat serving support as a real complication rather than a solved afterthought. KDA's benefit is also hardware- and implementation-dependent: a stronger formula can be unattractive if kernels, prefix cache behavior, or speculative decoding rollback become too expensive.

## What Changed
- Adds the RetNet-to-DeltaNet-to-Gated-DeltaNet lineage behind KDA.
- Makes channelized decay and kernel/numerical constraints part of the current KDA synthesis.
- Separates KDA's memory advantage from a broader claim that linear attention alone solves long-context retrieval.

## Related Concepts
- [[KimiK3]] - model case where KDA is scaled and discussed.
- [[KimiLinear]] - predecessor context for Kimi's linear-attention direction.
- [[NoPositionEncoding]] - complementary long-context design that relies partly on recurrent state for order and recency.
- [[PrefixCaching]] - serving optimization complicated by mutable KDA state.
- [[InferenceAccelerationStack]] - runtime layer affected by KDA kernels and cache lifecycle.
- [[ModelInfraCoDesign]] - co-design frame that KDA exemplifies.
- [[TransformerArchitecture]] - broader architecture family whose components KDA modifies.
