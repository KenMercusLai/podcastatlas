---
title: "TouchNet"
type: concept
tags: [robotics, data, tactile-sensing, datasets]
sources: [cong-hui-tiaowu-dao-you-ganzhi-chujue-shi-jiqiren-tongwang-zhineng-de-menpiao-ma-s10e19-f448a656-3004-430b-a853-79d1e77dcb53]
last_updated: 2026-07-08
---

# TouchNet

TouchNet is the tactile dataset project described by [[EricLiZhiqiang]] in [[cong-hui-tiaowu-dao-you-ganzhi-chujue-shi-jiqiren-tongwang-zhineng-de-menpiao-ma-s10e19-f448a656-3004-430b-a853-79d1e77dcb53]]. [[YimuTechnology]] frames it as an [[ImageNet]]-like effort for [[TactileSensing]]: a shared data resource that could make touch models easier to train, compare, and integrate into robot systems.

The source treats TouchNet as necessary because tactile AI lacks the historical data inheritance that computer vision received from large image datasets. The challenge is not only volume. Touch data also needs physical definitions for softness, hardness, roughness, smoothness, friction, and slip, plus alignment across tactile, visual, audio, and temporal streams.

## Key Claims
- Tactile AI is data-poor compared with vision and language, so shared datasets may be a field-level accelerator.
- Touch labels are harder than image labels because many tactile concepts require physical thresholds and continuous time-series evidence.
- [[TouchNet]] would support [[TactileTransformerEncoder]] training and multimodal alignment with visual robot inputs.
- The dataset sits inside a broader [[EmbodiedDataPyramid]] rather than replacing real deployment, simulation, or video pretraining.

## Connections
- [[ImageNet]] — analogy for a dataset that accelerates a field.
- [[YimuTechnology]] and [[EricLiZhiqiang]] — organization and speaker attached to the project.
- [[TactileSensing]], [[OpticalTactileSensing]], and [[TactileTransformerEncoder]] — data domain, sensor route, and model interface.
- [[EmbodiedDataPyramid]], [[RealRobotDataStrategy]], and [[RoboticsSimulationEvaluation]] — broader robot-data strategy concepts.
