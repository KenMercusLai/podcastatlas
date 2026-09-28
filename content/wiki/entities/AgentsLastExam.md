---
title: "Agent's Last Exam"
type: entity
tags: [project, ai, agents, benchmarks, evaluation]
sources:
  - e253-shui-zai-gei-damoxing-chuti-maiti-panjuan-liaoliao-ai-shuju-hangye-de-yemanshengzhang-0a1dd0c4-a1f7-4f7c-b334-bd807ca72a5d
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

# Agent's Last Exam

## Overview
Agent's Last Exam is an agent-evaluation project described in the source as collecting verifiable tasks from many professional and engineering subdomains so models can be tested on work beyond static question answering.

## Current Profile
The project is presented as an attempt to transfer the useful properties of coding benchmarks into broader work: a task should matter, run in an appropriate tool environment, and admit credible verification. Experts contribute or reconstruct real projects, while the project screens private, copyrighted, sensitive, fabricated, or otherwise noncompliant material.

Its public benchmark and any adjacent training-data activity must remain separate. [[SunYiyou|孙一游]] argues that publishing or selling the held-out evaluation tasks for training would contaminate the leaderboard, even though benchmark builders may use their domain knowledge to develop distinct training material. The source reports approximately 150 public tasks across more than 50 subdomains at the time of discussion and a plan to exceed 1,000 tasks; these figures are time-bound and not independently checked here.

## Key Characteristics
- Cross-domain benchmark centered on agent completion of professional and engineering work.
- Task design that combines instructions, tools or software, an execution environment, and verification.
- Expert-sourcing model using prior projects while screening privacy, copyright, and compliance risks.
- Held-out benchmark integrity separated from adjacent training-data creation.
- Quality-control burden involving fabricated work, process evidence, and costly expert review.
- Source-reported expansion from roughly 150 public tasks toward more than 1,000.

## Evidence
- Purpose and scope - [[e253-shui-zai-gei-damoxing-chuti-maiti-panjuan-liaoliao-ai-shuju-hangye-de-yemanshengzhang-0a1dd0c4-a1f7-4f7c-b334-bd807ca72a5d]] describes the project as extending verifiable evaluation beyond code into more than 50 subdomains.
- Environment structure - [[e253-shui-zai-gei-damoxing-chuti-maiti-panjuan-liaoliao-ai-shuju-hangye-de-yemanshengzhang-0a1dd0c4-a1f7-4f7c-b334-bd807ca72a5d]] links tasks with tools, sandboxes, programmatic checks, rubrics, and human judgment.
- Data governance - [[e253-shui-zai-gei-damoxing-chuti-maiti-panjuan-liaoliao-ai-shuju-hangye-de-yemanshengzhang-0a1dd0c4-a1f7-4f7c-b334-bd807ca72a5d]] preserves the rule against using the evaluation set as training material.
- Contributor quality - [[e253-shui-zai-gei-damoxing-chuti-maiti-panjuan-liaoliao-ai-shuju-hangye-de-yemanshengzhang-0a1dd0c4-a1f7-4f7c-b334-bd807ca72a5d]] reports synthetic or fabricated submissions and the resulting need for process evidence and expert review.

## Qualifications
The source is a podcast summary, not the project's technical paper, task repository, or current leaderboard. Task totals, planned scale, domain coverage, acceptance rules, and reported biology-workflow coverage remain source-scoped and time-sensitive. Meaningful work alignment does not by itself eliminate benchmark leakage, narrow specialization, flawed tests, or verifier gaming.

## What Changed
- Added the project as a concrete cross-domain environment benchmark.
- Established held-out evaluation integrity and contributor verification as core parts of its profile.

## Relationships
- [[SunYiyou|孙一游]] - participating researcher and source representative.
- [[AgentEvaluationBenchmarks]] - broader class of agent capability tests.
- [[EnvironmentBasedAgentBenchmarks]] - task, tool, sandbox, and verifier architecture used by the project.
- [[BenchmarkTrainingDataSeparation]] - governance boundary between measurement and model improvement.
- [[ExpertRubricVerification]] - method for evaluating outcomes that lack one exact answer.
- [[HumanDataContributorIncentiveAlignment]] - quality-control challenge in expert task sourcing.
