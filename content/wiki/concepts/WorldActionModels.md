---
title: "World Action Models"
type: concept
tags: [world-models, robotics, video-models]
sources: [ai-jibao-26q2-cong-coding-dao-rsi-qiangzhe-yu-qiang-de-weilai-1-171-1, jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1, na-tiao-luxian-caineng-tongwang-shijie-moxing-de-zhongju-duihua-huang-biwei-aether-ai-chuangshiren-lgg-env6jrpgvyiwtxw6bocdzdmr]
last_updated: 2026-07-08
---

# World Action Models

World action models, or WAMs, are discussed in [[na-tiao-luxian-caineng-tongwang-shijie-moxing-de-zhongju-duihua-huang-biwei-aether-ai-chuangshiren-lgg-env6jrpgvyiwtxw6bocdzdmr]] as an intermediate route between [[VideoModels]] and full [[WorldModels]]. [[HuangBiwei]] treats WAMs as stronger than pure [[VisionLanguageActionModels]] in the short term because abundant video data can help model action-conditioned dynamics.

[[jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1]] adds [[Nvidia]]'s three-way taxonomy: Video World Model, Action-Conditioned World Model, and World Action Model. In [[ChenZhePeter]]'s reading, the embodied-AI community cares most about WAM-like systems because they sit closest to robot policy, but they still fit into a broader [[WorldModelVLAFusion]] trend rather than replacing every VLA-style system.

[[ai-jibao-26q2-cong-coding-dao-rsi-qiangzhe-yu-qiang-de-weilai-1-171-1]] adds the broader AI-quarter frame. [[HenryYin]] says world models became hotter because RL-style world models and video-generation routes began to converge, with action-conditioned prediction as the key bridge between plausible video and robot decision-making.

## Limitation
The episode still does not treat WAM as the end state. Huang argues that a complete route needs [[CausalWorldModels]]: causal variables, causal structures, and transition dynamics grounded in the physical world rather than only action-conditioned video prediction.

## Connections
- [[CausalWorldModels]] — higher-ceiling route in the source.
- [[VisionLanguageActionModels]] — related robot-policy route with a lower ceiling in Huang's rating.
- [[VideoModels]] — data and modeling base from which WAM emerges.
- [[EmbodiedAI]] and [[AetherAI]] — deployment area and company context.
- [[Cosmos3]], [[Nvidia]], and [[WorldModelVLAFusion]] — Q2 2026 product and taxonomy context from the LateTalk source.
- [[PhysicalAI]], [[OpenAI]], and [[Anthropic]] — Q2 AI-quarter context linking world models back to frontier labs and robotics.
