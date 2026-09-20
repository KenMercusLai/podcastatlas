---
title: "Fine-Tuning Example Signal Amplification"
type: concept
knowledge_schema: synthesis-v1
tags: [ai, fine-tuning, data, alignment]
sources:
  - tech-20260915-tech-pod-128-tech-20260915-tech-pod-128
last_updated: 2026-09-21
---

# Fine-Tuning Example Signal Amplification

## Definition
Fine-tuning example signal amplification is the failure mode where an incidental pattern in a small or repeatedly reused post-training dataset becomes a disproportionately strong behavioral cue.

## Current Synthesis
The Marketplace Tech source illustrates the mechanism through personality customization. Examples intended to convey abstract traits such as playful or nerdy behavior included goblin references, and the model reportedly learned the concrete recurring feature more strongly than designers intended. A small, labor-intensive pool of human-labeled examples made that accidental signal harder to dilute.

The concept qualifies a simple account of [[SupervisedFineTuning]] as direct instruction following. Example-based post-training teaches through correlations inside the entire example, so behavior can move toward surface details that are easier for the model to imitate than the designer's unstated abstraction.

## Key Claims
- Fine-tuning examples communicate incidental details as well as intended labels, styles, or personality traits.
- Small datasets make a few repeated examples more capable of shaping visible behavior.
- Reusing older human-labeled datasets can carry historical quirks into newer model versions.
- A model can faithfully imitate the strongest available example signal while still missing the designer's intended abstraction.
- Visible oddities can therefore be evidence of misweighted training signals rather than independent model intent.

## Evidence
### Personality-example signal
- [[tech-20260915-tech-pod-128-tech-20260915-tech-pod-128]] says examples for a playful, nerdy personality contained goblin references that the model could interpret as the behavior to reproduce.

### Dataset-size bottleneck
- [[tech-20260915-tech-pod-128-tech-20260915-tech-pod-128]] says the human-labeling process was costly, the available fine-tuning dataset was relatively small, and a few goblin examples became overemphasized.

### Cross-version persistence
- [[tech-20260915-tech-pod-128-tech-20260915-tech-pod-128]] describes the examples as coming from an earlier dataset, supporting a source-scoped risk that reused post-training data can reintroduce old quirks.

## Counterevidence & Qualifications
- The source does not provide the dataset, example counts, training recipe, model version, ablation study, or provider postmortem needed to quantify the mechanism.
- It does not establish that small datasets always amplify incidental signals or that fine-tuning was the only cause of the reported behavior.
- The explanation is a useful hypothesis from a public interview, not direct evidence about model weights or internal representations.

## What Changed
- Created a canonical concept for the goblin case's small-data and incidental-example mechanism.

## Related Concepts
- [[SupervisedFineTuning]] - post-training method through which curated examples can shape behavior.
- [[ModelValueEmbedding]] - broader process by which training and product choices enter model outputs.
- [[BehavioralAlignmentPatching]] - downstream response when amplified signals create unwanted visible behavior.
- [[AIModelBiasGovernance]] - governance frame for unintended patterns learned from training data.
- [[ChatbotDomainBleedthrough]] - adjacent case where learned associations cross an intended behavior boundary.
