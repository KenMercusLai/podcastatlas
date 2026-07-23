---
title: "Token per Watt"
type: concept
tags: [ai, infrastructure, energy, semiconductors]
sources: [e230-1-wan-yi-shouru-yuqi-beihou-yingweida-de-dianfeng-yu-ruanlei-d97446f1-d6e3-4894-89d1-dca0a362b10b]
last_updated: 2026-07-23
---

# Token per Watt

Token per watt is the efficiency metric foregrounded in [[e230-1-wan-yi-shouru-yuqi-beihou-yingweida-de-dianfeng-yu-ruanlei-d97446f1-d6e3-4894-89d1-dca0a362b10b]] through [[Nvidia]]'s GTC messaging. The episode treats it as a sign that AI infrastructure is being measured by usable token output per energy input, not only by FLOPS, chip count, or benchmark speed.

The metric matters because [[AIInferenceCostStructure]] increasingly depends on power, cooling, memory movement, and data-center deployment. In the source, [[NvidiaBlackwellPlatform|Blackwell]] and [[NvidiaVeraRubinPlatform|Vera Rubin]] efficiency claims only become useful if they translate into lower cost and higher throughput inside real [[MaaSInfrastructure]] environments.

## Key Claims
- Token-per-watt shifts attention from raw accelerator specs to delivered AI work under energy constraints.
- The metric links model-serving economics to [[DataCenterPowerBottleneck|data-center power bottlenecks]] and [[DataCenterThermalManagement]].
- Communication and memory movement can reduce effective token-per-watt even when arithmetic units are fast.
- Token efficiency can increase total demand if it enables more agents and applications to run continuously.

## Connections
- [[Nvidia]], [[GPU]], [[NvidiaBlackwellPlatform]], and [[NvidiaVeraRubinPlatform]] - platform and product context.
- [[AIInferenceCostStructure]], [[InferenceAsCashFlow]], and [[JevonsParadoxInAI]] - demand and cost interpretation.
- [[DataCenterPowerBottleneck]], [[DataCenterThermalManagement]], and [[MaaSInfrastructure]] - physical serving constraints.
