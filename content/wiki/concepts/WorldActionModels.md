---
title: "World Action Models"
type: concept
tags: [world-models, robotics, video-models]
sources: [jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1, na-tiao-luxian-caineng-tongwang-shijie-moxing-de-zhongju-duihua-huang-biwei-aether-ai-chuangshiren-lgg-env6jrpgvyiwtxw6bocdzdmr]
last_updated: 2026-07-08
---

# World Action Models

World action models, or WAMs, are discussed in [[na-tiao-luxian-caineng-tongwang-shijie-moxing-de-zhongju-duihua-huang-biwei-aether-ai-chuangshiren-lgg-env6jrpgvyiwtxw6bocdzdmr]] as an intermediate route between [[VideoModels]] and full [[WorldModels]]. [[HuangBiwei]] treats WAMs as stronger than pure [[VisionLanguageActionModels]] in the short term because abundant video data can help model action-conditioned dynamics.

[[jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1]] adds [[Nvidia]]'s three-way taxonomy: Video World Model, Action-Conditioned World Model, and World Action Model. In [[ChenZhePeter]]'s reading, the embodied-AI community cares most about WAM-like systems because they sit closest to robot policy, but they still fit into a broader [[WorldModelVLAFusion]] trend rather than replacing every VLA-style system.

## Limitation
The episode still does not treat WAM as the end state. Huang argues that a complete route needs [[CausalWorldModels]]: causal variables, causal structures, and transition dynamics grounded in the physical world rather than only action-conditioned video prediction.

## Connections
- [[CausalWorldModels]] — higher-ceiling route in the source.
- [[VisionLanguageActionModels]] — related robot-policy route with a lower ceiling in Huang's rating.
- [[VideoModels]] — data and modeling base from which WAM emerges.
- [[EmbodiedAI]] and [[AetherAI]] — deployment area and company context.
- [[Cosmos3]], [[Nvidia]], and [[WorldModelVLAFusion]] — Q2 2026 product and taxonomy context from the LateTalk source.
