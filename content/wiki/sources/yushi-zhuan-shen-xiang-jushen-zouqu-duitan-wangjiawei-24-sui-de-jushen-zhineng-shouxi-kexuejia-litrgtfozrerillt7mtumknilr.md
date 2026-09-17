---
title: "于是转身向具身走去｜对话王家伟：24 岁的具身智能首席科学家"
type: source
tags: [podcast, shizilukou-crossing, robotics, embodied-ai, physical-ai, startups]
date: 2026-09-16
source_file: "/home/ken/repos/podcastatlas/content/episodes/于是转身向具身走去｜对话王家伟：24 岁的具身智能首席科学家 [litRgTDfOZReriLLT7MtUMkNI-Lr].md"
source_url: "https://www.xiaoyuzhoufm.com/episode/6aaa9f039d326477816a3488"
last_updated: 2026-09-17
---

# 于是转身向具身走去｜对话王家伟：24 岁的具身智能首席科学家

## Summary
This [[ShizilukouCrossing]] episode interviews [[WangJiawei|王家伟]], the 24-year-old chief scientist of [[ShenpuIntelligence|深普智能]], following his path from a USTC youth-class program and a joint PhD with [[MicrosoftResearchAsia]] through internships at [[DeepSeek]] and ByteDance Seed into embodied-intelligence entrepreneurship. The technical center is that embodied intelligence cannot be one general model: an upper "brain" for reasoning, planning, and world understanding has to be paired with a lower, real-time, controllable [[SmallBrainActionLayer|Action Policy]] or "small brain." The company's route combines self-built [[UMIGloveDataCollection|UMI-style data collection]], pretraining, a [[RobotAgenticOS|robot Agentic OS]] built around System 1 and System 2, and its own evaluation instead of a single VLA, world-model, or imitation-learning recipe.

## Key Claims
- A general model such as [[ChatGPT6Astra]] can surprise on robot manipulation, but the source uses its sped-up video, slow single-pass inference, and static-scene success to draw the [[GeneralModelRobotBoundary|general-model boundary]] at real-time recovery from physical disturbance rather than at grasping or task planning.
- [[ShenpuIntelligence|深普智能]] defines embodied intelligence through an [[EmbodiedCapabilityFramework|explicit capability framework]]: adaptability (zero-shot and few-shot through fully out-of-distribution scenes), steerability (control by language, image, and video), and context understanding.
- The company positions itself as a full-stack terminal company rather than a data company or a model company, on the argument that value comes from putting data, models, deployment, and the body into one product, and that full-stack work can itself become the moat.
- [[UMIGloveDataCollection|Self-built UMI-style collection hardware]] is treated as a differentiator: a six-view glove with millimeter localization and microsecond synchronization replaces base stations and reduces occlusion, and a trajectory-replay test that found over 95% of collected trajectories reproducible on the body justified scaling collection.
- [[EmbodiedContextMemory|Context and memory]] are treated as first-class capabilities across short, medium, and long horizons, where the short horizon can be a sub-second causal chain and longer horizons hold object, place, and human-partner knowledge; growing token counts then collide with real-time latency.
- Touch is deliberately staged rather than scaled: the open data carries no tactile signal, vision is judged sufficient for two-finger grip checks, and because tactile sensors differ in resolution and placement, committing to a hundred devices now risks a stranded data format.
- [[RobotEvaluationProblem|Robotics evaluation]] is called out as unreliable because benchmarks skew to simulation, can be gamed by post-training, and are hard to reproduce on real machines; the company says it will publish its own simple/medium/hard evaluation and disclose how much data a zero-shot or few-shot result used.
- The source reports a scaling signal while refusing a scaling-law claim: data diversity, compute, and volume show power-law-like improvement, but serious verification is missing, and the company's own cost-controlled UMI data with 90%-plus usability is what makes [[RobotScalingClaimCaution|controlled parameter and data-ratio experiments]] possible.

## Key Quotes
> "Keep the world simple" — the slogan the episode associates with [[ShenpuIntelligence|深普智能]].

> "上层需要具备推理、规划和世界理解能力的大脑，下层还需要可实时反应、稳定可控的 Action Policy，也就是类似'小脑'的能力。" — the source's central brain/small-brain architecture framing.

> "夹松了、杯子下滑、再夹紧" — the source's example of causal context unfolding inside about one second.

## Connections
- [[ShizilukouCrossing]] — show context for the interview.
- [[WangJiawei]] and [[ShenpuIntelligence]] — guest and company at the center of the episode.
- [[SmallBrainActionLayer]], [[EmbodiedCapabilityFramework]], [[EmbodiedContextMemory]], [[RobotAgenticOS]], [[UMIGloveDataCollection]], [[RobotScalingClaimCaution]], and [[TactileDataStagingChoice]] — concept pages added by this source.
- [[ChatGPT6Astra]] and [[GeneralModelRobotBoundary]] — the Astra robotics evidence and the boundary it draws around real-time physical control.
- [[RobotEvaluationProblem]], [[EgocentricRobotData]], and [[RobotDataScaleUp]] — evaluation, data-cost, and scaling branches the episode extends.
- [[DeepSeek]], [[MicrosoftResearchAsia]], and [[ByteDance]] — training and internship context behind the guest's route into embodied AI.
- [[LayeredRobotArchitecture]], [[VisionLanguageActionModels]], [[HomeServiceRobots]], and [[HumanoidRobotCommercialization]] — adjacent architecture, model, and commercialization frames.

## Contradictions
- No settled contradiction is recorded. The source is a chief-scientist interview that does not disclose model architecture, training cost, concrete evaluation results, or commercialization details, so its internal-capability claims remain source-scoped.
- Productive tension worth tracking: this source treats tactile data as a staged option, while [[TactileSensing]] and [[YimuTechnology]] argue that touch is core infrastructure for dexterous manipulation. The source also qualifies simulation-first and general-model-subsumption positions recorded elsewhere in the wiki without directly refuting them.
