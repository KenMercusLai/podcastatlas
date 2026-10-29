---
title: "Enterprise POC Discipline"
type: concept
knowledge_schema: synthesis-v1
tags: [enterprise-sales, saas, validation]
sources:
  - enterprise-sales-with-no-product-landing-a-big-four-customer
  - chatgpt-should-have-killed-his-ai-saas-instead-hes-nearing-10m
last_updated: 2026-10-30
---

# Enterprise POC Discipline

## Definition

Enterprise POC discipline is the practice of accepting and designing a proof of concept only when both sides define what is being proven, what evidence will count, who can buy, what timing and budget exist, and what rollout work follows if the proof succeeds.

## Current Synthesis

The bounded cases show two complementary proof designs. [[Templafy]] uses the commercial gate: a small enterprise POC is worth doing only when buyer intent, budget, timing, criteria, and expansion consequences are explicit. [[MosaicAI]] uses the diagnostic gate: historical tickets can estimate automatable work, savings, and candidate workflows quickly, but the company must state clearly that integration, adoption, change management, IT work, and realized outcomes remain unproven. A disciplined POC therefore proves a bounded proposition without disguising either procurement reality or the distance to production.

## Key Claims

- A small POC is weak validation if it lacks budget, timing, buyer intent, success criteria, and a path to expansion.
- Proof criteria should be defined before a tender or customer process turns them into one-sided requirements.
- Historical operating data can make a pilot concrete by establishing a baseline and identifying candidate workflows.
- A diagnostic pilot should distinguish estimated opportunity from realized deployment outcomes.
- Enterprise validation must test product behavior, buyer commitment, workflow fit, and procurement reality.
- Metrics should represent useful business work and be paired with quality, adoption, and cost evidence.
- A successful POC still needs named ownership for integration, security, change management, rollout, and post-launch verification.

## Evidence

Commercial proof gate:
- [[enterprise-sales-with-no-product-landing-a-big-four-customer]] says [[ChristianLund]] and [[Templafy]] answered POC requests with “yes, if,” requiring clear timing, budget, buying intent, success criteria, and rollout consequences.
- [[enterprise-sales-with-no-product-landing-a-big-four-customer]] notes that a small enterprise pilot can consume substantial security, approval, integration, and founder attention.

Diagnostic proof gate:
- [[chatgpt-should-have-killed-his-ai-saas-instead-hes-nearing-10m]] says Mosaic can analyze roughly 1,000 historical tickets during a five-day pilot to estimate automation opportunities, expected savings, and workflows.
- [[chatgpt-should-have-killed-his-ai-saas-instead-hes-nearing-10m]] explicitly separates this analysis from deeper integrations, adoption, IT work, and change management, and describes tickets handled per representative as a primary productivity measure.

## Counterevidence & Qualifications

Neither source supplies independent customer-side evaluation of the proof process. A paid or tightly specified pilot can still fail through biased samples, weak baselines, metric gaming, implementation drift, security limits, or executive sponsorship that does not survive rollout. Mosaic's five-day analysis is founder-described and should not be interpreted as evidence that complex enterprise support can be fully deployed in five days. Templafy's account also does not show that every high-potential buyer can specify budget and rollout before exploratory work.

## What Changed

- Converted the page to the synthesis-v1 schema.
- Added diagnostic analysis over historical operating data beside Templafy's commercial acceptance gate.
- Clarified the boundary between estimated pilot opportunity and realized production outcomes.

## Related Concepts

- [[EnterpriseCustomerAsMarket]] - expansion logic after a successful enterprise proof.
- [[FounderLedSales]] - founder involvement often needed to define criteria and interpret buyer commitment.
- [[FastProductValidation]] - broader practice of obtaining decision-relevant evidence quickly.
- [[CustomerPull]] - costly customer commitment that a disciplined proof seeks to test.
- [[ProductLedWillingnessToPay]] - value evidence that supports enterprise pricing.
- [[EnterpriseAIPilotPurgatory]] - failure mode when proof never converts into ownership, workflow change, or deployment.
- [[EnterpriseTechnicalSupportAutomation]] - Mosaic's technical-support use case for diagnostic proof.
