---
title: "Output Quality Gates"
type: concept
tags: [ai, quality, workflow, verification]
sources:
  - e245-cangzai-damoxing-beihoude-xinwenren-gptmen-de-huifu-shi-zheyang-xie-chulaide-5aeaeb64-9165-4271-9884-23329b511e11
  - e163-yaowanle-bu-shi-yaowanle-lun-yang-ai-de-xintai-yu-xiguan-lqezcpnw8p6cwhjr2wcw68x4uphb
  - ep391-dang-ai-wancheng-suoyou-gongzuo-yige-ren-yingdang-ruhe-zhengming-ziji-de-jiazhi-gkwridootojhakrdqqtwkv3q
last_updated: 2026-10-28
knowledge_schema: synthesis-v1
---

## Definition

Output quality gates are explicit standards and evidence requirements that determine whether AI-assisted work is accepted, revised, escalated, or rejected.

## Current Synthesis

Quality gates convert “make it better” into an observable review contract. They begin with product and task purpose: an airline support bot, research memo, personal assistant, design artifact, and software change do not share one universal definition of good. The gate may combine factual grounding, completeness, tone, uncertainty, privacy, cultural fit, tests, screenshots, decision usefulness, or user-specific style.

The sources also separate a good-looking output from a sound process. A fluent answer can still misunderstand intent, hide uncertainty, or rest on weak inputs. Users therefore need both outcome criteria and non-skippable process checks. Once made explicit, these standards can become reusable skills, project memory, rubrics, or review checkpoints, but the human remains responsible for whether the gate measures what actually matters.

## Key Claims

- Acceptance standards must be tied to the purpose and consequences of the task.
- A useful gate states observable reasons for acceptance or rejection rather than relying only on vague preference.
- Objective checks and contextual human judgment are complementary, especially in non-code work.
- Process requirements such as source grounding, uncertainty disclosure, privacy review, or testing can be as important as surface quality.
- Gates reduce continuous supervision when agents can stop at bounded checkpoints with review evidence.
- A reusable gate can become part of an [[AISkills|AI skill]], project memory, or agent workflow.
- Clear specifications still need revision when the chosen metric rewards the wrong output.

## Evidence

- Product-specific evaluation: [[e245-cangzai-damoxing-beihoude-xinwenren-gptmen-de-huifu-shi-zheyang-xie-chulaide-5aeaeb64-9165-4271-9884-23329b511e11]] decomposes answer quality into intent, tone, factual uncertainty, attribution, cultural context, and product purpose.
- Durable feedback: [[e163-yaowanle-bu-shi-yaowanle-lun-yang-ai-de-xintai-yu-xiguan-lqezcpnw8p6cwhjr2wcw68x4uphb]] treats acceptable-output definitions, rejection rules, prior mistakes, and examples as reusable context for an AI collaborator.
- Operational specification: [[ep391-dang-ai-wancheng-suoyou-gongzuo-yige-ren-yingdang-ruhe-zhengming-ziji-de-jiazhi-gkwridootojhakrdqqtwkv3q]] argues that vague wishes such as “make it look better” must be replaced with goals, structure, constraints, and a standard the user can inspect.
- Analysis boundary: [[ep391-dang-ai-wancheng-suoyou-gongzuo-yige-ren-yingdang-ruhe-zhengming-ziji-de-jiazhi-gkwridootojhakrdqqtwkv3q]] notes that abundant generated findings do not establish which result matters for a decision.

## Counterevidence & Qualifications

Not every valuable property can be fully specified in advance. Taste, novelty, empathy, strategic surprise, and changing context can resist fixed rubrics; overly narrow gates can create metric gaming or suppress exploration. The sources are practitioner accounts rather than controlled comparisons of gate designs. High-stakes work may require independent review, domain credentials, or formal validation beyond a user-authored checklist.

## What Changed

- Added the distinction between vague prompting and operational specification.
- Added decision usefulness as a gate for data-analysis output.
- Migrated the page to the synthesis-first schema while preserving its complete evidence inventory.

## Related Concepts

- [[AICodingVerification]] - code-specific evidence through tests, builds, CI, and runtime checks.
- [[AIAnswerEvaluation]] - content-specific decomposition of answer quality.
- [[AISkills]] - packages reusable standards and procedures for repeated work.
- [[ContextEngineering]] - supplies task, user, and project context needed to apply a gate.
- [[HumanJudgmentUnderAI]] - retains accountability for choosing and interpreting the standard.
- [[AgenticWorkflow]] - uses gates to control progression, escalation, and stopping.
- [[DurableSkillInvestmentUnderAI]] - treats standard setting and verification as transferable capabilities.
