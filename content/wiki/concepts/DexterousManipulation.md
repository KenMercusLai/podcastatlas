---
title: "Dexterous Manipulation"
type: concept
tags: [robotics, manipulation, hardware, data]
sources: [e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e, cong-hui-tiaowu-dao-you-ganzhi-chujue-shi-jiqiren-tongwang-zhineng-de-menpiao-ma-s10e19-f448a656-3004-430b-a853-79d1e77dcb53, jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1]
last_updated: 2026-07-16
---

# Dexterous Manipulation

Dexterous manipulation is the source's term space for high-degree-of-freedom hands, whole-body control, and fine object handling in [[EmbodiedAI]]. [[jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1]] treats dexterous hands as a key infrastructure layer because hand structure, degrees of freedom, drive method, sensors, thermal behavior, and retargeting constraints shape what robot data can be collected and what policies can transfer.

The episode contrasts direct-drive hands, cable-driven hands, and hybrid approaches. It presents [[FiveGRobotics]] as a possible infrastructure supplier for research, [[GenesisRobotics]] as a model/data company demonstrating early dexterous tasks, and [[Tesla]] as an industrial route whose Optimus hand choices can pull other large engineering teams toward cable-driven designs.

[[cong-hui-tiaowu-dao-you-ganzhi-chujue-shi-jiqiren-tongwang-zhineng-de-menpiao-ma-s10e19-f448a656-3004-430b-a853-79d1e77dcb53]] adds [[TactileSensing]] as the missing feedback layer for manipulation. [[EricLiZhiqiang]] argues that preprogrammed demos such as grabbing eggs or peeling shells do not prove general dexterity unless the robot can detect contact, force, slip, softness, texture, and error in real time across new objects.

[[e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e]] adds a gripper-first qualification through [[HanZheng]]. He argues that many useful manipulation tasks can be handled by simpler two-finger grippers before full dexterous hands are necessary, and that open-world object manipulation is already much harder than locomotion because contact, material, and object-state change have to be modeled.

## Key Claims
- Deformable objects such as clothes, soft packages, food, and plastic bags expose limits in rigid-body assumptions and simple grippers.
- High-DOF hands are not interchangeable data devices; different hand geometry, motors, and sensors make retargeting difficult.
- Independent hand suppliers may control an important data gateway if their hardware becomes widely used; full-stack robot-body companies may pull that data layer back inside the body.
- Fine insertion, fastening, gripping, and medical puncture tasks often depend on "feel" that is hard to specify visually or linguistically.
- [[OpticalTactileSensing]] is presented as one route for giving dexterous hands dense contact feedback without treating touch as ordinary vision.
- A dexterous hand is not automatically the best near-term end effector; task success, reliability, and cost can favor simpler grippers while the base manipulation model matures.

## Connections
- [[FiveGRobotics]], [[GenesisRobotics]], [[Tesla]], and [[UnitreeRobotics]] — hardware and ecosystem examples in the episode.
- [[RobotLogisticsSorting]] — practical scenario where dexterity matters.
- [[EmbodiedRobotDataParadigms]] and [[RealRobotDataStrategy]] — data implications of hand choice and retargeting.
- [[TactileSensing]], [[OpticalTactileSensing]], [[YimuTechnology]], and [[TactileTransformerEncoder]] — touch, hardware, company, and model-interface additions from the What's Next source.
- [[SuduTechnology]], [[OpenWorldRobotManipulation]], [[Structured3DRobotData]], and [[LayeredRobotArchitecture]] — E244's manipulation-first route.
