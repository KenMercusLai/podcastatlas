---
title: "Kimi Delta Attention / KDA"
type: concept
tags: [ai, model-architecture, inference, long-context]
sources: [xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]
last_updated: 2026-08-08
---

# Kimi Delta Attention / KDA

Kimi Delta Attention / KDA is the linear-attention mechanism discussed in [[xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]] as a central part of [[KimiK3|Kimi K3]]'s architecture. The source says K3 replaces most attention layers with KDA while periodically retaining global attention, producing a hybrid design rather than a pure full-attention or pure linear-attention model.

The tradeoff is memory efficiency versus state complexity. KDA compresses long history into recurrent state, reducing the cache and memory movement that make million-token contexts expensive, but that state can be overwritten rather than simply appended like a traditional KV cache. This makes [[PrefixCaching]], speculative sampling, rollback, and serving-engine implementation harder.

The source frames KDA as an engineering validation of linear attention at frontier-adjacent scale. It does not claim fixed-state attention solves long-context forgetting by itself; the episode says K3's retained global attention and hybrid structure are important for preserving access to older detail.

## Key Claims
- KDA makes long-context inference cheaper by keeping much of history in fixed or slowly growing recurrent state.
- K3's reported pattern is roughly three KDA layers followed by one global-attention layer.
- KDA complicates prefix reuse because recurrent state is mutable rather than append-only.
- Speculative sampling needs special rollback handling when intermediate KDA states have already been updated.
- The mechanism raises the value of [[ModelInfraCoDesign]] because model architecture, cache lifecycle, kernels, and serving engine have to line up.

## Connections
- [[KimiK3]], [[KimiLinear]], and [[MoonshotAI]] — model family and source context.
- [[AgentInferenceWorkload]], [[AIInferenceCostStructure]], [[PrefixCaching]], and [[InferenceAccelerationStack]] — serving-cost branch.
- [[NoPositionEncoding]], [[AttentionResidues]], and [[TransformerArchitecture]] — adjacent architecture changes.
- [[ModelInfraCoDesign]], [[OpenSourceAIInfrastructure]], and [[VLLM|vLLM]] — infrastructure implications.
