---
title: "Embodied Robot Data Paradigms"
type: concept
tags: [robotics, data, embodied-ai]
sources: [jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1]
last_updated: 2026-07-08
---

# Embodied Robot Data Paradigms

Embodied robot data paradigms are the changing collection methods behind robot model progress in [[jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1]]. [[ChenZhePeter]] says each model-paradigm shift tends to follow a data-paradigm shift, and the episode traces a path from Aloha-style real-robot teleoperation to UMI body-free collection, first-person video, whole-body motion capture, and dexterous-hand data.

This concept extends [[RealRobotDataStrategy]] and [[EmbodiedDataPyramid]]. It does not say one data type replaces all others; instead, it asks which data source makes a specific capability newly learnable and transferable to a given robot body.

## Key Claims
- Whole-body motion capture makes locomotion and manipulation data easier to scale when hardware such as [[UnitreeRobotics]] becomes a common research platform.
- Dexterous-hand data is highly hardware-specific because finger layout, degrees of freedom, motors, and sensors affect retargeting.
- UMI-style and egocentric data can broaden scene and task coverage, but robot-body deployment remains necessary for final grounding.

## Connections
- [[RealRobotDataStrategy]], [[EmbodiedDataPyramid]], and [[PhysicalWorldDataFlywheel]] — adjacent data-loop concepts.
- [[DexterousManipulation]] — hardware-specific data case.
- [[Generalist]] and [[GenesisRobotics]] — companies discussed through large interaction or dexterous-operation data claims.
