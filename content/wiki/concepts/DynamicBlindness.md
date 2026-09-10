---
title: "Dynamic Blindness"
type: concept
tags: [ai, llm, evaluation, enterprise-ai]
sources:
  - ep-41-the-reward-signal-the-missing-ingredient-in-every-ai-system-youve-built
last_updated: 2026-09-10
knowledge_schema: synthesis-v1
---

# Dynamic Blindness

## Definition
Dynamic blindness is the LLM failure mode described in [[ep-41-the-reward-signal-the-missing-ingredient-in-every-ai-system-youve-built]] where a model can make a locally plausible move while failing to account for downstream system consequences.

## Current Synthesis
The episode uses dynamic blindness to explain why prompt quality and local answer quality are insufficient for enterprise AI systems. A model that lacks state, feedback, and outcome awareness can satisfy the immediate request while damaging the broader workflow, which makes reward-signal and control-layer design part of reliability rather than a later optimization detail.

## Key Claims
- Dynamic blindness is a system-level failure, not merely a single bad answer.
- Stateless LLM behavior can miss how one response changes cumulative outcomes.
- Prompt engineering alone is unlikely to solve the failure mode if the architecture lacks feedback and outcome awareness.
- Reward signals, memory, RAG, knowledge graphs, or orchestration layers can reduce but not automatically eliminate the problem.

## Evidence
Failure framing:
- [[ep-41-the-reward-signal-the-missing-ingredient-in-every-ai-system-youve-built]] references ServiceNow's "dynamic blindness" as an example of LLMs doing something locally reasonable while breaking downstream outcomes.

Architecture explanation:
- [[ep-41-the-reward-signal-the-missing-ingredient-in-every-ai-system-youve-built]] has Liss connect dynamic blindness to missing reward signals, stateless generation, and lack of system-level outcome awareness.

Design implication:
- [[ep-41-the-reward-signal-the-missing-ingredient-in-every-ai-system-youve-built]] links the failure mode to the need for feedback loops, state, and governed control structures.

## Counterevidence & Qualifications
The ServiceNow reference is not independently ingested here, and the episode does not provide a benchmark taxonomy for dynamic blindness. The term should remain tied to this source until primary evidence is added.

## What Changed
- Added dynamic blindness as an enterprise LLM reliability failure mode connected to missing reward signals.

## Related Concepts
- [[ScenarioLevelRewardSignal]] - feedback mechanism proposed as a response to system-level blindness.
- [[ExperienceOrchestrator]] - control-layer response when models lack system-level awareness.
- [[AIVerification]] - evaluation boundary for checking downstream effects.
- [[RetrievalAugmentedGeneration]] - knowledge-grounding layer that helps context but does not by itself supply outcome awareness.
