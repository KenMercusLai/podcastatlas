---
title: "逯雨鑫 / 逯雨昕 / Lu Yuxin"
type: entity
knowledge_schema: synthesis-v1
tags: [ai, model-training, researcher]
sources:
  - yi-ge-ren-liang-zhou-shu-bai-meiyuan-ruhe-xun-chu-dengding-hugging-face-de-moxing-duitan-yanjiuyuan-lu-yuxin-lpxxrnwdhgnsrxuyhrfrv5t1lojt
last_updated: 2026-08-30
---

# 逯雨鑫 / 逯雨昕 / Lu Yuxin

## Overview
逯雨鑫 / 逯雨昕 is the AI researcher interviewed in [[yi-ge-ren-liang-zhou-shu-bai-meiyuan-ruhe-xun-chu-dengding-hugging-face-de-moxing-duitan-yanjiuyuan-lu-yuxin-lpxxrnwdhgnsrxuyhrfrv5t1lojt]]. The source presents her as a former data engineer and AI graduate student who built a narrowly improved open model before joining an AI lab.

## Current Profile
Her profile in the wiki is a practical post-training case rather than a general biography. She argues that useful small-model improvement can be self-taught when the target is narrow, the base model is suitable, and the builder is willing to spend most of the work on data. The episode uses her experience to connect individual model tinkering, application-company model ownership, and local AI adoption.

## Key Characteristics
- Built a source-reported high-ranking [[HuggingFace|Hugging Face]] open-model result before joining an AI lab.
- Frames post-training as an industrial skill path available beyond PhD or large-lab backgrounds.
- Treats [[SupervisedFineTuning|SFT]], [[QLoRA]], benchmark iteration, and failure-case diagnosis as realistic tools for individual builders.
- Emphasizes real trajectories, data audit, and target alignment more than training scripts or raw compute.
- Argues that application companies with real users may gain model capability through scenario data and post-training.
- Presents local AI as a privacy, cost, and refusal-policy tradeoff rather than as a current replacement for frontier models.

## Evidence
### Practical post-training case
- [[yi-ge-ren-liang-zhou-shu-bai-meiyuan-ruhe-xun-chu-dengding-hugging-face-de-moxing-duitan-yanjiuyuan-lu-yuxin-lpxxrnwdhgnsrxuyhrfrv5t1lojt]] reports a first model version in about five days, a second in two to three weeks, and a cost structure involving one 5090-class GPU, [[QLoRA]], and a few-hundred-dollar data budget.

### Data-first method
- [[yi-ge-ren-liang-zhou-shu-bai-meiyuan-ruhe-xun-chu-dengding-hugging-face-de-moxing-duitan-yanjiuyuan-lu-yuxin-lpxxrnwdhgnsrxuyhrfrv5t1lojt]] says the bottleneck was data insight and audit: real traces, open community data, manual review, and benchmark error analysis drove the iteration more than training runtime.

### Strategic interpretation
- [[yi-ge-ren-liang-zhou-shu-bai-meiyuan-ruhe-xun-chu-dengding-hugging-face-de-moxing-duitan-yanjiuyuan-lu-yuxin-lpxxrnwdhgnsrxuyhrfrv5t1lojt]] uses her experience to argue that applications, user data, and local deployment can shift some model work away from frontier labs, while leaving pretraining and frontier research lab-led.

## Qualifications
- The wiki has only this source for her profile; model ranking, cost, benchmark, and career details remain source-reported.
- The source title and body differ between 逯雨鑫 and 雨昕, so the page preserves both spellings without resolving the primary Chinese given name.
- The episode does not identify the AI lab, base model, benchmark, or model repository with enough detail for independent verification inside this ingest.

## What Changed
- Created a new person entity for the episode's guest and model-post-training practitioner.
- Established her as the human case connecting [[LowCostModelPostTraining]], [[DataFirstPostTraining]], and [[ApplicationCompanyModelCapability]].

## Relationships
- [[42Zhangjing]] - interview venue for her post-training account.
- [[HuggingFace]] - platform and leaderboard context for the source-reported model result.
- [[Qwen]] - base-model family she names as relatively practical for Chinese-capable small-model post-training.
- [[SupervisedFineTuning]] - training method she treats as the realistic default for many individuals and application companies.
- [[DataFirstPostTraining]] - operating method her project exemplifies.
- [[ApplicationCompanyModelCapability]] - strategic company-level implication she discusses.
