---
title: "Real Robot Data Strategy"
type: concept
tags: [robotics, data, models]
sources:
  - e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e
  - cong-hui-tiaowu-dao-you-ganzhi-chujue-shi-jiqiren-tongwang-zhineng-de-menpiao-ma-s10e19-f448a656-3004-430b-a853-79d1e77dcb53
  - jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1
  - 132-dui-xinghaitu-chuangshiren-gaojiyang-de-3-xiaoshi-fangtan
  - 134-shuju-de-zongshu-he-xiechen-liao-xinshidai-de-shiyou-lishi-bantu-shuju-jinzita-dingjia-yu-recipe
  - 166-xu-huazhe-zaici-jushen-chuangye-buxiang-cuoguo-zuida-de-xigua-1-166-1
  - 146-dui-physical-intelligence-ke-li-yiming-4-xiaoshi-fangtan-pi-de-kaiyuan-moxing-yanjiu-jiqiren-de-jianghu-zupu-yu-zhujiao-ljmazvdvad7o5md-nuiompd6-1nv
  - 147-he-mayi-lingbo-shenyujun-liao-jiqiren-yuansheng-jichu-moxing-danao-he-benti-de-guanxi-yuxunlian-yu-shuju-scale-up-laoshi-tangxiaoou-luxtyuafi-2onim15fw6lpypo2ga
  - bots-on-the-ground-china-leads-humanoid-race-6a91564cee851f3f31239bbf
last_updated: 2026-08-29
knowledge_schema: synthesis-v1
---

# Real Robot Data Strategy

## Definition
Real robot data strategy is the discipline of collecting, selecting, cleaning, pricing, and combining physical-world data so robot models can learn actions that transfer to real robot bodies and real environments.

## Current Synthesis
The bounded sources do not support a simple "more real data wins" rule. Real machine data remains the most grounded evidence because it includes embodiment, sensor noise, contact, failure, and control consequences, but it is expensive, scarce, body-specific, and hard to scale without deployed fleets. The practical synthesis is a recipe problem: real-machine data, teleoperation, robot-owned experience, egocentric human sensor data, first-person video, structured 3D data, tactile data, simulation, and task design have to be matched to the robot body and capability being trained.

The newest source makes the scale problem concrete through China. [[RobotTrainingCenters]] can stage coffee, pharmacy, grocery, and factory tasks for human-robot pairs, while [[JDCom|JD.com / 京东]] tries to collect large volumes of [[EgocentricRobotData]] from workers and outside participants. That strengthens the case that data infrastructure may become a national and corporate asset, while preserving earlier cautions that millions of hours are valuable only if the data is usable for models and deployment.

## Key Claims
- Real-machine data is valuable because it captures actual embodiment, sensor noise, contact, failures, and execution distributions.
- Real robot data is not automatically scalable; cost, robot availability, task design, body variation, and cleaning pipelines determine whether new hours improve capability.
- Simulation and structured 3D data remain important because the physical world contains geometry, material, friction, parts, and future-state dynamics that ordinary video cannot fully capture.
- Human-centric data, including first-person video and [[EgocentricRobotData]], can broaden scene coverage but still needs transfer into robot-body action.
- Robot-owned experience data is distinct from human demonstration because it records the robot's own attempts, corrections, and throughput limits.
- Tactile and dexterous-hand data are especially hardware-specific, so data recipes must account for sensors, degrees of freedom, latency, and retargeting.
- National-scale or company-scale collection infrastructure can accelerate robotics, but it also risks confusing raw hours with grounded, model-usable physical experience.

## Evidence
- Real-data and whole-machine evidence: [[132-dui-xinghaitu-chuangshiren-gaojiyang-de-3-xiaoshi-fangtan]] argues that the robot body is both product and data carrier, while still treating simulation, UMI-style collection, third-person data, and human-centric data as experimental ingredients.
- Simulation and recipe evidence: [[134-shuju-de-zongshu-he-xiechen-liao-xinshidai-de-shiyou-lishi-bantu-shuju-jinzita-dingjia-yu-recipe]] places real robot data at the valuable but costly top of an embodied data pyramid and argues for simulation, evaluation, and data-recipe co-creation.
- Structured manipulation evidence: [[e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e]] says robots lack a Tesla-like deployed fleet and need structured 3D data, sim-to-real work, and low-level manipulation primitives for open-world tasks.
- Paradigm-shift evidence: [[jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1]] and [[147-he-mayi-lingbo-shenyujun-liao-jiqiren-yuansheng-jichu-moxing-danao-he-benti-de-guanxi-yuxunlian-yu-shuju-scale-up-laoshi-tangxiaoou-luxtyuafi-2onim15fw6lpypo2ga]] show data collection shifting across Aloha-style teleoperation, UMI, egocentric video, whole-body motion capture, dexterous hands, and cross-body cleaning.
- Tactile-data evidence: [[cong-hui-tiaowu-dao-you-ganzhi-chujue-shi-jiqiren-tongwang-zhineng-de-menpiao-ma-s10e19-f448a656-3004-430b-a853-79d1e77dcb53]] argues that touch data can supply force, deformation, friction, and slip signals unavailable to vision alone, while still using simulation and video pretraining.
- Household and experience evidence: [[166-xu-huazhe-zaici-jushen-chuangye-buxiang-cuoguo-zuida-de-xigua-1-166-1]] and [[146-dui-physical-intelligence-ke-li-yiming-4-xiaoshi-fangtan-pi-de-kaiyuan-moxing-yanjiu-jiqiren-de-jianghu-zupu-yu-zhujiao-ljmazvdvad7o5md-nuiompd6-1nv]] emphasize selective video data, failure data, robot-owned attempts, reinforcement learning, and throughput as data-quality tests.
- China infrastructure evidence: [[bots-on-the-ground-china-leads-humanoid-race-6a91564cee851f3f31239bbf]] reports robot training centers, human-robot task stations, hourly training costs, and JD.com's plan to collect large-scale sensor-wearer movement data.

## Counterevidence & Qualifications
The sources disagree on weighting rather than on the existence of the bottleneck. Gao Jiyang and Shen Yujun lean toward real-machine grounding, Xie Chen stresses simulation and data recipes because real data is too costly to scale alone, and Han Zheng argues that structured 3D and layered manipulation may be necessary for generalization. The newest source's large-hour targets and training-center counts should not be read as proof of capability; the data still has to cover the right tasks, bodies, sensors, failures, and deployment conditions.

## What Changed
- Migrated the legacy page to the synthesis-v1 concept schema.
- Added China's robot-training-center buildout as a concrete real-machine data infrastructure case.
- Added JD.com's mass sensor-wearer plan as an egocentric data-scale strategy.
- Rebalanced the synthesis away from source-by-source accumulation toward a data-recipe view.

## Related Concepts
- [[RobotDataScaleUp]] - broader scale problem behind embodied foundation models.
- [[RobotTrainingCenters]] - staged real-machine collection infrastructure added by the newest source.
- [[EgocentricRobotData]] - human first-person sensor data that can broaden physical-task coverage.
- [[EmbodiedRobotDataParadigms]] - changing collection methods that make different robot-model routes possible.
- [[RoboticsSimulationEvaluation]] - simulation and evaluation route that complements expensive real-machine collection.
- [[RobotExperienceData]] - robot-owned attempts, failures, and corrections as a distinct data source.
- [[PhysicalWorldDataFlywheel]] - product-deployment loop that would make real-world robot data compound.
