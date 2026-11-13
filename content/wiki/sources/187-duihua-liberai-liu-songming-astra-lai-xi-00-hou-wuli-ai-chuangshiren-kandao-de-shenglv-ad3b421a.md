---
title: "187: 对话LiberAI刘松铭：Astra来袭，00后物理AI创始人看到的胜率"
type: source
tags: [podcast, physical-ai, robotics, world-action-models, startups]
sources: []
date: 2026-11-13
source_file: "/home/ken/repos/podcastatlas/content/episodes/ad3b421a-d013-4a69-9613-924fa6d47992 [ad3b421a-d013-4a69-9613-924fa6d47992].md"
source_url: "https://aphid.fireside.fm/d/1437767933/19a49f52-28ee-4e25-b8e9-4f0ee70917e0/ad3b421a-d013-4a69-9613-924fa6d47992.mp3"
duration: "7779"
last_updated: 2026-11-13
---

# 187: 对话LiberAI刘松铭：Astra来袭，00后物理AI创始人看到的胜率

## Summary
This [[LateTalk|晚点聊 LateTalk]] interview with [[LiuSongming|刘松明]], founder of [[LiberAI]], presents world modeling as a means toward commercially useful [[PhysicalAI|physical AI]] rather than a company mission by itself. Liber AI's response to general foundation models entering robotics is a selective full-stack strategy: let general models handle more semantic understanding and planning while the company concentrates on action generation, low-level control, embodiment, data collection, hardware fit, and delivery. The episode's most concrete technical claims concern its world action model, human-to-robot data mixture, glove-based collection, and reported zero-shot performance, but all performance and cost figures remain company-reported.

## Key Claims
- [[LiuSongming]] says [[LiberAI]] began in the second half of 2025 after earlier work on [[RDT1B]] suggested robot pretraining transfers capability across tasks, while scalable high-quality action data remained the central bottleneck.
- The company divides the robot stack into a slower System 2 for perception, understanding, and planning; a System 1 that turns intent into action; and a System 0 for reliable motion control. It expects general foundation models to cover more of System 2 than the contact-rich lower layers.
- Liber AI therefore treats models, data, collection devices, robot bodies, motion control, sensors, deployment, and scene operations as one [[PhysicalIntelligenceSystemStack|physical-intelligence system stack]], while buying mature components that do not directly determine model performance.
- The newly released model is described as a [[WorldActionModels|world action model]]. The source reports roughly 60–70% zero-shot success on grasping, about 30% on non-grasping tasks, and above 10% on some four- or five-step tasks.
- Pretraining reportedly mixes about 2.2 million hours of internet video, egocentric video, glove data, real-robot teleoperation, and cross-embodiment data across three stages that always retain both visual and action information.
- [[UMIGloveDataCollection|Free-glove data]] is presented as a bridge between abundant human video and precise robot control: the source claims 10,000 glove hours outperformed two million internet-video hours, and that glove data plus 25% of the real-robot teleoperation set beat the full teleoperation-only baseline.
- The robot body is optimized selectively around model-relevant waist, wrist, joint, and human-like motion properties; Liber AI says it does not intend to manufacture every component itself.
- Touch, cross-task reinforcement learning, hardware reliability, force and sound feedback, and the coupling between configuration, sensors, control algorithms, and motors remain unsolved or immature.
- The company is testing retail and service POCs, including beverage preparation, while aiming within two to three years for one repeatable, revenue-producing application whose value comes from model generalization rather than one-off automation.
- Liu argues that the most immediate competitors are non-standard automation and earlier delivery companies, because customer integration, hardware reliability, and scene infrastructure may be unattractive to foundation-model labs until the market becomes much larger.
- Capital discipline means comparing the learning efficiency of data and scaling routes, raising reserves before cash becomes scarce, and planning for a three-to-five-year industry cycle rather than assuming continuous market enthusiasm.

## Key Quotes
No reliable verbatim quotations are available in the supplied markdown. It is a structured episode summary rather than a transcript, so this note preserves attributed claims without inventing quotations.

## Connections
- [[LiuSongming]], [[LiberAI]], and [[RDT1B]] - founder, company, and pre-company research project at the center of the episode.
- [[WorldActionModels]], [[WorldModels]], and [[VisionLanguageActionModels]] - model routes compared through action-conditioned physical execution.
- [[PhysicalIntelligenceSystemStack]], [[LayeredRobotArchitecture]], and [[GeneralModelRobotBoundary]] - the full-stack and System 2/System 1/System 0 division used to position Liber AI against general models.
- [[UMIGloveDataCollection]], [[EmbodiedRobotDataParadigms]], [[RobotDataScaleUp]], and [[RobotTeleoperationAndRemoteTakeover]] - human, glove, and real-robot data mixture behind the reported pretraining results.
- [[TactileSensing]], [[RobotReinforcementLearning]], and [[ProductionRobotScenarioSelection]] - unresolved sensing and learning layers plus the search for a repeatable commercial scene.
- [[Kimi]] - foundation-model company with which Liber AI is discussing hardware-development and virtual-to-physical collaboration.

## Contradictions
- No settled contradiction is adopted. The source reinforces the wiki's layered-robot and full-stack-system view while supplying a company-specific implementation.
- The title spells the founder's given name “刘松铭,” while the body consistently uses “刘松明.” This wiki uses [[LiuSongming|刘松明]] and preserves the title mismatch as source-level identity uncertainty.
- Model success rates, the 2.2-million-hour mixture, glove-data substitution, teleoperation costs, body-comparison results, and superiority over general models are founder or company claims without disclosed protocols, full baselines, independent replication, or third-party evaluation.
- The claim that large foundation-model or manufacturing companies lack the incentive to perform detailed robot delivery is contingent on current market size and economics; their incentives could change if demand scales rapidly.
