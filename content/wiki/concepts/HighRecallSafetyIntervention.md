---
title: "High-Recall Safety Intervention / 高召回安全干预"
type: concept
tags: [safety, ai, platform-governance, risk-management]
sources:
  - no-228-duihua-didi-quxiaonan-pa-ni-juede-women-bu-anquan-geng-pa-ni-juede-women-juedui-anquan-gkwriueor0j1ayqkyatbzbpi
last_updated: 2026-09-07
knowledge_schema: synthesis-v1
---

# High-Recall Safety Intervention / 高召回安全干预

## Definition
High-recall safety intervention is a risk-control posture in which a platform deliberately favors catching as many possible severe incidents as possible, even when that creates many false alarms, user interruptions, and human-review burdens.

## Current Synthesis
The [[Didi]] source presents high recall as the central tradeoff in low-frequency, high-harm safety work. If the system waits for high precision, it may miss rare but serious events. If it maximizes recall, it calls users, routes cases to specialists, and escalates many orders that later prove harmless.

This makes high-recall safety different from ordinary engagement optimization. A false alarm can be annoying, but in this frame it is also evidence that the underlying order was safe. The hard product problem is to preserve enough user trust and privacy protection that people tolerate interventions without assuming either that the platform is unsafe or that it can make safety absolute.

## Key Claims
- Severe-harm prevention can rationally prioritize recall over precision.
- False alarms are an expected cost when risk signals are weak, sparse, or ambiguous.
- AI screening needs human review when physical-world context and escalation decisions matter.
- Model improvement changes the triage surface but does not remove the need for operational judgment.
- High recall can damage user experience if users do not understand why intervention happens.
- The posture depends on governance controls because more alerts can mean more data access, phone calls, and human inspection.

## Evidence
- Explicit metric priority - [[no-228-duihua-didi-quxiaonan-pa-ni-juede-women-bu-anquan-geng-pa-ni-juede-women-juedui-anquan-gkwriueor0j1ayqkyatbzbpi]] says recall is much more important than precision in [[Didi]]'s safety models.
- Screening funnel - [[no-228-duihua-didi-quxiaonan-pa-ni-juede-women-bu-anquan-geng-pa-ni-juede-women-juedui-anquan-gkwriueor0j1ayqkyatbzbpi]] describes daily orders passing through two AI layers before a smaller set reaches specialist review and intervention.
- False-alarm tolerance - [[no-228-duihua-didi-quxiaonan-pa-ni-juede-women-bu-anquan-geng-pa-ni-juede-women-juedui-anquan-gkwriueor0j1ayqkyatbzbpi]] notes that most intervened orders are later harmless, while treating that outcome as acceptable in safety work.
- Model capability - [[no-228-duihua-didi-quxiaonan-pa-ni-juede-women-bu-anquan-geng-pa-ni-juede-women-juedui-anquan-gkwriueor0j1ayqkyatbzbpi]] says large-model audio reasoning can catch contextual clues that keyword rules would not enumerate.
- Intervention friction - [[no-228-duihua-didi-quxiaonan-pa-ni-juede-women-bu-anquan-geng-pa-ni-juede-women-juedui-anquan-gkwriueor0j1ayqkyatbzbpi]] includes the case of repeated late-night calls after the platform saw driver stop and logout signals near a passenger's destination.

## Counterevidence & Qualifications
High recall is not a universal product rule. It is most defensible where harms are severe, time-sensitive, and hard to reverse. The source also makes clear that high recall still leaves gaps: offline rides, silent incidents, closed recording, post-order events, and premeditated acts can remain outside the platform's sensing boundary.

## What Changed
- Created the concept from the [[Didi]] ride-hailing safety episode.

## Related Concepts
- [[RideHailingSafetyOperations]] - operating system where high-recall triage is applied.
- [[PublicSafetyPrivacyTradeoff]] - governance cost of more sensing, alerts, and human access.
- [[HumanJudgmentUnderAI]] - human review needed after model triage.
- [[AIHardwarePrivacyExchange]] - broader exchange between sensor-based services and privacy exposure.
- [[AIGovernanceAndCompliance]] - policy and control layer needed when AI systems affect safety decisions.
- [[SafetyProductCredibility]] - trust problem created when users must believe both safety claims and limitation warnings.
