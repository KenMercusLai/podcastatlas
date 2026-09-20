---
title: "Janelle Shane"
type: entity
knowledge_schema: synthesis-v1
tags: [ai, author, science-communication]
sources:
  - tech-20260806-0806-mp-tech-pod-128-tech-20260806-0806-mp-tech-pod-128
  - tech-20260722-0722-mp-tech-pod-128-tech-20260722-0722-mp-tech-pod-128
  - tech-20260915-tech-pod-128-tech-20260915-tech-pod-128
last_updated: 2026-09-21
---

# Janelle Shane

## Overview
Janelle Shane is an AI author and science communicator associated with the [[AIWeirdnessBlog|AI Weirdness blog]]. In three [[MarketplaceTech]] "Uncanny AI" episodes, she interprets odd chatbot behavior as evidence of statistical association, imperfect salience, and fragile behavioral control rather than human-like intent.

## Current Profile
Shane's role across the bounded sources is to make model-behavior failures legible through concrete analogies. She separates memory from judgment when a chatbot resurfaces an irrelevant personal fact, separates fluent language from sealed domain boundaries when a model code-switches, and separates intended personality from learned example signals when a model becomes preoccupied with goblins.

Her explanations consistently support a cautious operational view: a plausible model-generated explanation is not proof of cause, accurate recall is not appropriate recall, and a prompt-level fix does not demonstrate that the underlying association has been removed. The newest source extends this stance into [[BehavioralAlignmentPatching]], [[FineTuningExampleSignalAmplification]], and [[AutomatedHiringProxyDiscrimination]].

## Key Characteristics
- Explains technical model behavior through accessible analogies without attributing human motives to the system.
- Treats fluent or correct output as compatible with poor domain boundaries, salience, or behavioral control.
- Distinguishes plausible explanations from verified causal accounts of model internals.
- Connects low-stakes AI oddities to higher-stakes privacy, safety, bias, and alignment risks.
- Emphasizes that training examples and human behavior can carry unintended associations into model outputs.

## Evidence
### Statistical and domain-boundary explanation
- [[tech-20260806-0806-mp-tech-pod-128-tech-20260806-0806-mp-tech-pod-128]] has Shane explain foreign-language slips through multilingual training data, probabilistic token prediction, and domains that are not cleanly walled off.

### Memory and social judgment
- [[tech-20260722-0722-mp-tech-pod-128-tech-20260722-0722-mp-tech-pod-128]] has Shane distinguish storing a personal detail from judging when it is relevant, proportionate, or sensitive to mention.

### Example signals and behavioral patching
- [[tech-20260915-tech-pod-128-tech-20260915-tech-pod-128]] has Shane explain goblin overuse through personality examples and small reused fine-tuning data, then connect patching to hidden side effects and human-bias replication.

## Qualifications
- These are public-facing explanations in short interviews, not provider-authored technical postmortems or direct inspections of model weights, prompts, and training datasets.
- Shane explicitly treats some causal explanations as plausible rather than confirmed when the relevant internal evidence is unavailable.
- The newest source's hiring examples describe a general discrimination mechanism without naming or auditing a particular deployed system.

## What Changed
- Added Shane's explanation of incidental example signals becoming over-weighted during personality tuning.
- Extended her profile from memory and language-boundary failures to behavioral alignment and proxy discrimination.
- Migrated the page to the synthesis-v1 entity schema.

## Relationships
- [[AIWeirdnessBlog]] - science-communication project through which Shane is identified.
- [[MarketplaceTech]] - interview venue for the bounded "Uncanny AI" episodes.
- [[MeganMcCartyCorino|Megan McCarty Carino]] - host who frames Shane's model-behavior explanations.
- [[ChatbotMemorySalienceFailure]] - failure mode Shane explains through remembered details used without proportion.
- [[ChatbotDomainBleedthrough]] - language and domain-boundary failure Shane explains through mixed training data.
- [[BehavioralAlignmentPatching]] - alignment-maintenance pattern Shane describes as repeated symptom-level repair.
- [[FineTuningExampleSignalAmplification]] - post-training mechanism used to explain the goblin case.
