---
title: "OpenRouter"
type: entity
tags: [ai, infrastructure, model-routing]
sources:
  - vol-172-codex-mai-zhongzhi-taocan-deepseek-fenggu-tiaojia-pingguo-chonghui-5-wanyi-deng-1-6685-1
  - all-in-with-chamath-jason-sacks-friedberg-more-trillion-dollar-ipos-anthropic-3t-zucks-price-war-china-ends-open-source-trump-accounts-42041390
  - featherless-ai-when-your-weekend-experiment-makes-more-than-your-startup
  - e246-hewei-zhengliu-liaoliao-guigu-ruhe-kan-zhongguo-kaifang-moxing-bijin-qianyan-5fd236d7-9a72-4b15-9e84-e83ceadd1b41
  - e258-liaoliao-guigu-chuangye-xiudaoyuan-hf0-yu-openrouter-zaoqi-gushi-f6618818-b288-4798-bab8-d60d77c70aff
last_updated: 2026-11-10
knowledge_schema: synthesis-v1
---

# OpenRouter

## Overview
OpenRouter is model-routing and API aggregation infrastructure that gives developers a common interface across multiple model providers.

## Current Profile
The source set places OpenRouter between model builders, hosted inference providers, and developers. Its value grows when open and closed models differ across capability, price, latency, policy, and availability, because one interface lowers the cost of changing the underlying model. [[FeatherlessAI|Featherless AI]] clarifies the layer boundary: Featherless hosts models, while OpenRouter routes requests to providers.

The new early-company account adds product formation. [[GuoJingACEStudio|郭靖]] says a small team initially considered a consumer model interface but found stronger developer demand for a unified API, then focused on integrating models quickly and reliably. As developer use accumulated, providers gained reasons to join for distribution, tests, usage, and leaderboard visibility. This supports a two-sided first-mover thesis, although price, reliability, provider dependence, and model portability continue to limit the moat.

## Key Characteristics
- Offers a common developer interface across diverse model providers.
- Lowers model-switching friction without making models fully fungible.
- Benefits from strong open and closed models coexisting at different price and performance points.
- Acts as a usage and willingness-to-pay signal across the model market.
- Depends on provider hosting rather than necessarily hosting every model itself.
- May gain two-sided network effects as developers attract providers and provider breadth attracts developers.

## Evidence
- Routing-market role - [[e246-hewei-zhengliu-liaoliao-guigu-ruhe-kan-zhongguo-kaifang-moxing-bijin-qianyan-5fd236d7-9a72-4b15-9e84-e83ceadd1b41]] uses OpenRouter as an intermediary that benefits from open and closed model diversity.
- Buyer-side cost role - [[all-in-with-chamath-jason-sacks-friedberg-more-trillion-dollar-ipos-anthropic-3t-zucks-price-war-china-ends-open-source-trump-accounts-42041390]] reports a source-scoped example of routing choices reducing model costs by roughly 95%.
- Layer boundary - [[featherless-ai-when-your-weekend-experiment-makes-more-than-your-startup]] distinguishes OpenRouter's routing from Featherless AI's direct model hosting.
- Market-signal role - [[vol-172-codex-mai-zhongzhi-taocan-deepseek-fenggu-tiaojia-pingguo-chonghui-5-wanyi-deng-1-6685-1]] describes OpenRouter as both switching infrastructure and evidence of which models users pay to use.
- Product formation - [[e258-liaoliao-guigu-chuangye-xiudaoyuan-hf0-yu-openrouter-zaoqi-gushi-f6618818-b288-4798-bab8-d60d77c70aff]] says developer demand redirected the early product toward a unified API and rapid, stable model integration.
- Network-effect thesis - [[e258-liaoliao-guigu-chuangye-xiudaoyuan-hf0-yu-openrouter-zaoqi-gushi-f6618818-b288-4798-bab8-d60d77c70aff]] links developer aggregation to provider distribution, real usage, and leaderboard visibility.

## Qualifications
Model switching remains constrained by differences in memory, context, behavior, harnesses, reliability, and provider policy. Cost-savings, early team behavior, product history, token growth, rankings, and first-mover advantage are source-scoped rather than audited. A competitor offering materially lower prices or better reliability could weaken interface-based advantage, and provider concentration can transmit upstream failures.

## What Changed
- Added an early product-formation account centered on developer demand for a unified API.
- Added a two-sided distribution and usage-data mechanism to the existing routing-market profile.
- Preserved provider dependence, price competition, and model-fungibility limits.

## Relationships
- [[ModelRoutingCostControl]] - operational practice OpenRouter enables.
- [[AIInferenceCostStructure]] - economic layer that makes routing valuable.
- [[FeatherlessAI]] - hosted inference provider that clarifies OpenRouter's routing-layer role.
- [[OpenSourceAIModels]] - model diversity that increases routing value.
- [[ClosedModelAPIMoatPressure]] - market pressure created when customers can switch across providers.
- [[HF0]] - residential accelerator context for the early-company account.
