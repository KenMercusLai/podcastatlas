---
title: "Actuarial Data Quality"
type: concept
tags: [insurance, data-quality, risk, modeling]
sources: [data-risk-and-actuarial-science-in-insurance]
last_updated: 2026-08-18
---

# Actuarial Data Quality

Actuarial data quality is the professional habit of asking what insurance data actually represents before using it for pricing, reserving, underwriting, or modeling. In [[data-risk-and-actuarial-science-in-insurance]], [[MaryPatCampbell]] ties this to [[ActuarialStandardsOfPractice]], especially ASOP 23 on data quality, and illustrates it with COVID reporting lags, policy flags, electronic health records, medical codes, missing values, true zeroes, implausible vital signs, temperature units, and currency mismatches.

The concept is adjacent to [[ExperimentalScienceDataQuality]] but lives in insurance operations. Scientific records need reproducibility; actuarial records need the same kind of provenance plus claim timing, policy state, reporting process, regulatory use, and business meaning.

## Key Claims
- Data fields are not self-explanatory; analysts need definitions, source-system context, and workflow knowledge.
- Occurrence dates and reporting dates can tell different stories, especially when weekends, holidays, or institutional reporting delays affect the feed.
- A zero can mean a real measured zero, a skipped measurement, a missing value, or a default value depending on the source system.
- Diagnosis and billing codes may show that a condition was tested for, not that the patient has the condition.
- Old prescriptions and stale records can mislead automated underwriting or health-data analysis.
- Reasonability checks should catch implausible ranges, wrong units, scale errors, and currency mismatches before modeling.
- Data quality does not require omniscient auditing of every record, but it does require enough checks to know whether a dataset is fit for actuarial use.

## Connections
- [[MaryPatCampbell]] - source speaker.
- [[ActuarialScience]] and [[InsuranceRiskTransfer]] - field and risk-transfer context.
- [[ActuarialStandardsOfPractice]] - professional standards frame.
- [[MortalityRiskPricing]], [[InsuranceClaimsHandling]], and [[AsymmetricInformation]] - applications where data meaning changes decisions.
- [[ExperimentalScienceDataQuality]], [[AIVerification]], and [[DomainExpertAlignment]] - adjacent data-quality and expert-review concepts.
