---
title: "LM Studio"
type: entity
knowledge_schema: synthesis-v1
tags: [ai, local-ai, model-serving]
sources:
  - ep-38-the-local-ai-stack-nobody-talks-about-but-should
last_updated: 2026-09-13
---

# LM Studio

## Overview
LM Studio is a local AI application discussed in [[ep-38-the-local-ai-stack-nobody-talks-about-but-should]] between easy local-model use and more technical serving infrastructure.

## Current Profile
The source positions LM Studio as a more configurable local-model option than [[Ollama]], especially when users want to choose quantization and parameters more directly. It still sits closer to practitioner workstation use than to production inference infrastructure.

## Key Characteristics
- Local-model application for users who want more control than Ollama.
- Requires more attention to quantization and parameters in the source.
- Sits in the middle of the convenience-control tradeoff.

## Evidence
### Configuration burden
- [[ep-38-the-local-ai-stack-nobody-talks-about-but-should]] says Rossiter uses LM Studio and that it requires more attention to quantization and parameters.

### Framework comparison
- [[ep-38-the-local-ai-stack-nobody-talks-about-but-should]] contrasts LM Studio with [[Ollama]] for ease and [[VLLM|vLLM]] for inference performance.

## Qualifications
- The source does not provide performance numbers or a product feature audit.
- LM Studio's role here is source-scoped to local AI experimentation and setup.

## What Changed
- Created LM Studio as a configurable local-model tool in the wiki.

## Relationships
- [[LocalAIFrameworkStack]] - local framework tradeoff it helps define.
- [[Ollama]] - easier entry comparison.
- [[VLLM|vLLM]] - more complex serving-performance comparison.
