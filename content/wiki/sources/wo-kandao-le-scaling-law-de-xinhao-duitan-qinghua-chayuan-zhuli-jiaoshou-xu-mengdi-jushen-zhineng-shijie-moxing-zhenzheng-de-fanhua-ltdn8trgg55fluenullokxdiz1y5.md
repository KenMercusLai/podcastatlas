---
title: "“我看到了 Scaling Law 的信号”｜对谈清华叉院助理教授徐梦迪：具身智能、世界模型、真正的泛化"
type: source
tags: [podcast, shizilukou-crossing, robotics, embodied-ai, world-models, continual-learning]
date: 2026-09-20
source_file: "/home/ken/repos/podcastatlas/content/episodes/“我看到了 Scaling Law 的信号” ｜ 对谈清华叉院助理教授徐梦迪：具身智能、世界模型、真正的泛化 [ltDn8TRgg55FlUENUlLokxDiz1Y5].md"
source_url: "https://www.xiaoyuzhoufm.com/episode/6ab0504f0916f6f8b4466ece"
last_updated: 2026-09-21
---

# “我看到了 Scaling Law 的信号”｜对谈清华叉院助理教授徐梦迪：具身智能、世界模型、真正的泛化

## Summary
This [[ShizilukouCrossing|十字路口Crossing]] episode interviews [[XuMengdi|徐梦迪]], an assistant professor at [[TsinghuaIIIS|清华大学交叉信息研究院]], about robot learning beyond a fixed pretraining distribution. Its central claim is that genuine generalization combines strong priors with [[RobotInContextLearning|fast in-context adaptation]] from demonstrations, corrections, bodily motion, and failures; [[WorldModels]] and [[VisionLanguageActionModels|VLA systems]] can be complementary, while data sources should be assigned by the capability and training stage they best support. The episode also strengthens the wiki's caution around embodied scaling and evaluation: lower held-out loss is an early signal, not a scaling law for useful robotics unless unseen-task success rises reliably under safety and real-time constraints.

## Key Claims
- Genuine robot generalization requires both broad pretrained knowledge and the ability to learn quickly after deployment; interpolation within familiar object positions is not equivalent to learning a new task.
- [[RobotInContextLearning]] aims to adapt behavior from demonstrations, language corrections, body motion, and suboptimal or failed trajectories without relying entirely on parameter updates.
- Prompt Decision Transformer, Hyper Decision Transformer, and Algorithm Distillation represent successive attempts to make model parameters encode a learning procedure rather than only memorized task behavior.
- [[WorldModels]] target task-independent regularities of how the world changes, while [[VisionLanguageActionModels|VLA models]] map perception and instructions toward action; the episode treats understanding/prediction and execution as potentially complementary.
- [[CapabilityDrivenRobotDataDesign]] assigns real-robot teleoperation, simulation, UMI-style collection, and human data different roles based on the desired capability and training stage rather than declaring one universal best source.
- [[RobotDeploymentDataLoop]] depends on a sufficiently capable base model: users will keep teaching and correcting a robot only when limited interaction produces visible improvement.
- Held-out loss reportedly improves as pretraining data grows from roughly one hundred thousand to one million hours, but [[RobotScalingClaimCaution|loss improvement is not task-success scaling]], especially in long-horizon contact-rich tasks.
- [[RobotEvaluationProblem|Embodied evaluation]] should measure unseen-task success, failure modes, safety boundaries, and latency because a robot's body turns errors into physical consequences and makes slow inference operationally limiting.
- Long-term research identity can emerge from sustained work on a consequential problem; independent researchers must define worthwhile questions as well as solve them.

## Key Quotes
> “真正的泛化” — the episode's label for combining prior knowledge with rapid learning in new environments.

> “损失和成功率并不直接挂钩” — the core qualification on interpreting an embodied-AI scaling signal.

> “学习如何学习” — the capability the episode connects to repeated adaptation across homes and service settings.

## Connections
- [[ShizilukouCrossing]] - show context for the interview.
- [[XuMengdi]] and [[TsinghuaIIIS]] - guest and current institutional setting.
- [[RobotInContextLearning]], [[RobotDeploymentDataLoop]], and [[CapabilityDrivenRobotDataDesign]] - main learning, deployment, and data-design concepts added by the source.
- [[RobotScalingClaimCaution]] and [[RobotEvaluationProblem]] - existing syntheses materially qualified by the loss/success gap and embodied safety requirements.
- [[WorldModels]], [[VisionLanguageActionModels]], and [[ContinualLearning]] - adjacent technical frames for world understanding, action, and post-deployment learning.
- [[RealRobotDataStrategy]], [[EmbodiedRobotDataTradeoff]], and [[UMIGloveDataCollection]] - existing data-route context for real machines, simulation, UMI, and human data.
- [[ProblemDefinitionInResearch]] and [[FeiFeiLi]] - research-method context behind the episode's distinction between solving and defining important problems.

## Contradictions
- The episode does not overturn the existing [[RobotScalingClaimCaution]]; it adds a somewhat stronger observed signal while preserving the same evidentiary boundary. Held-out-loss improvement across source-reported data scales does not establish a power law for unseen-task success.
- The preference for world models over task-enumerating VLA training is a research judgment, not comparative proof that one route dominates. The source itself leaves room for world-model/VLA complementarity.
- Claims about data-hour scale, current industry results, benchmark adequacy, future inflection timing, and the guest's team experiments remain source-scoped because the episode supplies no audited curves, protocols, or cross-model comparisons.
