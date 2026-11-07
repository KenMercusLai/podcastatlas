---
title: "锐评国模与 Neo Lab，畅谈 RL 人生与 RLaaS | 对谈 Mind Lab 首席科学家骁腾"
type: source
tags: [podcast, ai, reinforcement-learning, post-training, new-lab]
sources: []
date: 2026-11-07
source_file: "/home/ken/repos/podcastatlas/content/episodes/lkBT2upqW6EoxM0YjC1Zklr8WLgc [lkBT2upqW6EoxM0YjC1Zklr8WLgc].md"
source_url: "https://dts-api.xiaoyuzhoufm.com/track/648b0b641c48983391a63f98/6aec6bc06381f0f964c45068/media.xyzcdn.net/648b0b641c48983391a63f98/lkBT2upqW6EoxM0YjC1Zklr8WLgc.m4a"
duration: "3808"
last_updated: 2026-11-08
---

# 锐评国模与 Neo Lab，畅谈 RL 人生与 RLaaS | 对谈 Mind Lab 首席科学家骁腾

## Summary
This [[42Zhangjing]] episode interviews [[MaXiaoteng|马肖腾]] of [[MineLab]] about reinforcement learning, enterprise model post-training, AI-company competition, and the research-to-market discipline of a [[NewLabOrganization|New Lab]]. Its central operating thesis is [[EnterprisePostTrainingLoop|enterprise post-training as a feedback loop]]: customer environments supply proprietary data, tasks, failures, and benchmarks that can support repeated model improvement rather than a one-off fine-tuning job. The conversation also connects [[LowRankAdapterModelDiversity|LoRA-based model diversity]], [[ContinualLearning]], [[ResearchTaste]], and [[ReinforcementLearningDecisionHeuristics|RL-inspired decision heuristics]] while keeping costs, data access, evaluation, latency, and human-defined rewards visible.

## Key Claims
- [[MaXiaoteng|马肖腾]] describes a path from Tsinghua automation and large-scale multi-agent RL research into [[MineLab]], whose business shifted from consumer applications toward enterprise reinforcement-learning and post-training services.
- [[ReinforcementLearningDecisionHeuristics]] turns exploration versus exploitation, policy-value consistency, and discounting into personal rules: preserve some randomness, use action to revise beliefs, and balance long-term direction against executable near-term steps.
- The source treats post-training as a reusable foundational capability similar to recommendation systems: value comes from repeated exposure to real behavior, feedback, and vertical tasks rather than from a single generic model recipe.
- Public web data is described as increasingly exhausted, so durable advantage moves toward proprietary enterprise data and interactive environments that models can act in, receive feedback from, and learn within.
- [[EnterprisePostTrainingLoop]] requires a customer-owned benchmark before optimization; without a baseline and stable evaluation, neither capability improvement nor cost reduction can be demonstrated.
- Post-training can improve performance on a private benchmark or distill useful behavior into a cheaper model, but local deployment, privacy requirements, distributed training, and serving infrastructure raise implementation cost.
- The guest estimates that one frontier-model training iteration may cost tens of thousands of yuan and that an end-to-end engagement may range from hundreds of thousands to roughly one million yuan; these are experience-based ranges, not audited market prices.
- [[NewLabOrganization|New Lab]] is defined here by a research-product-design loop: real use cases should shape research questions, prototypes should collect evidence before large-scale promotion, and usefulness matters more than publication alone.
- [[DeepSeek]] is praised for model-infrastructure co-design and [[ZhipuAI]] for practical usability and data production, while [[OpenAI]] and [[Anthropic]] are treated as leading overseas labs; these are the guest's comparative judgments rather than benchmark-backed rankings.
- [[RecursiveSelfImprovement|RSI]] is narrowed from an open-ended autonomy slogan to greater AI participation in finding data, creating verifiable feedback, and improving training pipelines; human reward design, taste, and private data remain necessary.
- [[MineLabMint|Mint]] uses [[LowRankAdapterModelDiversity|LoRA-based specialization]] to explore larger base models, cheaper adapters, and many coexisting behavioral variants on shared foundations.
- [[ContinualLearning]] is framed as the unresolved problem of compressing long experience into durable judgment or “taste” without retaining every detail, possibly through lightweight and repeatedly updated memory units.

## Key Quotes
> "90 分主义" - the guest's shorthand for leaving capacity for exploration rather than optimizing every current task to completion.

> "企业要做后训练，首先得有自己的 benchmark" - the source's evaluation prerequisite for enterprise post-training.

> "真正的 New Lab" - the source's label for research organizations that connect technical work to real use and commercial feedback.

## Connections
- [[MaXiaoteng|马肖腾]], [[MineLab]], and [[MineLabMint|Mint]] - guest, company, and LoRA training-service context.
- [[EnterprisePostTrainingLoop]], [[ModelPostTrainingBottleneck]], [[AgentPostTraining]], and [[AIVerification]] - data, environment, benchmark, and delivery loop.
- [[LowRankAdapterModelDiversity]], [[QLoRA]], [[ModelDistillation]], and [[SpecializedIntelligence]] - low-cost specialization and heterogeneous-model branch.
- [[NewLabOrganization]], [[ResearchTaste]], and [[AIOrganizationDesign]] - research, product, design, and commercialization relationship.
- [[ReinforcementLearningDecisionHeuristics]], [[AgentRL]], and [[OrganizationalLongTermism]] - RL concepts applied to action and time horizons.
- [[ContinualLearning]], [[PersistentAgentMemory]], and [[HumanTasteAsAITrainingSignal]] - compressed experience, durable judgment, and human preference boundary.
- [[DeepSeek]], [[ZhipuAI]], [[OpenAI]], [[Anthropic]], and [[ModelInfraCoDesign]] - model-company and infrastructure comparison set.

## Contradictions
- No settled factual contradiction is adopted.
- The title says “Mind Lab” and names “骁腾,” while the supplied body consistently uses “MineLab” and “马肖腾”; the wiki consolidates the body forms under [[MineLab]] and [[MaXiaoteng]] while preserving the mismatch as source-level uncertainty.
- The source's claim that sub-1T model training has become a relatively standard recipe is qualified by its own emphasis on tacit infrastructure, architecture-hardware co-design, data access, environments, and evaluation.
- Company rankings, cost ranges, LoRA/full-training comparability, domestic-compute forecasts, and the future balance between general and specialized models remain guest judgments without independent validation in the supplied document.
