---
title: "蚂蚁灵波 / Ant Lingbo"
type: entity
tags: [company, robotics, embodied-ai, models]
sources: [147-he-mayi-lingbo-shenyujun-liao-jiqiren-yuansheng-jichu-moxing-danao-he-benti-de-guanxi-yuxunlian-yu-shuju-scale-up-laoshi-tangxiaoou-luxtyuafi-2onim15fw6lpypo2ga]
last_updated: 2026-08-07
---

# 蚂蚁灵波 / Ant Lingbo

Ant Lingbo / 蚂蚁灵波 is the [[AntGroup|蚂蚁集团]]-incubated embodied-intelligence company discussed in [[147-he-mayi-lingbo-shenyujun-liao-jiqiren-yuansheng-jichu-moxing-danao-he-benti-de-guanxi-yuxunlian-yu-shuju-scale-up-laoshi-tangxiaoou-luxtyuafi-2onim15fw6lpypo2ga]]. In the source, chief scientist [[ShenYujun|沈宇军]] says the company was formed to explore physical-world AI and chose to build the robot brain first rather than produce one universal robot body.

The company is a concrete case for [[EmbodiedNativeFoundationModels]]. Its model route starts from real sensors, depth, video sequence, action, and cross-embodiment data. The first generation supported nine robot configurations and simpler grasping or desktop tasks; the second generation expands toward more than twenty configurations, around 3B model scale, roughly 60,000 hours of data after stricter cleaning, and richer body parts such as head, waist, chassis, wrist cameras, and dexterous hands.

## Key Points
- Lingbo's strategic target is a reusable robot brain that can run across different brands and forms rather than a closed robot body.
- The company treats [[VisionLanguageActionModels]], video/action modeling, depth, and world-model-like work as parts of one physical-world stack.
- The source says deployment feedback changed the second-generation data and model priorities, especially around higher-quality data, more embodiments, and more complex tasks.
- Lingbo emphasizes real-machine data and eGo-style human first-person data, while treating simulation as more useful for evaluation and partial coverage than as the main general-training source.
- The source presents cooking, billiards, and desk-organizing demos as evidence of progress in long-horizon task pressure, random position handling, and human disturbance, not as proof that new-task generalization is solved.
- The company frames the next step as moving from visual-native and architecture-native work toward data-native embodied modeling.

## Connections
- [[ShenYujun|沈宇军]] — chief scientist and source speaker.
- [[AntGroup|蚂蚁集团]] — parent company and AI-first context.
- [[EmbodiedNativeFoundationModels]], [[RobotDataScaleUp]], and [[AINativeRobotics]] — central technical and strategic concepts.
- [[VisionLanguageActionModels]], [[WorldModels]], [[WorldActionModels]], and [[WorldModelVLAFusion]] — model-family context.
- [[RealRobotDataStrategy]], [[EmbodiedDataPyramid]], [[RoboticsSimulationEvaluation]], and [[Sim2Real]] — data and simulation comparison branch.
- [[TactileSensing]], [[DexterousManipulation]], and [[RobotFormFactorPragmatism]] — sensor, hand, and body-form questions that the source expects to co-evolve with model needs.
