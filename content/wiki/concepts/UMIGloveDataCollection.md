---
title: "UMI-Style Glove Data Collection / 手套式数据采集"
type: concept
tags: [robotics, data, embodied-ai, hardware]
sources:
  - yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

# UMI-Style Glove Data Collection / 手套式数据采集

## Definition
UMI-style glove data collection is a body-free manipulation-data method in which a person wears a sensor-rich handheld device or glove so that hand motion, camera views, and timing can be recorded as robot-trainable trajectories without operating a robot during collection.

## Current Synthesis
The source describes a self-built high-precision glove as [[ShenpuIntelligence|深普智能]]'s data differentiator. The device carries a head-mounted stereo camera plus an upper and a lower camera on each wrist, for six views; camera-based tracking localizes at millimeter scale and synchronizes at microsecond scale, which lets the team drop the base station and reduce occlusion. Before scaling, the company ran small experiments, real-machine evaluation, and trajectory replay, and found that more than 95% of collected trajectories could be reproduced on the body. It then open-sourced about 2,000 hours, reported internal data in the tens of thousands of hours, and cited more than 500,000 cumulative downloads across Hugging Face and ModelScope. The source also reports inbound data-purchase interest, usability feedback that the marker is too large and the glove heats up on real machines, and an annotation pipeline that first used [[ChatGPT6Astra]] and is moving toward a small in-house annotation model.

## Key Claims
- The collection device is a six-view glove with camera-based millimeter localization, microsecond synchronization, and no external base station.
- Trajectory replay on the real body is used as the test of whether collected data is worth scaling.
- Open-sourcing data is treated as both community service and a commercial lead channel.
- Annotation and cleaning are a separate bottleneck; the source reports that a general model annotated better than humans and could work continuously, but with low efficiency.
- Real-user feedback about marker size and glove heat is part of the data-quality loop rather than a finished-product claim.
- Body-free collection still has to be validated against real-machine reproduction before it counts as useful robot data.

## Evidence
- Device evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] describes the head stereo camera, the upper and lower wrist cameras, the six camera views, millimeter-scale localization, microsecond synchronization, the removal of the base station, and the occlusion goal.
- Validation evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] reports small-scale experiments, real-machine evaluation, trajectory replay, and the over-95% reproduction result that justified scaling collection.
- Scale evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] gives the 2,000 open-sourced hours, the tens-of-thousands-of-hours internal scale, the 500,000-plus cumulative downloads, and the inbound purchase inquiries.
- Feedback and annotation evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] records the marker-size and glove-heat feedback and the use of [[ChatGPT6Astra]] for annotation with a move toward an in-house annotation model.

## Counterevidence & Qualifications
The device design, replay rate, download count, and annotation quality are company-reported and not independently verified. The open dataset has no tactile channel, so this page describes a vision-based manipulation pipeline rather than a complete physical-data strategy. Collection hardware that a company builds itself is also a format commitment, which is exactly the kind of lock-in the source says it wants to avoid elsewhere.

## What Changed
- Created the concept from the source's six-camera UMI-style glove, its replay validation, and its open-source and annotation details.
- Separated body-free collection hardware from the broader real-robot data strategy.

## Related Concepts
- [[EmbodiedRobotDataParadigms]] - collection-method landscape in which UMI-style gloves are one paradigm.
- [[RealRobotDataStrategy]] - broader data-recipe problem that self-built collection feeds.
- [[RobotDataScaleUp]] - scaling question that replay validation and cleaning address.
- [[RobotTeleoperationAndRemoteTakeover]] - adjacent high-quality collection method that operates the robot directly.
- [[TactileDataStagingChoice]] - decision to leave the glove-based dataset without tactile data for now.
- [[EgocentricRobotData]] - first-person human data route that this glove-based method resembles but does not equal.
