---
title: "MOPD Post-Training"
type: concept
tags: [ai, post-training, distillation, agents]
sources: [xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]
last_updated: 2026-08-08
---

# MOPD Post-Training

MOPD post-training is the source-scoped recipe described in [[xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]] for merging domain-specialized expert models back into one model. The episode says [[KimiK3|Kimi K3]] first trains nine domain expert models, then uses MOPD to combine their capabilities.

The operational reason is team modularity. Coding agents, general agents, and generalist behavior can require different data, environments, reward strategies, rollout lengths, harnesses, and algorithms. MOPD lets domain teams deliver trained expert models without forcing every post-training recipe and infrastructure component into one shared pipeline.

## Key Claims
- Post-training can be organized around domain expert models before a later merge step.
- The recipe reduces coordination cost across teams working on different agent or reasoning domains.
- In this source, distillation is not only model compression; it is also a way to transfer multiple teacher capabilities into one student model.
- MOPD makes [[ModelHarnessCoEvolution]] organizational: each domain's harness and reward design can evolve before capabilities are merged.

## Connections
- [[KimiK3]], [[ModelDistillation]], [[OnPolicyDistillation]], and [[AgentPostTraining]] — source post-training context.
- [[AgentRL]], [[AgentHarness]], [[ModelHarnessCoEvolution]], and [[AIVerification]] — environment and evaluation implications.
- [[ZengZhiyuan]] and [[ZhaoChenyang]] — guests explaining the workflow.
