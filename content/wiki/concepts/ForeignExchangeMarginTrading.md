---
title: "Foreign Exchange Margin Trading / 外汇保证金交易"
type: concept
knowledge_schema: synthesis-v1
tags: [investing, foreign-exchange, leverage, margin, risk]
sources:
  - ep95-fx-zhanshi-jiuliumei-mama-kuidiao-de-qian-wo-yao-qinshou-zhuan-huilai-lgdurd85j7_cbimza4cegor-jfly
last_updated: 2026-10-19
---

# Foreign Exchange Margin Trading / 外汇保证金交易

## Definition

Foreign exchange margin trading is leveraged exposure to changes in a quoted currency pair, with profit and loss settled through the trading account and positions subject to collateral requirements and broker liquidation rules.

## Current Synthesis

EP95 separates the market object from ordinary travel exchange. A pair such as AUD/JPY states the value of one currency in another; opening long exposure benefits from a rise in the quoted relationship, while short exposure benefits from a fall. Closing realizes the result, whereas an open position carries floating profit or loss.

Margin makes a small amount of capital control a larger notional position. That can magnify gains, but it also means an adverse move can consume the account's collateral and trigger [[MarginTradingForcedSelling|forced liquidation]] before a hoped-for reversal. Interest differential or carry may add return, yet currency movement can dominate it.

## Key Claims

- A currency pair is a relative price, not a claim about one currency in isolation.
- Long and short positions allow directional exposure without ordinary physical currency delivery.
- Leverage magnifies account return and loss relative to posted margin.
- Floating loss becomes realized when the trader closes or the broker liquidates the position.
- Carry income is conditional because exchange-rate loss can exceed the interest differential.
- Borrowing outside the account to fund a leveraged derivative stacks debt leverage on market leverage.

## Evidence

### Pair and position mechanics
- [[ep95-fx-zhanshi-jiuliumei-mama-kuidiao-de-qian-wo-yao-qinshou-zhuan-huilai-lgdurd85j7_cbimza4cegor-jfly|EP95]] explains currency quotation, long and short exposure, opening, closing, and floating profit or loss through Kurumi's trades.

### Margin and liquidation
- [[ep95-fx-zhanshi-jiuliumei-mama-kuidiao-de-qian-wo-yao-qinshou-zhuan-huilai-lgdurd85j7_cbimza4cegor-jfly|EP95]] uses a ten-times-leverage example to show how an adverse move can exhaust capital and distinguishes broker liquidation from a voluntary stop.

### Carry and stacked leverage
- [[ep95-fx-zhanshi-jiuliumei-mama-kuidiao-de-qian-wo-yao-qinshou-zhuan-huilai-lgdurd85j7_cbimza4cegor-jfly|EP95]] connects AUD/JPY to interest-rate carry and warns that consumer borrowing or family assets add a second leverage layer.

## Counterevidence & Qualifications

The source is an introductory podcast recap built around a fictional work, not a jurisdiction-specific account agreement. Margin thresholds, negative-balance protection, rollover charges, tax treatment, settlement, and broker conduct vary. The ten-times example is explanatory arithmetic rather than a complete liquidation model, and the episode does not establish that every FX product or participant uses the same leverage.

## What Changed

- Created a reusable mechanics page separating retail FX exposure from ordinary currency exchange.
- Made voluntary stop loss, broker liquidation, carry income, and stacked borrowing distinct risks.

## Related Concepts

- [[MarginTradingForcedSelling]] - collateral failure can turn an adverse move into compulsory closure.
- [[YenCarryTrade]] - funding structure that uses low-cost yen against higher-return assets or currencies.
- [[CarryTradeUnwind]] - reversal process when funding currency, rates, or risk assets move against the trade.
- [[StopLossDiscipline]] - planned voluntary exit before the account reaches broker-imposed limits.
- [[PositionSizing]] - notional exposure must remain survivable relative to available capital.
- [[InvestmentRiskManagement]] - broader separation of leverage, liquidity, required spending, and uncertainty.
