---
title: "Benchmark–Training Data Separation / 评测集与训练数据隔离"
type: concept
tags: [ai, benchmarks, training-data, governance, evaluation]
sources:
  - e253-shui-zai-gei-damoxing-chuti-maiti-panjuan-liaoliao-ai-shuju-hangye-de-yemanshengzhang-0a1dd0c4-a1f7-4f7c-b334-bd807ca72a5d
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

# Benchmark–Training Data Separation / 评测集与训练数据隔离

## Definition
Benchmark–training data separation is the rule that held-out evaluation tasks must not be disclosed, sold, or reused as model-training examples when the resulting score is meant to measure unseen capability.

## Current Synthesis
Benchmarks and training data address related but different questions. A benchmark describes the gap between current performance and a desired capability; training data helps close known gaps. Because benchmark builders understand the task distribution, they may be well placed to create distinct training material, but authority over the exam creates a conflict if the exam itself becomes the lesson.

Leaderboard optimization is therefore not automatically illegitimate. It can represent useful progress when tasks correspond to real user work, evaluation items remain held out, and the learned capability improves several related tests or real outcomes. It becomes weak evidence when data leak, tasks are overly narrow, aggregate weights do not reflect users, tests reject valid solutions, or a nearly saturated benchmark leaves mostly broken and ambiguous items.

## Key Claims
- Held-out evaluation tasks should not be sold or used as training examples for the same reported benchmark.
- Benchmark creators can build adjacent training data if the artifacts and governance remain separate.
- Real-work relevance makes score optimization more meaningful but does not remove leakage risk.
- Cross-benchmark and real-world transfer are stronger evidence than improvement on one leaderboard.
- Aggregate benchmark weights embed judgments about which capabilities matter.
- Saturation and defective residual tasks can reduce a benchmark's discriminating value.

## Evidence
- Role separation - [[e253-shui-zai-gei-damoxing-chuti-maiti-panjuan-liaoliao-ai-shuju-hangye-de-yemanshengzhang-0a1dd0c4-a1f7-4f7c-b334-bd807ca72a5d]] contrasts forward-looking capability measurement with data used to improve present weaknesses.
- Integrity rule - [[e253-shui-zai-gei-damoxing-chuti-maiti-panjuan-liaoliao-ai-shuju-hangye-de-yemanshengzhang-0a1dd0c4-a1f7-4f7c-b334-bd807ca72a5d]] records [[SunYiyou|孙一游]]'s position that the evaluation set itself cannot be sold as training data.
- Meaningful optimization test - [[e253-shui-zai-gei-damoxing-chuti-maiti-panjuan-liaoliao-ai-shuju-hangye-de-yemanshengzhang-0a1dd0c4-a1f7-4f7c-b334-bd807ca72a5d]] ties useful benchmark gains to authentic tasks, held-out data, and generalized capability.
- Failure modes - [[e253-shui-zai-gei-damoxing-chuti-maiti-panjuan-liaoliao-ai-shuju-hangye-de-yemanshengzhang-0a1dd0c4-a1f7-4f7c-b334-bd807ca72a5d]] uses weighting, specialized game solving, leakage, ambiguous requirements, strict tests, and saturation as reasons to qualify leaderboard inference.

## Counterevidence & Qualifications
The source does not specify a formal contamination audit, disclosure standard, embargo design, or proof that a model has not encountered public benchmark material. Even without direct leakage, repeated leaderboard feedback can support overfitting. Conversely, poor transfer does not always mean cheating; it can reveal that the benchmark sampled a capability too narrowly or that deployment conditions differ from the test environment.

## What Changed
- Added an explicit commercial boundary between benchmark authority and adjacent data sales.
- Distinguished legitimate real-work optimization from contamination and narrow leaderboard specialization.

## Related Concepts
- [[AgentEvaluationBenchmarks]] - benchmark class whose scores depend on held-out integrity.
- [[EnvironmentBasedAgentBenchmarks]] - interactive tests where tasks, tools, and verifiers can also generate tempting training traces.
- [[AgentsLastExam|Agent's Last Exam]] - central project case for separating evaluation tasks from training products.
- [[AIBenchmarkGaming]] - broader family of score optimization that may or may not reflect useful capability.
- [[AIVerification]] - need to verify both task completion and the integrity of the measurement process.
- [[SyntheticAgentData]] - adjacent training material that must be checked for benchmark overlap and leakage.
