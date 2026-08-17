---
title: "Data, Risk, and Actuarial Science in Insurance"
type: source
tags: [podcast, data-science, insurance, actuarial-science]
sources: []
date: 2022-08-09
source_file: "/home/ken/repos/podcastatlas/content/episodes/18840BF8447E46C2B0BF75D5ACFF408E~8584444_2026-08-10-210944-8787-0-0-10.128 [18840BF8447E46C2B0BF75D5ACFF408E~8584444_2026-08-10-210944-8787-0-0-10.128.mp3？cdn_id=99&uuid=a07f8efa-15c7-ef48-fb69-9ef7dd58c617&wuuid=6a838287].md"
source_url: "https://pdcn.co/e/serve.castfire.com/audio/8584444/8584444_2026-08-10-210944.128.mp3?rssID=6736"
duration: "2729"
last_updated: 2026-08-18
---

## Summary
This [[DataScienceWithSam]] episode has [[SamDataScienceWithSam|Sam]] interview [[MaryPatCampbell|Mary Pat Campbell]] about [[ActuarialScience]], insurance risk, and the professional data standards that shape actuarial work. The conversation treats actuarial work as applied risk quantification: [[MortalityRiskPricing]], life annuities, property-and-casualty claims, reinsurance, and underwriting all depend on knowing what historical data can and cannot say about the future. Its core synthesis is that insurance data science is constrained domain work: [[ActuarialDataQuality]], [[ActuarialStandardsOfPractice]], [[InsuranceModelRegulatoryConstraint]], and [[DomainExpertAlignment]] matter as much as statistical fit or machine-learning capability.

## Key Claims
- [[MaryPatCampbell]] defines [[ActuarialScience]] as a field centered on quantifying risk, not just applying mathematics or financial engineering in isolation.
- Early actuarial work is tied to mortality tables and life annuities, while modern actuarial practice uses a broad toolkit for insurance, pensions, and other long-duration promises.
- Life insurance and annuity data often need aggregation through bodies such as the [[SocietyOfActuaries]] because deaths are relatively infrequent and policy liabilities can run for decades.
- The source distinguishes life insurance from property-and-casualty insurance: P&C policies can renew quickly and often generate faster claims feedback, while life-side [[MortalityRiskPricing]] has longer observation and projection lags.
- COVID mortality is presented as a warning against mechanically using an extreme recent year as the future pricing baseline; actuarial projection must separate shock experience from durable assumptions.
- Fraud and [[AsymmetricInformation]] appear most sharply through underwriting and selection risk, where the applicant may know risk information the insurer does not yet see.
- [[ActuarialDataQuality]] begins with asking what the data field actually represents: occurrence dates and report dates, policy flags, diagnosis codes, missing values, true zero values, units, and currencies can all change the interpretation.
- [[ActuarialStandardsOfPractice]] give professional structure to that judgment. The episode highlights ASOP 23 on data quality, ASOP 41 on actuarial communications, and ASOP 56 on modeling.
- The source treats reporting lag as a practical data problem: weekend or holiday dips in COVID death counts may reflect delayed reporting rather than real changes in mortality.
- Electronic health records and automated underwriting can contain bad inputs, such as a recorded weight of zero, old prescriptions that remain active in the file, or medical codes that mean testing rather than diagnosis.
- Reasonability checks are part of professional practice: impossible blood pressure, wrong temperature units, or currency mismatches should be caught before modeling.
- [[InsuranceModelRegulatoryConstraint]] means a technically predictive variable may still be unusable in insurance pricing if regulators, law, or fairness constraints reject it.
- The credit-scoring example in personal auto insurance shows why data scientists entering insurance cannot treat correlation strength as the only decision rule.
- [[MaryPatCampbell]] argues against professional gatekeeping between actuaries, statisticians, data scientists, machine-learning practitioners, and IT teams; the better pattern is collaboration under domain constraints.
- Statistical outputs also need actionability checks. A model result is not useful if it recommends writing more business in a past year or targeting a category the company cannot legally or operationally target.
- The career advice is that technical skill, coding, statistics, and model knowledge are necessary but insufficient without business context, regulatory awareness, and practical judgment.

## Key Quotes
> "tool bag" - Mary Pat Campbell's description of actuarial methods.

> "real or fake" - the source's data-validation framing.

> "correlation does not imply causation" - the host's warning before the discussion of observational insurance data.

## Connections
- [[DataScienceWithSam]], [[SamDataScienceWithSam]], [[MaryPatCampbell]], [[SocietyOfActuaries]], [[AmericanAcademyOfActuaries]], and [[CasualtyActuarialSociety]] - show, host, guest, and professional organization context.
- [[ActuarialScience]], [[InsuranceRiskTransfer]], [[MortalityRiskPricing]], [[AsymmetricInformation]], and [[InsuranceClaimsHandling]] - insurance-risk branch.
- [[ActuarialDataQuality]], [[ActuarialStandardsOfPractice]], [[AIVerification]], [[ExperimentalScienceDataQuality]], and [[DomainExpertAlignment]] - data-quality, standards, and expert-judgment branch.
- [[InsuranceModelRegulatoryConstraint]], [[AIGovernanceAndCompliance]], [[HumanJudgmentUnderAI]], and [[MedicalRiskManagement]] - regulated-model and professional-responsibility context.

## Contradictions
- No direct contradiction found.
- The source qualifies broader AI-in-work optimism by showing that insurance AI must pass actuarial data-quality, professional communication, regulatory, and actionability tests before a model can be operationally useful.
