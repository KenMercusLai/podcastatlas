---
title: "Trading Probability Calibration / 交易概率校准"
type: concept
tags: [trading, probability, risk, calibration]
sources:
  - ai-trading-juece-pianyi-xingdong-hengui-duitan-chao-3w-star-vibe-trading-zuozhe-haozhe-luz0eizpk9v3nz94iuutp1z9xj25
knowledge_schema: synthesis-v1
last_updated: 2026-09-28
---

# Trading Probability Calibration / 交易概率校准

## Definition
Trading probability calibration is the practice of testing whether stated confidence matches observed outcomes and whether the resulting edge remains after market pricing, evidence dependence, transaction costs, and position-size constraints.

## Current Synthesis
The source frames trading as betting on distributions rather than discovering one certain answer. An opportunity exists only when a trader's probability assessment differs meaningfully from the probability implied by price, and the difference survives costs and uncertainty.

A probability number is not self-validating. It needs empirical calibration, an explanation of the evidence chain, and dependency checks. Several bullish judgments derived from one news item are not independent confirmations; multiplying them as if they were can create false certainty. Position size should reflect calibrated confidence and downside, not the rhetorical precision of a model output.

## Key Claims
- Trades express probability differences, not certainty about a single future.
- Apparent edge must be compared with the market's implied view and reduced by transaction costs.
- Model confidence requires outcome-based calibration before it can guide risk.
- Shared evidence makes multiple judgments correlated rather than independent.
- Position size should respond to calibrated confidence, payoff, and loss tolerance.
- Bare probability outputs are better suited to low-risk triage than to complete investment decisions.

## Evidence
### Probability and price
- [[ai-trading-juece-pianyi-xingdong-hengui-duitan-chao-3w-star-vibe-trading-zuozhe-haozhe-luz0eizpk9v3nz94iuutp1z9xj25]] describes asset price as a weighted view of possible futures and locates opportunity in a probability gap after costs.

### Confidence and sizing
- [[ai-trading-juece-pianyi-xingdong-hengui-duitan-chao-3w-star-vibe-trading-zuozhe-haozhe-luz0eizpk9v3nz94iuutp1z9xj25]] says conviction should match position size while identifying model calibration as an unresolved problem.

### Dependence and explanation
- [[ai-trading-juece-pianyi-xingdong-hengui-duitan-chao-3w-star-vibe-trading-zuozhe-haozhe-luz0eizpk9v3nz94iuutp1z9xj25]] warns that judgments sharing one news source cannot be multiplied as independent probabilities and that unexplained numbers are difficult to trust through losses.

## Counterevidence & Qualifications
- Market-implied probabilities are difficult to extract from ordinary asset prices because discount rates, risk premia, liquidity, and multiple scenarios are entangled.
- Historical calibration can break under regime change, manipulation, or changes in the model and data pipeline.
- Good calibration does not guarantee profit when payoffs are asymmetric, costs are underestimated, or positions are too large.

## What Changed
- Added a trading-specific calibration model linking confidence to market pricing, dependence, costs, and sizing.

## Related Concepts
- [[PositionSizing]] - converts probability and payoff beliefs into bounded exposure.
- [[MarketEfficiency]] - determines how quickly probability-relevant public information enters price.
- [[FinancialDataAlignment]] - prevents false calibration from mismatched or dependent evidence.
- [[InvestmentRiskManagement]] - sets portfolio and loss boundaries around probabilistic decisions.
- [[AITrading]] - research workflow in which probability output remains one gated input rather than a final command.
