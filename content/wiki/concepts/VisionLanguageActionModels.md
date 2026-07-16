---
title: "Vision Language Action Models"
type: concept
tags: [robotics, embodied-ai, models]
sources: [e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e, cong-hui-tiaowu-dao-you-ganzhi-chujue-shi-jiqiren-tongwang-zhineng-de-menpiao-ma-s10e19-f448a656-3004-430b-a853-79d1e77dcb53, jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1, na-tiao-luxian-caineng-tongwang-shijie-moxing-de-zhongju-duihua-huang-biwei-aether-ai-chuangshiren-lgg-env6jrpgvyiwtxw6bocdzdmr, 131-yin-qi-churen-jieyue-xingchen-dongshizhang-de-fangtan, jushen-zhineng-de-taotian-da-paomo-zhong-ta-yijing-ba-jiqiren-songjin-300-ge-jiating-duihua-zhang-yi-weilaibuyuan-chuangshiren-ceo-lic8b7dkxts3qjrs6af1rgbf4xrf, 132-dui-xinghaitu-chuangshiren-gaojiyang-de-3-xiaoshi-fangtan, 134-shuju-de-zongshu-he-xiechen-liao-xinshidai-de-shiyou-lishi-bantu-shuju-jinzita-dingjia-yu-recipe, 166-xu-huazhe-zaici-jushen-chuangye-buxiang-cuoguo-zuida-de-xigua-1-166-1]
last_updated: 2026-07-16
---

# Vision Language Action Models

Vision language action models, or VLA models, are robot models discussed in [[na-tiao-luxian-caineng-tongwang-shijie-moxing-de-zhongju-duihua-huang-biwei-aether-ai-chuangshiren-lgg-env6jrpgvyiwtxw6bocdzdmr]] as one route toward [[EmbodiedAI]]. The source treats them as useful for connecting perception, instruction, and action, but limited as a final route to [[WorldModels]].

[[131-yin-qi-churen-jieyue-xingchen-dongshizhang-de-fangtan]] mentions VLA as one of [[StepFun]]'s model directions alongside base models and all-modal models. In that episode, VLA is less a detailed robotics architecture than a sign that foundation-model companies are moving from language and multimodal models toward terminals and physical interaction.

[[jushen-zhineng-de-taotian-da-paomo-zhong-ta-yijing-ba-jiqiren-songjin-300-ge-jiating-duihua-zhang-yi-weilaibuyuan-chuangshiren-ceo-lic8b7dkxts3qjrs6af1rgbf4xrf]] adds [[ZhangYi]]'s operator view from [[WeilaiBuyuan]]. He treats VLA as still iterating alongside [[WorldModels]], so [[F2HomeRobot]] uses real-home deployment and engineering integration while the modeling routes mature.

[[132-dui-xinghaitu-chuangshiren-gaojiyang-de-3-xiaoshi-fangtan]] adds [[GaoJiyang]]'s production-robot architecture through [[Xinghaitu]]. He describes a dual system where a vision-language model layer decomposes fuzzy instructions and handles logic, while VLA executes physical actions; he rejects putting every ability into one end-to-end model because endpoint compute and latency still matter.

[[134-shuju-de-zongshu-he-xiechen-liao-xinshidai-de-shiyou-lishi-bantu-shuju-jinzita-dingjia-yu-recipe]] adds [[XieChen]]'s data-demand view. He says large-model teams with VLA groups often have more compute and reinforcement-learning infrastructure than robot startups, but still need [[EmbodiedDataPyramid]], [[RoboticsSimulationEvaluation]], and [[DataRecipeCoCreation]] to test whether VLA capability is really improving.

[[jushen-jibao-26q2-shijie-moxing-dafeng-buting-he-buxiang-bei-tie-biaoqian-de-ren-1-170-1]] adds a route-convergence update. [[ChenZhePeter]] says VLA models are strong at instruction and action generation, while [[WorldModels]] improve prediction of future state; Physical Intelligence's Pi 0.7 is used as an example of VLA augmented with lightweight future-image prediction. The source also uses [[Generalist]] to show that some robot-model companies deliberately avoid the VLA label, even when their work remains adjacent to VLA and real interaction data.

[[cong-hui-tiaowu-dao-you-ganzhi-chujue-shi-jiqiren-tongwang-zhineng-de-menpiao-ma-s10e19-f448a656-3004-430b-a853-79d1e77dcb53]] adds a tactile extension. [[EricLiZhiqiang]] argues that VLA may need to evolve toward a VTLA-style stack where tactile signals are encoded by [[TactileTransformerEncoder]], aligned with visual features, and used by the robot backbone to reason about force, texture, softness, friction, and slip.

[[166-xu-huazhe-zaici-jushen-chuangye-buxiang-cuoguo-zuida-de-xigua-1-166-1]] adds a critique from [[XuHuazhe]]'s [[AINativeRobotics]] route. He does not reject VLA as a useful vocabulary, but argues that a household robot should not be reduced to small model stitching or one-task policies; the action and behavior layer should move toward [[UnifiedRobotModels]] if the goal is [[PhysicalAGI]].

[[e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e]] adds [[HanZheng]]'s distinction between deployed end-to-end behavior and training-time structure. He argues that a robot policy can run end-to-end at the edge while still learning through [[LayeredRobotArchitecture]], [[Structured3DRobotData]], and [[Sim2Real]] rather than pure imitation of human or teleoperation trajectories.

## Limitation
[[HuangBiwei]] argues that VLA generalization is constrained because the action side is a continuous space. Demonstration data can cover many examples, but cannot exhaustively cover all physical states, object conditions, and action variations a robot may encounter.

[[HanZheng]] adds a manipulation-specific limitation: imitation trajectories may reproduce the motion of opening or screwing without understanding the bottle cap, thread, rotation direction, material contact, or future-state change.

## Connections
- [[CausalWorldModels]] — route Huang presents as a higher-ceiling alternative.
- [[WorldActionModels]] — related intermediate approach described as stronger than VLA but still incomplete.
- [[EmbodiedAI]] and [[WorldModels]] — broader robotics and world-model context.
- [[AetherAI]] — company pursuing the causal route rather than a pure VLA route.
- [[StepFun]], [[YinQi]], and [[AIPlusTerminals]] — foundation-model and terminal strategy context where VLA appears as a future direction.
- [[WeilaiBuyuan]], [[F2HomeRobot]], and [[HouseholdRobotDataFlywheel]] — home-service robot deployment case where VLA remains a practical but unfinished route.
- [[Xinghaitu]], [[GaoJiyang]], [[RealRobotDataStrategy]], and [[ProductionRobotScenarioSelection]] — production-robot case where VLA is paired with instruction decomposition and real-scene data.
- [[XieChen]], [[GuanglunIntelligence]], [[EmbodiedDataPyramid]], and [[RoboticsSimulationEvaluation]] — data and evaluation infrastructure for VLA progress.
- [[WorldModelVLAFusion]], [[PhysicalIntelligence]], and [[Generalist]] — Q2 2026 examples where VLA becomes harder to separate from world-model and interaction-data routes.
- [[TactileSensing]], [[TouchNet]], and [[TactileTransformerEncoder]] — touch-modality extension that the What's Next source proposes for VLA-style systems.
- [[AINativeRobotics]], [[UnifiedRobotModels]], and [[PhysicalAGI]] — Xu Huazhe's critique of narrow task stitching.
- [[SuduTechnology]], [[LayeredRobotArchitecture]], [[Structured3DRobotData]], and [[Sim2Real]] — E244's alternative to pure VLA imitation.
