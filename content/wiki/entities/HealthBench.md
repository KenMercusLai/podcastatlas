---
title: "HealthBench"
type: entity
tags: [benchmark, ai, healthcare, evaluation]
sources: [e227-meiguo-yiliao-shichang-ai-zhengduozhan-jutou-yazhu-chuangye-gongsi-neng-ying-ma-f14f8686-a6e2-47ea-92c1-ca7e71199f67]
last_updated: 2026-08-05
---

# HealthBench

HealthBench is the medical AI evaluation benchmark discussed in [[e227-meiguo-yiliao-shichang-ai-zhengduozhan-jutou-yazhu-chuangye-gongsi-neng-ying-ma-f14f8686-a6e2-47ea-92c1-ca7e71199f67]]. The episode says [[OpenAI]] released it to evaluate medical AI through realistic conversation scenarios rather than only exam-style question answering.

The benchmark matters because it moves medical AI evaluation toward [[AIVerification]] in context. [[ZhouYebing]] contrasts it with MedQA and PubMedQA-like tests: real medical conversations require follow-up, uncertainty handling, multilingual communication, evidence quality, and judgment under incomplete patient context.

## Key Points
- The episode says HealthBench used 262 scorers from 60 countries, 26 specialties, and 49 languages.
- The reported scores cited in the episode were 60% for O3 and 32% in the difficult mode.
- The benchmark strengthens the wiki's distinction between book knowledge and clinical conversation.
- HealthBench does not remove the need for [[HumanJudgmentUnderAI]]; it makes evaluation more realistic by exposing where AI still fails.

## Connections
- [[OpenAI]] — benchmark publisher in the source.
- [[AIVerification]], [[AIHallucination]], and [[HumanJudgmentUnderAI]] — evaluation and responsibility context.
- [[EvidenceGroundedMedicalRAG]] and [[MedicalAIWorkflowIntegration]] — related medical-AI quality layers.
