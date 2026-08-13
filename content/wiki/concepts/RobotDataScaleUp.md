---
title: "Robot Data Scale Up"
type: concept
tags: [robotics, data, embodied-ai, scale]
sources: [150-dui-yingweida-yanjiu-fuzongcai-liu-mingyu-de-4-xiaoshi-fangtan-cosmos-3-shijie-moxing-wushu-huangrenxun-yingxiang-wode-he-ni-bu-xuyao-jibai-suoyou-duishou-lghqbpi7ehexavjv1gjrfv-24k8y, tech-20260807-0807-mp-tech-pod-128-tech-20260807-0807-mp-tech-pod-128, 147-he-mayi-lingbo-shenyujun-liao-jiqiren-yuansheng-jichu-moxing-danao-he-benti-de-guanxi-yuxunlian-yu-shuju-scale-up-laoshi-tangxiaoou-luxtyuafi-2onim15fw6lpypo2ga]
last_updated: 2026-08-13
---

# Robot Data Scale Up

[[150-dui-yingweida-yanjiu-fuzongcai-liu-mingyu-de-4-xiaoshi-fangtan-cosmos-3-shijie-moxing-wushu-huangrenxun-yingxiang-wode-he-ni-bu-xuyao-jibai-suoyou-duishou-lghqbpi7ehexavjv1gjrfv-24k8y]] adds [[Cosmos3]]'s "better data" version through [[LiuMingyu|Liu Ming-Yu / 刘洺堉]]. Liu separates navigation data, which can be more shareable, from manipulation data, which is messier because hands, contact, object states, and body configuration matter more. The source says Cosmos 3 adds egocentric data, including human-eye viewpoints and hand-operation footage, to improve [[PhysicalAI]] generalization.

Robot data scale up is the bottleneck named by [[ShenYujun|沈宇军]] in [[147-he-mayi-lingbo-shenyujun-liao-jiqiren-yuansheng-jichu-moxing-danao-he-benti-de-guanxi-yuxunlian-yu-shuju-scale-up-laoshi-tangxiaoou-luxtyuafi-2onim15fw6lpypo2ga]]. Shen says embodied intelligence has not yet reached a robot GPT-1 moment because the field lacks a data-scaling method comparable to internet-scale language data.

In the source, scaling does not mean simply recording more robot hours. [[AntLingbo|蚂蚁灵波]] expands from about 20,000 to about 60,000 hours in its second generation, but Shen emphasizes that stricter cleaning, task choice, body coverage, camera positions, degrees of freedom, and data usability matter as much as volume.

[[tech-20260807-0807-mp-tech-pod-128-tech-20260807-0807-mp-tech-pod-128]] adds a consumer-press example of this bottleneck through [[HouseholdRobotTrainingData]]. [[JoannaStern]] describes startups paying people to film ordinary chores with head-mounted cameras so robot models can capture hand movement, task sequencing, and physical interaction before robots can reliably gather enough experience on their own.

## Key Claims
- Real-machine data is valuable because it contains actual sensor noise, body constraints, execution latency, and physical failures.
- eGo-style first-person human data can scale some everyday scene and task coverage, but it may not contain enough hand-specific or contact-specific information for fine manipulation.
- Simulation is useful for evaluation and partial scenes, but the source treats it as insufficient for general flexible-object and complex manipulation training by itself.
- Cross-body data cleaning is hard because camera location, joint structure, hands, chassis, and degrees of freedom differ across embodiments.
- Task assignment is a data problem: a collection run has to cover head, waist, hands, base, wrist cameras, and scene changes rather than repeat one narrow behavior.
- Data quality and data modality can beat raw hours when model teams need action-relevant, physically grounded signal.
- The source's "data native" next step means collecting data in ways that match what embodied models can actually use.
- Marketplace Tech adds that first-person human chore footage can help scale everyday household-task coverage, but it also raises labor, privacy, and task-quality questions.
- Cosmos 3 adds that egocentric data can support developer starting points, but data still has to be evaluated against task-specific customer pain rather than volume alone.

## Connections
- [[RealRobotDataStrategy]] — existing page on target-domain and real-machine data.
- [[EmbodiedDataPyramid]] — adjacent view that balances real robot data with simulation and human/internet data.
- [[EmbodiedRobotDataParadigms]] — changing collection methods such as teleoperation, body-free capture, first-person video, motion capture, and dexterous-hand data.
- [[RoboticsSimulationEvaluation]] and [[Sim2Real]] — evaluation and simulation context that the source qualifies.
- [[RobotExperienceData]] and [[RobotReinforcementLearning]] — Physical Intelligence route where robot-owned attempts and corrections become data.
- [[EmbodiedNativeFoundationModels]] and [[VisionLanguageActionModels]] — model routes whose progress depends on scalable embodied data.
- [[HouseholdRobotTrainingData]], [[AITrainerLabor]], and [[HumanoidRobotCommercialization]] — paid human demonstration branch added by Marketplace Tech.
- [[Cosmos3]], [[WorldFoundationModels]], [[LiuMingyu|Liu Ming-Yu / 刘洺堉]], and [[RobotGeneralizationPerformanceTradeoff]] — Nvidia data and generalization branch added by episode 150.
