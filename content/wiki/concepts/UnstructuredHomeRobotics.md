---
title: "Unstructured Home Robotics"
type: concept
tags: [robotics, homes, ai, consumer-hardware]
sources:
  - yingweida-qidong-dui-huangrenxun-de-diaocha-xiaofei-pinpai-jiti-kuajie-chongwu-shengyi-gkwrijiox3zoafmb9at4mvyn
last_updated: 2026-11-10
knowledge_schema: synthesis-v1
---

# Unstructured Home Robotics

## Definition
Unstructured home robotics is the problem of making robots perceive, plan, move, and manipulate safely across varied households that lack the controlled layouts, objects, routines, and access rules of industrial settings.

## Current Synthesis
The source pairs two approaches. [[Apple]] reportedly trains its Halo control system in many programmatically generated simulated homes, seeking broader task variation before physical deployment. [[Amazon]] reorganizes a consumer-robotics team after Astro's limited invitation-only distribution, bringing industrial robotics experience toward a less predictable environment.

Both cases reinforce that stronger models are only one layer. Vision can miss contact, force, slippage, softness, occlusion, pets, people, and changing object locations; touch, sensors, batteries, recovery behavior, privacy, and household trust determine whether an impressive demonstration becomes a reliable product.

## Key Claims
- Household diversity makes fixed-layout training and evaluation insufficient.
- Procedurally varied simulation can broaden experience before costly physical collection.
- Vision-only control leaves contact and force information unresolved.
- Industrial robotics experience transfers only partially because homes are less standardized and more socially sensitive.
- Commercial viability requires safety, privacy, battery life, recovery, usefulness, and acceptable cost alongside model capability.

## Evidence
- Simulation route - [[yingweida-qidong-dui-huangrenxun-de-diaocha-xiaofei-pinpai-jiti-kuajie-chongwu-shengyi-gkwrijiox3zoafmb9at4mvyn]] reports roughly 1,000 generated home environments and about 300 hours of synthetic training data for Apple's Halo system.
- Perception boundary - [[yingweida-qidong-dui-huangrenxun-de-diaocha-xiaofei-pinpai-jiti-kuajie-chongwu-shengyi-gkwrijiox3zoafmb9at4mvyn]] says the reported system mainly uses vision and identifies touch as future work.
- Organizational route - [[yingweida-qidong-dui-huangrenxun-de-diaocha-xiaofei-pinpai-jiti-kuajie-chongwu-shengyi-gkwrijiox3zoafmb9at4mvyn]] describes Amazon moving much of the Astro team into a new home-robotics effort and acquiring a robotics startup.

## Counterevidence & Qualifications
The source provides no task benchmark, failure rate, hardware specification, acquisition identity, product timeline, price, or independent evaluation. Simulation diversity may not match physical homes, and adding touch creates hardware, calibration, data, and cost burdens. Team reorganization signals intent, not product-market fit.

## What Changed
- Created a shared household-complexity frame across Apple simulation research and Amazon product reorganization.
- Added touch, recovery, privacy, and trust as commercialization constraints beyond vision-led model progress.

## Related Concepts
- [[HomeServiceRobots]] - consumer category in which household usefulness and affordability must be proven.
- [[ConsumerRoboticsFullStack]] - integrated hardware, sensing, software, and cost stack needed for a product.
- [[EmbodiedAI]] - model and control layer connecting perception to physical action.
- [[RoboticsSimulationEvaluation]] - use of simulated environments to train and test embodied systems.
