---
title: "Liber AI"
type: entity
tags: [company, physical-ai, robotics, world-action-models]
sources:
  - 187-duihua-liberai-liu-songming-astra-lai-xi-00-hou-wuli-ai-chuangshiren-kandao-de-shenglv-ad3b421a
last_updated: 2026-11-13
knowledge_schema: synthesis-v1
---

# Liber AI

## Overview
Liber AI is a physical-AI startup founded by [[LiuSongming|刘松明]] that develops action models, data-collection systems, robot hardware integration, motion control, and scene deployments.

## Current Profile
The company positions itself neither as a pure world-model laboratory nor as a conventional robot integrator. Its strategy is selective vertical integration: own the model-relevant links from action data and collection hardware through policy, embodiment, control, and field feedback, while relying on suppliers for mature components that do not determine model performance. It expects general foundation models to become strong at semantic understanding and planning, leaving contact-rich execution, low-latency control, physical feedback, reliable hardware, and delivery as the harder specialization boundary.

Liber AI reports a three-stage world-action-model pretraining program using internet, egocentric, glove, real-robot, and cross-embodiment data. Its commercial plan remains exploratory: retail and service POCs should reveal infrastructure and data requirements before the company commits to a repeatable application.

## Key Characteristics
- Selective full-stack coverage across models, data, collection devices, robot bodies, control, sensing, deployment, and scene feedback.
- A layered product thesis in which general models can supply more System 2 planning while Liber AI focuses on System 1 action and System 0 control.
- Human-data pretraining connected to robot execution through glove data, real-robot teleoperation, and embodiment-conditioned policies.
- Hardware design chosen for model transfer and physical performance rather than complete component self-sufficiency.
- A commercialization target of one repeatable, revenue-producing scenario within two to three years, without a final scene selected yet.
- Capital allocation centered on comparative scaling efficiency, technical leadership, and multi-year financing resilience.

## Evidence
- Strategy and architecture: [[187-duihua-liberai-liu-songming-astra-lai-xi-00-hou-wuli-ai-chuangshiren-kandao-de-shenglv-ad3b421a]] describes the System 2/System 1/System 0 split, the cooperation thesis for general models, and the company's selective full-stack route.
- Data and model: [[187-duihua-liberai-liu-songming-astra-lai-xi-00-hou-wuli-ai-chuangshiren-kandao-de-shenglv-ad3b421a]] reports the mixed 2.2-million-hour corpus, three pretraining stages, glove-data ablations, cross-embodiment conditioning, and zero-shot tests.
- Hardware and deployment: [[187-duihua-liberai-liu-songming-astra-lai-xi-00-hou-wuli-ai-chuangshiren-kandao-de-shenglv-ad3b421a]] connects body configuration, sensors, motors, control, tactile limits, beverage-service POCs, and the two-to-three-year commercial target.
- Organization and finance: [[187-duihua-liberai-liu-songming-astra-lai-xi-00-hou-wuli-ai-chuangshiren-kandao-de-shenglv-ad3b421a]] attributes technical-first resource allocation, fundraising reserves, hiring priority, and three-to-five-year cycle planning to the founder.

## Qualifications
The supplied source is a founder interview summarized by the episode producer, not an independent technical audit. Training scale, success rates, data-substitution efficiency, hardware comparisons, commercial readiness, funding position, and competitive claims remain attributed to Liber AI. The company has not yet demonstrated in this source a fully autonomous, repeatable, profitable deployment.

## What Changed
- Created the entity around Liber AI's selective full-stack physical-AI strategy.
- Separated the company's reported model and data results from its still-open commercial-scene choice.
- Preserved tactile sensing, reinforcement learning, hardware reliability, and deployment economics as unresolved constraints.

## Relationships
- [[LiuSongming]] - founder and final decision-maker.
- [[RDT1B]] - pre-company research lineage supporting the pretraining thesis.
- [[WorldActionModels]] - model family used for Liber AI's action-conditioned policy route.
- [[PhysicalIntelligenceSystemStack]] - system-level architecture the company is attempting to integrate selectively.
- [[UMIGloveDataCollection]] - lower-cost human-action data bridge in the reported training mixture.
- [[Kimi]] - prospective foundation-model collaborator for hardware development and virtual-to-physical workflows.
