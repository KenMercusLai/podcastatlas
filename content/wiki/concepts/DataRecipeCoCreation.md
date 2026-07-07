---
title: "Data Recipe Co-Creation"
type: concept
tags: [ai, data, model-training]
sources: [134-shuju-de-zongshu-he-xiechen-liao-xinshidai-de-shiyou-lishi-bantu-shuju-jinzita-dingjia-yu-recipe]
last_updated: 2026-07-08
---

# Data Recipe Co-Creation

Data recipe co-creation is the process of data companies and model teams jointly discovering which data improves model behavior. In [[134-shuju-de-zongshu-he-xiechen-liao-xinshidai-de-shiyou-lishi-bantu-shuju-jinzita-dingjia-yu-recipe]], [[XieChen]] compares the current robotics and post-training stage to earlier frontier-model periods where data vendors and model labs had to iterate together.

## Key Claims
- A data company cannot prove value by delivering files alone if the model team cannot show that the data improves training or evaluation.
- Model teams and data teams can blame each other when a run fails, so recipe discovery requires shared metrics, experiments, and trust.
- For [[EmbodiedAI]], the recipe may mix real robot trajectories, simulation, human first-person data, internet data, expert feedback, and challenge evaluations.
- Finding the right proportions may require large compute budgets, so data strategy is coupled to [[FrontierModelScaling]] rather than separate from it.
- The process makes [[DataPricingInAI]] less commodity-like: higher-value data is judged by learning impact, not only collection cost.

## Connections
- [[EmbodiedDataPyramid]] — data layers whose proportions need to be discovered.
- [[DataEngineLearningLoop]] — operating system for repeated recipe testing.
- [[GuanglunIntelligence]] and [[ScaleAI]] — source company and historical comparator.
- [[OpenAI]], [[GoogleDeepMind]], [[Nvidia]], [[ByteDance]], [[Alibaba]], and [[Qwen]] — model and platform companies the source expects to participate in physical-AI data demand.
