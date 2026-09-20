---
title: "HanaPino"
type: entity
tags: [product, ai, semiconductors, inference]
knowledge_schema: synthesis-v1
sources:
  - e251-tuili-xinpian-zhi-zhan-liaoliao-groq-cerebras-yu-openai-sanda-lujing-yu-bill-dally-de-sheji-zhexue-786d63c4-d46c-4ff3-80f8-fc895b2a57f0
last_updated: 2026-09-20
---

# HanaPino

## Overview
HanaPino is the source-named [[OpenAI]] and [[Broadcom]] inference chip discussed in [[e251-tuili-xinpian-zhi-zhan-liaoliao-groq-cerebras-yu-openai-sanda-lujing-yu-bill-dally-de-sheji-zhexue-786d63c4-d46c-4ff3-80f8-fc895b2a57f0|E251]]. The episode presents it as a relatively general inference accelerator that retains [[HighBandwidthMemory|HBM]] and integrates different workload-specific blocks on one die.

## Current Profile
The chip is framed as a power-first alternative to SRAM-heavy, system-level heterogeneity. It is said to cover prefill and decode, attention and feed-forward work, and small matrix multiplication while power-gating unused blocks as "dark silicon." That choice can raise silicon cost but increase tokens produced within a fixed electricity envelope.

## Key Characteristics
- Uses HBM rather than storing the full fixed model-weight working set in distributed SRAM.
- Places heterogeneous compute functions inside one chip instead of assigning them to separate chip types.
- Supports small-dimension matrix multiplication to improve small-batch inference behavior.
- Uses selective power gating or reduced activity in unused regions to prioritize energy efficiency.
- Is described as a general inference path with future training support, not a narrow decode-only accelerator.

## Evidence
- Architecture and workload breadth: [[e251-tuili-xinpian-zhi-zhan-liaoliao-groq-cerebras-yu-openai-sanda-lujing-yu-bill-dally-de-sheji-zhexue-786d63c4-d46c-4ff3-80f8-fc895b2a57f0|E251]] says HanaPino covers multiple inference phases and even demonstrated non-LLM workloads.
- Memory and power tradeoff: [[e251-tuili-xinpian-zhi-zhan-liaoliao-groq-cerebras-yu-openai-sanda-lujing-yu-bill-dally-de-sheji-zhexue-786d63c4-d46c-4ff3-80f8-fc895b2a57f0|E251]] contrasts its HBM4 bandwidth and on-chip heterogeneity with SRAM-heavy multi-chip systems.
- Software path: [[e251-tuili-xinpian-zhi-zhan-liaoliao-groq-cerebras-yu-openai-sanda-lujing-yu-bill-dally-de-sheji-zhexue-786d63c4-d46c-4ff3-80f8-fc895b2a57f0|E251]] says kernels are written in a Wulong language and that [[Codex]] helped automate optimization.

## Qualifications
The page reflects one podcast's reading of public materials and a Hot Chips presentation. Launch date, nine-month development cycle, HBM bandwidth, Rubin comparison, Wulong/Codex workflow, and future training support have not been independently verified here and remain source-scoped.

## What Changed
- Established the first canonical profile for HanaPino.
- Positioned the chip as a power-constrained, on-chip-heterogeneous counterpoint to SRAM-heavy inference systems.

## Relationships
- [[OpenAI]] - model company identified by the source as the chip's developer and intended user.
- [[Broadcom]] - implementation partner named in the source.
- [[HighBandwidthMemory]] - memory technology retained to provide capacity and bandwidth.
- [[InferenceDecodeBandwidth]] - decode bottleneck addressed through HBM bandwidth and workload-specific blocks.
- [[AIChipSpecialization]] - specialization case that preserves broader workload coverage than a decode-only design.
