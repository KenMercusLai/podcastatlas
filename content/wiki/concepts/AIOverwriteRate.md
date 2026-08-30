---
title: "AI Overwrite Rate"
type: concept
tags: [ai, metrics, enterprise-ai, workflow]
sources:
  - ep-43-the-outsiders-advantage-how-diverse-perspectives-unlock-enterprise-ai-success
last_updated: 2026-08-31
knowledge_schema: synthesis-v1
---

# AI Overwrite Rate

## Definition
AI overwrite rate is the frequency with which users receive an AI suggestion but reject, replace, or return to the old way of working instead of accepting the AI-supported output.

## Current Synthesis
The EP43 source presents overwrite rate as a practical metric for adoption because it sits closer to workflow behavior than logins, license counts, or training completion. If users routinely overwrite suggestions, the adoption team needs to ask whether the problem is output quality, workflow fit, policy, trust, incentives, or user understanding.

The metric is not a simple "lower is better" score. In high-stakes or human-review workflows, overwriting can be responsible judgment. Its value is diagnostic: it creates a trace that prompts investigation into why AI suggestions are or are not becoming accepted work.

## Key Claims
- Overwrite rate measures acceptance of AI-supported work more directly than tool access or launch activity.
- A high overwrite rate can reveal model-quality, workflow-fit, trust, policy, or incentive failures.
- A low overwrite rate is not automatically good if users accept AI output without enough review.
- The metric should be paired with frontline interviews to understand why users return to old workflows.
- Overwrite rate complements [[AIAdoptionBaselineMeasurement]] by showing post-rollout behavior against the intended change.

## Evidence
- Metric recommendation: [[ep-43-the-outsiders-advantage-how-diverse-perspectives-unlock-enterprise-ai-success]] says Sumayya recommends tracking how often users receive an AI suggestion but go back to the old way of working.
- Measurement shift: [[ep-43-the-outsiders-advantage-how-diverse-perspectives-unlock-enterprise-ai-success]] frames the recommendation as a move from implementation activity to observed workflow change.
- Trust context: [[ep-43-the-outsiders-advantage-how-diverse-perspectives-unlock-enterprise-ai-success]] links rejection of AI workflows to awareness, workflow fit, and institutional trust.
- Human-review boundary: [[ep-43-the-outsiders-advantage-how-diverse-perspectives-unlock-enterprise-ai-success]] treats user behavior as evidence requiring interpretation rather than as raw compliance.

## Counterevidence & Qualifications
Overwrite rate is not a universal adoption KPI. In domains where review is mandatory, users should overwrite bad or unsupported suggestions. The metric becomes useful when teams ask why overwrites happen and whether they correlate with quality, trust, role, task type, policy, or training.

## What Changed
- Initial synthesis created for the EP43 overwrite-rate metric.

## Related Concepts
- [[AIAdoptionBehavioralSignals]] - broader class of behavior-based AI adoption evidence.
- [[QuietAIAdoptionDeparture]] - related signal for full non-return rather than suggestion rejection.
- [[AIAdoptionBaselineMeasurement]] - baseline layer needed to interpret workflow change.
- [[ModelWorkflowFit]] - fit problem that overwrite rate can expose.
- [[HumanJudgmentUnderAI]] - review boundary that can make overwriting healthy rather than pathological.
- [[InstitutionalTrustAIAdoption]] - trust condition that may affect whether users accept AI suggestions.
