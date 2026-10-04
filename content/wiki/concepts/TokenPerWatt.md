---
title: "Token per Watt"
type: concept
knowledge_schema: synthesis-v1
tags: [ai, infrastructure, energy, semiconductors]
sources:
  - e230-1-wan-yi-shouru-yuqi-beihou-yingweida-de-dianfeng-yu-ruanlei-d97446f1-d6e3-4894-89d1-dca0a362b10b
  - guochan-ai-suanli-neng-ping-chaojiedian-wandao-chaoche-ma-waic-shendu-guancha-s10e23-a6c6ab3e-72b2-470b-aefd-04b19679d37f
  - ep-36-nvidia-gtc-2026-everything-that-matters-recapped
last_updated: 2026-10-05
---

# Token per Watt

## Definition
Token per watt is an AI-infrastructure efficiency metric that relates delivered model-token output to energy input, shifting attention from peak chip specifications toward useful serving work under power constraints.

## Current Synthesis
Across the sources, token per watt is a system metric rather than a chip-only benchmark. Memory movement, interconnect, cooling, utilization, software, workload mix, and rack deployment all affect how much usable inference a given power envelope can deliver. It is especially useful for comparing large systems whose aggregate compute rises by adding accelerators, but it remains incomplete unless token quality, latency, task success, cost, and total facility energy are specified.

## Key Claims
- Token per watt shifts evaluation from raw FLOPS or chip counts toward delivered AI work under energy constraints.
- Memory movement, communication, cooling, utilization, and software can dominate effective system efficiency.
- Larger supernodes can increase aggregate compute while worsening power efficiency.
- Inference- and agent-oriented platforms make continuous output efficiency more economically important.
- Better efficiency can expand total demand, so lower energy per token does not guarantee lower aggregate energy use.

## Evidence
### Nvidia infrastructure framing
- [[e230-1-wan-yi-shouru-yuqi-beihou-yingweida-de-dianfeng-yu-ruanlei-d97446f1-d6e3-4894-89d1-dca0a362b10b]] uses token per watt to interpret Nvidia's shift from isolated GPU performance toward full-stack token production.
- [[ep-36-nvidia-gtc-2026-everything-that-matters-recapped]] presents useful intelligence output per watt as a planning metric for Vera Rubin and the broader inference economy.

### Supernode comparison
- [[guochan-ai-suanli-neng-ping-chaojiedian-wandao-chaoche-ma-waic-shendu-guancha-s10e23-a6c6ab3e-72b2-470b-aefd-04b19679d37f]] uses higher-power domestic supernodes to show why aggregate compute alone cannot establish system efficiency or competitive catch-up.

## Counterevidence & Qualifications
- Tokens are not uniform units of value across models, modalities, context lengths, quality levels, or tasks.
- Vendor claims may omit facility overhead, utilization, networking, cooling, or workload assumptions.
- A system can improve tokens per watt while increasing total electricity consumption through greater usage.
- Energy efficiency does not resolve supply, latency, reliability, capital cost, or data-center power availability.

## What Changed
- Migrated the concept to the synthesis-v1 schema.
- Added the GTC recap's inference-economy and enterprise-planning interpretation.
- Clarified that output quality and total facility boundaries are necessary for meaningful comparison.

## Related Concepts
- [[AIInferenceCostStructure]] - economic structure that energy efficiency helps determine.
- [[InferenceAsCashFlow]] - recurring-demand thesis that makes serving efficiency important.
- [[DataCenterPowerBottleneck]] - physical limit motivating output-per-energy metrics.
- [[DataCenterThermalManagement]] - facility overhead affecting realized efficiency.
- [[AIInfrastructureFullStackMoat]] - system integration layer behind delivered rather than theoretical output.
- [[JevonsParadoxInAI]] - demand response that can offset per-token efficiency gains.
- [[AIAcceleratorSupernode]] - system scale where raw compute and energy efficiency can diverge.
