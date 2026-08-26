---
title: "Kimi K3"
type: entity
tags: [ai, model, china, coding]
sources:
  - zhengliu-fengbao-yichang-wuren-gongkai-tanlun-de-jishu-jingsai-1-179-1
  - zhizhuxia-xinpian-naxia-jinban-guonei-piaofang-ai-moxing-baofa-jiagezhan-1004403588
  - xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1
  - e246-hewei-zhengliu-liaoliao-guigu-ruhe-kan-zhongguo-kaifang-moxing-bijin-qianyan-5fd236d7-9a72-4b15-9e84-e83ceadd1b41
  - yao-shunyu-laidao-tengxun-300tian-1-176-1
  - tech-20260731-0731-mp-tech-pod-128-tech-20260731-0731-mp-tech-pod-128
  - ai-bu-zhi-bi-zhishang-waic-he-kimi-k3-toulule-shenme-xin-jingzheng-1
  - guochan-ai-suanli-neng-ping-chaojiedian-wandao-chaoche-ma-waic-shendu-guancha-s10e23-a6c6ab3e-72b2-470b-aefd-04b19679d37f
  - 152-lingdu-kimi-k3-jishu-baogao-cong-jiagou-chuangxin-liaoqi-zhuyili-meixue-duojiaoshi-zhengliu-he-kaiyuan-moe-lrvngxoafcz7vzh8hywulkwnb6n6
last_updated: 2026-08-26
knowledge_schema: synthesis-v1
---

# Kimi K3

## Overview
Kimi K3 is a [[Kimi]] model/product from [[MoonshotAI|Moonshot AI / 月之暗面]] that the wiki tracks as a Chinese open-weight frontier-model pressure point and as a technical architecture case. Across the current source inventory, K3 sits at the intersection of open-weight release governance, model distillation accusations, enterprise cost routing, AI coding workflow fit, MoE scaling, long-context architecture, and infrastructure co-design.

## Current Profile
The current synthesis is that Kimi K3 should not be reduced to either "cheap open model" or "distilled closed model." The technical sources present it as a large hybrid MoE system built from [[KimiDeltaAttention|KDA]], Gated MLA, [[AttentionResidues]], [[NoPositionEncoding|NoPE]], [[LatentMoE]], [[QuantileBalancing]], optimizer and activation-stability choices, [[OnPolicyDistillation|OPD]], [[MultiTeacherDistillation]], and serving-stack work. The market and governance sources treat that capability as pressure on closed API economics, enterprise model sovereignty, and U.S.-China AI narratives, while keeping provenance accusations source-scoped because public evidence remains incomplete.

## Key Characteristics
- Large open-weight model case: K3 is treated as a full-weight release whose adoption and commercial terms matter for [[OpenSourceAIModels|open-model]] competition.
- Integrated architecture system: K3 combines hybrid linear attention, MoE routing, long-context design, optimizer/activation stability, and post-training methods rather than relying on one isolated trick.
- Workflow-fit model: hands-on coding and agent examples describe K3 as useful for long-running, specification-heavy tasks while still costly or slow for immediate interaction.
- Closed-model pressure point: K3 appears repeatedly as evidence that capable open weights can compress API pricing, weaken provider lock-in, and make local deployment more attractive.
- Distillation-governance flashpoint: K3 is named in public suspicion and debate, but the wiki keeps copying claims separate from proven technical provenance.
- Infrastructure stress test: K3's scale, hybrid attention, MoE communication, and long-context support make inference engines, kernels, accelerators, and cluster networking part of the model story.

