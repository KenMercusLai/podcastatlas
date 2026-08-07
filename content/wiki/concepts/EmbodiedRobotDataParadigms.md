---
title: "Embodied Robot Data Paradigms"
type: concept
tags: [robotics, data, embodied-ai]
sources: [jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1, 147-he-mayi-lingbo-shenyujun-liao-jiqiren-yuansheng-jichu-moxing-danao-he-benti-de-guanxi-yuxunlian-yu-shuju-scale-up-laoshi-tangxiaoou-luxtyuafi-2onim15fw6lpypo2ga]
last_updated: 2026-08-07
---

# Embodied Robot Data Paradigms

Embodied robot data paradigms are the changing collection methods behind robot model progress in [[jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1]]. [[ChenZhePeter]] says each model-paradigm shift tends to follow a data-paradigm shift, and the episode traces a path from Aloha-style real-robot teleoperation to UMI body-free collection, first-person video, whole-body motion capture, and dexterous-hand data.

[[147-he-mayi-lingbo-shenyujun-liao-jiqiren-yuansheng-jichu-moxing-danao-he-benti-de-guanxi-yuxunlian-yu-shuju-scale-up-laoshi-tangxiaoou-luxtyuafi-2onim15fw6lpypo2ga]] adds [[AntLingbo|蚂蚁灵波]]'s data-native turn. [[ShenYujun|沈宇军]] says the hard part is not only choosing a collection device, but deciding what tasks to assign, how to cover head/waist/base/hand degrees of freedom, and how to clean data across bodies with different cameras and kinematics.

This concept extends [[RealRobotDataStrategy]] and [[EmbodiedDataPyramid]]. It does not say one data type replaces all others; instead, it asks which data source makes a specific capability newly learnable and transferable to a given robot body.

## Key Claims
- Whole-body motion capture makes locomotion and manipulation data easier to scale when hardware such as [[UnitreeRobotics]] becomes a common research platform.
- Dexterous-hand data is highly hardware-specific because finger layout, degrees of freedom, motors, and sensors affect retargeting.
- UMI-style and egocentric data can broaden scene and task coverage, but robot-body deployment remains necessary for final grounding.
- Cross-embodiment cleaning becomes its own paradigm problem when the same model is expected to learn across mobile bases, wrists, heads, waists, grippers, and dexterous hands.

## Connections
- [[RealRobotDataStrategy]], [[EmbodiedDataPyramid]], and [[PhysicalWorldDataFlywheel]] — adjacent data-loop concepts.
- [[DexterousManipulation]] — hardware-specific data case.
- [[Generalist]] and [[GenesisRobotics]] — companies discussed through large interaction or dexterous-operation data claims.
- [[AntLingbo]], [[ShenYujun]], [[RobotDataScaleUp]], and [[EmbodiedNativeFoundationModels]] — data-native and cross-body cleaning update from episode 147.
