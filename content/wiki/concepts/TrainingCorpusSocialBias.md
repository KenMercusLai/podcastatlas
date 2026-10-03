---
title: "Training-Corpus Social Bias"
type: concept
tags: [ai, training-data, bias, natural-language-processing]
sources:
  - ep174-yiqing-xia-de-kuaguo-zhilu-ckwrimaeijawabaaaacyyipn
last_updated: 2026-10-03
knowledge_schema: synthesis-v1
---

# Training-Corpus Social Bias

## Definition
Training-corpus social bias is the reproduction of unequal social associations and distorted event frequencies when a language model learns statistical relationships from human-produced text.

## Current Synthesis
[[ep174-yiqing-xia-de-kuaguo-zhilu-ckwrimaeijawabaaaacyyipn|EP174]] distinguishes two problems. Associational bias links groups to roles or traits—for example women with assistants, men with leaders, or Black people with violent crime. Reporting bias means the frequency of a phrase in text reflects what people choose to record, not the frequency of the underlying event: killing may appear more often than breathing even though breathing is vastly more common.

The synthesis therefore resists treating data cleaning as the discovery of a neutral corpus. Filtering, committee review, evaluation, and governance can reduce harms, but the target itself requires normative judgment about which associations are unjust, which frequencies are artifacts of reporting, and which real inequalities a model should describe without reproducing as prescription.

## Key Claims
- Models can inherit social associations from existing text without an explicit discriminatory rule.
- Textual co-occurrence is not a neutral map of society because publication and reporting select unusual, salient, or conflict-rich events.
- Removing obvious slurs does not solve role, race, religion, or frequency distortions embedded in ordinary language.
- Mitigation requires technical evaluation plus normative and domain judgment about desired behavior.
- A corpus cannot be assumed unbiased merely because it is large or naturally occurring.

## Evidence
- Social association: [[ep174-yiqing-xia-de-kuaguo-zhilu-ckwrimaeijawabaaaacyyipn|EP174]] gives gender-role and race-crime examples of learned word relationships.
- Reporting-frequency distortion: [[ep174-yiqing-xia-de-kuaguo-zhilu-ckwrimaeijawabaaaacyyipn|EP174]] contrasts the textual prominence of killing with the real-world prevalence of breathing.
- Mitigation boundary: [[ep174-yiqing-xia-de-kuaguo-zhilu-ckwrimaeijawabaaaacyyipn|EP174]] mentions cleaner-data filtering and ethics committees while acknowledging that complete neutrality is unavailable.

## Counterevidence & Qualifications
The episode provides illustrative examples but no named model, corpus, metric, benchmark, effect size, or mitigation result. The race-crime example is presented as a possible learned association, not a documented audit finding in the source. Describing a statistical association is also distinct from endorsing it, and not every observed disparity originates in training data.

## What Changed
- Initial synthesis created around the distinction between social association and reporting-frequency bias.

## Related Concepts
- [[AIModelBiasGovernance]] - broader organizational practice for detecting and governing unfair model behavior.
- [[LanguageDependentAIBias]] - shows how corpus history and filtering can vary across languages.
- [[PublicationBias]] - adjacent selection problem in which recorded evidence differs from the full underlying event set.
- [[CulturalBiasInTesting]] - evaluation-side risk when the test itself encodes narrow assumptions.
- [[RepresentationLearning]] - technical process through which patterns in data become operational features.
