---
title: "Tactile Sensing"
type: concept
tags: [robotics, sensors, embodied-ai, multimodal-ai]
sources: [cong-hui-tiaowu-dao-you-ganzhi-chujue-shi-jiqiren-tongwang-zhineng-de-menpiao-ma-s10e19-f448a656-3004-430b-a853-79d1e77dcb53]
last_updated: 2026-07-08
---

# Tactile Sensing

Tactile sensing is the robot ability to perceive contact, force, texture, friction, slip, softness, hardness, and other near-field physical signals. In [[cong-hui-tiaowu-dao-you-ganzhi-chujue-shi-jiqiren-tongwang-zhineng-de-menpiao-ma-s10e19-f448a656-3004-430b-a853-79d1e77dcb53]], [[EricLiZhiqiang]] argues that tactile sensing is not a peripheral sensor feature but a core infrastructure layer for [[EmbodiedAI]].

The source's argument starts from the limits of vision. Cameras and lidar can identify objects and support motion, but they struggle with fine contact precision, hidden contact surfaces, and force feedback. For [[DexterousManipulation]], that means a robot may know where a cup is but not whether it is slipping, how much force to apply, or how the grip should change when the cup is full rather than empty.

## Key Claims
- Touch supplies the close-range feedback that vision loses under occlusion, contact, and force-control constraints.
- Human fine manipulation depends heavily on tactile feedback; examples such as buttoning, threading a needle, cable insertion, and medical puncture show why visual plans alone are insufficient.
- Tactile data can be relatively close to ground truth for force and deformation, but it is also high-frequency and continuous, so it creates latency and alignment requirements.
- Tactile sensing can make [[VisionLanguageActionModels]] more physically grounded by adding a touch modality rather than only vision and language.
- Near-term commercialization is more plausible in bounded industrial and medical tasks than in open-ended home robotics.

## Connections
- [[OpticalTactileSensing]] — technical route emphasized by the episode.
- [[TouchNet]] and [[TactileTransformerEncoder]] — data and modeling infrastructure for touch.
- [[EmbodiedAI]], [[DexterousManipulation]], [[RealRobotDataStrategy]], and [[PhysicalWorldDataFlywheel]] — broader robotics concepts extended by tactile sensing.
- [[YimuTechnology]] and [[EricLiZhiqiang]] — company and guest associated with the source's tactile-sensing thesis.
