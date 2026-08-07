---
title: "Huawei CM384"
type: entity
tags: [ai, semiconductors, huawei, infrastructure]
sources: [guochan-ai-suanli-neng-ping-chaojiedian-wandao-chaoche-ma-waic-shendu-guancha-s10e23-a6c6ab3e-72b2-470b-aefd-04b19679d37f]
last_updated: 2026-08-07
---

# Huawei CM384

Huawei CM384 is the domestic [[AIAcceleratorSupernode|AI accelerator supernode]] case highlighted in [[guochan-ai-suanli-neng-ping-chaojiedian-wandao-chaoche-ma-waic-shendu-guancha-s10e23-a6c6ab3e-72b2-470b-aefd-04b19679d37f]]. The source presents it as China's most widely discussed supernode comparison point against [[NvidiaGB200NVL72|Nvidia GB200 NVL72]].

The episode's core tradeoff is scale versus efficiency. CM384 is described as using many more Huawei accelerators to reach higher aggregate BF16 compute than NVL72, while also carrying much higher cited power consumption. That makes CM384 a useful case for [[DomesticAIChipCatchUp]]: system-level design can offset weaker per-chip performance, but the result still has to pass power, cooling, software, and customer-order tests.

## Connections
- [[Huawei]] and [[HiSilicon]] — company and chip-design context.
- [[AIAcceleratorSupernode]] and [[ScaleUpAIInterconnect]] — system category and interconnect logic.
- [[NvidiaGB200NVL72]] — comparison case in the source.
- [[DataCenterPowerBottleneck]], [[DataCenterThermalManagement]], and [[DomesticAIChipOrderValidation]] — constraints that decide whether the system is usable at scale.
