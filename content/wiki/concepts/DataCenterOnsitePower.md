---
title: "Data Center Onsite Power"
type: concept
tags: [ai, data-centers, energy, infrastructure]
knowledge_schema: synthesis-v1
sources:
  - all-in-with-chamath-jason-sacks-friedberg-the-future-of-everything-what-ceos-of-circle-crowdstrike-more-see-coming-in-2026-39870920
  - all-in-with-chamath-jason-sacks-friedberg-inside-americas-ai-strategy-infrastructure-regulation-and-global-competition-39846955
  - tech-20260129-0129-mp-tech-pod-128-tech-20260129-0129-mp-tech-pod-128
  - tsr-s5-davidkirtley-v2-audio-tsr-s5-davidkirtley-v2-audio
  - tech-20260216-0216-mp-tech-pod-128-tech-20260216-0216-mp-tech-pod-128
  - all-in-with-chamath-jason-sacks-friedberg-can-the-ai-industry-regulate-itself-stripe-wants-paypal-china-catches-up-ny-bans-datacenters-42134305
last_updated: 2026-08-28
---

# Data Center Onsite Power

## Definition
Data center onsite power is the pattern where a data-center developer generates, stores, or manages electricity at or near the facility instead of relying only on ordinary grid interconnection and utility supply.

## Current Synthesis
The page now synthesizes onsite power as a deployment workaround, a competitiveness policy, and an industrial constraint shift. Earlier sources show concrete forms: Crusoe's Abilene mix of substation access, onsite gas, and batteries; Caterpillar generators used as primary power; Redwood second-life batteries for off-grid supply; and Helion's speculative fusion-at-customer-site route. The latest All-In source adds the macro pressure: if U.S. electricity capacity is tight and PJM auctions signal scarcity, behind-the-meter power becomes a way for AI data centers to add net supply rather than only compete with households.

The current judgment is that onsite power compresses grid-delay risk but does not eliminate energy politics. It moves the bottleneck from utility interconnection to turbines, batteries, fuel, emissions, maintenance, siting, and public legitimacy. Its strongest strategic role appears when projects add genuinely incremental power and avoid cost shifting.

## Key Claims
- Onsite power can shorten deployment timelines when interconnection queues are too slow for AI compute demand.
- The relevant onsite-power stack includes generation, batteries, substations, fuel logistics, controls, maintenance, and permitting, not only a generator next to a building.
- Behind-the-meter generation can reduce ratepayer conflict only if it adds net supply and does not hide emissions or grid-upgrade costs elsewhere.
- Natural-gas generators often win on speed, while battery storage, geothermal, hydro, nuclear, and fusion routes depend on different maturity and permitting constraints.
- Generator and turbine suppliers become AI infrastructure actors when data centers use their equipment as primary operating power.
- Onsite power is tied to global siting competition because energizable power can command a premium and delayed projects can move to friendlier jurisdictions.
- The approach strengthens [[AIComputeContinuity]] when it is reliable, but weak operations can make power equipment itself the continuity risk.

## Evidence
- Full-stack onsite case: [[all-in-with-chamath-jason-sacks-friedberg-the-future-of-everything-what-ceos-of-circle-crowdstrike-more-see-coming-in-2026-39870920]] describes Crusoe's Abilene project with a large substation, onsite gas generation, batteries, and future clean-power interest.
- Behind-the-meter policy claim: [[all-in-with-chamath-jason-sacks-friedberg-inside-americas-ai-strategy-infrastructure-regulation-and-global-competition-39846955]] argues data centers can add net supply when they build their own power.
- Storage route: [[tech-20260129-0129-mp-tech-pod-128-tech-20260129-0129-mp-tech-pod-128]] adds Redwood Materials and second-life EV batteries as an onsite/off-grid data-center power route.
- Generator route: [[tech-20260216-0216-mp-tech-pod-128-tech-20260216-0216-mp-tech-pod-128]] shows Caterpillar natural-gas generators moving from backup equipment into primary power for some AI data centers.
- Speculative clean route: [[tsr-s5-davidkirtley-v2-audio-tsr-s5-davidkirtley-v2-audio]] presents Helion's plan for generators placed directly at data centers, factories, and manufacturing sites.
- Scarcity and siting claim: [[all-in-with-chamath-jason-sacks-friedberg-can-the-ai-industry-regulate-itself-stripe-wants-paypal-china-catches-up-ny-bans-datacenters-42134305]] links behind-the-meter power to PJM supply stress, possible long-run U.S. power shortages, and premium pricing for energizable data-center sites.

## Counterevidence & Qualifications
Onsite power can make local electricity constraints less visible without making them disappear. Gas plants still need fuel and emissions approval; batteries need charging and lifecycle management; fusion and small modular reactors remain source-described future routes rather than routine data-center options.

The All-In macro power-shortage and PJM claims are source-scoped. They are useful for mapping the argument but should not be treated as a settled grid forecast without primary utility and market data.

## What Changed
- Added the July 18 All-In source's link between behind-the-meter power, PJM scarcity, and global data-center siting.
- Updated the synthesis from a workaround catalogue to a constraint-shift model covering equipment, fuel, emissions, reliability, and politics.
- Clarified that onsite power is most defensible when it creates incremental capacity rather than shifting public-grid costs.

## Related Concepts
- [[AIEnergyBottleneck]] - macro constraint onsite power attempts to compress.
- [[DataCenterPowerBottleneck]] - facility-level power bottleneck that drives onsite generation and storage.
- [[AIComputeContinuity]] - reliability outcome affected by local power architecture.
- [[MaaSInfrastructure]] - model-serving infrastructure that depends on available energy.
- [[DataCenterPhysicalResilience]] - backup-power layer that can become primary operating power.
- [[DataCenterCostShifting]] - ratepayer-risk frame behind behind-the-meter arguments.
- [[CommercialFusionPower]] - speculative future clean-power path for dense industrial loads.
- [[EnergyFirstNeocloud]] - data-center strategy that starts from power availability.
