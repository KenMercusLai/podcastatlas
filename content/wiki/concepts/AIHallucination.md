---
title: "AI Hallucination"
type: concept
tags: [ai, reliability, verification, judgment]
sources: [tech-20260202-0202-mp-tech-pod-128-tech-20260202-0202-mp-tech-pod-128]
last_updated: 2026-07-12
---

# AI Hallucination

AI hallucination is the failure mode where a model produces plausible but false, unsupported, or misgrounded output. In [[tech-20260202-0202-mp-tech-pod-128-tech-20260202-0202-mp-tech-pod-128]], [[ChristopherMims]] says hallucination is not simply a bug but part of how modern AI works, even as engineers continue reducing the rate of mistakes.

The concept gives a general reliability frame for narrower pages such as [[LegalAIHallucination]]. Hallucination matters because fluent output can hide weak evidence, weak reasoning, or missing context, making [[HumanJudgmentUnderAI]], [[OutputQualityGates]], and domain expertise part of safe AI use.

## Key Claims
- Hallucination is not limited to one domain; it appears wherever a system produces confident-looking output without adequate grounding.
- Better models and retrieval systems can reduce hallucination, but they do not remove the user's need to verify important claims.
- The risk is highest when the user lacks enough expertise to notice errors or when the output affects legal, medical, financial, educational, or operational decisions.
- Treating hallucination as a system property encourages review practices rather than blind trust.

## Connections
- [[ChristopherMims]], [[HowToAI|How to AI]], and [[ExpertiseAmplifiedAIUse]] - source frame for why expertise matters.
- [[HumanJudgmentUnderAI]], [[OutputQualityGates]], and [[DomainExpertAlignment]] - safeguards against plausible wrong output.
- [[LegalAIHallucination]], [[LLMWorldModelGap]], [[RetrievalAugmentedGeneration]], and [[AISearchEvaluation]] - related reliability and grounding concepts.
