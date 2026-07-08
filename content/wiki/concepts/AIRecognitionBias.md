---
title: "AI Recognition Bias"
type: concept
tags: [ai, computer-vision, bias]
sources: [ganguan-fangda-shijie-he-renning-liao-guanniao-ziran-yu-ziyou-e583dac2-bad8-4208-8d35-0c3de8594779]
last_updated: 2026-07-09
---

# AI Recognition Bias

AI recognition bias is the failure mode where a classifier appears to recognize the intended object but is partly relying on irrelevant training signals. In [[ganguan-fangda-shijie-he-renning-liao-guanniao-ziran-yu-ziyou-e583dac2-bad8-4208-8d35-0c3de8594779]], [[RenNing]] describes this through bird-recognition tools such as [[Dongniao]]: rare bird photos are scarce, so a model may learn photographer, camera, or background patterns instead of the bird traits humans care about.

The concept is a concrete computer-vision version of [[HumanJudgmentUnderAI]]. AI can accelerate identification, but field knowledge and evidence still matter when records are rare, images are ambiguous, or downstream data will enter [[CitizenScience]] records.

## Key Claims
- Sparse rare-class data makes models more likely to learn spurious correlations.
- The model's high confidence does not prove it used the same traits a domain expert would use.
- Training data can encode photographer behavior, location bias, camera artifacts, and background conditions.
- Recognition tools should support field observation and verification rather than replace them.

## Connections
- [[Dongniao]] - source tool example.
- [[BirdwatchingAsAttention]] - human observational practice that model output should support.
- [[CitizenScience]] - data quality matters when identifications become shared records.
- [[HumanJudgmentUnderAI]] - broader verification and responsibility frame.
- [[RepresentationLearning]] - adjacent machine-learning concept about learned abstractions.
