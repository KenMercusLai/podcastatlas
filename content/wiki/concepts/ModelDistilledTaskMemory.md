---
title: "Model-Distilled Task Memory / 模型蒸馏式任务记忆"
type: concept
tags: [models, agents, distillation, memory]
sources:
  - ljfjtmoafzywi-agbwi1wzpghcax-ljfjtmoafzywi-agbwi1wzpghcax
last_updated: 2026-11-15
knowledge_schema: synthesis-v1
---

# Model-Distilled Task Memory / 模型蒸馏式任务记忆

## Definition
Model-distilled task memory is the conversion of a frontier model's successful task trajectory—tool calls, intermediate choices, result, and user preference—into a smaller or cheaper model that can reproduce a recurring task with less deliberation.

## Current Synthesis
The source frames task memory as a System 2-to-System 1 transition. A strong model solves a new problem through expensive reasoning; repeated validated trajectories then train a routing model to choose tools and paths quickly, including among several acceptable routes according to user preference. This differs from storing a static workflow because the learned routine can generalize within its training scope, but it is also less transparent and deterministic.

The useful hybrid is therefore not “model instead of controls.” Frontier reasoning, distilled recurrence, caching, deterministic checks, and escalation can occupy different layers. The smaller model should handle stable, well-evaluated work while novel, consequential, or drifting cases return to stronger reasoning and human review.

## Key Claims
- First-time complex work and repeated stable work can use different model and cost profiles.
- Tool trajectories and user preferences can become training signals for task-routing models.
- Distillation may preserve flexible task reproduction better than a fully fixed workflow within a bounded domain.
- Small-model recurrence can reduce latency and inference cost only if evaluation catches drift and failure.
- Enterprise-specific models can encode operational knowledge, but model parameters do not automatically provide provenance, deletion, or auditability.

## Evidence
- **Task-routing model:** [[ljfjtmoafzywi-agbwi1wzpghcax-ljfjtmoafzywi-agbwi1wzpghcax]] says AFK records frontier-model tool use, results, and preferences to train cheaper task reproduction.
- **“Muscle memory” analogy:** [[ljfjtmoafzywi-agbwi1wzpghcax-ljfjtmoafzywi-agbwi1wzpghcax]] compares repeated execution with a conditioned response after initial cortical reasoning.
- **Internal work model:** [[ljfjtmoafzywi-agbwi1wzpghcax-ljfjtmoafzywi-agbwi1wzpghcax]] describes a roughly 20B–40B enterprise model for operating systems, dynamic software, and company-specific work.

## Counterevidence & Qualifications
The source supplies no benchmark, training recipe, customer data, or comparison against prompt caching, skills, deterministic automation, retrieval, or ordinary fine-tuning. Distilled trajectories can reproduce hidden errors, lose provenance, become stale, or generalize outside their valid scope. Model size, cost, security, and performance claims remain founder-reported.

## What Changed
- Created the concept to separate model-level recurrent task learning from static workflow storage and general agent memory.

## Related Concepts
- [[OrganizationalAgentLearning]] - company-wide source of repeated trajectories and validation signals.
- [[AgentSelfEvolution]] - broader improvement loop involving skills, memory, and harness feedback.
- [[ModelRoutingCostControl]] - routes work by capability, price, latency, and risk.
- [[TopModelBuildRuntimeSplit]] - adjacent separation between frontier-model construction and cheaper production execution.
- [[PersistentAgentMemory]] - explicit retained context rather than behavior compressed into model parameters.
- [[AIVerification]] - acceptance layer needed before and after task distillation.
