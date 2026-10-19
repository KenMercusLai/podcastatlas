---
title: "AI Hallucination"
type: concept
tags: [ai, reliability, verification, judgment]
sources:
  - ep-47-the-ai-pioneer-who-decided-privacy-matters-more-than-hype
  - ep-17-ais-impact-on-creativity-a-consumers-perspective
  - e227-meiguo-yiliao-shichang-ai-zhengduozhan-jutou-yazhu-chuangye-gongsi-neng-ying-ma-f14f8686-a6e2-47ea-92c1-ca7e71199f67
  - tech-20260202-0202-mp-tech-pod-128-tech-20260202-0202-mp-tech-pod-128
  - tech-20261019-1019-mp-tech-pod-128-tech-20261019-1019-mp-tech-pod-128
last_updated: 2026-10-19
knowledge_schema: synthesis-v1
---

# AI Hallucination

## Definition
AI hallucination is a model failure in which fluent output contains false, unsupported, invented, or contextually misgrounded claims that can appear credible enough to escape casual review.

## Current Synthesis
Hallucination is not confined to spectacular invention. It includes fabricated authorities, plausible factual errors, incorrect code, unsupported medical language, and retrieval of the wrong time-bound referent. The California election example is especially instructive: [[ChatGPT]] answered about a different Proposition 4 from 2024 and then made a false claim about the reporter's ability to vote. The answer was related in form but wrong in temporal and civic context.

Across consumer, professional, medical, and election settings, the response is not blind trust or blanket rejection. Treat language models as probabilistic assistants; strengthen prompts and grounding; inspect citations; test code and claims; prefer explicit uncertainty when evidence is absent; and keep domain experts or responsible users accountable for consequential decisions. Risk rises when polished language exceeds the user's capacity to detect the error or when the domain has low tolerance for mistakes.

## Key Claims
- Hallucination includes contextual misgrounding and stale referent selection, not only invented facts or citations.
- Better prompting, retrieval, and newer models may reduce errors but cannot transfer verification responsibility to the system.
- Fluent language and attached links can make wrong answers appear more authoritative than their evidence warrants.
- Consequence and detectability matter together: medical, legal, election, financial, and operational errors deserve stronger gates.
- Expertise improves error detection, while novice users may benefit from AI precisely where they are least able to evaluate it.
- Safe use favors source grounding, explicit uncertainty, external checks, and human ownership of important output.

## Evidence
- Probabilistic-system boundary - [[ep-47-the-ai-pioneer-who-decided-privacy-matters-more-than-hype]] contrasts LLM error with solved checkers and recommends supervised augmented intelligence, citations, and an explicit "does not know" response when grounding is absent.
- Everyday workflow risk - [[ep-17-ais-impact-on-creativity-a-consumers-perspective]] requires fact-checking drafts, editing generated language, testing code, and respecting professional data boundaries even in low-barrier use.
- Clinical stakes - [[e227-meiguo-yiliao-shichang-ai-zhengduozhan-jutou-yazhu-chuangye-gongsi-neng-ying-ma-f14f8686-a6e2-47ea-92c1-ca7e71199f67]] makes evidence-grounded retrieval, realistic evaluation, privacy, and clinician responsibility central where error tolerance is low.
- Expertise and assistance - [[tech-20260202-0202-mp-tech-pod-128-tech-20260202-0202-mp-tech-pod-128]] argues that experts may gain more because they know what to ask and can recognize weak output, while treating AI as an assistant rather than a replacement.
- Election-context failure - [[tech-20261019-1019-mp-tech-pod-128-tech-20261019-1019-mp-tech-pod-128]] documents the wrong-year proposition answer and cites a separate case involving an invented Scottish election candidate.

## Counterevidence & Qualifications
The sources do not establish one fixed hallucination rate across models, dates, prompts, tools, or domains. Retrieval, citations, precise prompts, and product safeguards can improve performance, and the California answers became more useful after the prompt specified the proposition, election date, and year. Improvement is not proof of correctness: citations may be irrelevant or ideologically framed, multiple systems may share the same source, and even expert review can miss errors. The term “hallucination” itself may anthropomorphize a statistical failure mode.

## What Changed
- Added temporal and jurisdictional misgrounding as a distinct form of hallucination.
- Extended the synthesis from consumer, technical, and medical use into election research.
- Migrated the page to synthesis-v1 while preserving the complete source inventory.

## Related Concepts
- [[AIVerification]] - broader discipline of checking AI answers, actions, hypotheses, and outputs.
- [[AIAssistedElectionResearch]] - civic workflow where time, jurisdiction, and source authority are essential.
- [[AIElectionMisinformationRisk]] - public harm that can result from either malicious generation or ordinary model error.
- [[HumanJudgmentUnderAI]] - responsibility boundary for deciding whether output is safe to use.
- [[DeterministicAIVerification]] - contrast between tightly checkable bounded systems and probabilistic language output.
- [[LegalAIHallucination]] - domain-specific fabrication of cases, citations, or authority.
- [[EvidenceGroundedMedicalRAG]] - grounding pattern used to reduce unsupported medical answers.
