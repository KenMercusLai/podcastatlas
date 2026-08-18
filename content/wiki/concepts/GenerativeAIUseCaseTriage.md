---
title: "Generative AI Use-Case Triage"
type: concept
tags: [generative-ai, risk, governance, data-science]
sources: [ep-15-unveiling-data-scientists-role-in-the-generative-ai-era]
last_updated: 2026-08-18
---

# Generative AI Use-Case Triage

Generative AI use-case triage is the practice of deciding whether a problem should use a generative model, a simpler machine-learning model, deterministic rules, human review, or some combination of these. In [[ep-15-unveiling-data-scientists-role-in-the-generative-ai-era]], [[MarinaDataScienceWithSam|Marina]] makes this part of the data scientist role: generative AI can be useful, but it should not be the default answer for every business target.

The source's triage boundary is risk-sensitive. Low-risk documentation retrieval may tolerate a different review pattern than healthcare, where a bad answer can cause serious harm. Data scientists therefore need to evaluate hallucination risk, bias, privacy, sample coverage, available success criteria, and the cost of mistakes before choosing an AI workflow.

This concept connects [[AIVerification]] and [[AIModelBiasGovernance]] to practical implementation. A generative AI workflow may be acceptable if it has automatic checks, human checks, or domain-specific limits; another use case may be better served by discriminative AI, conventional machine learning, or a rules-based system.

## Key Claims
- Generative AI should be selected because it fits the use case, not because it is fashionable.
- Text-heavy outputs can be harder to validate than numeric predictions with established KPIs.
- High-stakes domains need stronger safeguards, more explicit success criteria, and clearer responsibility.
- Bias and hallucination can make a use case non-implementable until data, rules, or review mechanisms improve.
- Human review is a design choice, not merely a fallback after a model fails.
- Simpler models can be more appropriate when the task has clearer labels, lower ambiguity, or stronger verification paths.

## Connections
- [[DataScientistGenerativeAIFluency]] - role-level skill set that includes triage.
- [[MarinaDataScienceWithSam]], [[DataScienceWithSam]], and [[SamDataScienceWithSam]] - source context.
- [[AIVerification]], [[AIModelBiasGovernance]], [[HumanJudgmentUnderAI]], and [[AIGovernanceAndCompliance]] - evaluation and responsibility frame.
- [[DomainExpertAlignment]] - domain expertise needed to decide whether a generated output meets the real target.
