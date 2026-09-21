---
title: "Technology Reuse and Scenario Adaptation / 技术复用与场景适配"
type: concept
tags: [product-strategy, robotics, consumer-hardware, capability-reuse]
sources:
  - shangye-xiaoyang-50-dou-zai-taolun-jiawu-jiqiren-buru-guanxin-daodi-you-shenme-jiawu-1017031596
last_updated: 2026-09-21
knowledge_schema: synthesis-v1
---

# Technology Reuse and Scenario Adaptation / 技术复用与场景适配

## Definition
Technology reuse and scenario adaptation is a product-development model in which a company carries a mature capability stack into an adjacent use case while separately engineering the environmental, safety, interaction, and market requirements that do not transfer.

## Current Synthesis
[[shangye-xiaoyang-50-dou-zai-taolun-jiawu-jiqiren-buru-guanxin-daodi-you-shenme-jiawu-1017031596|商业小样50]] expresses the model through [[QianChengEcovacs|Qian Cheng]]'s "80% technology reuse, 20% scenario migration" formula. [[EcovacsRobotics|Ecovacs]] can reuse perception, mapping, path planning, and motion control from floor-cleaning robots, yet a window robot still needs continuous adhesion and fall protection, a lawn robot needs outdoor positioning and animal avoidance, and a pool robot needs underwater durability.

The ratio is best read as a strategic heuristic, not a measured engineering law. Its strongest insight is that the smaller non-reusable remainder may determine whether the product works at all. Scenario adaptation also includes local housing patterns, channels, teams, and customer habits, so commercial transfer is broader than technical porting.

## Key Claims
- A reusable capability stack can reduce the cost and uncertainty of entering adjacent categories.
- The non-reusable remainder often contains safety-critical or product-defining work.
- Shared surface features do not make environments equivalent; orientation, weather, water, terrain, animals, and maintenance change the system requirements.
- Scenario migration includes demand discovery, channels, and local organizational knowledge as well as engineering.
- Repeatedly executing the reuse-and-adaptation cycle can become a stronger moat than any individual feature.

## Evidence
- **Reusable core:** [[shangye-xiaoyang-50-dou-zai-taolun-jiawu-jiqiren-buru-guanxin-daodi-you-shenme-jiawu-1017031596|商业小样50]] identifies sensing, mapping, path planning, and movement control across Ecovacs products.
- **Safety-critical adaptation:** [[shangye-xiaoyang-50-dou-zai-taolun-jiawu-jiqiren-buru-guanxin-daodi-you-shenme-jiawu-1017031596|商业小样50]] uses window adhesion, secure movement, and synchronized wiping to show why vertical operation is not simply floor cleaning turned sideways.
- **Environmental adaptation:** [[shangye-xiaoyang-50-dou-zai-taolun-jiawu-jiqiren-buru-guanxin-daodi-you-shenme-jiawu-1017031596|商业小样50]] says GOAT must handle trees, slopes, positioning interference, and small animals, while ULTRAMARINE must tolerate underwater corrosion.
- **Market adaptation:** [[shangye-xiaoyang-50-dou-zai-taolun-jiawu-jiqiren-buru-guanxin-daodi-you-shenme-jiawu-1017031596|商业小样50]] uses European garden size and German channel behavior to show that local product-market fit cannot be inferred from total category demand alone.

## Counterevidence & Qualifications
- The 80/20 division is a source-attributed management model, not an independently measured allocation of engineering effort.
- Adjacent-category reuse does not prove profitability, and a shared technology base can tempt a company into markets where distribution, support, liability, or demand is weak.
- The bounded source focuses on one sponsor company and provides little evidence from competitors or failed transfers.

## What Changed
- Created the concept from the Ecovacs window, lawn, and pool-cleaning cases.
- Expanded "scenario" beyond engineering to include local demand, channels, and organization.

## Related Concepts
- [[HomeServiceRobots]] - household category where chore-specific adaptation can beat form-factor novelty.
- [[RobotFormFactorPragmatism]] - embodiment should follow task and environment requirements.
- [[LocalizedProductDefinition]] - local use conditions determine which product changes matter.
- [[GlobalProductLocalization]] - extends adaptation into organization, channels, culture, regulation, and service.
- [[SlowProductMarketFit]] - long iteration may be required before an adapted category reaches demand maturity.
- [[ConsumerBrandMoat]] - repeated product and market execution can become a system-level moat.
