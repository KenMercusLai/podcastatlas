---
title: "Sim2Real"
type: concept
tags: [robotics, simulation, embodied-ai]
sources: [e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e]
last_updated: 2026-07-16
---

# Sim2Real

Sim2Real is the robotics route of training or testing behavior in simulation and transferring it to real robots. In [[e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e]], [[HanZheng]] argues that robot manipulation cannot skip Sim2Real if the goal is reliable operation on unseen objects and unseen environments.

The source's version of Sim2Real is not simply prettier virtual worlds. It emphasizes [[Structured3DRobotData]], physical consistency, GPU-parallel environments, hardware-specific noise, and bottom-level manipulation skills that can survive transfer to the real robot body.

## Key Claims
- Simulation must be physically useful, not merely visually realistic.
- The simulator and hardware have to co-evolve because motor noise, response curves, gripper structure, and boot-time differences can affect transfer.
- Real robot data remains necessary, but it is too scarce and expensive to be the only source of open-world manipulation learning.
- [[RoboticsSimulationEvaluation]] and [[EmbodiedDataPyramid]] become practical infrastructure when Sim2Real is treated as training, evaluation, and feedback rather than as a single transfer trick.

## Connections
- [[SuduTechnology]] and [[HanZheng]] - source company and guest.
- [[ManiSkill]], [[ShapeNet]], and [[PartNet]] - project and data-set context.
- [[OpenWorldRobotManipulation]] and [[LayeredRobotArchitecture]] - capability target and architecture route.
- [[RealRobotDataStrategy]] - route the source qualifies rather than rejects.
