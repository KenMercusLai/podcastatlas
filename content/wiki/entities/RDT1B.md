---
title: "RDT-1B"
type: entity
tags: [project, robotics, pretraining, diffusion]
sources:
  - 187-duihua-liberai-liu-songming-astra-lai-xi-00-hou-wuli-ai-chuangshiren-kandao-de-shenglv-ad3b421a
last_updated: 2026-11-13
knowledge_schema: synthesis-v1
---

# RDT-1B

## Overview
RDT-1B is a robot-pretraining research project associated in the source with [[LiuSongming|刘松明]] and his collaborators before the founding of [[LiberAI]].

## Current Profile
The interview presents RDT-1B as evidence that robot tasks share transferable capability: a pretrained model followed by a small amount of task-specific post-training reportedly outperformed training only on the post-training data, including on unseen tasks. The project used a diffusion approach suited to continuous actions and published detailed training and failure lessons, which helped create a large technical community around the work.

Its strategic importance in this source is not that it solved general robot manipulation. It clarified the next bottleneck: producing diverse, precise, high-quality robot-action data cheaply enough for pretraining to continue scaling.

## Key Characteristics
- Large-scale robot pretraining intended to transfer capability across tasks.
- Diffusion-based modeling chosen for continuous action data.
- Evaluation emphasis on the value of pretraining before small task-specific post-training.
- Detailed open technical documentation and failure reporting.
- Community formation that connected researchers, industrial practitioners, and later startup collaborators.

## Evidence
- Transfer and post-training: [[187-duihua-liberai-liu-songming-astra-lai-xi-00-hou-wuli-ai-chuangshiren-kandao-de-shenglv-ad3b421a]] reports that pretrained models with limited post-training data beat post-training-only baselines on unseen tasks.
- Method and disclosure: [[187-duihua-liberai-liu-songming-astra-lai-xi-00-hou-wuli-ai-chuangshiren-kandao-de-shenglv-ad3b421a]] attributes the diffusion choice and detailed open training lessons to the project.
- Research-to-company bridge: [[187-duihua-liberai-liu-songming-astra-lai-xi-00-hou-wuli-ai-chuangshiren-kandao-de-shenglv-ad3b421a]] describes the project's discussion groups and industry feedback as inputs to Liu's later founder network and data strategy.

## Qualifications
The supplied source does not provide the paper, repository, benchmark protocol, contributor list, training corpus, or numerical results needed to audit RDT-1B directly. All technical and community-impact claims on this page are bounded to the interview and should be checked against primary project materials if later ingested.

## What Changed
- Created the project page from its role in Liu's research and company formation.
- Separated the reported transfer result from the unresolved robot-data scaling bottleneck.

## Relationships
- [[LiuSongming]] - researcher and later founder associated with the project in the source.
- [[LiberAI]] - later company whose pretraining and data strategy draws on this research lineage.
- [[RobotDataScaleUp]] - bottleneck the project reportedly made more visible.
- [[VisionLanguageActionModels]] - adjacent robot-policy family discussed in the same research period.
- [[WorldActionModels]] - later action-conditioned route pursued by Liber AI.
