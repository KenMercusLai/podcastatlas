---
title: "Vision Language Action Models"
type: concept
tags: [robotics, embodied-ai, models]
sources: [na-tiao-luxian-caineng-tongwang-shijie-moxing-de-zhongju-duihua-huang-biwei-aether-ai-chuangshiren-lgg-env6jrpgvyiwtxw6bocdzdmr, 131-yin-qi-churen-jieyue-xingchen-dongshizhang-de-fangtan, jushen-zhineng-de-taotian-da-paomo-zhong-ta-yijing-ba-jiqiren-songjin-300-ge-jiating-duihua-zhang-yi-weilaibuyuan-chuangshiren-ceo-lic8b7dkxts3qjrs6af1rgbf4xrf]
last_updated: 2026-07-07
---

# Vision Language Action Models

Vision language action models, or VLA models, are robot models discussed in [[na-tiao-luxian-caineng-tongwang-shijie-moxing-de-zhongju-duihua-huang-biwei-aether-ai-chuangshiren-lgg-env6jrpgvyiwtxw6bocdzdmr]] as one route toward [[EmbodiedAI]]. The source treats them as useful for connecting perception, instruction, and action, but limited as a final route to [[WorldModels]].

[[131-yin-qi-churen-jieyue-xingchen-dongshizhang-de-fangtan]] mentions VLA as one of [[StepFun]]'s model directions alongside base models and all-modal models. In that episode, VLA is less a detailed robotics architecture than a sign that foundation-model companies are moving from language and multimodal models toward terminals and physical interaction.

[[jushen-zhineng-de-taotian-da-paomo-zhong-ta-yijing-ba-jiqiren-songjin-300-ge-jiating-duihua-zhang-yi-weilaibuyuan-chuangshiren-ceo-lic8b7dkxts3qjrs6af1rgbf4xrf]] adds [[ZhangYi]]'s operator view from [[WeilaiBuyuan]]. He treats VLA as still iterating alongside [[WorldModels]], so [[F2HomeRobot]] uses real-home deployment and engineering integration while the modeling routes mature.

## Limitation
[[HuangBiwei]] argues that VLA generalization is constrained because the action side is a continuous space. Demonstration data can cover many examples, but cannot exhaustively cover all physical states, object conditions, and action variations a robot may encounter.

## Connections
- [[CausalWorldModels]] — route Huang presents as a higher-ceiling alternative.
- [[WorldActionModels]] — related intermediate approach described as stronger than VLA but still incomplete.
- [[EmbodiedAI]] and [[WorldModels]] — broader robotics and world-model context.
- [[AetherAI]] — company pursuing the causal route rather than a pure VLA route.
- [[StepFun]], [[YinQi]], and [[AIPlusTerminals]] — foundation-model and terminal strategy context where VLA appears as a future direction.
- [[WeilaiBuyuan]], [[F2HomeRobot]], and [[HouseholdRobotDataFlywheel]] — home-service robot deployment case where VLA remains a practical but unfinished route.
