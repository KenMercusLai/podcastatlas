---
title: "Embodied Native Foundation Models"
type: concept
tags: [robotics, embodied-ai, foundation-models, physical-ai]
sources: [147-he-mayi-lingbo-shenyujun-liao-jiqiren-yuansheng-jichu-moxing-danao-he-benti-de-guanxi-yuxunlian-yu-shuju-scale-up-laoshi-tangxiaoou-luxtyuafi-2onim15fw6lpypo2ga]
last_updated: 2026-08-07
---

# Embodied Native Foundation Models

Embodied native foundation models are [[ShenYujun|沈宇军]]'s core thesis in [[147-he-mayi-lingbo-shenyujun-liao-jiqiren-yuansheng-jichu-moxing-danao-he-benti-de-guanxi-yuxunlian-yu-shuju-scale-up-laoshi-tangxiaoou-luxtyuafi-2onim15fw6lpypo2ga]]. The idea is that robot intelligence should not be treated as a language model or digital video model with a mechanical arm attached. It needs a model stack native to sensors, spatial perception, video time, action, embodiment, and real-time physical execution.

The source makes this a practical strategy for [[AntLingbo|蚂蚁灵波]]. The company tries to build a robot brain that can run across many bodies, while leaving body form and scene selection open. In Shen's framing, language models remain useful for understanding instructions, but the embodied model must learn how to turn that instruction into physically successful action.

## Key Claims
- Physical-world models need sensor-native input because real robot cameras, depth sensors, wrist cameras, and noisy data differ from clean academic datasets.
- Spatial understanding is not the same as semantic recognition: a robot must know whether something can be reached, touched, blocked, or acted on.
- Video modeling for robots differs from digital-world generation because robot control needs real-time, forward-time, action-relevant prediction rather than slow, bidirectional, quality-first generation.
- Cross-embodiment brain work requires many configurations, body parts, camera placements, degrees of freedom, and task distributions.
- [[VisionLanguageActionModels]], [[WorldModels]], [[WorldActionModels]], and VA-style work may converge when the system has to connect perception, future state, and action.
- [[RobotDataScaleUp]] is the limiting condition: embodied-native architecture is not enough without data that scales and remains useful to the model.
- Better robot brains will reshape sensor and body requirements, so "brain first" still implies body and sensor co-evolution.

## Connections
- [[AntLingbo|蚂蚁灵波]] and [[ShenYujun|沈宇军]] — company and source speaker.
- [[AINativeRobotics]], [[EmbodiedAI]], [[PhysicalAI]], and [[PhysicalAGI]] — broader robot-intelligence frames.
- [[VisionLanguageActionModels]], [[WorldModels]], [[WorldActionModels]], and [[WorldModelVLAFusion]] — model families this source links together.
- [[RobotDataScaleUp]], [[RealRobotDataStrategy]], and [[EmbodiedRobotDataParadigms]] — data bottlenecks behind the concept.
- [[TactileSensing]], [[DexterousManipulation]], and [[RobotFormFactorPragmatism]] — sensor, hand, and body questions the source expects to change with model progress.
