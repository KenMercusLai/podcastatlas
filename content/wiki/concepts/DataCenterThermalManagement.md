---
title: "Data Center Thermal Management"
type: concept
tags: [infrastructure, ai, data-centers, cooling]
sources: [shangye-xiaoyang-43-ai-shidai-shui-zai-gei-fuwuqi-jiangwen-992085076, kate-crawford-mapping-empires]
last_updated: 2026-07-10
---

# Data Center Thermal Management

Data center thermal management is the system of removing, transporting, exchanging, and controlling heat so compute equipment can run safely and efficiently. [[shangye-xiaoyang-43-ai-shidai-shui-zai-gei-fuwuqi-jiangwen-992085076]] adds this as the cooling-specific layer of the wiki's AI infrastructure synthesis: dense GPU racks make heat removal a limiting condition for [[AIComputeContinuity]], [[MaaSInfrastructure]], and [[DataCenterPhysicalResilience]].

The source frames the shift from air cooling toward liquid and water-based systems as a response to higher rack power density. Thermal management is not only a mechanical-design problem; it also includes pumps, variable-frequency control, temperature and pressure sensing, water treatment, heat exchange, maintenance, and energy optimization.

[[kate-crawford-mapping-empires]] adds the water-politics layer. [[KateCrawford]] treats data-center cooling as part of [[AIMetabolicInfrastructure]] because freshwater demand, heat, electricity, and local ecological burdens decide who pays for AI capacity.

## Key Claims
- AI data centers behave like compute factories, and factories need thermal systems that match production load.
- Liquid cooling becomes more attractive when air cooling cannot carry enough heat away from dense GPU racks.
- Pumps and control systems matter because cooling demand changes with workload, temperature, pressure, and flow conditions.
- Cooling energy use affects operating cost, so thermal management is an efficiency problem as well as a safety problem.
- Water quality, scaling, and contaminants can degrade equipment over time, making cooling a maintenance and reliability discipline.
- Prefabricated cooling stations can compress deployment time by moving installation and testing off site before final connection.
- Cooling demand is also a public-resource issue when AI data centers require large volumes of freshwater in stressed regions.

## Connections
- [[DataCenterPhysicalResilience]] — cooling failure can interrupt data-center operations even without external attack.
- [[AIComputeContinuity]] — model-serving continuity depends on keeping GPU clusters within thermal limits.
- [[MaaSInfrastructure]] and [[AIInferenceCostStructure]] — token supply has cooling and energy costs beneath API pricing.
- [[HoloAssets]] and [[CAPEXOPEXSubstitution]] — hard infrastructure that absorbs AI-era spending.
- [[Grundfos]] and [[HenanSmartSupercomputingCenter]] — company and project cases used by the source.
- [[AIMetabolicInfrastructure]] and [[JevonsParadoxInAI]] — resource-demand frame added by the Crawford source.
