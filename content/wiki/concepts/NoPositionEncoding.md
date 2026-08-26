---
title: "NoPE / No Position Encoding"
type: concept
tags: [ai, model-architecture, long-context]
sources:
  - xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1
  - 152-lingdu-kimi-k3-jishu-baogao-cong-jiagou-chuangxin-liaoqi-zhuyili-meixue-duojiaoshi-zhengliu-he-kaiyuan-moe-lrvngxoafcz7vzh8hywulkwnb6n6
last_updated: 2026-08-26
knowledge_schema: synthesis-v1
---

# NoPE / No Position Encoding

## Definition
NoPE / no position encoding is a model-architecture pattern that removes or minimizes explicit positional encodings, relying instead on surrounding attention state, recurrence, decay, and training dynamics to carry order and recency information.

## Current Synthesis
In the Kimi K3 cluster, NoPE is not treated as a standalone trick. It works because [[KimiDeltaAttention|KDA]] recurrent state and decay already encode sequence-order information, while periodic full attention supplies global access. The earlier source emphasized that [[KimiLinear]] had already used NoPE and that K3 scaled the broader design to a much larger hybrid architecture. The new technical reading adds the rationale for removing RoPE in the full-attention part of a hybrid model: if linear attention already provides position and recency signals, explicit rotary parameters can make million-token extension less natural and may mostly add recency bias rather than true long-context capacity.

## Key Claims
- NoPE shifts positional information from explicit embeddings toward recurrent state, gating, decay, and learned attention behavior.
- The pattern depends heavily on the surrounding architecture; KDA and periodic global attention are part of why NoPE can be plausible in K3.
- Removing RoPE can make context extension simpler because the model avoids length-specific rotary parameter adjustment.
- NoPE does not by itself guarantee long-context recall; memory capacity, training curriculum, retained global attention, and serving support still matter.
- In K3, NoPE is best read as part of a hybrid long-context recipe rather than a general rejection of position information.

## Evidence
- Kimi lineage: [[xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]] says K3 mostly removes explicit position encoding and relates that choice to KDA, gating, decay, [[KimiLinear]], and million-token context extension.
- RoPE tradeoff: [[152-lingdu-kimi-k3-jishu-baogao-cong-jiagou-chuangxin-liaoqi-zhuyili-meixue-duojiaoshi-zhengliu-he-kaiyuan-moe-lrvngxoafcz7vzh8hywulkwnb6n6]] argues that full-attention NoPE in a hybrid model can ease long-context scaling because the linear-attention part already carries position information.
- Recency qualification: [[152-lingdu-kimi-k3-jishu-baogao-cong-jiagou-chuangxin-liaoqi-zhuyili-meixue-duojiaoshi-zhengliu-he-kaiyuan-moe-lrvngxoafcz7vzh8hywulkwnb6n6]] treats RoPE mainly as a recency-bias mechanism and warns that it may not directly improve long-context capacity.

## Counterevidence & Qualifications
The sources do not claim that explicit position encodings are obsolete across all model families. NoPE's apparent value in K3 is tied to KDA, hybrid attention, training scale, and infrastructure choices. A model without adequate recurrence, global attention, data curriculum, or serving support could lose positional reliability even if explicit position encodings are removed.

## What Changed
- Adds the full-attention NoPE rationale from the K3 technical reading.
- Clarifies that NoPE's role is to reduce long-context friction in a hybrid architecture, not to deny the need for order information.
- Narrows RoPE discussion to source-scoped claims about recency bias and length extrapolation.

## Related Concepts
- [[KimiDeltaAttention]] - recurrent attention mechanism that carries much of NoPE's order signal in K3.
- [[KimiK3]] - model case where NoPE is scaled to million-token context.
- [[KimiLinear]] - earlier Kimi-family model associated with NoPE use.
- [[AttentionResidues]] - adjacent architecture change in the K3 stack.
- [[TransformerArchitecture]] - broader architecture family whose positional mechanisms NoPE modifies.
- [[ModelInfraCoDesign]] - runtime and training frame needed to make long-context architecture deployable.
