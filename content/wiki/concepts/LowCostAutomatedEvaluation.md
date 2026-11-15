---
title: "Low-Cost Automated Evaluation / 低成本自动化评估"
type: concept
tags: [ai, evaluation, rsi, optimization]
sources:
  - lhhxptqoanrsmgih0htfelq-znbg-lhhxptqoanrsmgih0htfelq-znbg
last_updated: 2026-11-16
knowledge_schema: synthesis-v1
---

# Low-Cost Automated Evaluation / 低成本自动化评估

## Definition

Low-cost automated evaluation is a feedback condition in which a candidate result can be scored repeatedly, objectively enough, and cheaply enough for an AI system to search for improvements across many iterations.

## Current Synthesis

[[lhhxptqoanrsmgih0htfelq-znbg-lhhxptqoanrsmgih0htfelq-znbg]] treats evaluator quality as the practical gate on [[RecursiveSelfImprovement]]. Code execution, kernel correctness and speed, or speech-recognition error rates can support rapid search because feedback is automatic and comparatively cheap. Aesthetic quality, open-ended writing, chip tape-out, and drug experiments resist the same loop because standards are contested, incomplete, slow, or physically expensive. More metrics are not automatically better: an incomplete scorecard can invite proxy optimization and capability regression outside the measured dimensions.

## Key Claims

- Cheap, repeatable feedback lets models explore many candidate changes without requiring human review at every step.
- Objective-seeming metrics remain dangerous when they omit important dimensions or can be gamed.
- Physical experimentation can remain the bottleneck even when AI makes proposal generation nearly free.
- Subjective domains still require expert judgment, disagreement handling, and explicit value choices.
- Evaluation cost helps explain why RSI arrives unevenly across kernels, code, speech, science, and creative work.

## Evidence

### Verifiable engineering loops
- [[lhhxptqoanrsmgih0htfelq-znbg-lhhxptqoanrsmgih0htfelq-znbg]] uses word-error rate, performance constraints, kernel tests, and a guest-reported TTS optimization as examples of rapid feedback-driven improvement.

### Evaluation bottlenecks
- [[lhhxptqoanrsmgih0htfelq-znbg-lhhxptqoanrsmgih0htfelq-znbg]] contrasts those loops with aesthetics, writing, chip fabrication, and drug testing, where judgment or validation is slower, costlier, or less objective.

## Counterevidence & Qualifications

- The source supplies no benchmark artifacts for the reported 1,700% TTS improvement, so the magnitude, baseline, quality constraints, and reproducibility remain unverified.
- A score can be automated and still reward the wrong behavior; coverage, adversarial tests, and human review remain necessary.
- Human disagreement does not imply that a task is impossible to evaluate, only that its evaluator may need structured judgment rather than one scalar metric.

## What Changed

- Established evaluation cost, automation, and objectivity as a joint explanation for where practical RSI appears first.

## Related Concepts

- [[RecursiveSelfImprovement]] - depends on feedback that can safely support repeated improvement cycles.
- [[GenerativeAIEvaluationDiscipline]] - supplies representative datasets and experiment design around automated metrics.
- [[AIVerification]] - asks whether the evaluated output is actually correct enough to use.
- [[ResearchTaste]] - selects worthwhile goals when correctness alone does not establish importance.
- [[AICodingVerification]] - applies executable checks and review to software changes.
