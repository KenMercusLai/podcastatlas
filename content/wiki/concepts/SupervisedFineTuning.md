---
title: "Supervised Fine-Tuning / SFT"
type: concept
knowledge_schema: synthesis-v1
tags: [ai, model-training, post-training]
sources:
  - yi-ge-ren-liang-zhou-shu-bai-meiyuan-ruhe-xun-chu-dengding-hugging-face-de-moxing-duitan-yanjiuyuan-lu-yuxin-lpxxrnwdhgnsrxuyhrfrv5t1lojt
last_updated: 2026-08-30
---

# Supervised Fine-Tuning / SFT

## Definition
Supervised fine-tuning is a post-training method that trains a model on curated input-output examples or trajectories so its behavior moves toward a target task, style, or workflow.

## Current Synthesis
In this episode, SFT is the practical default for individual builders and application companies that want a small model to improve in a specific domain. It can function as a form of [[ModelDistillation]] when examples are produced or shaped by a stronger teacher model, but its success depends on target alignment, data quality, and evaluation rather than on the training label alone.

## Key Claims
- SFT is often more realistic than [[AgentRL|RL]] for low-budget, target-specific model improvement.
- SFT can transfer part of a stronger teacher model's behavior into a smaller student model when the examples match the desired target.
- SFT does not guarantee general capability improvement; it can improve one benchmark while degrading another.
- The method's practical difficulty is data construction and review, not only running the training job.
- SFT remains bounded by the base model's capacity and by whether the selected examples actually shift the learned behavior.

## Evidence
### Method choice
- [[yi-ge-ren-liang-zhou-shu-bai-meiyuan-ruhe-xun-chu-dengding-hugging-face-de-moxing-duitan-yanjiuyuan-lu-yuxin-lpxxrnwdhgnsrxuyhrfrv5t1lojt]] says the guest chose SFT because it was more practical for an individual project than RL or more complex post-training methods.

### Distillation role
- [[yi-ge-ren-liang-zhou-shu-bai-meiyuan-ruhe-xun-chu-dengding-hugging-face-de-moxing-duitan-yanjiuyuan-lu-yuxin-lpxxrnwdhgnsrxuyhrfrv5t1lojt]] accepts the host's summary that stronger teacher-model data can be used through SFT to distill a small model for a narrow domain.

### Evaluation loop
- [[yi-ge-ren-liang-zhou-shu-bai-meiyuan-ruhe-xun-chu-dengding-hugging-face-de-moxing-duitan-yanjiuyuan-lu-yuxin-lpxxrnwdhgnsrxuyhrfrv5t1lojt]] links SFT to benchmark iteration: train, evaluate, inspect failures, change data, and repeat.

## Counterevidence & Qualifications
- The source does not provide a full SFT tutorial, hyperparameter recipe, or reproducible training run.
- SFT can overfit a benchmark or pull behavior away from other capabilities if the target and evaluation are too narrow.
- Stronger post-training methods may be necessary when rewards, tool feedback, or long-horizon behavior cannot be captured well by supervised examples.

## What Changed
- Created a canonical SFT concept so post-training pages can link to the method without treating it as a one-off abbreviation.

## Related Concepts
- [[LowCostModelPostTraining]] - application context where SFT is the default low-budget method.
- [[ModelDistillation]] - teacher-student transfer pattern that can use SFT data.
- [[DataFirstPostTraining]] - data discipline that determines SFT usefulness.
- [[ModelPostTrainingBottleneck]] - broader problem SFT only partially solves.
- [[AgentPostTraining]] - harder setting where SFT may need real trajectories and tool feedback.
- [[AIVerification]] - evaluation requirement after fine-tuning.
