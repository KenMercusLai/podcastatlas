---
title: "Capability-Driven Robot Data Design / 能力反推机器人数据"
type: concept
tags: [robotics, data, embodied-ai, training]
sources:
  - wo-kandao-le-scaling-law-de-xinhao-duitan-qinghua-chayuan-zhuli-jiaoshou-xu-mengdi-jushen-zhineng-shijie-moxing-zhenzheng-de-fanhua-ltdn8trgg55fluenullokxdiz1y5
last_updated: 2026-09-21
knowledge_schema: synthesis-v1
---

# Capability-Driven Robot Data Design / 能力反推机器人数据

## Definition
Capability-driven robot data design selects data modalities, trajectories, and collection methods by reasoning backward from the behavior a model must learn rather than treating raw hours or one collection device as the objective.

## Current Synthesis
The bounded source turns robot-data strategy into a capability-and-stage allocation problem. Smooth action needs smooth trajectories; recovery needs failures plus corrections; perception tasks such as segmentation, tracking, and depth reconstruction need different signals from new-task adaptation. Human video offers broad and inexpensive scene coverage, UMI-style data narrows the gap toward manipulation, simulation cheaply varies appearance and geometry, and real-robot teleoperation most closely matches the target body. The practical question is which mixture makes a specified capability learnable at pretraining, mid-training, or post-training time.

## Key Claims
- The desired capability should determine data content, modality, and collection method.
- Failure recovery cannot be learned from success-only trajectories; failures and corrections must be represented.
- Human, UMI-style, simulation, and real-robot data occupy different points in cost, coverage, embodiment match, and controllability.
- Simulation is especially useful when controllable variation in position, texture, and color matters.
- Real-robot teleoperation is closest to deployment and therefore especially useful for fine-tuning or post-training.
- Morphology transfer is a necessary bridge when inexpensive human data is used to train robot action.

## Evidence
- Capability-first evidence: [[wo-kandao-le-scaling-law-de-xinhao-duitan-qinghua-chayuan-zhuli-jiaoshou-xu-mengdi-jushen-zhineng-shijie-moxing-zhenzheng-de-fanhua-ltdn8trgg55fluenullokxdiz1y5]] says smoothness, recovery, segmentation, tracking, reconstruction, and in-context learning imply different data requirements.
- Stage-allocation evidence: [[wo-kandao-le-scaling-law-de-xinhao-duitan-qinghua-chayuan-zhuli-jiaoshou-xu-mengdi-jushen-zhineng-shijie-moxing-zhenzheng-de-fanhua-ltdn8trgg55fluenullokxdiz1y5]] assigns simulation to pretraining or mid-training and real-robot teleoperation to fine-tuning or post-training.
- Coverage evidence: [[wo-kandao-le-scaling-law-de-xinhao-duitan-qinghua-chayuan-zhuli-jiaoshou-xu-mengdi-jushen-zhineng-shijie-moxing-zhenzheng-de-fanhua-ltdn8trgg55fluenullokxdiz1y5]] describes human data as cheap and broad, with UMI positioned between human and robot data.

## Counterevidence & Qualifications
The source offers a design framework rather than measured allocation ratios. Morphology transfer remains an open technical problem, and broad human data may not contain the sensor, contact, latency, or action distributions of a target robot. The best mixture can change with body, task, model architecture, and deployment environment.

## What Changed
- Created the concept to make desired model capability, rather than raw data volume, the organizing unit of robot-data strategy.

## Related Concepts
- [[EmbodiedRobotDataTradeoff]] - broader tradeoff among simulation, real machines, human data, and task-specific data.
- [[RealRobotDataStrategy]] - target-body grounding and physical feedback branch.
- [[UMIGloveDataCollection]] - intermediate manipulation-data collection route.
- [[RobotExperienceData]] - robot-owned attempts and corrections needed for improvement and recovery.
- [[Sim2Real]] - transfer boundary between controlled synthetic variation and physical execution.
- [[RobotDataScaleUp]] - scale challenge qualified by capability relevance and data mixture.
