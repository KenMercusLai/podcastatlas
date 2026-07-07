---
title: "Real Robot Data Strategy"
type: concept
tags: [robotics, data, models]
sources: [132-dui-xinghaitu-chuangshiren-gaojiyang-de-3-xiaoshi-fangtan, 134-shuju-de-zongshu-he-xiechen-liao-xinshidai-de-shiyou-lishi-bantu-shuju-jinzita-dingjia-yu-recipe]
last_updated: 2026-07-08
---

# Real Robot Data Strategy

Real robot data strategy is the approach to robot model training described by [[GaoJiyang]] in [[132-dui-xinghaitu-chuangshiren-gaojiyang-de-3-xiaoshi-fangtan]]. He argues that useful embodied intelligence should be trained as much as possible on target-domain data, while still experimenting with simulation, teleoperation, human-centric data, point-of-view data, third-person video, and other sources.

[[134-shuju-de-zongshu-he-xiechen-liao-xinshidai-de-shiyou-lishi-bantu-shuju-jinzita-dingjia-yu-recipe]] qualifies this view through [[XieChen]]. He agrees that real robot data is valuable, but argues it can be overestimated when treated as the main scalable path; in his [[EmbodiedDataPyramid]], real robot data is the top layer because it is accurate, expensive, and hard to scale.

## Key Claims
- Traditional graphics simulation can have a large sim-to-real gap, so it should not be assumed to replace real robot operation data.
- Data cost has to be counted together with training cost and engineer cost; low-quality data can waste the expensive parts of the stack.
- The right "data recipe" is empirical: different data types may help, but their proportions have to be discovered through experiments.
- Scaling real data requires entering real scenes and distributing collection devices or robots widely enough for the data to compound.

## Connections
- [[PhysicalWorldDataFlywheel]] — larger loop that turns data into product improvement.
- [[Xinghaitu]], [[GaoJiyang]], and [[VisionLanguageActionModels]] — source company, speaker, and model route.
- [[CausalWorldModels]] and [[WorldModels]] — adjacent model directions where data quality and physical grounding also matter.
- [[EmbodiedAI]] — broader field where real-world distribution shift makes data strategy central.
- [[XieChen]], [[GuanglunIntelligence]], [[EmbodiedDataPyramid]], and [[RoboticsSimulationEvaluation]] — source and concepts that put real robot data inside a simulation-centered data loop.
