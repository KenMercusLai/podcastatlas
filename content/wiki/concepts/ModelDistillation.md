---
title: "Model Distillation / 模型蒸馏"
type: concept
tags: [ai, machine-learning, models]
sources: [xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1, e246-hewei-zhengliu-liaoliao-guigu-ruhe-kan-zhongguo-kaifang-moxing-bijin-qianyan-5fd236d7-9a72-4b15-9e84-e83ceadd1b41]
last_updated: 2026-08-08
---

# Model Distillation / 模型蒸馏

[[xiangjie-kimi-k3-qiangdao-chongji-anthropic-guzhi-de-moxing-shenmeyang-1-177-1]] adds a post-training workflow version through [[KimiK3|Kimi K3]]. [[ZengZhiyuan]] distinguishes classic distillation, off-policy distillation, and [[OnPolicyDistillation]], then uses [[MOPDPostTraining|MOPD]] to show distillation as capability merging across domain experts and reasoning-effort levels, not only small-model compression or copying.

Model distillation is the machine-learning technique discussed in [[e246-hewei-zhengliu-liaoliao-guigu-ruhe-kan-zhongguo-kaifang-moxing-bijin-qianyan-5fd236d7-9a72-4b15-9e84-e83ceadd1b41]], where a smaller or cheaper model learns behavior from a stronger teacher model. [[WangTiezhen|王铁镇]] distinguishes the classic form, where a student can learn from output probability distributions or logits, from the public accusation that a model was built by scraping another model's text outputs.

The concept matters because the episode treats "distillation" as several different claims that should not be collapsed. A model can use teacher outputs legally or openly, violate an API provider's terms by mass generation, learn from already-public model outputs on the internet, or be falsely accused because its behavior resembles another model. The source argues that proving [[KimiK3|Kimi K3]]'s core capability came from a specific closed model would require evidence beyond model identity confusion or short timing narratives.

## Key Claims
- Distillation is a standard technique, not inherently a misconduct category.
- Closed APIs usually do not expose the logits needed for classic full-probability distillation.
- Training on generated text is a weaker and broader claim than classic distillation.
- [[DeepSeek]] is used as an example of a model family whose R1-era outputs and artifacts were described as more open to downstream distillation.
- Distillation can improve smaller models, but the source says architecture, data engineering, RL, inference optimization, and [[ScalingEfficiency]] also have to be considered.
- Terms-of-service violations, copying accusations, and technical distillation are different questions.
- In agent post-training, distillation may be used to merge domain specialists into one model, but it still needs reliable teacher scoring and external supervision.

## Connections
- [[KimiK3]], [[MoonshotAI]], [[DeepSeek]], and [[OpenSourceAIModels]] - model cases in the episode.
- [[ModelIdentityDataPollution]] - why self-identification errors are weak evidence for distillation.
- [[ScalingEfficiency]], [[ModelPostTrainingBottleneck]], and [[AgentPostTraining]] - adjacent model-improvement mechanisms.
- [[OpenModelSafetyGovernance]] and [[AIGovernanceAndCompliance]] - compliance and transparency layer when model-generated data is used.
- [[OnPolicyDistillation]], [[MOPDPostTraining]], [[KimiK3]], and [[AIVerification]] - K3 post-training branch added by LateTalk episode 177.
