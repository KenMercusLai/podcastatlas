---
title: "Model Collapse"
type: concept
tags: [ai, training-data, model-quality]
sources:
  - tech-20260824-mp-tech-pod-128-tech-20260824-mp-tech-pod-128
  - tech-20251219-1219-mp-tech-pod-128-tech-20251219-1219-mp-tech-pod-128
  - kate-crawford-mapping-empires
  - 174-women-hai-neng-gei-suanfa-dang-duojiu-de-pinwei-laoshi-duitan-yamaxun-agi-cha-sheng-lrs0qgmr9gy1nbdtrsvn2lx5dxza
  - tech-20261111-1111-mp-tech-pod-128-tech-20261111-1111-mp-tech-pod-128
last_updated: 2026-11-11
knowledge_schema: synthesis-v1
---

# Model Collapse

## Definition
Model collapse is the loss of quality, diversity, rare patterns, or distributional fidelity that can occur when models repeatedly learn from generated outputs instead of sufficiently grounded and varied evidence.

## Current Synthesis
The concept spans several scales. [[KateCrawford]] supplies the broad warning that recursive synthetic training can erase outliers and narrow distributions; public [[AISlop]] can contaminate future crawls; and [[NegativeParallelism]] shows how one stylistic tic can reinforce itself before broad degradation is visible. [[ChaSheng]] supplies the necessary qualification: synthetic data is not automatically harmful when it carries information and is filtered and evaluated. The new [[Reddit]] source adds an ecosystem dependency—fresh human discussion is not only a training input but a renewable resource whose production can weaken when AI summaries and access walls reduce contributor incentives.

## Key Claims
- Repeated training on generated outputs can narrow distributions and weaken rare, minority, or unusual patterns.
- Public synthetic content can enter later training corpora, turning platform quality into model-data quality.
- Recursive effects can begin as amplified style patterns without yet constituting broad model failure.
- Synthetic data can still help when it is informative, grounded, filtered, evaluated, and mixed for diversity.
- Fresh human and physical-world evidence remains important for maintaining novelty, coverage, and contact with changing reality.
- Access, traffic, and contributor incentives therefore affect the long-run supply of useful human-generated training material.

## Evidence
- Distributional collapse - [[kate-crawford-mapping-empires]] describes recursive synthetic training as flattening diversity, erasing outliers, and degrading model quality.
- Public-corpus contamination - [[tech-20251219-1219-mp-tech-pod-128-tech-20251219-1219-mp-tech-pod-128]] connects media-scale AISlop with future training feedback loops.
- Style reinforcement - [[tech-20260824-mp-tech-pod-128-tech-20260824-mp-tech-pod-128]] says repeated AI use of negative parallelism can seed later synthetic data and amplify the same construction.
- Conditional value of synthetic data - [[174-women-hai-neng-gei-suanfa-dang-duojiu-de-pinwei-laoshi-duitan-yamaxun-agi-cha-sheng-lrs0qgmr9gy1nbdtrsvn2lx5dxza]] treats collapse as a data-quality problem rather than a ban on generated examples.
- Human-data renewal - [[tech-20261111-1111-mp-tech-pod-128-tech-20261111-1111-mp-tech-pod-128]] reports rapid degradation after repeated AI-on-AI training and argues that Reddit's daily human discussion remains necessary, while access barriers may weaken its production.

## Counterevidence & Qualifications
The sources do not establish a universal threshold at which synthetic data causes collapse, and the newest episode does not identify the cited study or experimental conditions. Style repetition is not equivalent to system-wide degradation, public slop is not necessarily selected for training, and carefully generated, filtered, or simulator-grounded data can add information. The contributor-incentive link is an ecosystem inference, not a measured model-performance result.

## What Changed
- Migrated Model Collapse to synthesis-v1 from its complete five-source evidence inventory.
- Added fresh human contribution as a renewable-data dependency rather than treating the problem only as corpus contamination.
- Preserved the qualification that informative, filtered synthetic data can remain useful.

## Related Concepts
- [[AISlop]] - public synthetic material that may contaminate later corpora.
- [[DataRecipeCoCreation]] - governs filtering, mixture, evaluation, and grounding choices.
- [[AITrainingDataScarcity]] - adjacent pressure that makes synthetic data attractive despite quality risk.
- [[NegativeParallelism]] - narrow recursive style-amplification example.
- [[HumanKnowledgeCommonsSustainability]] - explains how access and incentives affect the renewal of human-generated knowledge.
- [[HumanJudgmentUnderAI]] - supplies evaluation and review when generated data appears plausible.
