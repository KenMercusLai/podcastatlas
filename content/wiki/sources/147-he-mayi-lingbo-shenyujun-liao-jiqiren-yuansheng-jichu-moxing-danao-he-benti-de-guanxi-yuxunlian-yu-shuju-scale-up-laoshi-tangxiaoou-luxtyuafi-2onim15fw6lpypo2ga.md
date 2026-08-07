---
title: "147. 和蚂蚁灵波沈宇军聊：机器人原生基础模型、大脑和本体的关系、预训练与数据scale up、老师汤晓鸥"
type: source
tags: [podcast, robotics, embodied-ai, physical-ai, foundation-models]
sources: []
date: 2026-07-22
source_file: "/home/ken/repos/podcastatlas/content/episodes/147. 和蚂蚁灵波沈宇军聊：机器人原生基础模型、大脑和本体的关系、预训练与数据scale up、老师汤晓鸥 [luXTyuAfi_2ONiM15fW6Lpypo2GA].md"
source_url: "https://www.xiaoyuzhoufm.com/episode/6a5f79b3a3fec224d5a128cd"
last_updated: 2026-08-07
---

# 147. 和蚂蚁灵波沈宇军聊：机器人原生基础模型、大脑和本体的关系、预训练与数据scale up、老师汤晓鸥

## Summary
This [[ZhangXiaojunCommercialInterviews]] episode interviews [[ShenYujun|沈宇军]], chief scientist of [[AntLingbo|蚂蚁灵波]], about building a robot "brain" before committing to a single robot body. The interview argues that [[EmbodiedNativeFoundationModels]] should start from real sensors, spatial perception, video time series, action, and robot data rather than simply adapting digital-world language or video models. Its central bottleneck is [[RobotDataScaleUp]]: Shen says embodied AI has not reached a robot GPT-1 moment because the field still lacks a scalable, useful data path comparable to internet-scale language data.

## Key Claims
- [[AntLingbo|蚂蚁灵波]] was set up inside [[AntGroup|蚂蚁集团]] to explore physical-world AI and embodied intelligence, with the strategic choice to build a cross-embodiment robot brain rather than a single proprietary body.
- [[ShenYujun|沈宇军]] moved from [[TsinghuaUniversity|清华大学]], [[SenseTime|商汤]], [[ChineseUniversityOfHongKong|香港中文大学]], [[TangXiaoou|汤晓鸥]]'s team, image generation, and [[ByteDance|字节跳动]] visual applications toward robotics because robots make vision valuable inside the physical world.
- Shen argues that a robot-native model stack needs physical-world pretraining: real sensor noise, depth, contactability, spatial geometry, video sequence, action, and real-time execution all differ from clean academic data or digital video generation.
- The first generation of Lingbo's brain used depth, video action, world model, and [[VisionLanguageActionModels|VLA]] directions across nine configurations for simpler grasping and desktop tasks.
- The second generation expands from about 20,000 hours to about 60,000 hours of data, from nine to more than twenty configurations, and from arms/grippers toward head, waist, mobile chassis, wrist cameras, and dexterous hands.
- The source presents data cleaning as part of scaling: first-generation data had to be reprocessed through a stricter pipeline before the second-generation training set became meaningfully larger.
- Shen treats real-machine data as the main training source, eGo-style human first-person data as useful, and simulation as stronger for evaluation and partial scenes than for general manipulation training.
- [[RobotDataScaleUp]] depends on task design, body coverage, camera positions, degrees of freedom, and cross-body cleaning, not only on recording more hours.
- Lingbo's updated VLA work is valuable partly because real deployment shows what data industrial tasks actually require.
- The source separates "intent execution" from "intent origin": Lingbo currently aims to do the instructed task well, not to make robots autonomously infer higher-order goals such as noticing rain and deciding to fetch an umbrella.
- Shen says the second generation improves random-position and disturbance handling, including billiards and desk-organizing examples, but still lacks strong new-task generalization.
- He thinks the robot GPT-1 moment has not arrived because embodied data still has no clearly scalable collection route; when embodied data can scale toward internet-data levels, the field will be closer.
- Shen expects robot brains, bodies, sensors, dexterous hands, tactile sensors, and data systems to rise in alternating waves rather than one layer solving the whole problem first.
- The episode's final bet is "embodied-native": embodied intelligence should have its own models, while large language models remain useful as an instruction-understanding entrance.

## Key Quotes
> "具身原生" — Shen's final description of the core bet.

> "数据不够" — his diagnosis of the main robot-intelligence bottleneck.

> "J 人" — the practical personality he says he would prefer in a robot.

## Connections
- [[ShenYujun|沈宇军]], [[AntLingbo|蚂蚁灵波]], and [[AntGroup|蚂蚁集团]] — guest, company, and parent-company context.
- [[TangXiaoou|汤晓鸥]], [[SenseTime|商汤]], [[TsinghuaUniversity|清华大学]], [[ChineseUniversityOfHongKong|香港中文大学]], and [[ByteDance|字节跳动]] — career and research lineage.
- [[EmbodiedNativeFoundationModels]], [[AINativeRobotics]], [[PhysicalAI]], and [[EmbodiedAI]] — core robotics-model thesis.
- [[RobotDataScaleUp]], [[RealRobotDataStrategy]], [[EmbodiedDataPyramid]], and [[EmbodiedRobotDataParadigms]] — data-route and data-quality context.
- [[VisionLanguageActionModels]], [[WorldModels]], [[WorldActionModels]], and [[WorldModelVLAFusion]] — model-family context around VLA, video, world, and VA-style work.
- [[MixtureOfExperts|MOE]], [[RobotEvaluationProblem]], [[RoboticsSimulationEvaluation]], and [[Sim2Real]] — architecture, measurement, and simulation context.
- [[PhysicalIntelligence]], [[Generalist]], [[TactileSensing]], [[DexterousManipulation]], and [[HumanoidRobotCommercialization]] — external route comparisons and adjacent hardware/sensor trends.

## Contradictions
- No direct contradiction found. The source reinforces the wiki's [[EmbodiedAI]] and [[AINativeRobotics]] branches while adding Ant Lingbo's robot-brain-first version.
- Productive tension to track: [[RobotDataScaleUp]] leans more heavily toward real-machine data than [[EmbodiedDataPyramid]], where [[XieChen]] places simulation and data recipes at the center because real robot data is too costly to scale alone.
- Productive tension to track: Shen's route emphasizes cross-embodiment robot-native foundation models, while [[e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e]] argues that low-level structured manipulation and [[LayeredRobotArchitecture]] remain necessary for open-world reliability.
