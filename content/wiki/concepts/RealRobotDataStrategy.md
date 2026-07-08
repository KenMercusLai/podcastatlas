---
title: "Real Robot Data Strategy"
type: concept
tags: [robotics, data, models]
sources: [cong-hui-tiaowu-dao-you-ganzhi-chujue-shi-jiqiren-tongwang-zhineng-de-menpiao-ma-s10e19-f448a656-3004-430b-a853-79d1e77dcb53, jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1, 132-dui-xinghaitu-chuangshiren-gaojiyang-de-3-xiaoshi-fangtan, 134-shuju-de-zongshu-he-xiechen-liao-xinshidai-de-shiyou-lishi-bantu-shuju-jinzita-dingjia-yu-recipe]
last_updated: 2026-07-08
---

# Real Robot Data Strategy

Real robot data strategy is the approach to robot model training described by [[GaoJiyang]] in [[132-dui-xinghaitu-chuangshiren-gaojiyang-de-3-xiaoshi-fangtan]]. He argues that useful embodied intelligence should be trained as much as possible on target-domain data, while still experimenting with simulation, teleoperation, human-centric data, point-of-view data, third-person video, and other sources.

[[134-shuju-de-zongshu-he-xiechen-liao-xinshidai-de-shiyou-lishi-bantu-shuju-jinzita-dingjia-yu-recipe]] qualifies this view through [[XieChen]]. He agrees that real robot data is valuable, but argues it can be overestimated when treated as the main scalable path; in his [[EmbodiedDataPyramid]], real robot data is the top layer because it is accurate, expensive, and hard to scale.

[[jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1]] adds [[EmbodiedRobotDataParadigms]] as the time-varying version of the data problem. [[ChenZhePeter]] traces shifts from Aloha-style real-robot teleoperation to UMI body-free collection, egocentric video, whole-body motion capture, and dexterous-hand data, arguing that each model-route change depends on a new way to collect relevant physical experience.

[[cong-hui-tiaowu-dao-you-ganzhi-chujue-shi-jiqiren-tongwang-zhineng-de-menpiao-ma-s10e19-f448a656-3004-430b-a853-79d1e77dcb53]] adds [[EricLiZhiqiang]]'s tactile-data version. He says real machine data is best but may only be 10-20% of the recipe because collection is costly and scarce; [[YimuTechnology]] therefore combines real [[TactileSensing]] data, simulation with [[OpticalTactileSensing]], and large-scale video pretraining before aligning touch with robot actions.

## Key Claims
- Traditional graphics simulation can have a large sim-to-real gap, so it should not be assumed to replace real robot operation data.
- Data cost has to be counted together with training cost and engineer cost; low-quality data can waste the expensive parts of the stack.
- The right "data recipe" is empirical: different data types may help, but their proportions have to be discovered through experiments.
- Scaling real data requires entering real scenes and distributing collection devices or robots widely enough for the data to compound.
- Dexterous-hand data is especially body-specific: hand geometry, motors, degrees of freedom, and sensors can make retargeting across hardware difficult.
- Tactile data adds force, deformation, friction, and slip signals that visual data does not contain, but it must be processed quickly enough for real-time correction.

## Connections
- [[PhysicalWorldDataFlywheel]] — larger loop that turns data into product improvement.
- [[Xinghaitu]], [[GaoJiyang]], and [[VisionLanguageActionModels]] — source company, speaker, and model route.
- [[CausalWorldModels]] and [[WorldModels]] — adjacent model directions where data quality and physical grounding also matter.
- [[EmbodiedAI]] — broader field where real-world distribution shift makes data strategy central.
- [[XieChen]], [[GuanglunIntelligence]], [[EmbodiedDataPyramid]], and [[RoboticsSimulationEvaluation]] — source and concepts that put real robot data inside a simulation-centered data loop.
- [[EmbodiedRobotDataParadigms]], [[RobotTeleoperationAndRemoteTakeover]], [[DexterousManipulation]], and [[Generalist]] — new data-collection and body-specific-data layer from the LateTalk source.
- [[YimuTechnology]], [[TactileSensing]], [[OpticalTactileSensing]], [[TouchNet]], and [[TactileTransformerEncoder]] — tactile real-data and model-interface layer added by the What's Next source.
