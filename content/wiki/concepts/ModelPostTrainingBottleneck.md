---
title: "Model Post-Training Bottleneck"
type: concept
tags: [ai, model-training, post-training]
sources: [vol-114-ai-de-2025-he-deepseek-men-de-weilai-duitan-fudan-zhangqi-jiaoshou-lhvhnvqtvuv4ln-cckcpedgldolo]
last_updated: 2026-08-06
---

# Model Post-Training Bottleneck

Model post-training bottleneck is the episode's reminder that a useful large model is not finished when pretraining succeeds. In [[vol-114-ai-de-2025-he-deepseek-men-de-weilai-duitan-fudan-zhangqi-jiaoshou-lhvhnvqtvuv4ln-cckcpedgldolo]], [[ZhangQi|张奇]] argues that pretraining supplies much of a model's knowledge, but post-training decides whether that latent knowledge becomes reliable behavior for a task.

The bottleneck is partly data matching. Zhang says that if a model has already remembered the relevant knowledge during pretraining, a small amount of aligned training data may unlock usable answers; if not, adding supervised data later can fail or even disturb other behavior. The source therefore treats post-training as a costly, expert-heavy search process rather than a simple "add labels" phase.

## Key Claims
- Post-training must match the knowledge and behavior the base model can actually support.
- More high-quality-looking data is not automatically better if it does not align with what the model already learned.
- Frontier labs' advantage may include tacit formulas, evaluation know-how, expert labeling, and large-scale trial-and-error after pretraining.
- [[DeepSeek]] can reduce the visible cost story around pretraining and inference, while the post-training layer can remain expensive and hard to copy.
- Agent systems intensify the bottleneck because the model must learn reflection, tool use, memory, failure recovery, and environment feedback.

## Connections
- [[AgentPostTraining]], [[AgentRL]], and [[TrainingComputeAllocation]] — agent-specific versions of the bottleneck.
- [[DeepSeek]], [[OpenAI]], [[MOSS]], and [[FrontierModelScaling]] — model organizations and scaling context.
- [[InterleavedThinking]], [[LongHorizonAI]], and [[AgenticWorkflow]] — behaviors that require stronger post-training and evaluation.
- [[ModelWorkflowFit]], [[AICodingVerification]], and [[HumanJudgmentUnderAI]] — deployment-side evidence that post-training alone is not enough.
