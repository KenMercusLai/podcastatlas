---
title: "High-Frequency Trading / 高频交易"
type: concept
tags: [finance, quantitative-finance, electronic-trading, market-structure]
sources:
  - e259-jixie-shenjiao-yu-fanrenxing-celve-huaerjie-lianghua-jutou-de-ai-zhilu-bc105fa7-23de-4c70-a338-6d70daf9aed1
knowledge_schema: synthesis-v1
last_updated: 2026-11-23
---

# High-Frequency Trading / 高频交易

## Definition

High-frequency trading is automated trading at millisecond-to-hour horizons that seeks small short-lived price or spread opportunities through repeated, low-latency decisions and execution.

## Current Synthesis

The episode places high-frequency trading inside a historical shift from speed competition toward a broader model-and-capacity competition. Latency remains consequential, especially for short-lived opportunities, but physical limits and crowded infrastructure reduce the marginal value of another small speed gain. Firms increasingly combine low latency with richer models, more compute, and strategies able to deploy greater capital.

## Key Claims

- Short holding periods allow many small opportunities to accumulate rather than relying on one large forecast.
- Low-latency infrastructure remains necessary where opportunities disappear quickly.
- Speed improvements face physical and competitive limits and declining marginal returns.
- Very rapid reactions can increase market sensitivity and contribute to collective instability.
- Model quality, capacity, risk control, and execution are complements to speed.
- High data volume can still contain few independent observations because records are correlated.

## Evidence

- **Time horizon and economics:** [[e259-jixie-shenjiao-yu-fanrenxing-celve-huaerjie-lianghua-jutou-de-ai-zhilu-bc105fa7-23de-4c70-a338-6d70daf9aed1]] contrasts millisecond-to-hour high-frequency activity with day-to-week medium-frequency trading.
- **Strategic shift:** [[e259-jixie-shenjiao-yu-fanrenxing-celve-huaerjie-lianghua-jutou-de-ai-zhilu-bc105fa7-23de-4c70-a338-6d70daf9aed1]] argues that latency still matters while additional gains have become less valuable relative to complex models and larger-capacity strategies.

## Counterevidence & Qualifications

The source does not quantify spreads, latency, volatility, flash-crash causation, or consumer benefit. High-frequency trading includes heterogeneous strategies; liquidity provision, arbitrage, and directional prediction should not be collapsed into one conduct category.

## What Changed

- Added a qualified concept distinguishing enduring latency needs from declining returns to pure speed competition.

## Related Concepts

- [[MarketMaking]] - liquidity-provision function often implemented at high frequency.
- [[FinancialAIQuantitativeTrading]] - model layer increasingly complementing latency.
- [[FinancialMarketNonstationarity]] - changing market state that alters short-horizon behavior.
- [[QuantitativeOverfitting]] - risk created by searching correlated high-volume records.
- [[InvestmentRiskManagement]] - control layer for scaled automated decisions.
