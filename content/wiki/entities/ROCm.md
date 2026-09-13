---
title: "ROCm"
type: entity
knowledge_schema: synthesis-v1
tags: [ai, hardware, software-stack]
sources:
  - ep-38-the-local-ai-stack-nobody-talks-about-but-should
last_updated: 2026-09-13
---

# ROCm

## Overview
ROCm is the AMD-associated accelerator software stack named in [[ep-38-the-local-ai-stack-nobody-talks-about-but-should]].

## Current Profile
The source uses ROCm as one of the three local AI hardware-framework branches: [[CUDA]] for Nvidia, ROCm for [[AMD]], and [[AppleMetal|Metal]] for Apple. Its role is to show that local AI hardware selection includes software compatibility and ecosystem support.

## Key Characteristics
- AMD-side accelerator framework in the episode's comparison.
- Contrasted with [[CUDA]] and [[AppleMetal|Metal]].
- Relevant because model-serving tools and enterprise environments may support stacks unevenly.

## Evidence
### Framework comparison
- [[ep-38-the-local-ai-stack-nobody-talks-about-but-should]] names ROCm as AMD's hardware-level framework.

### Compatibility implication
- [[ep-38-the-local-ai-stack-nobody-talks-about-but-should]] explains Rossiter's [[NvidiaDGXSpark]] choice partly through alignment with client Nvidia/CUDA environments, making ROCm part of the alternative-stack comparison.

## Qualifications
- The source does not analyze ROCm maturity, supported devices, or model-framework coverage.
- This is a source-scoped stack anchor, not full ROCm documentation.

## What Changed
- Created ROCm as the AMD software-stack comparison point for local AI.

## Relationships
- [[AMD]] - associated hardware vendor.
- [[CUDA]] - Nvidia stack comparison.
- [[AppleMetal]] - Apple stack comparison.
- [[LocalAIHardwareSelection]] - compatibility dimension it informs.
