---
title: "Structured 3D Robot Data"
type: concept
tags: [robotics, data, 3d-data, embodied-ai]
sources: [e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e]
last_updated: 2026-07-16
---

# Structured 3D Robot Data

Structured 3D robot data is the episode's answer to why internet image and video scale is not enough for manipulation. In [[e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e]], [[HanZheng]] argues that robots need accurate geometry, material, friction, elasticity, parts, and dynamics, especially when tasks require millimeter-level contact.

The source traces a data lineage from [[ImageNet]] to [[ShapeNet]], [[PartNet]], and PartNet Mobility, then argues that the remaining gap is still large. A robot opening, grasping, inserting, or screwing objects needs structured physical affordances, not only a mesh, label, or video prior.

## Key Claims
- 2D images and video can imply 3D structure but usually do not provide precise contact-relevant geometry and dynamics.
- Open-world manipulation needs data on object parts, motion constraints, material properties, friction, deformation, and task affordances.
- Non-structured 3D asset collections can be large while still containing duplicates, game assets, or objects that are poor training material for robots.
- Structured 3D data is valuable because it feeds [[Sim2Real]], [[RoboticsSimulationEvaluation]], and low-level manipulation skill learning.

## Connections
- [[SuHao]], [[ImageNet]], [[ShapeNet]], and [[PartNet]] - research and data lineage.
- [[OpenWorldRobotManipulation]] - capability target.
- [[EmbodiedDataPyramid]] and [[RealRobotDataStrategy]] - adjacent data strategy concepts.
- [[SuduTechnology]] - company building around this source's route.
