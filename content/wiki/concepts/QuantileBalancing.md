---
title: "Quantile Balancing"
type: concept
tags: [ai, model-architecture, moe, training]
sources: [xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]
last_updated: 2026-08-08
---

# Quantile Balancing

Quantile balancing is the [[MixtureOfExperts|MoE]] routing-stability method discussed in [[xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]]. The source says [[KimiK3|Kimi K3]] routes each token to a small number of experts from a very large pool, making expert-load balance a core training-stability issue.

The episode contrasts quantile balancing with earlier auxiliary load-balancing losses and fixed-step bias-update methods associated with [[DeepSeek]]-style MoE. Quantile balancing estimates bias adjustments from routing-score quantiles, aiming to rebalance expert load without adding a direct quality-versus-balance loss term or hand-tuning a fixed update step.

## Key Claims
- Sparse MoE models can fail or underperform if routing concentrates too much traffic on a subset of experts.
- Auxiliary balancing losses can trade off model quality against load balance.
- Fixed-step bias updates reduce that tradeoff but still need hyperparameter tuning.
- Quantile-based updates use score distribution information to choose adjustment size more directly.
- The source treats the method as one likely reason K3 could scale its sparse expert design.

## Connections
- [[KimiK3]], [[MixtureOfExperts]], and [[DeepSeek]] — model and comparison context.
- [[ModelInfraCoDesign]], [[AIClusterNetworking]], and [[FrontierModelScaling]] — scaling and infrastructure implications.
- [[ZengZhiyuan]], [[PerHeadMuon]], and [[AttentionResidues]] — source's technical explanation cluster.
