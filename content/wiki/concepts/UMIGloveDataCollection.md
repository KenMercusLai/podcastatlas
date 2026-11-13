---
title: "UMI-Style Glove Data Collection / 手套式数据采集"
type: concept
tags: [robotics, data, embodied-ai, hardware]
sources:
  - yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr
  - 187-duihua-liberai-liu-songming-astra-lai-xi-00-hou-wuli-ai-chuangshiren-kandao-de-shenglv-ad3b421a
last_updated: 2026-11-13
knowledge_schema: synthesis-v1
---

# UMI-Style Glove Data Collection / 手套式数据采集

## Definition
UMI-style glove data collection is a body-free manipulation-data method in which a person wears a sensor-rich handheld device or glove so that hand motion, camera views, timing, and sometimes pose or action information can be recorded as robot-trainable trajectories without operating a robot during collection.

## Current Synthesis
The two bounded sources describe glove collection as a bridge between cheap but action-poor human video and precise but expensive real-robot teleoperation. [[ShenpuIntelligence|深普智能]] emphasizes measurement quality and validation: its six-view device uses camera-based millimeter localization and microsecond synchronization without an external base station, and the team says trajectory replay reproduced more than 95% of collected trajectories on the body before it scaled collection. It later open-sourced about 2,000 hours, reported internal data in the tens of thousands of hours, and disclosed annotation and usability bottlenecks.

[[LiberAI]] emphasizes learning efficiency. Its source says natural glove motion aligns better with human video than slow, viewpoint-mismatched teleoperation and adds precise action information absent from ordinary internet video. The company reports that 10,000 glove hours outperformed two million internet-video hours, and that glove data combined with 25% of its real-robot teleoperation data beat a full teleoperation-only baseline. The synthesis is not that gloves eliminate real-robot data: they may reduce its share while robot deployment remains necessary for embodiment calibration, contact, evaluation, and final reliability.

## Key Claims
- Glove collection can add precise human-action information that ordinary internet video lacks while avoiding the full cost and throughput limits of operating robots during every recording.
- Device precision, synchronization, occlusion handling, annotation, and trajectory replay determine whether nominal collection hours become usable robot data.
- Glove motion may align more naturally with human video than robot teleoperation, but cross-embodiment mapping is still required before execution.
- Real-robot data remains necessary for body calibration, contact dynamics, evaluation, and deployment even if glove data substitutes for part of the teleoperation set.
- Open data can function as research infrastructure and as a commercial lead channel, but download volume is not evidence of deployed robot performance.
- Collection-device usability and sensor choices can create heat, marker-size, tactile, and format-lock-in constraints.

## Evidence
- Device precision and validation: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] describes the six views, millimeter localization, microsecond synchronization, removal of the base station, replay testing, and reported over-95% reproduction rate.
- Scale, annotation, and usability: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] gives the open and internal hours, download and purchase interest, annotation pipeline, marker-size issue, and glove-heat feedback.
- Human-to-robot bridge: [[187-duihua-liberai-liu-songming-astra-lai-xi-00-hou-wuli-ai-chuangshiren-kandao-de-shenglv-ad3b421a]] explains the missing-action problem in internet video, the natural-motion argument against teleoperation, and embodiment conditioning.
- Reported substitution efficiency: [[187-duihua-liberai-liu-songming-astra-lai-xi-00-hou-wuli-ai-chuangshiren-kandao-de-shenglv-ad3b421a]] reports the 10,000-hour versus two-million-hour comparison and the glove-plus-25%-teleoperation ablation.

## Counterevidence & Qualifications
Device designs, replay rates, download counts, annotation quality, performance comparisons, substitution ratios, and cost estimates are company-reported and not independently verified. The sources do not show common tasks, bodies, protocols, or data-accounting rules that would make their hour counts directly comparable. The Shenpu open dataset has no tactile channel, so glove pipelines are not a complete physical-data strategy. Self-built collection hardware also creates a format commitment, and natural human motion can still differ from robot kinematics, force limits, sensing, and contact dynamics.

## What Changed
- Added Liber AI's use of glove data as an action-information bridge between internet video and robot control.
- Added the reported data-ablation case for partial substitution of real-robot teleoperation.
- Clarified that glove efficiency does not remove embodiment, contact, evaluation, or final-deployment requirements.

## Related Concepts
- [[EmbodiedRobotDataParadigms]] - collection-method landscape in which UMI-style gloves are one paradigm.
- [[RealRobotDataStrategy]] - broader data-recipe problem that self-built collection feeds.
- [[RobotDataScaleUp]] - scaling question that replay validation and cleaning address.
- [[RobotTeleoperationAndRemoteTakeover]] - adjacent high-quality collection method that operates the robot directly.
- [[TactileDataStagingChoice]] - decision to leave the glove-based dataset without tactile data for now.
- [[EgocentricRobotData]] - first-person human data route that this glove-based method resembles but does not equal.
- [[WorldActionModels]] - action-conditioned model family that can consume mixed human, glove, and robot data.
- [[LiberAI]] - company reporting glove-data substitution and cross-embodiment results.
