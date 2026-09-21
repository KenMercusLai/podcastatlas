---
title: "Robot In-Context Learning / 机器人上下文学习"
type: concept
tags: [robotics, embodied-ai, in-context-learning, continual-learning]
sources:
  - wo-kandao-le-scaling-law-de-xinhao-duitan-qinghua-chayuan-zhuli-jiaoshou-xu-mengdi-jushen-zhineng-shijie-moxing-zhenzheng-de-fanhua-ltdn8trgg55fluenullokxdiz1y5
last_updated: 2026-09-21
knowledge_schema: synthesis-v1
---

# Robot In-Context Learning / 机器人上下文学习

## Definition
Robot in-context learning is the ability of a robot to infer and improve a task from interaction history—such as demonstrations, instructions, corrections, bodily motion, prior attempts, and failures—without requiring every new behavior to be written into model parameters through offline retraining.

## Current Synthesis
The bounded source treats robot generalization as prior knowledge plus rapid learning. Pretraining supplies a safe and capable starting point, but open-world deployment introduces new tasks, objects, preferences, and failure conditions that cannot all be enumerated. In-context learning therefore aims to make past interaction function as a learning signal: demonstrations can define a household preference, corrections can redirect behavior, and suboptimal trajectories can teach the model to improve its next action. The strongest form is not merely copying a prompt but learning how to learn across repeated deployments.

## Key Claims
- Pretrained capability and post-deployment adaptation are complementary requirements for genuine generalization.
- Interpolation to a familiar task with a new object position is weaker than learning a genuinely new task from context.
- Useful context can include expert and suboptimal robot trajectories, human demonstrations, body motion, language instructions, and corrections.
- Parameter-free contextual adaptation may reduce catastrophic forgetting and become more attractive as foundation-model pretraining improves.
- Learning from failed execution history requires the model to represent a learning procedure, not only an expert policy.
- Household and service preferences are a natural use case because users need to define behavior that pretraining cannot exhaustively encode.

## Evidence
- Generalization boundary: [[wo-kandao-le-scaling-law-de-xinhao-duitan-qinghua-chayuan-zhuli-jiaoshou-xu-mengdi-jushen-zhineng-shijie-moxing-zhenzheng-de-fanhua-ltdn8trgg55fluenullokxdiz1y5]] distinguishes strong priors plus fast adaptation from offline imitation within a familiar distribution.
- Method progression: [[wo-kandao-le-scaling-law-de-xinhao-duitan-qinghua-chayuan-zhuli-jiaoshou-xu-mengdi-jushen-zhineng-shijie-moxing-zhenzheng-de-fanhua-ltdn8trgg55fluenullokxdiz1y5]] connects Prompt Decision Transformer, adapter-generating Hyper Decision Transformer, and Algorithm Distillation to increasingly general contextual adaptation.
- Feedback diversity: [[wo-kandao-le-scaling-law-de-xinhao-duitan-qinghua-chayuan-zhuli-jiaoshou-xu-mengdi-jushen-zhineng-shijie-moxing-zhenzheng-de-fanhua-ltdn8trgg55fluenullokxdiz1y5]] names failed trajectories, language correction, human motion, human demonstrations, and robot demonstrations as possible learning context.
- User-preference case: [[wo-kandao-le-scaling-law-de-xinhao-duitan-qinghua-chayuan-zhuli-jiaoshou-xu-mengdi-jushen-zhineng-shijie-moxing-zhenzheng-de-fanhua-ltdn8trgg55fluenullokxdiz1y5]] uses different household clothing-storage preferences to show why user teaching remains necessary.

## Counterevidence & Qualifications
The source reports encouraging simulation results for navigation and locomotion but says complex real-robot manipulation remains difficult. Adaptation is unsafe when the base model is too weak, and contextual learning does not remove latency, memory length, embodiment, data quality, or evaluation problems. The episode does not provide comparative benchmarks showing that context-only adaptation already outperforms fine-tuning in deployed robotics.

## What Changed
- Created the concept to separate genuine new-task adaptation from offline imitation and distribution-internal interpolation.

## Related Concepts
- [[ContinualLearning]] - broader ability to keep learning without destructive forgetting.
- [[RobotDeploymentDataLoop]] - deployment mechanism that can supply repeated context and correction.
- [[EmbodiedContextMemory]] - memory horizon needed to retain causal and user-specific context.
- [[RobotExperienceData]] - the robot's own attempts and failures as learning material.
- [[RobotGeneralizationPerformanceTradeoff]] - evaluation tension between broad adaptation and reliable task execution.
- [[VisionLanguageActionModels]] - action-model family that may receive contextual demonstrations and instructions.
