---
title: "AI Model Censorship"
type: concept
tags: [ai, censorship, governance, china]
sources: [tech-20260804-0803-mp-tech-pod-128-tech-20260804-0803-mp-tech-pod-128, a-hawk-who-flew-on-political-winds-lindsey-graham-6a54b56575790d5f01515d55]
last_updated: 2026-08-08
---

# AI Model Censorship

[[tech-20260804-0803-mp-tech-pod-128-tech-20260804-0803-mp-tech-pod-128]] adds the open-weight mitigation question. [[AdamSiegel]] says censorship remains one U.S. concern around Chinese AI models, but downloaded open-weight models can be retrained or adapted by users who want different answer behavior. The episode therefore separates default model behavior from what downstream users can do once weights are available locally.

AI model censorship is the pattern in [[a-hawk-who-flew-on-political-winds-lindsey-graham-6a54b56575790d5f01515d55]] where models refuse, deflect, or give party-line answers on politically sensitive subjects. The episode's main case is Chinese models answering questions about Tibet, Taiwan, and Tiananmen, which the source calls the "three T's test."

The concept is not limited to one refusal message. The source says censorship can enter through post-training, where answers are rated as good or bad, and through language-specific training data drawn from a controlled internet. That links model censorship to [[LanguageDependentAIBias]] rather than treating it only as a visible safety filter.

## Key Claims
- Refusal behavior can hide what a model has learned from the corpus without erasing that underlying information.
- Post-training can make some answers politically unacceptable even when the base model has relevant knowledge.
- A censored public internet can shape the training distribution before any explicit refusal rule is added.
- Censorship tests reveal political alignment and governance pressure, not just technical capability.
- Open weights may let downstream users modify answer behavior, but that does not erase questions about the released model's defaults, training distribution, or provenance.

## Connections
- [[AIModelValueSurveying]] - survey method that exposes value and refusal patterns.
- [[LanguageDependentAIBias]] - language and corpus route into model answers.
- [[WorldValuesSurvey]] - contrast with cross-national survey mapping.
- [[AIGovernanceAndCompliance]] - broader AI governance branch.
- [[HumanJudgmentUnderAI]] - users need to know when fluent answers are policy-shaped.
- [[ChineseOpenWeightAIStrategy]] and [[OpenWeightReleaseBoundary]] - open-weight deployment branch that can reduce but not remove censorship concerns.
