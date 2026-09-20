---
title: "Claimy"
type: entity
tags: [company, insurance, ai, testing]
sources:
  - tech-20260917-0917-mp-tech-pod-128-tech-20260917-0917-mp-tech-pod-128
last_updated: 2026-09-20
knowledge_schema: synthesis-v1
---

## Overview
Claimy is an AI-insurance startup that tests customer agents for failures and uses the results in insurance pricing.

## Current Profile
Claimy's model joins underwriting with technical risk reduction. It tries to provoke claim-relevant failures during onboarding, lets customers improve and retest their systems, and associates stronger scores with lower premiums.

## Key Characteristics
- Uses [[AIAgentRiskTesting|adversarial agent testing]] to estimate failure risk before coverage.
- Tests concrete harms such as disclosure of sensitive customer information.
- Makes remediation and retesting part of the underwriting loop.
- Connects better test scores with lower insurance premiums.

## Evidence
### Failure discovery
- [[tech-20260917-0917-mp-tech-pod-128-tech-20260917-0917-mp-tech-pod-128]] reports that one tested agent disclosed a previous customer's age and personal profile in under ten minutes.

### Price-linked remediation
- [[tech-20260917-0917-mp-tech-pod-128-tech-20260917-0917-mp-tech-pod-128]] says failed agents can be improved and retested, with stronger results producing lower premiums.

## Qualifications
- The episode does not disclose Claimy's test suite, score calibration, false-positive rate, policy terms, customer count, or claims outcomes.
- A detected privacy failure demonstrates a vulnerability but does not by itself establish an actuarial loss probability.

## What Changed
- Established Claimy as a test-linked AI insurance model.
- Added remediation and premium reduction as its central incentive loop.

## Relationships
- [[InesButemacha]] - Claimy representative explaining its testing and pricing model.
- [[AIAgentRiskTesting]] - technical control at the center of Claimy's approach.
- [[AIInsuranceDataScarcity]] - uncertainty Claimy's tests attempt to reduce.
- [[CorgiAIInsurance|Corgi]] - peer startup offering explicit AI liability coverage.
