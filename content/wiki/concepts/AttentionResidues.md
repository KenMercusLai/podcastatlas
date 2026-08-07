---
title: "Attention Residues"
type: concept
tags: [ai, model-architecture, training]
sources: [xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]
last_updated: 2026-08-08
---

# Attention Residues

Attention Residues are described in [[xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]] as [[KimiK3|Kimi K3]]'s mechanism for improving information flow across model depth. The source says ordinary residual connections add shallow-layer outputs into deeper layers, but as models get deeper, newly written information can be diluted by accumulated residual streams.

The source's interpretation is that Attention Residues rotate attention from the sequence direction into the layer direction. Instead of every deeper layer receiving a simple sum of earlier representations, it can selectively read shallower-layer information, which may preserve useful features more flexibly.

## Key Claims
- Attention Residues address depth-wise information flow, not only long-context sequence flow.
- The mechanism is compared with other multi-stream or compressed-residual approaches but is described as more attention-like and selective.
- Its upside is higher expressive capacity; its practical value still depends on implementation and training stability.
- In the episode's broader frame, Attention Residues are one reason "Transformer" now covers a family of heavily modified architectures.

## Connections
- [[KimiK3]], [[KimiDeltaAttention]], and [[NoPositionEncoding]] — K3 architecture branch.
- [[TransformerArchitecture]], [[FrontierModelScaling]], and [[ModelInfraCoDesign]] — model-design context.
- [[ZengZhiyuan]] and [[ZhaoChenyang]] — guests explaining the architecture.
- [[MixtureOfExperts]], [[QuantileBalancing]], and [[PerHeadMuon]] — adjacent scaling and stability mechanisms.
