---
title: "Video-MME"
type: entity
tags: [project, benchmark, video-understanding, ai-evaluation]
sources:
  - ai-shidai-phd-lushang-de-10-ge-guanjian-wenti-duitan-lilei-gangda-phd-xiaomi-mimo-yanjiuyuan-lpbsxeoxbcgtv0qckx8lctpdwviv
last_updated: 2026-10-26
knowledge_schema: synthesis-v1
---

# Video-MME

## Overview
Video-MME is an AI video-understanding benchmark cited by [[LiLeiXiaomiMiMo|李磊]] as an example of evaluation that extends the measured capability from very short clips toward videos lasting more than an hour.

## Current Profile
Within the bounded episode, Video-MME matters less as a leaderboard than as an example of [[BenchmarkAdoptionDesign]]: it proposes a consequential new evaluation dimension and is meant to be reproducible, easy to run, and compatible with common evaluation ecosystems.

## Key Characteristics
- Targets long-duration video understanding rather than only short-clip performance.
- Is presented as measuring a new or materially extended model capability.
- Illustrates the importance of realistic tasks rather than obviously artificial test prompts.
- Connects scientific contribution to reproducibility, usability, and ecosystem integration.

## Evidence
- Capability evidence: [[ai-shidai-phd-lushang-de-10-ge-guanjian-wenti-duitan-lilei-gangda-phd-xiaomi-mimo-yanjiuyuan-lpbsxeoxbcgtv0qckx8lctpdwviv]] says the benchmark extends video evaluation from roughly six seconds to more than an hour.
- Adoption evidence: [[ai-shidai-phd-lushang-de-10-ge-guanjian-wenti-duitan-lilei-gangda-phd-xiaomi-mimo-yanjiuyuan-lpbsxeoxbcgtv0qckx8lctpdwviv]] uses it while arguing that benchmarks need one-command execution, reproducibility, and compatibility with mainstream tools.

## Qualifications
The current wiki evidence is one guest's retrospective description. It does not independently verify dataset composition, duration distribution, contamination controls, scoring validity, model rankings, adoption, or whether long-video scores predict real user outcomes.

## What Changed
- Added Video-MME as a bounded project profile and benchmark-design example.

## Relationships
- [[LiLeiXiaomiMiMo|李磊]] - interview guest who uses the benchmark as his design example.
- [[BenchmarkAdoptionDesign]] - framework describing why a scientifically meaningful benchmark also needs low-friction adoption.
- [[AgentEvaluationBenchmarks]] - adjacent evaluation branch with different task and safety concerns.
- [[AIResearchFeedbackCompression]] - evaluation can shorten experiment cycles when results are reproducible and operationally easy to obtain.
