---
title: "World Action Models"
type: concept
tags: [world-models, robotics, video-models]
sources: [173-duihua-yao-song-shenjian-dongfang-kongjian-zaichufa-tiancai-shaonian-shinian-hou-1-173-1, ai-jibao-26q2-cong-coding-dao-rsi-qiangzhe-yu-qiang-de-weilai-1-171-1, jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1, na-tiao-luxian-caineng-tongwang-shijie-moxing-de-zhongju-duihua-huang-biwei-aether-ai-chuangshiren-lgg-env6jrpgvyiwtxw6bocdzdmr, 147-he-mayi-lingbo-shenyujun-liao-jiqiren-yuansheng-jichu-moxing-danao-he-benti-de-guanxi-yuxunlian-yu-shuju-scale-up-laoshi-tangxiaoou-luxtyuafi-2onim15fw6lpypo2ga]
last_updated: 2026-08-07
---

# World Action Models

World action models, or WAMs, are discussed in [[na-tiao-luxian-caineng-tongwang-shijie-moxing-de-zhongju-duihua-huang-biwei-aether-ai-chuangshiren-lgg-env6jrpgvyiwtxw6bocdzdmr]] as an intermediate route between [[VideoModels]] and full [[WorldModels]]. [[HuangBiwei]] treats WAMs as stronger than pure [[VisionLanguageActionModels]] in the short term because abundant video data can help model action-conditioned dynamics.

[[jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1]] adds [[Nvidia]]'s three-way taxonomy: Video World Model, Action-Conditioned World Model, and World Action Model. In [[ChenZhePeter]]'s reading, the embodied-AI community cares most about WAM-like systems because they sit closest to robot policy, but they still fit into a broader [[WorldModelVLAFusion]] trend rather than replacing every VLA-style system.

[[ai-jibao-26q2-cong-coding-dao-rsi-qiangzhe-yu-qiang-de-weilai-1-171-1]] adds the broader AI-quarter frame. [[HenryYin]] says world models became hotter because RL-style world models and video-generation routes began to converge, with action-conditioned prediction as the key bridge between plausible video and robot decision-making.

[[147-he-mayi-lingbo-shenyujun-liao-jiqiren-yuansheng-jichu-moxing-danao-he-benti-de-guanxi-yuxunlian-yu-shuju-scale-up-laoshi-tangxiaoou-luxtyuafi-2onim15fw6lpypo2ga]] adds [[AntLingbo|蚂蚁灵波]]'s physical-world version through [[ShenYujun|沈宇军]]. The source says digital video generation and robot execution have different requirements: robots need real-time, one-way, action-relevant modeling, so Video, World, and VA-style work only matter if they improve physical action.

[[173-duihua-yao-song-shenjian-dongfang-kongjian-zaichufa-tiancai-shaonian-shinian-hou-1-173-1]] adds [[YaoSong]]'s industry-cycle reading. He argues that WAM attention is not only hype because it may push physical-intelligence algorithms forward, but he is skeptical of companies that rely only on an ultimate general model story without a business base, data loop, and [[MilestoneCommercialization]] path.

## Limitation
The episode still does not treat WAM as the end state. Huang argues that a complete route needs [[CausalWorldModels]]: causal variables, causal structures, and transition dynamics grounded in the physical world rather than only action-conditioned video prediction.

Shen adds that action-conditioned modeling also has a data condition: without [[RobotDataScaleUp]], a robot-native VA route can improve fixed tasks but still struggle to generalize to unseen tasks.

Yao adds a company-building limitation: WAM research still has to be embedded in [[PhysicalIntelligenceSystemStack]], scenario access, and commercial milestones, or the strongest-financed model-only companies may be the only ones able to survive the long route.

## Connections
- [[CausalWorldModels]] — higher-ceiling route in the source.
- [[VisionLanguageActionModels]] — related robot-policy route with a lower ceiling in Huang's rating.
- [[VideoModels]] — data and modeling base from which WAM emerges.
- [[EmbodiedAI]] and [[AetherAI]] — deployment area and company context.
- [[Cosmos3]], [[Nvidia]], and [[WorldModelVLAFusion]] — Q2 2026 product and taxonomy context from the LateTalk source.
- [[PhysicalAI]], [[OpenAI]], and [[Anthropic]] — Q2 AI-quarter context linking world models back to frontier labs and robotics.
- [[AntLingbo]], [[ShenYujun]], [[EmbodiedNativeFoundationModels]], and [[RobotDataScaleUp]] — physical-world VA route added by episode 147.
- [[YaoSong]], [[StridingAI]], [[PhysicalIntelligenceSystemStack]], and [[MilestoneCommercialization]] — WAM hype and business-base caution added by episode 173.
