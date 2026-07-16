---
title: "ShapeNet"
type: entity
tags: [dataset, robotics, 3d-data]
sources: [e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e]
last_updated: 2026-07-16
---

# ShapeNet

ShapeNet is a 3D object data set discussed in [[e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e]]. The source presents it as a successor to the [[ImageNet]]-style idea of large structured data, but moved from 2D images toward object shape.

The source also treats ShapeNet as insufficient for full robot manipulation by itself. Robot policies need not only shapes, but also object parts, articulation, material, friction, elasticity, and contact dynamics, which leads the episode toward [[PartNet]] and [[Structured3DRobotData]].

## Connections
- [[SuHao]] - researcher context in the source.
- [[PartNet]] - next data-set layer around parts and mobility.
- [[Structured3DRobotData]] and [[Sim2Real]] - why the data set matters for robot training.
