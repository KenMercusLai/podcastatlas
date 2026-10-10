---
title: "Generative AI Use-Case Triage"
type: concept
tags: [generative-ai, risk, governance, data-science]
sources:
  - ep-15-unveiling-data-scientists-role-in-the-generative-ai-era
  - ep-24-redefining-data-science-in-the-generative-ai-era
last_updated: 2026-10-10
knowledge_schema: synthesis-v1
---

# Generative AI Use-Case Triage

## Definition
Generative AI use-case triage is the risk-sensitive choice among a generative model, another model class, deterministic rules, retrieval, automatic checks, human review, or no AI based on task fit and verification feasibility.

## Current Synthesis
The central rule across EP15 and EP24 is to choose the model for the problem, not the project for the model. Language generation, chat, and email drafting may naturally fit an LLM; tasks with stable labels, strict correctness requirements, or clearer numeric targets may favor conventional ML or rules. Triage evaluates output type, data, domain language, hallucination and bias risk, privacy, stakes, available success criteria, and the cost of mistakes. Safeguards are part of architecture rather than an apology after deployment: automatic checks, retrieval, bounded behavior, and human review can make some workflows viable, while other cases should remain non-generative.

## Key Claims
- Model choice should follow the use case rather than fashion or platform availability.
- Language-heavy tasks are plausible LLM candidates, but that does not make every mixed-data or unstructured-data problem generative.
- Validation difficulty, error cost, privacy, bias, and domain stakes determine the required safeguards.
- Human review and automatic checks are deliberate system components, not only fallbacks after failure.
- Simpler or more deterministic methods can be superior when labels, rules, and verification paths are clearer.
- Retrieval and vector infrastructure can ground a workflow, but they do not remove the need to measure retrieval and answer quality.

## Evidence
### Risk-sensitive selection
- [[ep-15-unveiling-data-scientists-role-in-the-generative-ai-era]] compares generative AI with discriminative models, rules, automatic checks, and human checks, especially in high-stakes healthcare contexts.

### Problem-led model choice
- [[ep-24-redefining-data-science-in-the-generative-ai-era]] states the selection rule directly, preferring LLMs for language tasks while retaining other models for other problem structures.
- [[ep-24-redefining-data-science-in-the-generative-ai-era]] also connects RAG, embeddings, and vector databases to unstructured-data workflows without treating lower preprocessing effort as proof of fitness.

## Counterevidence & Qualifications
- Neither source supplies a formal decision matrix, comparative error rates, cost model, or regulated deployment case study.
- A task can move between categories as models, controls, data, and verification infrastructure improve.
- Lower apparent preprocessing effort may shift work into parsing, chunking, metadata, retrieval evaluation, monitoring, or review rather than eliminating it.

## What Changed
- Added a sharper problem-first rule and distinguished natural language fit from universal LLM suitability.
- Added retrieval infrastructure as a possible component whose quality still requires evaluation.

## Related Concepts
- [[DataScientistGenerativeAIFluency]] - role-level capability that includes model and safeguard selection.
- [[AIVerification]] - external checks used to judge whether a candidate workflow is safe and useful.
- [[DomainExpertAlignment]] - field knowledge needed to define the real target and error cost.
- [[GenerativeAIEvaluationDiscipline]] - experiment practice for testing a proposed use case across representative cases.
- [[RetrievalAugmentedGeneration]] - grounding architecture that triage may select for knowledge-intensive language tasks.
- [[HumanJudgmentUnderAI]] - retained responsibility for consequential decisions and exceptions.
