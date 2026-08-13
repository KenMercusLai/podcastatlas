---
title: "World Foundation Models"
type: concept
tags: [ai, world-models, robotics, physical-ai, foundation-models]
sources: [150-dui-yingweida-yanjiu-fuzongcai-liu-mingyu-de-4-xiaoshi-fangtan-cosmos-3-shijie-moxing-wushu-huangrenxun-yingxiang-wode-he-ni-bu-xuyao-jibai-suoyou-duishou-lghqbpi7ehexavjv1gjrfv-24k8y]
last_updated: 2026-08-13
---

# World Foundation Models

World foundation models are [[LiuMingyu|Liu Ming-Yu / 刘洺堉]]'s preferred label for [[Cosmos3]] in [[150-dui-yingweida-yanjiu-fuzongcai-liu-mingyu-de-4-xiaoshi-fangtan-cosmos-3-shijie-moxing-wushu-huangrenxun-yingxiang-wode-he-ni-bu-xuyao-jibai-suoyou-duishou-lghqbpi7ehexavjv1gjrfv-24k8y]]. The term narrows the overbroad [[WorldModels]] label: instead of simply generating plausible video or simulated scenes, the model should provide reusable starting points for developers building [[PhysicalAI]] systems.

In the source, a world foundation model helps through better data, better starting points, and better environments. Better data includes physical-world and egocentric examples; better starting points mean open pretrained models that customers can post-train for their own tasks; better environments point toward simulated worlds where robots and physical agents can practice before costly real-world deployment.

## Key Claims
- A world foundation model is infrastructure, not just a content product; it should help downstream teams train, evaluate, and adapt physical-world agents.
- Action is a first-class modality because physical agents change the world rather than only describe or observe it.
- Useful architecture may mix discrete and continuous signal paths so language, video, audio, and action can be combined without forcing every modality into one representation style.
- Evaluation has to connect benchmarks and arena comparisons to real customer pain because [[PhysicalAI]] failures are often task, body, scene, and cost specific.
- Open releases can be strategic even for a large infrastructure company when they grow the developer ecosystem and reveal future hardware, serving, and simulation needs.
- A single model is unlikely to become the next [[CUDA]] by itself; the platform effect comes from model, serving, infrastructure, tools, hardware feedback, and customer workflows together.

## Connections
- [[CosmosLab]], [[Cosmos3]], [[Nvidia]], and [[LiuMingyu|Liu Ming-Yu / 刘洺堉]] — source team, product, company, and speaker.
- [[WorldModels]], [[WorldActionModels]], and [[WorldModelVLAFusion]] — neighboring model-family concepts.
- [[PhysicalAI]], [[EmbodiedAI]], [[RobotGeneralizationPerformanceTradeoff]], and [[RobotDataScaleUp]] — physical-world problem field.
- [[RoboticsSimulationEvaluation]] — environment and evaluation layer.
- [[LargeCompanyOpenSourceStrategy]] and [[AIInfrastructureFullStackMoat]] — ecosystem and platform strategy behind the release.

