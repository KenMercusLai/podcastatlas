---
title: "Financial Market Non-Stationarity / 金融市场非平稳性"
type: concept
tags: [finance, machine-learning, markets, model-risk]
sources:
  - e259-jixie-shenjiao-yu-fanrenxing-celve-huaerjie-lianghua-jutou-de-ai-zhilu-bc105fa7-23de-4c70-a338-6d70daf9aed1
knowledge_schema: synthesis-v1
last_updated: 2026-11-23
---

# Financial Market Non-Stationarity / 金融市场非平稳性

## Definition

Financial market non-stationarity is the condition in which the data-generating process changes over time because participants, regimes, information, rules, liquidity, and strategies change.

## Current Synthesis

The source treats non-stationarity as a fundamental difference between finance and stable benchmark domains. A model may receive reliable feedback only after weeks, months, or years, yet the opportunity being studied can disappear sooner. Participants also adapt and conceal information, so deployment changes the environment being modeled. Validation must therefore cover multiple regimes without pretending that long histories make the future stationary.

## Key Claims

- Historical relationships can weaken when market participants, rules, or conditions change.
- Slow and noisy rewards can arrive after the target regime has ended.
- More rows do not guarantee more evidence when observations share underlying causes.
- Strategy deployment can alter prices and reduce the opportunity being predicted.
- Long backtests improve regime coverage but cannot prove future stability.
- Continual monitoring and differentiated research are necessary because the benchmark never ends.

## Evidence

- **Feedback mismatch:** [[e259-jixie-shenjiao-yu-fanrenxing-celve-huaerjie-lianghua-jutou-de-ai-zhilu-bc105fa7-23de-4c70-a338-6d70daf9aed1]] notes that a four-week improvement cycle can lag a market state lasting only two weeks.
- **Adaptive environment:** [[e259-jixie-shenjiao-yu-fanrenxing-celve-huaerjie-lianghua-jutou-de-ai-zhilu-bc105fa7-23de-4c70-a338-6d70daf9aed1]] describes markets as partly observed strategic systems in which participants hide information and trades affect prices.
- **Validation boundary:** [[e259-jixie-shenjiao-yu-fanrenxing-celve-huaerjie-lianghua-jutou-de-ai-zhilu-bc105fa7-23de-4c70-a338-6d70daf9aed1]] favors multi-year testing across states while acknowledging delayed, confounded feedback.

## Counterevidence & Qualifications

Non-stationarity does not imply that no regularity persists or that modeling is futile. Some mechanisms may remain stable enough to exploit, especially when updated and diversified. The episode offers conceptual and practitioner reasoning, not a formal test of how quickly particular markets or signals change.

## What Changed

- Made feedback delay, adaptive participants, and regime duration explicit within the wiki's market-change branch.

## Related Concepts

- [[MarketRegimeShift]] - discrete or salient change within the broader non-stationary process.
- [[AlphaDecay]] - weakening of a particular signal through crowding, adaptation, or changed conditions.
- [[QuantitativeOverfitting]] - confusion of historical fit with durable structure.
- [[FinancialAIQuantitativeTrading]] - modeling domain constrained by changing data generation.
- [[QuantitativeResearchDiscipline]] - process for monitoring and revising claims under change.
