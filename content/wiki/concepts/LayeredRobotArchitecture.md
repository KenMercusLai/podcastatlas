---
title: "Layered Robot Architecture"
type: concept
tags: [robotics, architecture, embodied-ai]
sources: [e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e]
last_updated: 2026-07-16
---

# Layered Robot Architecture

Layered robot architecture is the episode's route distinction between high-level reasoning/planning and low-level physical manipulation. In [[e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e]], [[HanZheng]] predicts that this layered structure may return to the mainstream as teams hit the limits of scarce real robot data and narrow end-to-end imitation.

The source defines the upper layer as understanding the environment, decomposing the task, and choosing a plan. The lower layer is concrete manipulation such as opening a door, grabbing a bottle, unscrewing a cap, pouring water, or inserting an object. The source's nuance is that deployment can still be end-to-end at the edge while pretraining uses interpretable intermediate structure.

## Key Claims
- Layering is not the same as brittle rule stitching; it can include learned geometry, material, kinematics, object-part, and future-state representations.
- Reliable short manipulation skills are prerequisites for long-horizon tasks because failures compound across steps.
- [[PhysicalIntelligence]] and [[Generalist]] are framed as stronger in upper-level reasoning or robot-brain work, while [[SuduTechnology]] emphasizes bottom-level manipulation.
- The architecture works best when tied to [[Sim2Real]], hardware/software co-design, and [[Structured3DRobotData]].

## Connections
- [[VisionLanguageActionModels]] and [[WorldModelVLAFusion]] - adjacent model architectures.
- [[ManiSkill]] - short-skill and task-composition context.
- [[OpenWorldRobotManipulation]] - evaluation bar for the lower-level skills.
- [[EmbodiedAIValueChain]] - business question of who owns the brain, body, data, and developer platform.
