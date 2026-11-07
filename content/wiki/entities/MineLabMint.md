---
title: "Mint (MineLab)"
type: entity
knowledge_schema: synthesis-v1
tags: [ai, lora, model-training]
sources:
  - lkbt2upqw6eoxm0yjc1zklr8wlgc-lkbt2upqw6eoxm0yjc1zklr8wlgc
last_updated: 2026-11-08
---

# Mint (MineLab)

## Overview
Mint is the LoRA-centered model-training service attributed to [[MineLab]] in the supplied interview.

## Current Profile
Mint emerged from MineLab's attempt to train large models with limited H800 capacity. The source says the team found that LoRA could approach full fine-tuning on many tasks, then explored scaling base-model size, lowering adapter cost, and increasing the number of coexisting adapters.

## Key Characteristics
- LoRA-based post-training service.
- Originated as a compute-constrained training approach.
- Targets low-cost specialization on shared foundation models.
- Explores serving many adapters with different capabilities and behavior.

## Evidence
### Training route
- [[lkbt2upqw6eoxm0yjc1zklr8wlgc-lkbt2upqw6eoxm0yjc1zklr8wlgc]] says the team adopted LoRA on a small H800 cluster and later organized the resulting work as Mint.

### Scaling direction
- [[lkbt2upqw6eoxm0yjc1zklr8wlgc-lkbt2upqw6eoxm0yjc1zklr8wlgc]] names base-model scale, adapter cost, and adapter count as the three scaling axes.

## Qualifications
- The source does not provide independent benchmarks, customer results, architecture details, or production serving scale.
- “Approaches full training” is task-dependent and remains a company-reported generalization.
- The generic product name is disambiguated as MineLab Mint in the canonical page key.

## What Changed
- Established Mint as MineLab's LoRA-based post-training and multi-adapter service.

## Relationships
- [[MineLab]] - company developing the service.
- [[MaXiaoteng|Ma Xiaoteng / 马肖腾]] - source speaker describing the service.
- [[LowRankAdapterModelDiversity]] - model-society thesis enabled by many adapters.
- [[QLoRA]] - adjacent parameter-efficient training method.
- [[ModelPostTrainingBottleneck]] - broader data, evaluation, and iteration constraint Mint still faces.
