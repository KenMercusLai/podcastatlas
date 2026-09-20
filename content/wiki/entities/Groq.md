---
title: "Groq"
type: entity
tags: [company, ai, semiconductors, inference]
knowledge_schema: synthesis-v1
sources:
  - e230-1-wan-yi-shouru-yuqi-beihou-yingweida-de-dianfeng-yu-ruanlei-d97446f1-d6e3-4894-89d1-dca0a362b10b
  - e228-guge-tpu-neng-handong-yingweida-ma-qian-tpu-gongchengshi-shouci-jiemi-fd17090c-0d72-4c0d-aa3e-9b00bc062149
  - e251-tuili-xinpian-zhi-zhan-liaoliao-groq-cerebras-yu-openai-sanda-lujing-yu-bill-dally-de-sheji-zhexue-786d63c4-d46c-4ff3-80f8-fc895b2a57f0
last_updated: 2026-09-20
---

# Groq

## Overview
Groq is an inference-chip company used across the sources as the leading example of SRAM-heavy, compiler-centered, deterministic low-latency specialization. Its architecture moves much scheduling work before runtime and keeps data close to compute, trading generality and capacity for predictable execution and fast token delivery.

## Current Profile
The current profile is technically differentiated but workload-bounded. Earlier sources position Groq as a low-latency complement rather than a universal [[Nvidia]] or [[TPU]] replacement. [[e251-tuili-xinpian-zhi-zhan-liaoliao-groq-cerebras-yu-openai-sanda-lujing-yu-bill-dally-de-sheji-zhexue-786d63c4-d46c-4ff3-80f8-fc895b2a57f0|E251]] explains the mechanism more precisely: compiler-time schedules and on-chip SRAM reduce runtime uncertainty and memory movement, while dynamic [[MixtureOfExperts|MoE]] routing can force over-communication or idle hardware. The episode also reports a late-2025 Nvidia acquisition and interprets it as a route for adding a bandwidth-oriented architecture outside the mature GPU product path.

## Key Characteristics
- Uses an SRAM-heavy design to bring model data close to compute and reduce memory-access variability.
- Centers hardware design on deterministic, ahead-of-time compiler scheduling.
- Targets latency-sensitive inference such as agents, real-time voice, and serial model-call workflows.
- Faces efficiency pressure when runtime-dependent workloads such as MoE do not fit static schedules cleanly.
- Competes at system and software level, not through isolated chip specifications alone.

## Evidence
- Low-latency niche: [[e230-1-wan-yi-shouru-yuqi-beihou-yingweida-de-dianfeng-yu-ruanlei-d97446f1-d6e3-4894-89d1-dca0a362b10b|E230]] uses Groq to show where communication-efficient inference can matter despite Nvidia's full-stack moat.
- Market segmentation: [[e228-guge-tpu-neng-handong-yingweida-ma-qian-tpu-gongchengshi-shouci-jiemi-fd17090c-0d72-4c0d-aa3e-9b00bc062149|E228]] contrasts Groq's single-user latency orientation with TPU-favorable, high-throughput batching.
- Architecture and qualification: [[e251-tuili-xinpian-zhi-zhan-liaoliao-groq-cerebras-yu-openai-sanda-lujing-yu-bill-dally-de-sheji-zhexue-786d63c4-d46c-4ff3-80f8-fc895b2a57f0|E251]] connects deterministic SRAM execution to decode bandwidth and explains the mismatch between static schedules and dynamic expert routing.

## Qualifications
The sources do not provide independently comparable cost, latency, utilization, or energy benchmarks. Groq's advantage depends on model shape, batching, interconnect, compiler quality, and acceptable idle capacity. The reported Nvidia acquisition, its price, and its strategic rationale remain source-scoped rather than independently verified here.

## What Changed
- Migrated the page to the synthesis-v1 entity schema.
- Added the deterministic compiler and SRAM mechanism behind the low-latency profile.
- Added MoE runtime routing as a concrete qualification and the reported acquisition as source-scoped context.

## Relationships
- [[LowLatencyInferenceChip]] - chip category for Groq's latency-oriented specialization.
- [[InferenceDecodeBandwidth]] - data-movement bottleneck its SRAM and scheduling choices target.
- [[MixtureOfExperts]] - dynamic workload pattern that strains static schedules.
- [[Nvidia]] - incumbent and reported acquirer in the newest source.
- [[TPU]] - high-throughput specialized accelerator contrasted with Groq's latency niche.
- [[AIChipSpecialization]] - broader tradeoff between workload fit and flexibility.