## Evidence
- Open-weight and market pressure: [[e246-hewei-zhengliu-liaoliao-guigu-ruhe-kan-zhongguo-kaifang-moxing-bijin-qianyan-5fd236d7-9a72-4b15-9e84-e83ceadd1b41]] frames K3 as a Silicon Valley open-weight surprise; [[zhizhuxia-xinpian-naxia-jinban-guonei-piaofang-ai-moxing-baofa-jiagezhan-1004403588]] and [[tech-20260731-0731-mp-tech-pod-128-tech-20260731-0731-mp-tech-pod-128]] place it in price and U.S.-market-anxiety comparisons.
- Technical architecture: [[xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]] identifies KDA, Attention Residues, NoPE, quantile balancing, Per-Head Muon, MOPD, AgentIn, and kernel work as the K3 technical cluster; [[152-lingdu-kimi-k3-jishu-baogao-cong-jiagou-chuangxin-liaoqi-zhuyili-meixue-duojiaoshi-zhengliu-he-kaiyuan-moe-lrvngxoafcz7vzh8hywulkwnb6n6]] adds the paper-reading layer around 2.8T total parameters, roughly 100B active parameters, 1M context, Latent MoE, multi-teacher distillation, and detailed infra choices.
- Workflow fit and cost: [[ai-bu-zhi-bi-zhishang-waic-he-kimi-k3-toulule-shenme-xin-jingzheng-1]] reports a K3 coding-agent task that worked but consumed significant time and tokens; [[xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]] similarly separates long-running agent strength from small interactive latency needs.
- Competitive context: [[yao-shunyu-laidao-tengxun-300tian-1-176-1]] uses K3 as pressure on [[TencentHunyuan]] and Chinese model teams; [[zhengliu-fengbao-yichang-wuren-gongkai-tanlun-de-jishu-jingsai-1-179-1]] uses it in the broader distillation and Chinese open-model debate.
- Hardware and serving implications: [[guochan-ai-suanli-neng-ping-chaojiedian-wandao-chaoche-ma-waic-shendu-guancha-s10e23-a6c6ab3e-72b2-470b-aefd-04b19679d37f]] connects K3 scale to supernode and domestic accelerator constraints; [[152-lingdu-kimi-k3-jishu-baogao-cong-jiagou-chuangxin-liaoqi-zhuyili-meixue-duojiaoshi-zhengliu-he-kaiyuan-moe-lrvngxoafcz7vzh8hywulkwnb6n6]] details KDA context parallelism, dynamic expert parallelism, offloading, and inference-engine adaptation.

## Qualifications
K3's public sources do not make full model-development reproducibility available: open weights are not the same as released raw data, training recipe, full RL environment, verifier system, or expert checkpoints. Distillation claims remain source-scoped and should not be inferred from identity confusion, timing, or similarity alone. The hands-on workflow sources show practical capability but also latency, token-cost, and task-fit limits. The technical-report readings are interpretive source notes, so exact implementation details should be treated as grounded in those episodes unless separately verified from the paper or code.

## What Changed
- The new technical-report reading sharpens K3's profile from general open-weight pressure to effective 2.8T/100B-active/1M-context scaling.
- The synthesis now includes [[LatentMoE]] and [[MultiTeacherDistillation]] as distinct K3-relevant concepts.
- KDA, NoPE, MoE routing, and infra co-design are now framed as linked implementation choices rather than separate feature labels.
- The current judgment gives more weight to K3's cumulative architecture-and-systems integration while preserving the earlier governance and market qualifications.

## Relationships
- [[MoonshotAI]] - developer/company context for the Kimi and K3 model line.
- [[Kimi]] - parent product/model family.
- [[KimiLinear]] - predecessor context for KDA and NoPE experiments.
- [[KimiDeltaAttention]] - central linear-attention mechanism in K3's hybrid architecture.
- [[LatentMoE]] - MoE communication design linked to K3 scaling and inference latency.
- [[QuantileBalancing]] - expert-load balancing method used in K3's MoE discussion.
- [[NoPositionEncoding]] - long-context position-handling pattern in K3's hybrid attention.
- [[MultiTeacherDistillation]] - post-training capability-merge pattern highlighted by the new technical reading.
- [[ModelInfraCoDesign]] - systems frame connecting K3 architecture to kernels, serving engines, hardware, and agent workloads.
- [[ClosedModelAPIMoatPressure]] - business consequence of strong open-weight alternatives.
- [[ModelDistillationEvidence]] - evidence standard needed for K3-related copying or provenance claims.
