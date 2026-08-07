---
title: "Robot Data Scale Up"
type: concept
tags: [robotics, data, embodied-ai, scale]
sources: [147-he-mayi-lingbo-shenyujun-liao-jiqiren-yuansheng-jichu-moxing-danao-he-benti-de-guanxi-yuxunlian-yu-shuju-scale-up-laoshi-tangxiaoou-luxtyuafi-2onim15fw6lpypo2ga]
last_updated: 2026-08-07
---

# Robot Data Scale Up

Robot data scale up is the bottleneck named by [[ShenYujun|沈宇军]] in [[147-he-mayi-lingbo-shenyujun-liao-jiqiren-yuansheng-jichu-moxing-danao-he-benti-de-guanxi-yuxunlian-yu-shuju-scale-up-laoshi-tangxiaoou-luxtyuafi-2onim15fw6lpypo2ga]]. Shen says embodied intelligence has not yet reached a robot GPT-1 moment because the field lacks a data-scaling method comparable to internet-scale language data.

In the source, scaling does not mean simply recording more robot hours. [[AntLingbo|蚂蚁灵波]] expands from about 20,000 to about 60,000 hours in its second generation, but Shen emphasizes that stricter cleaning, task choice, body coverage, camera positions, degrees of freedom, and data usability matter as much as volume.

## Key Claims
- Real-machine data is valuable because it contains actual sensor noise, body constraints, execution latency, and physical failures.
- eGo-style first-person human data can scale some everyday scene and task coverage, but it may not contain enough hand-specific or contact-specific information for fine manipulation.
- Simulation is useful for evaluation and partial scenes, but the source treats it as insufficient for general flexible-object and complex manipulation training by itself.
- Cross-body data cleaning is hard because camera location, joint structure, hands, chassis, and degrees of freedom differ across embodiments.
- Task assignment is a data problem: a collection run has to cover head, waist, hands, base, wrist cameras, and scene changes rather than repeat one narrow behavior.
- Data quality and data modality can beat raw hours when model teams need action-relevant, physically grounded signal.
- The source's "data native" next step means collecting data in ways that match what embodied models can actually use.

## Connections
- [[RealRobotDataStrategy]] — existing page on target-domain and real-machine data.
- [[EmbodiedDataPyramid]] — adjacent view that balances real robot data with simulation and human/internet data.
- [[EmbodiedRobotDataParadigms]] — changing collection methods such as teleoperation, body-free capture, first-person video, motion capture, and dexterous-hand data.
- [[RoboticsSimulationEvaluation]] and [[Sim2Real]] — evaluation and simulation context that the source qualifies.
- [[RobotExperienceData]] and [[RobotReinforcementLearning]] — Physical Intelligence route where robot-owned attempts and corrections become data.
- [[EmbodiedNativeFoundationModels]] and [[VisionLanguageActionModels]] — model routes whose progress depends on scalable embodied data.
