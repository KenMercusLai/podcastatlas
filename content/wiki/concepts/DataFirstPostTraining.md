---
title: "Data-First Post-Training / 数据优先后训"
type: concept
knowledge_schema: synthesis-v1
tags: [ai, model-training, data, post-training]
sources:
  - yi-ge-ren-liang-zhou-shu-bai-meiyuan-ruhe-xun-chu-dengding-hugging-face-de-moxing-duitan-yanjiuyuan-lu-yuxin-lpxxrnwdhgnsrxuyhrfrv5t1lojt
last_updated: 2026-08-30
---

# Data-First Post-Training / 数据优先后训

## Definition
Data-first post-training is the view that post-training progress depends primarily on target diagnosis, data selection, data cleaning, manual audit, and evaluation feedback rather than on the mechanical act of launching a training job.

## Current Synthesis
The episode makes this concept concrete through a small-model project where training took hours, while useful data construction took days or weeks. Real user trajectories and open community traces carry the strongest signal when they match the target behavior. Synthetic data remains useful, but mainly as a repair tool for diagnosed failure modes rather than as a generic substitute for real interaction data.

## Key Claims
- Data insight is the central bottleneck once scripts, base models, and public benchmarks are available.
- Real task traces are usually more valuable than generic synthetic examples because they contain actual user intent and model failure patterns.
- Synthetic data is most useful when it targets a specific diagnosed weakness, such as premature task-completion claims.
- Manual audit remains necessary because examples that look good may fail to improve the student model.
- Benchmark failures should feed back into data changes rather than only into hyperparameter changes.
- Data-first post-training requires accepting capacity limits: a smaller student model may not learn everything a stronger teacher demonstrates.

## Evidence
### Time allocation
- [[yi-ge-ren-liang-zhou-shu-bai-meiyuan-ruhe-xun-chu-dengding-hugging-face-de-moxing-duitan-yanjiuyuan-lu-yuxin-lpxxrnwdhgnsrxuyhrfrv5t1lojt]] says the first version spent roughly three days on data and one day on training, while the second spent about twelve days of a two-week cycle on data and only hours on each training run.

### Real versus synthetic data
- [[yi-ge-ren-liang-zhou-shu-bai-meiyuan-ruhe-xun-chu-dengding-hugging-face-de-moxing-duitan-yanjiuyuan-lu-yuxin-lpxxrnwdhgnsrxuyhrfrv5t1lojt]] estimates real data at roughly 60-70% of the final mix and treats synthetic data as targeted补强 for observed model errors.

### Audit and iteration
- [[yi-ge-ren-liang-zhou-shu-bai-meiyuan-ruhe-xun-chu-dengding-hugging-face-de-moxing-duitan-yanjiuyuan-lu-yuxin-lpxxrnwdhgnsrxuyhrfrv5t1lojt]] reports manually checking about 500 examples out of a 5,000-example set and repeatedly using benchmark errors to refine the training distribution.

## Counterevidence & Qualifications
- The source is a post-training practitioner account rather than an independent ablation study.
- Data-first does not mean data-only; base-model choice, training method, evaluation design, and serving constraints still shape outcomes.
- Real user traces raise privacy, consent, and provenance issues that the episode does not fully operationalize.

## What Changed
- Created a dedicated concept for the source's claim that data work, not training runtime, is the practical center of small-model post-training.
- Added a sharper distinction between real traces and synthetic repair examples.

## Related Concepts
- [[ModelPostTrainingBottleneck]] - general bottleneck that data-first work addresses.
- [[LowCostModelPostTraining]] - practical route where data-first work dominates the cost.
- [[ModelDistillation]] - teacher-student transfer method whose quality depends on target-aligned data.
- [[SyntheticAgentData]] - adjacent data type that can support post-training when environments and scoring are controlled.
- [[AgentPostTraining]] - agent-workflow version where traces and failure recovery become training material.
- [[AIVerification]] - validation layer needed to judge whether the data actually improves behavior.
