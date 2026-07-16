---
title: "PartNet / PartNet Mobility"
type: entity
tags: [dataset, robotics, 3d-data]
sources: [e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e]
last_updated: 2026-07-16
---

# PartNet / PartNet Mobility

PartNet and PartNet Mobility are discussed in [[e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e]] as 3D data-set steps beyond [[ShapeNet]]. The source says they add object parts and mobility constraints, making them more relevant to robot manipulation than shape-only data.

The episode still treats them as far from enough: a few thousand articulated objects cannot cover open-world bottle caps, drawers, deformable materials, friction, elasticity, and other physical details. This limitation becomes one reason [[SuduTechnology]] emphasizes [[Structured3DRobotData]] and [[Sim2Real]] rather than relying only on internet video or existing 3D assets.

## Connections
- [[SuHao]] and [[ShapeNet]] - data lineage in the source.
- [[Structured3DRobotData]] - broader concept this source adds.
- [[OpenWorldRobotManipulation]] - capability target that demands more than part labels.
