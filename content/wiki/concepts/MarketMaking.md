---
title: "Market Making / 做市"
type: concept
tags: [finance, market-structure, liquidity, trading]
sources:
  - e259-jixie-shenjiao-yu-fanrenxing-celve-huaerjie-lianghua-jutou-de-ai-zhilu-bc105fa7-23de-4c70-a338-6d70daf9aed1
knowledge_schema: synthesis-v1
last_updated: 2026-11-23
---

# Market Making / 做市

## Definition

Market making is the continuous provision of executable buy and sell quotes so other participants can transact without waiting for a perfectly matched counterparty.

## Current Synthesis

The episode presents market making as both a service and a risky trading business. A market maker can earn the bid-ask spread across many transactions while increasing immediacy and liquidity, but it must manage inventory, adverse price moves, model error, latency, market impact, and operational failure. High transaction volume does not make the activity riskless; automation can scale both small edges and mistakes.

## Key Claims

- Continuous two-sided quotations reduce the need for buyers and sellers to arrive simultaneously.
- Bid-ask spreads are a primary revenue channel rather than a guaranteed profit.
- Faster and more reliable execution can lower trading friction for other market participants.
- Inventory, price, execution, and system risks remain even when each individual spread is small.
- Quantitative models and infrastructure jointly determine whether quoted opportunities can be captured safely.
- Greater automation raises the importance of hard risk and compliance controls.

## Evidence

- **Liquidity function:** [[e259-jixie-shenjiao-yu-fanrenxing-celve-huaerjie-lianghua-jutou-de-ai-zhilu-bc105fa7-23de-4c70-a338-6d70daf9aed1]] explains continuous bids and offers as a way to provide liquidity and immediate counterparties.
- **Economics and risk:** [[e259-jixie-shenjiao-yu-fanrenxing-celve-huaerjie-lianghua-jutou-de-ai-zhilu-bc105fa7-23de-4c70-a338-6d70daf9aed1]] links spread capture to repeated transactions while emphasizing execution systems, risk control, and the cost of automated failure.

## Counterevidence & Qualifications

The source gives an industry-level explanation rather than a market-specific microstructure study. Market makers differ across assets, venues, obligations, holding periods, and business models. Improved liquidity in normal conditions does not establish resilience during stress or prove that every form of high-frequency activity benefits every participant.

## What Changed

- Added a dedicated market-structure concept separating liquidity provision from directional speculation.

## Related Concepts

- [[HighFrequencyTrading]] - short-horizon approach often used in electronic market making.
- [[FinancialAIQuantitativeTrading]] - model and infrastructure stack supporting automated quotes and decisions.
- [[InvestmentRiskManagement]] - survival controls around inventory, execution, and operational exposure.
- [[PaymentForOrderFlow]] - distinct routing relationship involving market makers and brokers.
- [[FinancialMarketNonstationarity]] - changing conditions that alter spread, volatility, and model behavior.
