---
title: "Real Robot Data Strategy"
type: concept
tags: [robotics, data, models]
sources: [e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e, cong-hui-tiaowu-dao-you-ganzhi-chujue-shi-jiqiren-tongwang-zhineng-de-menpiao-ma-s10e19-f448a656-3004-430b-a853-79d1e77dcb53, jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1, 132-dui-xinghaitu-chuangshiren-gaojiyang-de-3-xiaoshi-fangtan, 134-shuju-de-zongshu-he-xiechen-liao-xinshidai-de-shiyou-lishi-bantu-shuju-jinzita-dingjia-yu-recipe, 166-xu-huazhe-zaici-jushen-chuangye-buxiang-cuoguo-zuida-de-xigua-1-166-1, 146-dui-physical-intelligence-ke-li-yiming-4-xiaoshi-fangtan-pi-de-kaiyuan-moxing-yanjiu-jiqiren-de-jianghu-zupu-yu-zhujiao-ljmazvdvad7o5md-nuiompd6-1nv]
last_updated: 2026-07-18
---

# Real Robot Data Strategy

Real robot data strategy is the approach to robot model training described by [[GaoJiyang]] in [[132-dui-xinghaitu-chuangshiren-gaojiyang-de-3-xiaoshi-fangtan]]. He argues that useful embodied intelligence should be trained as much as possible on target-domain data, while still experimenting with simulation, teleoperation, human-centric data, point-of-view data, third-person video, and other sources.

[[134-shuju-de-zongshu-he-xiechen-liao-xinshidai-de-shiyou-lishi-bantu-shuju-jinzita-dingjia-yu-recipe]] qualifies this view through [[XieChen]]. He agrees that real robot data is valuable, but argues it can be overestimated when treated as the main scalable path; in his [[EmbodiedDataPyramid]], real robot data is the top layer because it is accurate, expensive, and hard to scale.

[[jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1]] adds [[EmbodiedRobotDataParadigms]] as the time-varying version of the data problem. [[ChenZhePeter]] traces shifts from Aloha-style real-robot teleoperation to UMI body-free collection, egocentric video, whole-body motion capture, and dexterous-hand data, arguing that each model-route change depends on a new way to collect relevant physical experience.

[[cong-hui-tiaowu-dao-you-ganzhi-chujue-shi-jiqiren-tongwang-zhineng-de-menpiao-ma-s10e19-f448a656-3004-430b-a853-79d1e77dcb53]] adds [[EricLiZhiqiang]]'s tactile-data version. He says real machine data is best but may only be 10-20% of the recipe because collection is costly and scarce; [[YimuTechnology]] therefore combines real [[TactileSensing]] data, simulation with [[OpticalTactileSensing]], and large-scale video pretraining before aligning touch with robot actions.

[[166-xu-huazhe-zaici-jushen-chuangye-buxiang-cuoguo-zuida-de-xigua-1-166-1]] adds [[XuHuazhe]]'s household-robot version. He expects more video data to enter robot training, says teleoperation can show progress but may not be the final data source, and argues that failure data or suboptimal data should be used selectively rather than discarded or mixed blindly.

[[e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e]] adds [[HanZheng]]'s sharper critique of real-data scaling. He argues that robots do not yet have a Tesla-like deployed fleet, and that asking users to teleoperate household robots at massive scale is not a realistic substitute. The source therefore treats real robot data as necessary validation and adaptation data, not as the sole source of [[OpenWorldRobotManipulation]].

[[146-dui-physical-intelligence-ke-li-yiming-4-xiaoshi-fangtan-pi-de-kaiyuan-moxing-yanjiu-jiqiren-de-jianghu-zupu-yu-zhujiao-ljmazvdvad7o5md-nuiompd6-1nv]] adds [[KPhysicalIntelligence|K]]'s [[RobotExperienceData]] distinction. Human teleoperation data can start a policy, but π0.6* uses robot-owned attempts, failures, and correction traces so [[RobotReinforcementLearning]] can improve task throughput on real machines.

## Key Claims
- Traditional graphics simulation can have a large sim-to-real gap, so it should not be assumed to replace real robot operation data.
- Data cost has to be counted together with training cost and engineer cost; low-quality data can waste the expensive parts of the stack.
- The right "data recipe" is empirical: different data types may help, but their proportions have to be discovered through experiments.
- Scaling real data requires entering real scenes and distributing collection devices or robots widely enough for the data to compound.
- Robotics lacks the autonomous-driving-style installed fleet that would make passive real-world data collection cheap and broad.
- Dexterous-hand data is especially body-specific: hand geometry, motors, degrees of freedom, and sensors can make retargeting across hardware difficult.
- Tactile data adds force, deformation, friction, and slip signals that visual data does not contain, but it must be processed quickly enough for real-time correction.
- [[UnifiedRobotModels]] require data selection, not only data volume, because post-training can otherwise improve fixed tasks while shrinking generalization.
- [[RobotExperienceData]] is valuable because it binds action, failure, correction, and embodiment in the robot's own hardware rather than only in human demonstrations.

## Connections
- [[PhysicalWorldDataFlywheel]] — larger loop that turns data into product improvement.
- [[Xinghaitu]], [[GaoJiyang]], and [[VisionLanguageActionModels]] — source company, speaker, and model route.
- [[CausalWorldModels]] and [[WorldModels]] — adjacent model directions where data quality and physical grounding also matter.
- [[EmbodiedAI]] — broader field where real-world distribution shift makes data strategy central.
- [[XieChen]], [[GuanglunIntelligence]], [[EmbodiedDataPyramid]], and [[RoboticsSimulationEvaluation]] — source and concepts that put real robot data inside a simulation-centered data loop.
- [[EmbodiedRobotDataParadigms]], [[RobotTeleoperationAndRemoteTakeover]], [[DexterousManipulation]], and [[Generalist]] — new data-collection and body-specific-data layer from the LateTalk source.
- [[YimuTechnology]], [[TactileSensing]], [[OpticalTactileSensing]], [[TouchNet]], and [[TactileTransformerEncoder]] — tactile real-data and model-interface layer added by the What's Next source.
- [[PokeRobotics]], [[XuHuazhe]], [[AINativeRobotics]], [[UnifiedRobotModels]], and [[RobotActiveUseMetrics]] — household-robot data route added by episode 166.
- [[SuduTechnology]], [[Structured3DRobotData]], [[Sim2Real]], and [[OpenWorldRobotManipulation]] — E244's critique of real-data-only scaling.
- [[PhysicalIntelligence]], [[PhysicalIntelligencePiSeries]], [[RobotExperienceData]], and [[RobotReinforcementLearning]] — experience-data and performance-improvement route added by episode 146.
