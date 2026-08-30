---
title: "High Bandwidth Memory"
type: concept
tags: [ai, semiconductors, memory, infrastructure]
knowledge_schema: synthesis-v1
sources:
  - tech-20260123-0123-mp-tech-pod-128-tech-20260123-0123-mp-tech-pod-128
  - tech-20260113-0113-mp-tech-pod-128-tech-20260113-0113-mp-tech-pod-128
  - e230-1-wan-yi-shouru-yuqi-beihou-yingweida-de-dianfeng-yu-ruanlei-d97446f1-d6e3-4894-89d1-dca0a362b10b
  - tech-20251219-1219-mp-tech-pod-128-tech-20251219-1219-mp-tech-pod-128
  - cunchu-sanjutou-po-wanyi-shizhi-cunchu-chaoji-zhouqi-heshi-neng-jianding-s10e13-c47ff830-8cb5-4e58-b7d7-1a04e4e5a4c1
  - ep270-yi-mei-xinpian-de-manchang-zhengtu-women-li-suanli-ziyou-haiyou-duoyuan-lm7lxlmcnjwnawtq-9typc-fnrci
  - e228-guge-tpu-neng-handong-yingweida-ma-qian-tpu-gongchengshi-shouci-jiemi-fd17090c-0d72-4c0d-aa3e-9b00bc062149
  - all-in-with-chamath-jason-sacks-friedberg-socialists-sweep-nyc-china-catches-up-in-coding-ai-memory-crunch-microns-blowout-quarter-41835335
last_updated: 2026-08-31
---

# High Bandwidth Memory

## Definition
High bandwidth memory is stacked, high-throughput memory placed close to AI accelerators so models can move parameters, activations, and inference cache data fast enough for training and inference workloads.

## Current Synthesis
HBM is now one of the wiki's clearest physical AI bottlenecks. Marketplace sources explain that AI chips need fast memory close to accelerators and that supply is concentrated among [[MicronTechnology|Micron Technology]], [[SKHynix|SK Hynix]], and [[Samsung]]. Technical sources add that HBM sits inside a wider memory hierarchy with advanced packaging, memory-wall pressure, CXL, flash, and accelerator roadmaps. The new All-In episode sharpens the market-cycle view: 8-high stacks are moving toward 12- and 16-high stacks, Micron's 2026 supply is described as sold out, and [[GavinBaker|Gavin Baker]] calls DRAM/HBM capacity one of AI's most important bottlenecks.

## Key Claims
- AI acceleration depends on fast memory bandwidth and capacity as well as raw compute.
- HBM demand can lift memory suppliers such as [[MicronTechnology]], [[SKHynix]], and [[Samsung]] when AI data-center buildout accelerates.
- Supplier concentration, advanced packaging, yield, and fab capital intensity make HBM shortages hard to solve quickly.
- HBM demand is intensified by inference, long-context KV cache, and larger model-memory footprints, not only training.
- AI memory demand can spill into consumer markets by changing product focus, capacity allocation, and pricing.
- Alternative memory architectures can improve utilization but do not replace HBM in the hottest low-latency layer in the source set.
- Local fab expansion can make HBM capacity a community-benefit, water, emissions, labor, and land-use issue.

## Evidence
- Public explanation and consumer spillover: [[tech-20260113-0113-mp-tech-pod-128-tech-20260113-0113-mp-tech-pod-128]] says HBM is needed to train and run AI, is paired with [[Nvidia]] chips, and can create shortages for other memory-using products.
- Supplier and manufacturing governance: [[tech-20260123-0123-mp-tech-pod-128-tech-20260123-0123-mp-tech-pod-128]] places Micron among the few HBM suppliers and uses [[MicronClayMegaFab|Micron's planned Clay mega fab]] to surface jobs, wetlands, emissions, and water commitments.
- Component role and scale: [[tech-20251219-1219-mp-tech-pod-128-tech-20251219-1219-mp-tech-pod-128]] uses Micron and Nvidia GB200 memory capacity to show why HBM is part of [[AIHardwareSupplyChainPressure]] rather than only a specification.
- Architecture and alternatives: [[cunchu-sanjutou-po-wanyi-shizhi-cunchu-chaoji-zhouqi-heshi-neng-jianding-s10e13-c47ff830-8cb5-4e58-b7d7-1a04e4e5a4c1]] places HBM in [[AIDataCenterMemoryHierarchy]] and contrasts it with [[HighBandwidthFlash]], [[CXLMemoryPooling]], and NAND+DPU prefetching.
- Packaging and memory wall: [[ep270-yi-mei-xinpian-de-manchang-zhengtu-women-li-suanli-ziyou-haiyou-duoyuan-lm7lxlmcnjwnawtq-9typc-fnrci]] links HBM to [[AdvancedPackaging]] and the [[MemoryWall]].
- Platform ramp risk: [[e230-1-wan-yi-shouru-yuqi-beihou-yingweida-de-dianfeng-yu-ruanlei-d97446f1-d6e3-4894-89d1-dca0a362b10b]] makes HBM4/HBM4e an assumption behind Nvidia platform volume, while [[e228-guge-tpu-neng-handong-yingweida-ma-qian-tpu-gongchengshi-shouci-jiemi-fd17090c-0d72-4c0d-aa3e-9b00bc062149]] makes HBM supply a ceiling for TPU expansion.
- New market-cycle update: [[all-in-with-chamath-jason-sacks-friedberg-socialists-sweep-nyc-china-catches-up-in-coding-ai-memory-crunch-microns-blowout-quarter-41835335]] says Micron's 2026 HBM supply is sold out and frames stacked DRAM/HBM capacity as the most important AI bottleneck in Baker's view.

## Counterevidence & Qualifications
HBM is a bottleneck but not the only one: advanced packaging, GPUs, networking, power, cooling, site readiness, and demand timing all affect delivered AI capacity. Some source figures are product or market commentary rather than filings. Memory is cyclical, so supplier strength can reverse if supply catches demand or AI capex slows.

## What Changed
- Migrated the page to the synthesis-first concept schema.
- Added Micron's All-In quarter and sold-out 2026 supply as source-scoped evidence.
- Added stacked DRAM progression from 8-high to 12- and 16-high HBM stacks.
- Elevated inference and consumer-device spillover in the current synthesis.

## Related Concepts
- [[MicronTechnology]] - supplier case and new quarter signal.
- [[AIHardwareSupplyChainPressure]] - broader supply-chain implication of memory scarcity.
- [[AIDataCenterMemoryHierarchy]] - architecture frame that locates HBM in the low-latency layer.
- [[MemoryWall]] - compute limit HBM helps address.
- [[AdvancedPackaging]] - manufacturing requirement for stacked memory near accelerators.
- [[MemoryChipShortage]] - consumer-market spillover from AI demand.
- [[DataCenterPowerBottleneck]] - adjacent physical constraint on delivered AI capacity.
