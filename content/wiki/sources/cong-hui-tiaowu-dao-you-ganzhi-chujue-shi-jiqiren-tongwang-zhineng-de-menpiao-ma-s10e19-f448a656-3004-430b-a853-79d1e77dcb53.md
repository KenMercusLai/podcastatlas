---
title: "从会跳舞到有感知，触觉是机器人通往智能的门票吗？｜ S10E19"
type: source
tags: [podcast, robotics, embodied-ai, tactile-sensing]
sources: []
date: 2026-07-01
source_file: "/home/ken/repos/podcastatlas/content/episodes/从会跳舞到有感知，触觉是机器人通往智能的门票吗？｜ S10E19 [f448a656-3004-430b-a853-79d1e77dcb53].md"
source_url: "https://guiguzaozhidao.fireside.fm/20240433"
last_updated: 2026-07-08
---

## Summary
This [[WhatsNextKejiZaozhidao]] episode interviews [[EricLiZhiqiang]], founder and CEO of [[YimuTechnology]], about why [[TactileSensing]] may be a missing infrastructure layer for [[EmbodiedAI]]. The source argues that robot vision alone is limited by precision, occlusion, and lack of force feedback, especially in [[DexterousManipulation]]. It presents [[OpticalTactileSensing]], [[TouchNet]], and [[TactileTransformerEncoder]] as Yimu's route for turning touch into model-ready data, while treating industrial assembly and medical manipulation as nearer-term deployment paths than general home robots.

## Key Claims
- Vision is not enough for fine manipulation because it cannot reliably resolve millimeter-scale contact, hidden contact surfaces, or gripping force.
- [[EricLiZhiqiang]] scores robot mobility around 90, dexterous hands below 60, tactile capability around 45-50, and the robot "brain" around 30, using those rough scores to argue that physical perception and model understanding remain the bottlenecks.
- Demo tasks such as grabbing eggs or peeling shells do not prove general [[EmbodiedAI]] unless the robot can transfer to different object sizes, textures, and failure states with real-time force feedback.
- The episode says tactile technology has moved through electromagnetic, piezoresistive, and capacitive routes, but that the field is converging toward vision-tactile or optical-tactile methods.
- [[OpticalTactileSensing]] is described as using skin deformation and light changes to infer force distribution, texture, friction, slip, and contact state; Yimu claims high point density and near-human performance on several tactile dimensions.
- The source frames 2026 as a tactile-sensing inflection point because model builders working on [[VisionLanguageActionModels]] and [[WorldModels]] are encountering the limits of vision and language without touch.
- Yimu wants to open simulation tools and some tactile data, and plans [[TouchNet]] as a tactile dataset inspired by [[ImageNet]].
- Tactile input may turn VLA into a VTLA-style model stack, where [[TactileTransformerEncoder]] converts touch into semantic signals that can align with visual features and feed a larger robot model.
- Tactile data is treated as low-latency, relatively accurate, and high-frequency continuous data, so its modeling cannot simply copy static visual recognition pipelines.
- The source's data recipe uses scarce real-machine data, larger simulation data, and broad video pretraining; Eric says real data may only be 10-20% because it is expensive and hard to collect.
- Industrial scenes such as screwdriving, cable insertion, battery-pack assembly, and other "master worker feel" processes are presented as more plausible first markets than home robots.
- Medical puncture and fine surgery are used as examples where touch and force feedback are prerequisites for moving beyond teleoperated systems.
- Yimu's claimed differentiation is cross-disciplinary control of chips, optical design, materials, simulation, algorithms, and data, including a thin silicon-photonics sensing stack and durable soft material.
- The company positions itself as a physical access-layer infrastructure provider rather than as a robot-brain or full robot-body company.

## Key Quotes
> "触觉不是锦上添花" — the episode's answer to whether robot touch is optional.

> "大语言模型可以读万卷书，物理 AI 需要行万里路" — Eric's contrast between language data and physical-world experience.

> "触觉不是一个传感器，而是机器人进入人类物理世界的一张门票" — the source's closing infrastructure frame.

## Connections
- [[EricLiZhiqiang]] and [[YimuTechnology]] — guest and company anchoring the episode.
- [[TactileSensing]], [[OpticalTactileSensing]], [[TouchNet]], and [[TactileTransformerEncoder]] — new touch-specific concepts added by the source.
- [[EmbodiedAI]], [[DexterousManipulation]], [[VisionLanguageActionModels]], [[WorldModels]], and [[WorldModelVLAFusion]] — broader robotics-model context that the episode qualifies with touch.
- [[EmbodiedDataPyramid]], [[RealRobotDataStrategy]], [[RoboticsSimulationEvaluation]], and [[PhysicalWorldDataFlywheel]] — data strategy concepts extended by the source's tactile-data recipe.
- [[FigureAI]], [[Meta]], [[Google]], [[Tesla]], and [[Nvidia]] — companies referenced as part of the broader visual-tactile, robot-model, or simulation ecosystem.
- [[ImageNet]] — analogy for why a shared tactile dataset could matter for model progress.

## Contradictions
- No direct contradiction found. The source reinforces prior wiki claims that real robot data is valuable but expensive, while adding the narrower claim that tactile data may be closer to force and deformation ground truth than visual data. Its positive claims about Yimu's point density, material durability, and near-production readiness are recorded as source claims rather than independently verified benchmarks.
