---
title: "Token per Watt"
type: concept
tags: [ai, infrastructure, energy, semiconductors]
sources: [e230-1-wan-yi-shouru-yuqi-beihou-yingweida-de-dianfeng-yu-ruanlei-d97446f1-d6e3-4894-89d1-dca0a362b10b, guochan-ai-suanli-neng-ping-chaojiedian-wandao-chaoche-ma-waic-shendu-guancha-s10e23-a6c6ab3e-72b2-470b-aefd-04b19679d37f]
last_updated: 2026-08-07
---

# Token per Watt

Token per watt is the efficiency metric foregrounded in [[e230-1-wan-yi-shouru-yuqi-beihou-yingweida-de-dianfeng-yu-ruanlei-d97446f1-d6e3-4894-89d1-dca0a362b10b]] through [[Nvidia]]'s GTC messaging. The episode treats it as a sign that AI infrastructure is being measured by usable token output per energy input, not only by FLOPS, chip count, or benchmark speed.

The metric matters because [[AIInferenceCostStructure]] increasingly depends on power, cooling, memory movement, and data-center deployment. In the source, [[NvidiaBlackwellPlatform|Blackwell]] and [[NvidiaVeraRubinPlatform|Vera Rubin]] efficiency claims only become useful if they translate into lower cost and higher throughput inside real [[MaaSInfrastructure]] environments.

[[guochan-ai-suanli-neng-ping-chaojiedian-wandao-chaoche-ma-waic-shendu-guancha-s10e23-a6c6ab3e-72b2-470b-aefd-04b19679d37f]] adds the domestic [[AIAcceleratorSupernode|supernode]] tradeoff. A system such as [[HuaweiCM384]] can post higher aggregate compute than [[NvidiaGB200NVL72|NVL72]] while using far more total power, so token-per-watt helps distinguish usable efficiency from raw system size.

## Key Claims
- Token-per-watt shifts attention from raw accelerator specs to delivered AI work under energy constraints.
- The metric links model-serving economics to [[DataCenterPowerBottleneck|data-center power bottlenecks]] and [[DataCenterThermalManagement]].
- Communication and memory movement can reduce effective token-per-watt even when arithmetic units are fast.
- Token efficiency can increase total demand if it enables more agents and applications to run continuously.
- Supernode catch-up needs token-per-watt discipline because adding accelerators can raise compute and power at the same time.

## Connections
- [[Nvidia]], [[GPU]], [[NvidiaBlackwellPlatform]], and [[NvidiaVeraRubinPlatform]] - platform and product context.
- [[AIInferenceCostStructure]], [[InferenceAsCashFlow]], and [[JevonsParadoxInAI]] - demand and cost interpretation.
- [[DataCenterPowerBottleneck]], [[DataCenterThermalManagement]], and [[MaaSInfrastructure]] - physical serving constraints.
- [[HuaweiCM384]], [[NvidiaGB200NVL72]], and [[DomesticAIChipOrderValidation]] - WAIC source's supernode efficiency comparison.
