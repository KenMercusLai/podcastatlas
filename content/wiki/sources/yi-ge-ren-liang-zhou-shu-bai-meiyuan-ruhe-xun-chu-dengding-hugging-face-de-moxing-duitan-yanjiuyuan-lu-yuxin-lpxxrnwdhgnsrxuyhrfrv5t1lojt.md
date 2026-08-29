---
title: "一个人、两周、数百美元，如何训出登顶 Hugging Face 的模型 | 对谈研究员逯雨鑫"
type: source
tags: [podcast, ai, model-training, post-training, local-ai]
sources: []
date: 2026-08-29
source_file: "/home/ken/repos/podcastatlas/content/episodes/一个人、两周、数百美元，如何训出登顶 Hugging Face 的模型 ｜ 对谈研究员逯雨鑫 [lpXxRnwDHgNSrxuyHrfrv5t1lOjT].md"
source_url: "https://www.xiaoyuzhoufm.com/episode/6a8ed6e7ef65145dfcc5d249"
duration: "2850"
last_updated: 2026-08-30
---

# 一个人、两周、数百美元，如何训出登顶 Hugging Face 的模型 | 对谈研究员逯雨鑫

## Summary
This [[42Zhangjing]] episode interviews [[LuYuxin|逯雨鑫 / 逯雨昕]] about making a high-ranking [[HuggingFace|Hugging Face]] open-model result before joining an AI lab. The practical center is [[LowCostModelPostTraining]]: choose a clear target, pick a suitable base model such as [[Qwen]], build a data pipeline, use [[SupervisedFineTuning|SFT]] and [[QLoRA]], then iterate against benchmarks and failure cases. The strategic half connects [[DataFirstPostTraining]], [[ApplicationCompanyModelCapability]], and [[LocalAIPrivacyTradeoff]]: application companies may own more post-training and user-data loops, while local models trade frontier capability for privacy, cost control, and policy independence.

## Key Claims
- [[LuYuxin]] says her first model version took about five days and the second two to three weeks, using one 5090-class GPU, [[QLoRA]], and a few-hundred-dollar data-generation budget.
- The episode frames personal or application-company model work as target-specific [[ModelPostTrainingBottleneck|post-training]], not as frontier pretraining; gains on an agentic benchmark can coexist with weaker general benchmark behavior.
- [[SupervisedFineTuning|SFT]] is treated as the realistic default for individuals and many application companies because [[AgentRL|RL]] and more complex methods raise cost and infrastructure demands.
- [[DataFirstPostTraining]] is the core operating lesson: public scripts, benchmarks, and cloud tools exist, but the guest says most project time went into data insight, data cleaning, and audit.
- Real traces from users and open communities are treated as more useful than generic synthetic data, while synthetic data is useful for targeted failure repair such as overconfident task-completion claims.
- [[ModelDistillation]] works only when the teacher-model outputs move the student toward the intended target; a [[Qwen]]-sized or 12B-class student may fail to absorb a stronger teacher's full behavior because of capacity gap.
- [[ApplicationCompanyModelCapability]] may grow as companies with direct customers collect first-party interaction data, build domain evaluations, and post-train smaller models for their own scenarios.
- AI labs are still positioned as important for frontier research, pretraining, and large-scale serving; the source does not claim individuals or ordinary application firms can replace that layer.
- [[LocalAIPrivacyTradeoff]] is presented as a likely reason local models spread: sensitive data, high token cost, and safety refusals can make a weaker local model preferable for some domains.

## Key Quotes
> "95% 的时间都用在做数据上" - the episode's practical post-training bottleneck.

> "几千条量级" - the source's claimed useful data scale for a narrow target.

> "先明确目标，再选底座模型" - the workflow order emphasized by the guest.

## Connections
- [[LuYuxin]] - guest and source-reported builder of the pre-lab model.
- [[42Zhangjing]] - show context for the interview.
- [[HuggingFace]], [[Qwen]], [[QLoRA]], and [[SupervisedFineTuning]] - platform, base-model, and training-method context.
- [[ModelPostTrainingBottleneck]], [[ModelDistillation]], [[DataFirstPostTraining]], and [[LowCostModelPostTraining]] - core technical synthesis.
- [[AgentPostTraining]], [[SyntheticAgentData]], [[ModelWorkflowFit]], and [[AIVerification]] - agentic benchmark, data, and evaluation context.
- [[ApplicationCompanyModelCapability]], [[AIApplicationLayerMoat]], [[AIDataFlywheel]], and [[ModelSovereignty]] - company strategy and data-control branch.
- [[LocalAIPrivacyTradeoff]], [[LocalPrivateAI]], [[LocalAIWorkstation]], [[AIQueryPrivacyRisk]], and [[AIInferenceCostStructure]] - local AI, privacy, and cost branch.
- [[OpenAI]], [[Anthropic]], [[Claude]], [[ChatGPT]], [[Codex]], [[VLLM|vLLM]], and [[SGLang]] - model, assistant, coding-tool, and serving references.

## Contradictions
- No settled contradiction found. The source complements existing distillation and post-training pages by narrowing the claim to domain-specific small-model improvement rather than general frontier-model replacement.
- It qualifies stronger local-AI optimism by saying the guest still uses local AI less today because current local models remain weaker and error-prone compared with frontier services.
- The name spelling is source-scoped: the title/frontmatter use 逯雨鑫, while the body repeatedly uses 雨昕; the wiki keeps both under [[LuYuxin]] pending stronger identity evidence.
