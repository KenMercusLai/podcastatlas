---
title: "AI Insurance Data Scarcity"
type: concept
tags: [ai, insurance, actuarial-science, risk-modeling]
sources:
  - tech-20260917-0917-mp-tech-pod-128-tech-20260917-0917-mp-tech-pod-128
last_updated: 2026-09-20
knowledge_schema: synthesis-v1
---

## Definition
AI insurance data scarcity is the lack of stable, long-run loss and exposure evidence needed to estimate how often AI systems cause covered harm and how severe those losses will be.

## Current Synthesis
Insurers can model familiar hazards with historical events, exposure maps, and established causal categories. AI changes faster, is deployed across heterogeneous workflows, and can fail through language, calculation, privacy, or service behavior, so past loss experience is thin and may become obsolete quickly. Structured testing can add evidence, but it does not substitute for validated claims history.

## Key Claims
- Thin claims history weakens estimates of AI-loss frequency and severity.
- Rapid model and deployment changes can make older evidence less representative.
- Ambiguous policy wording obscures which incidents count as covered AI losses.
- Scenario testing can reveal failure modes before claims occur but requires calibration to real exposure.
- Data scarcity can produce divergent insurer responses, including cautious exclusions and specialist coverage.

## Evidence
### Historical-model contrast
- [[tech-20260917-0917-mp-tech-pod-128-tech-20260917-0917-mp-tech-pod-128]] reports [[JohnFarleyGallagher|John Farley]]'s contrast between Florida hurricane models and the lack of comparable historical AI data.

### Supplemental testing evidence
- [[tech-20260917-0917-mp-tech-pod-128-tech-20260917-0917-mp-tech-pod-128]] presents [[Claimy]]'s agent testing and premium scores as one attempt to quantify risk before a mature loss record exists.

## Counterevidence & Qualifications
- The episode establishes a general evidence deficit but does not quantify its size or compare actual insurer datasets.
- Technical evaluation data and conventional business-loss data measure different things; combining them requires an explicit causal model.
- AI is not one homogeneous peril, so data scarcity may vary substantially by use case, control environment, and policy trigger.

## What Changed
- Established historical loss scarcity as the central constraint on AI insurance pricing.
- Added hurricane catastrophe modeling as the mature-risk comparison.
- Added agent testing as a partial evidence source with unresolved calibration limits.

## Related Concepts
- [[AILiabilityInsurance]] - coverage category whose pricing depends on usable loss evidence.
- [[AIAgentRiskTesting]] - produces prospective behavioral evidence under controlled scenarios.
- [[InsuranceRiskTransfer]] - requires credible event definitions and pricing assumptions.
- [[AIGovernanceAndCompliance]] - affects exposure quality and the interpretation of observed failures.
