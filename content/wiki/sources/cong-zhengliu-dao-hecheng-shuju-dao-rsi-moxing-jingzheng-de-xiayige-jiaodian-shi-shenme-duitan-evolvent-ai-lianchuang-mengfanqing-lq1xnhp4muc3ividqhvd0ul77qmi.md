---
title: "从蒸馏到合成数据到 RSI，模型竞争的下一个焦点是什么？｜对谈 Evolvent AI 联创孟繁青"
type: source
tags: [podcast, ai, rsi, synthetic-data, post-training]
sources: []
date: 2026-08-08
source_file: "/home/ken/repos/podcastatlas/content/episodes/从蒸馏到合成数据到 RSI，模型竞争的下一个焦点是什么？｜对谈 Evolvent AI 联创孟繁青 [lq1xnhp4MuC3iViDqhVd0Ul77QmI].md"
source_url: "https://www.xiaoyuzhoufm.com/episode/6a75424b000a55a9bb042560"
duration: "3570"
last_updated: 2026-08-09
---

# 从蒸馏到合成数据到 RSI，模型竞争的下一个焦点是什么？｜对谈 Evolvent AI 联创孟繁青

## Summary
This [[42Zhangjing]] episode interviews [[MengFanqing|孟繁青]], co-founder of [[EvolventAI|Evolvent AI]], on how model competition is moving from post-training recipes and data toward [[RecursiveSelfImprovement|RSI]]. The episode argues that post-training work is becoming more service-like inside model labs, making [[SyntheticAgentData]], [[EnvironmentBasedAgentBenchmarks]], evaluation design, and fast iteration increasingly central. Its larger synthesis is that [[ModelDistillation]] can accelerate weaker models, but durable competition still depends on architecture, pretraining, high-quality data, environments, organization, and whether systems can turn feedback into future capability through [[RSIData]].

## Key Claims
- [[MengFanqing]] says large-lab post-training has become more engineeringized: researchers often submit data and training requests while stable internal services handle much of the SFT or RL workflow.
- [[EnvironmentBasedAgentBenchmarks]] are replacing static question-answer tests in some areas: the benchmark becomes a simulated work environment where an agent operates tools, receives feedback, and is scored on multiple behaviors.
- Data quality is hard to judge before training; practical validation still depends on whether a model improves without benchmark hacking or leakage.
- Chinese model labs are narrowing the gap with overseas frontier labs, and the source attributes this to constrained-resource architecture and efficiency work as well as data and organization, not only to [[ModelDistillation]].
- [[Kimi]] and [[DeepSeek]] are used as examples of domestic model work shaped by architecture or efficiency pressure, including Kimi's linear-attention direction and DeepSeek's Multi Latent Attention.
- [[ModelDistillation]] is framed as a useful shortcut and acceleration tool, especially for lagging models with larger learning margin, but not as the decisive reason domestic models have become strong.
- [[RecursiveSelfImprovement|RSI]] is defined broadly as giving a model an environment and a goal, letting it act, observe feedback, modify prior actions, and try to break through its previous ceiling.
- The episode rejects a separate "RSI base model" category: RSI ability is expected to be increasingly internalized by stronger base models through pretraining, world-model-like knowledge, and longer context.
- [[ModelHarnessCoEvolution|Harness]] layers are expected to become simpler but not disappear, because models are trained with the harnesses they will use and vertical applications may still need workflows around smaller models.
- [[SyntheticAgentData]] can overlap with distillation when the exploration agent is an outside stronger model such as [[Claude]], but complex environments, task design, and scoring make this more than copying teacher answers.
- [[RSIData]] is presented as a likely next data demand: trajectories where one model helps train or improve another smaller model, including long-running environment, training, evaluation, and revision traces.
- Personal AI usage traces are unlikely to sell directly because they are noisy, hard to clean, and raise compliance problems.
- The data-company filter is tightening: teams need hands-on researchers who can build environments, run training, clean trajectories, and follow rapidly changing model-lab demand.
- The source treats [[AutoResearch]] and [[AIForScience]] as important next directions after coding pipelines stabilize, while keeping organization speed and technical execution as durable differentiators.
- Multimodal work is not dismissed as outside the intelligence mainline, but the source says text is more compressed and easier to optimize than noisy multimodal inputs.

## Key Quotes
> "post-training 很多时候是在做数据" — Meng's summary of where post-training leverage has moved.

> "给模型一个环境和目标" — the episode's compact RSI definition.

> "蒸馏不是决定性因素" — the source's position on domestic model progress.

## Connections
- [[42Zhangjing]], [[MengFanqing]], and [[EvolventAI]] — show, guest, and startup context.
- [[RSIBenchData]], [[RSIData]], [[SyntheticAgentData]], and [[EnvironmentBasedAgentBenchmarks]] — new data and benchmark branch added by this source.
- [[RecursiveSelfImprovement]], [[AutoResearch]], [[AIForAI]], [[AIForScience]], and [[MLCoding]] — broader AI-for-AI and research automation context.
- [[AgentPostTraining]], [[ModelPostTrainingBottleneck]], [[AgentData]], [[AIDataInfrastructure]], and [[DataPricingInAI]] — post-training and data-market context.
- [[AgentEvaluationBenchmarks]], [[AgentHarness]], [[ModelHarnessCoEvolution]], [[AIVerification]], and [[WorldModels]] — environment, harness, verifier, and feedback mechanism.
- [[ModelDistillation]], [[OnPolicyDistillation]], [[KimiK3]], and [[ModelInfraCoDesign]] — distillation and model-factory context.
- [[Kimi]], [[MoonshotAI]], [[DeepSeek]], [[ZhipuAI]], [[ByteDance]], and [[TencentHunyuan]] — domestic model-lab comparison set.
- [[Claude]], [[OpenAI]], and [[Anthropic]] — outside model and frontier-lab references used in the data and Auto Research discussion.
- [[AIOrganizationDesign]] and [[ResearchTaste]] — organization and hands-on research judgment as competitive bottlenecks.

## Contradictions
- No direct contradiction found.
- The source reinforces [[yu-tian-yuandong-liao-rsi-moxing-zi-jinhua-ruhe-daolai-1-178-1]] by treating RSI as AI improving AI, but shifts emphasis from research taste and scaling dynamics toward data, environments, harnesses, and long-running trajectories.
- The source qualifies [[e246-hewei-zhengliu-liaoliao-guigu-ruhe-kan-zhongguo-kaifang-moxing-bijin-qianyan-5fd236d7-9a72-4b15-9e84-e83ceadd1b41]] by arguing that distillation is a useful acceleration route rather than the decisive explanation for Chinese model progress.
- The source qualifies [[AITrainingDataScarcity]] and [[ModelCollapse]] concerns by saying high-quality data can keep growing through agent and synthetic loops, while also warning that synthetic data is not infinite and still needs environment, scoring, diversity, and verification.
