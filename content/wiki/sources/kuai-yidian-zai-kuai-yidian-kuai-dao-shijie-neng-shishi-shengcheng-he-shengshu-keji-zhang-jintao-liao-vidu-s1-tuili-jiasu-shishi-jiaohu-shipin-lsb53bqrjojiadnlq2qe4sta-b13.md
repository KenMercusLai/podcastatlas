---
title: "快一点！再快一点！快到世界能实时生成｜和生数科技张金涛聊：Vidu S1、推理加速、实时交互视频"
type: source
tags: [podcast, ai, video, inference]
sources: []
date: 2026-07-19
source_file: "/home/ken/repos/podcastatlas/content/episodes/快一点！再快一点！快到世界能实时生成｜和生数科技张金涛聊：Vidu S1、推理加速、实时交互视频 [lsB53BqRjojiaDNLQ2QE4StA_B13].md"
source_url: "https://www.xiaoyuzhoufm.com/episode/6a5c6a91a3fec224d59fd014"
last_updated: 2026-08-07
---

## Summary
This [[ShizilukouCrossing]] episode interviews [[ZhangJintao]] of [[ShengshuTechnology]] about [[ViduS1]], [[RealTimeInteractiveVideoGeneration]], and the engineering work needed to make video generation faster than playback. The source argues that real-time visual generation is not just a bigger-hardware problem: [[SageAttention]], [[TurboDiffusion]], model distillation, sparse attention, cluster scheduling, and hardware-algorithm co-design all sit inside an [[InferenceAccelerationStack]]. Its product synthesis is that streaming, interactive video moves [[VideoModels]] from offline clip generation toward live sessions where characters must understand voice, video, screens, and user intent while preserving speed, identity, and coherence.

## Key Claims
- [[ZhangJintao]] is described as a 26-year-old [[TsinghuaUniversity|Tsinghua University]] doctoral student who had previously done inference-acceleration research and visited [[UCBerkeley|UC Berkeley]].
- At [[ShengshuTechnology]], Zhang is said to work on [[ViduS1]], inference acceleration, cluster deployment, and the full [[StreamingVideoGeneration]] chain from data and training algorithms to engineering and evaluation.
- [[ViduS1]] is presented as a live interactive product: a user can upload a character image, choose or clone a voice, and talk to the character through voice while the generated video responds in real time.
- The source-scoped performance claim is that S1 can stream long-form generation at 540P and roughly 25 to 42 FPS, with the team prioritizing latency and responsiveness before maximum image quality.
- [[SageAttention]] is described as a faster Attention operator that matters more for multimodal and video generation because those workloads can be compute-bound rather than only memory-bound.
- [[TurboDiffusion]] is presented as a model-level acceleration project that combines faster operators with distillation and sparse-attention fine-tuning to reduce diffusion-model complexity.
- Zhang divides inference acceleration into operator acceleration, model-complexity reduction, and engineering/deployment optimization, including multi-card parallelism, communication-compute overlap, request scheduling, and large-cluster deployment.
- The source distinguishes [[StreamingVideoGeneration]] from ordinary offline video generation: every frame must be produced in time, quality must not drift over long sessions, and input feedback must remain correct.
- Zhang frames online visual entertainment as a larger long-term demand category than pre-generated clips, with possible scenes including conversation, romance, games, pets, desktop assistance, and everyday companion experiences.
- The source attributes part of Chinese video-model strength to visual-entertainment data quantity, data quality, preference alignment, data construction, and ecosystems such as short video, livestream commerce, and social platforms.
- Zhang argues that AI is not merely a bubble because it can meet many human needs, but he also says technical strength alone does not make someone a good founder; management, coordination, and judgment matter.

## Key Quotes
> "生成速度必须超过播放速度" — Zhang's concise boundary for streaming video generation.

> "在线的、实时交互的视频" — the source's main product category distinction.

> "每一行代码都正确" — Zhang's engineering definition of world-leading execution.

## Connections
- [[ZhangJintao]], [[ShengshuTechnology]], [[Vidu]], and [[ViduS1]] — guest, company, model/product family, and real-time product case.
- [[SageAttention]], [[TurboDiffusion]], and [[InferenceAccelerationStack]] — technical acceleration thread.
- [[StreamingVideoGeneration]], [[RealTimeInteractiveVideoGeneration]], [[VideoModels]], and [[MultimodalIntelligence]] — model and interaction frame.
- [[AIInteractiveEntertainment]], [[AISimulationContent]], [[AIStartupUnitEconomics]], and [[ProductLedWillingnessToPay]] — user-demand and monetization frame for live visual sessions.
- [[AIInferenceCostStructure]], [[MaaSInfrastructure]], [[HighThroughputInferenceBatching]], [[LowLatencyInferenceChip]], and [[AIChipSpecialization]] — serving, scheduling, and hardware-software economics.
- [[GPU]], [[Nvidia]], AMD, [[Huawei]], [[ByteDance]], [[Tencent]], and [[Google]] — hardware and company context mentioned in the source's adoption and deployment discussion.
- [[TsinghuaUniversity]], [[UCBerkeley]], [[TransformerArchitecture]], [[MixtureOfExperts]], and [[DiffusionTransformers]] — research and architecture context.

## Contradictions
- No direct contradiction found. The source extends the existing [[VideoModels]] and [[WorldModels]] pages by separating offline video quality from real-time interactive continuity, while keeping S1's performance, price, and adoption claims source-scoped rather than independently verified.
