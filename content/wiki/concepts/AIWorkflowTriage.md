---
title: "AI Workflow Triage"
type: concept
tags: [ai, workflow, enterprise-ai, operations]
sources: [tech-20260311-0311-mp-tech-pod-128-tech-20260311-0311-mp-tech-pod-128, tsr-ycoffsite-jakeheller-audioonly-v1final-tsr-ycoffsite-jakeheller-audioonly-v1final, e240-openai-lianshou-pe-zaxia-40-yi-meiyuan-liaoliao-guigu-zuihuo-xin-zhiwei-fde]
last_updated: 2026-07-12
---

# AI Workflow Triage

AI workflow triage is the implementation discipline of decomposing a business process before deciding where AI belongs. In [[e240-openai-lianshou-pe-zaxia-40-yi-meiyuan-liaoliao-guigu-zuihuo-xin-zhiwei-fde]], [[Oliver]] describes [[InvisibleTechnologies]] breaking workflows into steps and deciding which should be deterministic, which can use AI, and which require human review. The concept keeps [[AgenticWorkflow]] grounded in operating reality: not every step benefits from probabilistic generation or agent judgment.

[[tsr-ycoffsite-jakeheller-audioonly-v1final-tsr-ycoffsite-jakeheller-audioonly-v1final]] adds the startup-discovery version. [[JakeHeller]] and a co-founder tested an unreleased [[GPT4|GPT-4]] model against many legal workflows over a weekend, including document review, legal research, contract drafting, and other customer-requested jobs. The case shows triage at the strategy stage: the tests helped [[Casetext]] decide which old work to stop and which new [[CoCounsel|Co-Counsel]] direction to pursue.

[[tech-20260311-0311-mp-tech-pod-128-tech-20260311-0311-mp-tech-pod-128]] adds the newsroom version through [[ThePlainDealer|the Plain Dealer]]. Transcribing meetings, scanning municipal sites, summarizing letters, and reviewing court rulings are lower-risk support tasks, while the [[AIRewriteDesk]] moves into a more sensitive publication step where [[HumanJudgmentUnderAI]], [[AIContentProvenance]], and [[AIJournalismTrust]] matter more.

## Key Claims
- Good AI deployment starts with a workflow map rather than a model demo.
- Deterministic steps such as account reconciliation or arithmetic should use hard-coded systems, math, or system-of-record data when exactness is required.
- AI-suitable steps often involve language, search, synthesis, recommendation, customer context, or unstructured document handling.
- Human-review steps remain important where judgment, permission, accountability, customer trust, or regulatory responsibility cannot be delegated cleanly.
- The triage frame explains why enterprise AI value can be large even when only part of a workflow is automated: value comes from the redesigned system, not from forcing AI into every step.
- In a [[FrontierModelInflectionPivot]], workflow triage can be a founder-level decision tool rather than only an implementation method.
- Newsroom triage should distinguish evidence-gathering and signal-finding from published writing, because the latter carries authorship, trust, and public accountability.

## Connections
- [[InvisibleTechnologies]] and [[Oliver]] — source company and speaker.
- [[BusinessLedAITransformation]] — organization-level frame that requires workflow diagnosis.
- [[HumanJudgmentUnderAI]] — responsibility boundary around AI-supported steps.
- [[AgenticWorkflow]], [[DeterministicAuditData]], and [[AICodingVerification]] — adjacent workflow, evidence, and verification themes.
- [[Casetext]], [[CoCounsel|Co-Counsel]], [[VerticalWorkflowAI]], and [[FrontierModelInflectionPivot]] - legal AI product-strategy case.
- [[NewsroomAIAdoption]], [[AIRewriteDesk]], [[AIWrittenJournalism]], [[ThePlainDealer]], and [[AIJournalismTrust]] - newsroom workflow-boundary case.
