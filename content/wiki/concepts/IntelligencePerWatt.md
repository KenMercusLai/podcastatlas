---
title: "Intelligence Per Watt"
type: concept
tags: [ai, energy-efficiency, hardware, benchmarking]
knowledge_schema: synthesis-v1
sources:
  - all-in-with-chamath-jason-sacks-friedberg-naveen-rao-4d-computing-ais-energy-wall-beating-biology-42983573
last_updated: 2026-10-04
---

# Intelligence Per Watt

## Definition
Intelligence per watt is an objective for maximizing useful, quality-adjusted AI capability or output for each unit of electrical power rather than maximizing raw operations alone.

## Current Synthesis
[[NaveenRao|Naveen Rao]] uses intelligence per watt as the north-star metric for [[UnconventionalAI|Unconventional AI]]. The framing usefully shifts attention from peak FLOPS toward delivered capability, data movement, and energy, especially when power limits deployment. It is not yet a standardized benchmark: "intelligence" must be operationalized through matched tasks, quality, latency, reliability, and system boundaries before different substrates can be compared.

## Key Claims
- Useful model capability per unit energy is more decision-relevant than peak arithmetic throughput when electricity is binding.
- The metric must include output quality and workload fit or low-power but low-quality results can look artificially strong.
- Data movement, memory, networking, conversion, cooling, and idle overhead can materially change end-to-end results.
- Biological brains motivate the target but do not supply a task-equivalent benchmark by themselves.
- Large efficiency gains can enable local, distributed, or robotic AI where centralized data-center power is unavailable.
- Lower per-task energy may increase aggregate use through [[JevonsParadoxInAI|Jevons paradox]].

## Evidence
- Optimization target: [[all-in-with-chamath-jason-sacks-friedberg-naveen-rao-4d-computing-ais-energy-wall-beating-biology-42983573]] explicitly presents intelligence per watt as the company's central goal.
- Prototype claim: [[all-in-with-chamath-jason-sacks-friedberg-naveen-rao-4d-computing-ais-energy-wall-beating-biology-42983573]] reports approximately 500 nanojoules per generated image and a long-term 1,000-fold efficiency ambition.
- Deployment implications: [[all-in-with-chamath-jason-sacks-friedberg-naveen-rao-4d-computing-ais-energy-wall-beating-biology-42983573]] connects higher efficiency to smaller distributed facilities and energy-constrained robots.

## Counterevidence & Qualifications
There is no universal unit of intelligence, and benchmark selection can hide accuracy, diversity, latency, training, memory, host-system, cooling, or manufacturing costs. The source's prototype number lacks an independent matched comparison and full measurement boundary. A large device-level gain may shrink after model conversion and system integration, while lower cost can raise total electricity demand rather than reduce it.

## What Changed
- Created the concept as a quality-adjusted objective rather than accepting a raw company performance number.
- Added explicit workload, measurement-boundary, and rebound-demand requirements.

## Related Concepts
- [[AIInferenceCostStructure]] - economic measure of serving cost that energy efficiency can alter.
- [[AIDataMovementEnergyCost]] - architectural component that can dominate power use.
- [[PhysicalDynamicalComputing]] - substrate proposed to improve the metric.
- [[BiologicalProcessorEnergyEfficiency]] - biological benchmark and alternative-substrate context.
- [[DataCenterPowerBottleneck]] - infrastructure constraint that makes per-watt capability valuable.
- [[JevonsParadoxInAI]] - rebound effect that can offset aggregate energy savings.
