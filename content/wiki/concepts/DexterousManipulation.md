---
title: "Dexterous Manipulation"
type: concept
tags: [robotics, manipulation, hardware, data]
sources: [jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1]
last_updated: 2026-07-08
---

# Dexterous Manipulation

Dexterous manipulation is the source's term space for high-degree-of-freedom hands, whole-body control, and fine object handling in [[EmbodiedAI]]. [[jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1]] treats dexterous hands as a key infrastructure layer because hand structure, degrees of freedom, drive method, sensors, thermal behavior, and retargeting constraints shape what robot data can be collected and what policies can transfer.

The episode contrasts direct-drive hands, cable-driven hands, and hybrid approaches. It presents [[FiveGRobotics]] as a possible infrastructure supplier for research, [[GenesisRobotics]] as a model/data company demonstrating early dexterous tasks, and [[Tesla]] as an industrial route whose Optimus hand choices can pull other large engineering teams toward cable-driven designs.

## Key Claims
- Deformable objects such as clothes, soft packages, food, and plastic bags expose limits in rigid-body assumptions and simple grippers.
- High-DOF hands are not interchangeable data devices; different hand geometry, motors, and sensors make retargeting difficult.
- Independent hand suppliers may control an important data gateway if their hardware becomes widely used; full-stack robot-body companies may pull that data layer back inside the body.

## Connections
- [[FiveGRobotics]], [[GenesisRobotics]], [[Tesla]], and [[UnitreeRobotics]] — hardware and ecosystem examples in the episode.
- [[RobotLogisticsSorting]] — practical scenario where dexterity matters.
- [[EmbodiedRobotDataParadigms]] and [[RealRobotDataStrategy]] — data implications of hand choice and retargeting.
