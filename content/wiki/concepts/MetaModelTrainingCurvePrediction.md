---
title: "Meta-Model Training Curve Prediction"
type: concept
tags: [ai, model-training, model-design, ai-research]
sources: [149-qinli-zhongmei-new-labs-ziben-kuangchao-he-qinghua-liuziming-liao-ai-for-ai-jizhi-kejieshixing-he-max-tegmark-lm33q4n6w8tzcd2fxdbuk9unc2xv]
last_updated: 2026-08-08
---

# Meta-Model Training Curve Prediction

Meta-model training curve prediction is [[LiuZiming|Liu Ziming]]'s proposed "next curve" task in [[149-qinli-zhongmei-new-labs-ziben-kuangchao-he-qinghua-liuziming-liao-ai-for-ai-jizhi-kejieshixing-he-max-tegmark-lm33q4n6w8tzcd2fxdbuk9unc2xv]]. The input is a candidate model plus conditions such as dataset and optimizer; the output is a predicted training curve. Liu contrasts this with next-token prediction in language models and next-state prediction in [[WorldModels]].

The source says the idea came partly from Liu training himself: he repeatedly predicted training curves before running experiments and improved over dozens of days. The model version would scale that judgment by training on many diverse small models and their curves, then using the learned predictor to rank architecture ideas before spending real compute.

## Key Claims
- The task is to predict how a model will train, not to generate code or text directly.
- If accurate enough, the meta-model can cheaply triage many architecture hypotheses.
- The data requirement is many model/curve pairs, which may favor diverse smaller experiments over a single giant cluster run.
- Curve prediction is part of "smarter" [[AIForAI]] because it selects fewer better experiments rather than only running many trials.
- The concept depends on [[PhysicsOfAI]] because predictions need stable structure across architectures, data, and optimization conditions.

## Connections
- [[LiuZiming|Liu Ziming]] — source proposer.
- [[AIForAI]], [[AutoResearch]], and [[OPHISResearchWorkflow]] — research-automation context.
- [[PhysicsOfAI]], [[ResearchTaste]], and [[TrainingComputeAllocation]] — theory, judgment, and compute-triage context.
- [[TrainingAutopilot]] and [[VibeTraining]] — product horizons that could use meta-model predictions.
- [[WorldModels]] — contrast with next-state prediction.
