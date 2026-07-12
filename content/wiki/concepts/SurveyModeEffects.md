---
title: "Survey Mode Effects"
type: concept
tags: [surveys, measurement, methodology]
sources: [tech-20260209-0209-mp-tech-pod-128-tech-20260209-0209-mp-tech-pod-128]
last_updated: 2026-07-12
---

# Survey Mode Effects

Survey mode effects are measurement changes caused by how people answer a survey rather than by the underlying trait the survey is trying to measure. In [[tech-20260209-0209-mp-tech-pod-128-tech-20260209-0209-mp-tech-pod-128]], the relevant mode is device type: smartphone respondents perform worse on knowledge questions than desktop, laptop, or tablet respondents in [[CarlyUrban]]'s experiment.

The episode turns survey mode effects into a policy-risk concept. If a financial-literacy survey changes from mostly desktop completion to majority smartphone completion, then a reported knowledge decline may combine real knowledge change with [[SmartphoneSurveyPenalty]].

## Key Claims
- Mode effects can distort time-series comparisons when the response channel changes across survey waves.
- Device effects can also distort cross-country comparisons if mobile response rates differ by country.
- Attention checks may not catch every mode effect because respondents can pass a simple check while still spending little effort on later knowledge items.
- The fix is not necessarily banning phones; phones may improve representativeness.
- Researchers can reduce risk by tracking device type, response time, question placement, and mobile response rates.

## Connections
- [[SmartphoneSurveyPenalty]] - concrete mode effect from the source.
- [[FinancialLiteracyMeasurement]] - survey domain affected by the mode shift.
- [[NationalFinancialCapabilityStudy]] - repeated survey where device mix changed.
- [[UnderstandingAmericaStudy]] - panel used to isolate device assignment.
- [[AIAssistedSurveyResponse]] - possible next mode effect as respondents use chatbots during surveys.
