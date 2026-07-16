---
title: "Embodied Data Pyramid"
type: concept
tags: [robotics, data, embodied-ai]
sources: [e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e, cong-hui-tiaowu-dao-you-ganzhi-chujue-shi-jiqiren-tongwang-zhineng-de-menpiao-ma-s10e19-f448a656-3004-430b-a853-79d1e77dcb53, jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1, 134-shuju-de-zongshu-he-xiechen-liao-xinshidai-de-shiyou-lishi-bantu-shuju-jinzita-dingjia-yu-recipe]
last_updated: 2026-07-16
---

# Embodied Data Pyramid

Embodied data pyramid is [[XieChen]]'s frame for combining data sources in [[EmbodiedAI]]. In [[134-shuju-de-zongshu-he-xiechen-liao-xinshidai-de-shiyou-lishi-bantu-shuju-jinzita-dingjia-yu-recipe]], the top layer is real robot teleoperation or body data, the middle layer is simulation data, and the bottom layer is internet-scale and human first-person data.

[[jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1]] extends the top and bottom of this pyramid by naming concrete collection shifts: Aloha-style teleoperation, UMI-style body-free data, first-person video, whole-body motion capture, and dexterous-hand datasets. The source's [[EmbodiedRobotDataParadigms]] concept keeps the pyramid dynamic by asking which new data source unlocks which robot capability.

[[cong-hui-tiaowu-dao-you-ganzhi-chujue-shi-jiqiren-tongwang-zhineng-de-menpiao-ma-s10e19-f448a656-3004-430b-a853-79d1e77dcb53]] adds a tactile-data layer through [[YimuTechnology]]. [[EricLiZhiqiang]] says real tactile robot data is valuable but expensive, simulation data should be expanded with [[OpticalTactileSensing]], and large-scale video data can still help pretrain visual priors before touch and action are added.

[[e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e]] adds a structured-3D manipulation layer. [[HanZheng]] argues that real robot operation, teleoperation, motion capture, and first-person video are too scarce or incomplete to cover arbitrary object manipulation, so [[Structured3DRobotData]] and [[Sim2Real]] need to sit between internet-scale priors and real robot validation.

## Key Claims
- Real robot data is most physically accurate but expensive, hard to scale, and therefore too narrow to carry general robotics learning alone.
- [[RoboticsSimulationEvaluation]] is the scalable middle layer because it can generate repeated tasks, failures, counterfactuals, and evaluation scenarios.
- Human first-person and internet data are larger and less body-specific, but can provide scene, object, task, and daily-life priors.
- The pyramid should be a loop: real-world and human data can be converted into simulation worlds, while simulation outputs must be checked against real-world results.
- This creates a tension with pure [[RealRobotDataStrategy]]: real data stays necessary, but the source argues it should not dominate the recipe by default.
- Hardware-specific dexterous-hand data complicates the pyramid because "real robot data" does not transfer cleanly when hand structure, sensors, or drive method change.
- [[TactileSensing]] creates a special data problem because it is high-frequency and continuous while also being closer to force and deformation ground truth than ordinary visual data.
- [[TouchNet]] is proposed as a field-level tactile dataset, but the source still places it inside a broader recipe of scarce real data, simulation, and video pretraining.
- [[Structured3DRobotData]] adds a geometry, parts, material, friction, and dynamics layer that ordinary video and teleoperation cannot supply cleanly.

## Connections
- [[DataAsEducation]] — broader metaphor behind the pyramid.
- [[DataRecipeCoCreation]] — process for discovering how much of each layer improves a model.
- [[PhysicalWorldDataFlywheel]] — adjacent real-world data-loop concept from the [[Xinghaitu]] source.
- [[WorldModels]] and [[VisionLanguageActionModels]] — model routes that need physical-world data and evaluation.
- [[GuanglunIntelligence]] — company building simulation-centered data infrastructure in the source.
- [[EmbodiedRobotDataParadigms]], [[DexterousManipulation]], and [[RobotTeleoperationAndRemoteTakeover]] — collection-method updates from the LateTalk source.
- [[TactileSensing]], [[OpticalTactileSensing]], [[TouchNet]], and [[TactileTransformerEncoder]] — tactile data, sensor route, dataset, and model-interface additions from the What's Next source.
- [[SuduTechnology]], [[ShapeNet]], [[PartNet]], and [[Sim2Real]] — structured 3D and simulation route added by E244.
