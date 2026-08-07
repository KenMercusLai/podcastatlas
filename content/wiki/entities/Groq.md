---
title: "Groq"
type: entity
tags: [company, ai, semiconductors, inference]
sources: [e230-1-wan-yi-shouru-yuqi-beihou-yingweida-de-dianfeng-yu-ruanlei-d97446f1-d6e3-4894-89d1-dca0a362b10b, e228-guge-tpu-neng-handong-yingweida-ma-qian-tpu-gongchengshi-shouci-jiemi-fd17090c-0d72-4c0d-aa3e-9b00bc062149]
last_updated: 2026-08-07
---
# Groq

Groq appears in [[e230-1-wan-yi-shouru-yuqi-beihou-yingweida-de-dianfeng-yu-ruanlei-d97446f1-d6e3-4894-89d1-dca0a362b10b]] as the reference example for LPU-style [[LowLatencyInferenceChip|low-latency inference chips]]. The episode highlights the SRAM-heavy design pattern: keeping more data on chip can reduce repeated memory movement and improve response latency for some agentic workloads.

The source does not present Groq as a general [[Nvidia]] replacement. It uses the company to explain where [[AIChipSpecialization]] can still matter: low latency, communication-energy reduction, and specialized inference paths, especially when general GPU clusters are powerful but not always optimized for every workload.

[[e228-guge-tpu-neng-handong-yingweida-ma-qian-tpu-gongchengshi-shouci-jiemi-fd17090c-0d72-4c0d-aa3e-9b00bc062149]] adds a clearer contrast with [[TPU]]. [[HenryTPUEngineer|Henry]] frames Groq as compiler-centered and inference-only, suited to low-latency uses such as agents, realtime voice, and high-frequency settings. That contrasts with [[HighThroughputInferenceBatching|TPU-favorable]] cloud workloads where many requests can be batched across a large system.

## Connections
- [[LowLatencyInferenceChip]] and [[AIChipSpecialization]] - technical category and specialization frame.
- [[Nvidia]], [[GPU]], and [[AIInfrastructureFullStackMoat]] - incumbent comparison.
- [[InferenceAsCashFlow]], [[MemoryWall]], and [[AIInferenceCostStructure]] - demand and data-movement context.
- [[HighThroughputInferenceBatching]], [[TPU]], and [[XLACompiler]] — E228's high-throughput versus low-latency inference split.
