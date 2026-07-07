---
title: "134. 【数据的综述】和谢晨聊，新时代的石油、历史、版图、数据金字塔、定价与Recipe"
type: source
tags: [podcast, ai, data, robotics, embodied-ai, simulation]
sources: []
date: 2026-03-30
source_file: "/home/ken/repos/podcastatlas/content/episodes/134. 【数据的综述】和谢晨聊，新时代的石油、历史、版图、数据金字塔、定价与Recipe [lkInPy65_ZR4cQmK23rmHJ_hhLVQ].md"
source_url: "https://www.xiaoyuzhoufm.com/episode/69c953b4b977fb2c478df5c3"
last_updated: 2026-07-08
---

## Summary
This [[ZhangXiaojunCommercialInterviews]] episode interviews [[XieChen]], founder and CEO of [[GuanglunIntelligence]], about data as the third pillar of AI beside compute and algorithms. The discussion reframes data from labeled files into [[DataAsEducation]]: task design, expert feedback, failure correction, evaluation, and environments that let models learn. For [[EmbodiedAI]], Xie argues that real robot data is necessary but too costly to scale alone, so useful progress depends on an [[EmbodiedDataPyramid]] centered on [[RoboticsSimulationEvaluation]], [[DataEngineLearningLoop]], and [[DataRecipeCoCreation]].

## Key Claims
- [[XieChen]]'s path from physics and quantitative finance into dynamic pricing, [[Cruise]], [[Nvidia]], and autonomous-driving simulation shapes his view that simulation can be a real training and evaluation tool rather than only a demo environment.
- Data is increasingly like education: early datasets such as [[ImageNet]] looked like static textbooks, [[ScaleAI]] industrialized annotation as a factory, and frontier post-training/evaluation now depends on experts who can set tasks, grade answers, and supply feedback.
- In the current large-model stage, pretraining text is less the only bottleneck; post-training, evaluation, and difficult feedback data become more important for large language models and digital agents.
- For [[EmbodiedAI]], real teleoperation or robot-body data is accurate but expensive and hard to scale, so it should be the smallest and most valuable layer rather than the whole strategy.
- The episode's [[EmbodiedDataPyramid]] puts real robot data at the top, simulation data in the middle, and internet plus human first-person data at the bottom; Xie argues the layers should form a loop rather than remain isolated.
- [[RoboticsSimulationEvaluation]] is framed as a prerequisite for general-purpose robots because real homes, factories, and tasks cannot be repeated at enough scale for systematic training and measurement.
- Good robotics data can include failure, correction, and diverse solution paths; "perfect" trajectories are not always the highest-value examples once models can learn from recovery.
- [[WorldModels]] and [[VisionLanguageActionModels]] are treated as complementary: world models can supply physical prediction and cloud-brain context, while VLA models translate perception and instructions into action.
- Xie contrasts robot data with [[Tesla]]'s Data Engine: robots do not yet have millions of deployed units producing cheap real-world feedback, so a simulation-centered loop has to substitute for the missing fleet-scale shadow mode.
- Data companies may move from Data Factory to [[DataEngineLearningLoop]], selling environments, evaluation, feedback, and recipe discovery rather than standardized labeled files.
- [[DataRecipeCoCreation]] matters because data companies and model teams have to discover which data actually improves training; recipe quality cannot be separated from model architecture, compute, and evaluation.
- [[DataPricingInAI]] rises with customization and feedback value: pretraining-like data is more standardized, while post-training, evaluation, expert feedback, and embodied trajectories can command much higher prices.
- The embodied-AI industry is likely to split into model-brain companies, robot-body companies, data/simulation companies, and scenario owners rather than being monopolized by a single full-stack player.

## Key Quotes
> "数据约等于教育" — Xie's core metaphor for moving beyond static labeled files.

> "没有仿真这件事做不成" — Xie on why simulation is necessary for robotics.

> "Data Engine" — Xie's preferred frame for [[GuanglunIntelligence]], contrasted with a Data Factory.

## Connections
- [[XieChen]], [[GuanglunIntelligence]], [[Cruise]], [[Nvidia]], and [[ScaleAI]] — person, company, autonomous-driving/simulation context, infrastructure context, and data-industry comparator.
- [[ImageNet]], [[DataAsEducation]], [[DataEngineLearningLoop]], [[DataRecipeCoCreation]], and [[DataPricingInAI]] — source's data-industry history and business-model frame.
- [[EmbodiedAI]], [[EmbodiedDataPyramid]], [[RoboticsSimulationEvaluation]], [[RealRobotDataStrategy]], and [[PhysicalWorldDataFlywheel]] — robotics data strategy and its tension with real-world fleet data.
- [[WorldModels]], [[VisionLanguageActionModels]], [[WorldActionModels]], and [[VideoModels]] — technical model routes around physical prediction, action, and simulation.
- [[OpenAI]], [[GoogleDeepMind]], [[Nvidia]], [[ByteDance]], [[Alibaba]], and [[Qwen]] — model-company and platform-company players Xie expects to matter in physical AI.
- [[UnitreeRobotics]] and [[ZhiyuanRobotics]] — robot-body commercialization examples used to separate body companies from brain/data companies.
- [[Xinghaitu]] and [[AetherAI]] — prior wiki robotics sources that make the same field's route-level disagreements visible.

## Contradictions
- No direct contradiction with prior wiki content.
- The source creates a productive tension with [[RealRobotDataStrategy]] and [[PhysicalWorldDataFlywheel]] from the [[Xinghaitu]] source. [[GaoJiyang]] emphasizes the robot body as the real data carrier, while [[XieChen]] argues that real robot data is overestimated if it is treated as scalable by itself; the difference is a weighting dispute inside a shared embodied-AI data problem.
- The source also qualifies [[WorldModels]] and [[VideoModels]] optimism: Xie sees world models as possibly becoming a class of simulation, but says ordinary video generation is not yet simulation unless it supports reproducible action, physical accuracy, and counterfactual control.
