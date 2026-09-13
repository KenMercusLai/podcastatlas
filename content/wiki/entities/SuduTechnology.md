---
title: "速度科技 / Sudu Technology"
type: entity
tags: [company, robotics, embodied-ai]
sources:
  - e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e
  - dang-jushen-zhineng-zoudao-shizilukou-duitan-sudu-mayi-lingbo-zibianliang-poke-sizhong-yixian-panduan-ls6w3mrjjrecuqg33yc3lbdmdzpf
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

# 速度科技 / Sudu Technology

## Overview
速度科技 is the robotics company represented by [[HanZheng]] in [[e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e]] and [[dang-jushen-zhineng-zoudao-shizilukou-duitan-sudu-mayi-lingbo-zibianliang-poke-sizhong-yixian-panduan-ls6w3mrjjrecuqg33yc3lbdmdzpf]]. The wiki now tracks it as a full-stack manipulation and simulation route inside embodied AI.

## Current Profile
Sudu's route emphasizes [[Sim2Real]], physically useful simulation, hardware/software co-design, and stable low-level manipulation skills. The new four-company debate sharpens the earlier E244 position: simulation is not a rejection of real data, but a way to scale pretraining for grasping, placing, assembly, and other short skills before they are composed under [[LayeredRobotArchitecture]].

## Key Characteristics
- Builds around low-level manipulation reliability rather than only high-level robot reasoning.
- Treats simulation as a scalable training and reinforcement-learning layer for basic physical skills.
- Still accepts real-world data as useful for grounding, validation, and physical transfer.
- Uses [[LayeredRobotArchitecture]] to connect upper-level understanding with lower-level execution.
- Defines commercialization through high success rate, generalized handling of objects and environments, and low deployment adaptation cost.

## Evidence
- Full-stack evidence: [[e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e]] describes Sudu as building robot body and robot brain together because hardware configuration and manipulation policy affect transfer.
- Simulation evidence: [[e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e]] links Sudu to [[Structured3DRobotData]], GPU-parallel simulation, hardware-specific noise modeling, and open-world manipulation tests.
- New debate evidence: [[dang-jushen-zhineng-zoudao-shizilukou-duitan-sudu-mayi-lingbo-zibianliang-poke-sizhong-yixian-panduan-ls6w3mrjjrecuqg33yc3lbdmdzpf]] records Han Zheng saying Sudu uses simulation while still treating real-world data as useful.
- Commercial evidence: [[dang-jushen-zhineng-zoudao-shizilukou-duitan-sudu-mayi-lingbo-zibianliang-poke-sizhong-yixian-panduan-ls6w3mrjjrecuqg33yc3lbdmdzpf]] records Han emphasizing near-perfect success, fast correction, object/environment generalization, and low post-training cost.

## Qualifications
Sudu's strongest evidence in the wiki remains source-reported demonstrations and operator claims. The new source records confidence in near-term stable skills, but does not independently benchmark Sudu against other robot companies or provide deployment-scale customer data.

## What Changed
- Converted the page to the synthesis-v1 entity schema.
- Added the Shizilukou Crossing debate as evidence that Sudu's simulation route is stage-specific, not simulation-only.
- Added commercialization requirements around high success rate and low deployment adaptation cost.

## Relationships
- [[HanZheng]] - Sudu speaker and route explainer.
- [[Sim2Real]] - core training and transfer method in Sudu's route.
- [[LayeredRobotArchitecture]] - architecture Sudu uses to connect high-level planning with short skills.
- [[EmbodiedRobotDataTradeoff]] - new data tradeoff sharpened by the four-company debate.
- [[RobotDeploymentSuccessEconomics]] - commercial test the new source applies to Sudu's route.
