---
title: "Financial Data Alignment / 金融数据对齐"
type: concept
tags: [finance, data-quality, trading, validation]
sources:
  - ai-trading-juece-pianyi-xingdong-hengui-duitan-chao-3w-star-vibe-trading-zuozhe-haozhe-luz0eizpk9v3nz94iuutp1z9xj25
knowledge_schema: synthesis-v1
last_updated: 2026-09-28
---

# Financial Data Alignment / 金融数据对齐

## Definition
Financial data alignment is the process of making values comparable and decision-valid across adjustment conventions, units, currencies, time granularity, markets, source versions, release times, missingness, and shared information dependencies.

## Current Synthesis
The source treats alignment as the core verifier between plausible financial reasoning and a usable trading conclusion. A model can reason fluently while comparing adjusted with unadjusted prices, confusing units, mixing markets or periods, silently accepting missing data, or using values that were not available at the decision time.

Alignment is therefore both semantic and temporal. It asks what a field means, which version was known, whether two series can be compared, and whether several judgments are actually independent or inherit the same upstream source. When the required input is absent, the system should expose the gap and stop rather than complete a backtest with silent substitution.

## Key Claims
- Small unit or convention mismatches can create order-of-magnitude financial errors.
- Market, currency, adjustment, and time-granularity differences must be explicit before comparison.
- Missing data should trigger a visible stop or qualification rather than silent continuation.
- Release time and later revision history are part of a financial value's meaning.
- Shared upstream information can make apparently separate judgments correlated.
- More data does not create alpha unless it makes a specific proposition testable and decision-relevant.

## Evidence
### Semantic alignment
- [[ai-trading-juece-pianyi-xingdong-hengui-duitan-chao-3w-star-vibe-trading-zuozhe-haozhe-luz0eizpk9v3nz94iuutp1z9xj25]] names adjustment method, amount unit, time granularity, and market-specific source as error-prone dimensions.

### Temporal and missingness controls
- [[ai-trading-juece-pianyi-xingdong-hengui-duitan-chao-3w-star-vibe-trading-zuozhe-haozhe-luz0eizpk9v3nz94iuutp1z9xj25]] requires point-in-time availability and says an agent should stop and report a missing input instead of silently completing the test.

### Dependency awareness
- [[ai-trading-juece-pianyi-xingdong-hengui-duitan-chao-3w-star-vibe-trading-zuozhe-haozhe-luz0eizpk9v3nz94iuutp1z9xj25]] warns that multiple conclusions may depend on the same news item, so one upstream error can invalidate an entire chain.

## Counterevidence & Qualifications
- Perfect alignment does not establish causality, robustness, tradability, or profitability.
- Some historical datasets cannot reconstruct every contemporaneous revision, timestamp, or market convention, so residual uncertainty must remain visible.
- Proprietary data may add information, but the source does not show that alignment always dominates exclusivity or model capability.

## What Changed
- Added a finance-specific data-quality model joining semantics, timing, missingness, and dependency structure.

## Related Concepts
- [[PointInTimeBacktesting]] - temporal subset focused on what information existed at the historical decision time.
- [[TradingProbabilityCalibration]] - depends on correctly aligned outcomes and correlated evidence.
- [[AITrading]] - uses alignment as a gate before action.
- [[AIDataReadiness]] - broader organizational foundation for clean, contextualized, governed data.
- [[QuantitativeOverfitting]] - remains possible even after data fields are correctly aligned.
