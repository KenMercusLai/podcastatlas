---
title: "Per-Head Muon"
type: concept
tags: [ai, optimization, training, model-architecture]
sources: [xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]
last_updated: 2026-08-08
---

# Per-Head Muon

Per-Head Muon is the optimizer variation described in [[xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]] as part of [[KimiK3|Kimi K3]]'s training recipe. The source explains Muon as an optimizer that approximately orthogonalizes momentum before applying updates, reducing the chance that learning collapses into a few dominant directions.

K3's source-specific extension is to apply that logic per attention head. [[ZengZhiyuan]] says per-head treatment can keep different attention heads' update scales more balanced, while [[ZhaoChenyang]] points to implementation difficulty around fused QKV tensors, distributed optimizer state, communication, and orthogonalization pipelines.

## Key Claims
- Optimizer design affects whether large training runs stay stable and make useful long-term parameter updates.
- Per-head orthogonalization can reduce imbalance among attention heads.
- The implementation is an infrastructure problem as much as an algorithm problem because model parallelism and optimizer state are distributed.
- Optimizer research is a promising AI-agent domain because experiments are structured, measurable, and easier to automate than open-ended discovery.

## Connections
- [[KimiK3]], [[AttentionResidues]], [[KimiDeltaAttention]], and [[TransformerArchitecture]] — model architecture and optimization context.
- [[ModelInfraCoDesign]], [[FrontierModelScaling]], and [[MLCoding]] — training-infrastructure context.
- [[KernelDevelopmentAgents]], [[RecursiveSelfImprovement]], and [[AICodingVerification]] — AI-assisted research and verification branch.
