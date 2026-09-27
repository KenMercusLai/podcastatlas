---
title: "Decision–Action Cost Asymmetry / 决策—行动成本不对称"
type: concept
tags: [ai, decision-making, trading, risk]
sources:
  - ai-trading-juece-pianyi-xingdong-hengui-duitan-chao-3w-star-vibe-trading-zuozhe-haozhe-luz0eizpk9v3nz94iuutp1z9xj25
knowledge_schema: synthesis-v1
last_updated: 2026-09-28
---

# Decision–Action Cost Asymmetry / 决策—行动成本不对称

## Definition
Decision–action cost asymmetry is the condition in which AI can generate opinions and candidate decisions at near-zero marginal cost while real action still consumes capital, creates exposure, and assigns responsibility for irreversible consequences.

## Current Synthesis
In many AI workflows execution becomes cheap while deciding what to do remains scarce. The source argues that finance can invert this pattern: markets already contain abundant forecasts, opinions, and recommendations, and models make them cheaper still, but every trade commits money and creates downside.

The appropriate design response is an asymmetric funnel. Generate widely, verify aggressively, act rarely, bound each action, and preserve a named decision owner. Systems fail when they turn every cheap judgment into a trade and create overtrading, or when excessive caution blocks every action without an intelligible reason.

## Key Claims
- Lowering the cost of a decision does not lower the cost of being wrong in action.
- Decision volume should be much larger than action volume in high-stakes systems.
- Every permitted action needs a reason, risk boundary, and accountable owner.
- Constraint systems create value by refusing or narrowing action, not only by improving model output.
- A useful system must explain both why it acted and why it stopped.

## Evidence
### Financial asymmetry
- [[ai-trading-juece-pianyi-xingdong-hengui-duitan-chao-3w-star-vibe-trading-zuozhe-haozhe-luz0eizpk9v3nz94iuutp1z9xj25]] contrasts abundant, low-cost market judgments with the real cost of capital allocation, loss, and responsibility.

### System-design consequence
- [[ai-trading-juece-pianyi-xingdong-hengui-duitan-chao-3w-star-vibe-trading-zuozhe-haozhe-luz0eizpk9v3nz94iuutp1z9xj25]] defines a good system as one that produces many candidate decisions but executes few, each with a reason, boundary, and responsible person.

### Failure modes
- [[ai-trading-juece-pianyi-xingdong-hengui-duitan-chao-3w-star-vibe-trading-zuozhe-haozhe-luz0eizpk9v3nz94iuutp1z9xj25]] identifies overtrading and unexplained paralysis as opposite failures of the decision-to-action gate.

## Counterevidence & Qualifications
- Some financial decisions are costly to formulate when they require proprietary data, expert labor, infrastructure, or regulatory review; the asymmetry is strongest at the marginal generation layer.
- Inaction also has opportunity cost, so “act rarely” is not a universal preference for passivity.
- A human approval click is not meaningful accountability when the reviewer cannot inspect the evidence or is overwhelmed by decision volume.

## What Changed
- Added a general control principle for systems in which generated judgments scale faster than accountable action.

## Related Concepts
- [[AITrading]] - financial system design built around the asymmetry.
- [[AgentTrustCalibration]] - expands autonomy only as evidence and safeguards justify it.
- [[HumanJudgmentUnderAI]] - preserves responsibility for high-stakes contextual decisions.
- [[InvestmentRiskManagement]] - translates action cost into portfolio limits and loss discipline.
- [[PositionSizing]] - controls how much capital a permitted action can expose.
