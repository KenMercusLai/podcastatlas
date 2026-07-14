---
title: "In-House Banking Software"
type: concept
tags: [fintech, banking, infrastructure, software]
sources: [tsr-s5-tomblomfield-v2-audio-tsr-s5-tomblomfield-v2-audio]
last_updated: 2026-07-14
---

# In-House Banking Software

In-house banking software is the strategy of building core banking, customer, fraud, data, and operational systems internally instead of relying mainly on outsourced vendor stacks. [[tsr-s5-tomblomfield-v2-audio-tsr-s5-tomblomfield-v2-audio]] adds the concept through [[Monzo]], where [[TomBlomfield]] says the team chose to build much of the bank's software from scratch using Go.

The source presents the approach as both product advantage and risk-control advantage. Internally built systems helped Monzo deliver real-time balances, push notifications, clearer merchant names, maps, logos, categorization, mobile support, and a more human product experience. The same architecture let the team respond to new fraud patterns in about 24 hours, while legacy banks using outsourced systems could move more slowly.

The concept is not a blanket argument against vendors. The Monzo case works because the product promise depended on speed, data, and customer-visible banking behavior. In a regulated bank, the cost of owning software is high, but the cost of being unable to change critical systems can be higher.

## Key Claims
- In regulated fintech, software architecture can determine both product feel and risk response speed.
- Building internally can turn operational changes into same-day or next-day product and fraud interventions.
- Customer-visible delight may depend on backend control over transaction metadata, notifications, categorization, and support workflows.
- In-house systems increase responsibility because the startup owns more reliability, compliance, and risk operations.
- Vendor systems can preserve speed to launch, but they may limit differentiation if many banks share the same operational surface.

## Connections
- [[Monzo]] and [[TomBlomfield]] - source case.
- [[BankingProductDelight]], [[EarlyFintechFraudControls]], and [[RegulatedFintechCapitalPressure]] - product, fraud, and financing consequences.
- [[MoneyMovementInfrastructure]], [[SaaSTrustMoat]], and [[TrustAsBusinessAsset]] - adjacent infrastructure and trust concepts.
