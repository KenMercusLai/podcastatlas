---
title: "E253｜谁在给大模型出题、卖题、判卷？聊聊AI数据行业的野蛮生长"
type: source
tags: [podcast, ai, data, post-training, agents, benchmarks]
sources: []
date: 2026-09-28
source_file: "/home/ken/repos/podcastatlas/content/episodes/E253｜谁在给大模型出题、卖题、判卷？聊聊AI数据行业的野蛮生长 [0a1dd0c4-a1f7-4f7c-b334-bd807ca72a5d].md"
source_url: "https://sv101.fireside.fm/267"
duration: "3485"
last_updated: 2026-09-28
---

# E253｜谁在给大模型出题、卖题、判卷？聊聊AI数据行业的野蛮生长

## Summary
This [[SiliconValley101|硅谷101]] episode with [[HeYunzhong|何韵中]] and [[SunYiyou|孙一游]] explains how AI-data work is moving from static labels toward expert-authored tasks, rubrics, software tools, sandboxes, verifiers, and complete agent environments. Using [[ScaleAI|Scale AI]] and [[AgentsLastExam|Agent's Last Exam]] as central cases, it argues that durable advantage increasingly lies in acquiring real workflows, aligning expert incentives, preventing benchmark leakage and reward hacking, and continually discovering valuable tasks rather than selling one data format indefinitely.

## Key Claims
- [[ExpertRubricVerification]] turns professional judgment into explicit conditions that models, programs, specialist reward models, or humans can use to evaluate an output; it complements rather than replaces an execution environment.
- A complete agent environment combines a task, tools, a sandbox or simulator, and one or more verifiers that inspect final output, state changes, process evidence, or resource use.
- [[AgentsLastExam|Agent's Last Exam]] aims to extend verifiable agent evaluation beyond code into real professional and engineering work, but its task counts, domain coverage, and expansion plans remain source-reported snapshots.
- [[BenchmarkTrainingDataSeparation]] is a governance boundary: benchmark authors may understand a capability gap well enough to build adjacent training data, but selling or training on the held-out evaluation tasks would contaminate the measurement.
- Benchmark optimization can be useful when tasks represent valuable work, the evaluation set remains held out, and improvements generalize; a high score can still mislead when tasks are narrow, weights are arbitrary, tests are flawed, or the benchmark is saturated.
- [[VerticalAIDataProcurement]] becomes harder outside public code because medical records, private databases, commercial engineering software, real projects, licenses, privacy, and expert time must be acquired before workflows can be converted into training environments.
- Reward hacking remains a systems problem: providers can use strong models to search for shortcuts and combine programmatic checks, rubrics, preference judgments, state inspection, step counts, and resource costs.
- Task difficulty must match the target model; tasks that are trivial yield little learning, while impossible tasks produce neither successful trajectories nor useful reward.
- [[HumanDataContributorIncentiveAlignment]] matters because authorship credit, hourly pay, and other rewards can induce synthetic or fabricated submissions unless projects require process evidence and costly verification.
- The episode expects third-party data suppliers to persist where procurement, licensing, expert recruitment, trust, and vertical research are expensive, while generic synthetic data becomes easier to reproduce.

## Key Quotes
The supplied source is a structured episode summary and does not preserve verbatim transcript quotations.

## Connections
- [[SiliconValley101|硅谷101]], [[HeYunzhong|何韵中]], and [[SunYiyou|孙一游]] - show and central speakers.
- [[ScaleAI|Scale AI]] - data supplier and post-training research context represented by He.
- [[AgentsLastExam|Agent's Last Exam]] - cross-domain agent-evaluation project represented by Sun.
- [[AgentEvaluationBenchmarks]] and [[EnvironmentBasedAgentBenchmarks]] - broader benchmark and environment layers extended by the episode.
- [[ExpertRubricVerification]], [[BenchmarkTrainingDataSeparation]], [[VerticalAIDataProcurement]], and [[HumanDataContributorIncentiveAlignment]] - principal concepts added by this source.
- [[AIVerification]], [[AgentPostTraining]], [[SyntheticAgentData]], and [[AITrainingDataScarcity]] - adjacent verification, training, synthesis, and scarcity branches.
- SWE-bench Verified - example used to discuss flawed tests, ambiguous tasks, leakage, and benchmark saturation.
- [[ModelContextProtocol|MCP]], APIs, and software scripts - ways professional workflows can remain code-mediated even outside conventional programming tasks.

## Contradictions
- No settled contradiction found. The episode reinforces the shift from static data toward environments and feedback loops while rejecting a simple replacement story: rubrics remain useful inside environment-based training when programmatic correctness is incomplete.
- The episode qualifies leaderboard scores as evidence of capability. Optimization may be meaningful when tasks mirror real work and remain held out, but specialization, arbitrary weighting, leakage, defective tests, and saturation can weaken the inference from score to general ability.
- Market forecasts, procurement costs, benchmark coverage estimates, project task counts, and claims about data-company durability come from the guests' observations rather than systematic market evidence and remain source-scoped.
