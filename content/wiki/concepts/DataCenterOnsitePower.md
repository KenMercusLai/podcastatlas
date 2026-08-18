---
title: "Data Center Onsite Power"
type: concept
tags: [ai, data-centers, energy, infrastructure]
sources: [all-in-with-chamath-jason-sacks-friedberg-the-future-of-everything-what-ceos-of-circle-crowdstrike-more-see-coming-in-2026-39870920, all-in-with-chamath-jason-sacks-friedberg-inside-americas-ai-strategy-infrastructure-regulation-and-global-competition-39846955, tech-20260129-0129-mp-tech-pod-128-tech-20260129-0129-mp-tech-pod-128, tsr-s5-davidkirtley-v2-audio-tsr-s5-davidkirtley-v2-audio, tech-20260216-0216-mp-tech-pod-128-tech-20260216-0216-mp-tech-pod-128]
last_updated: 2026-08-18
---

# Data Center Onsite Power

[[all-in-with-chamath-jason-sacks-friedberg-the-future-of-everything-what-ceos-of-circle-crowdstrike-more-see-coming-in-2026-39870920]] adds a full-stack onsite-power case through [[Crusoe]]. The source's Abilene project combines a 1.2 gigawatt substation, 350 megawatts of onsite gas generation, battery smoothing for GPU-cluster fluctuations, and future interest in hydro, geothermal, and small modular reactors.

[[all-in-with-chamath-jason-sacks-friedberg-inside-americas-ai-strategy-infrastructure-regulation-and-global-competition-39846955]] adds the behind-the-meter policy version. [[DavidSacks|David Sacks]] argues that if data centers can build their own power generation, they can add net supply and spread fixed grid costs rather than simply competing with households for existing electricity.

Data center onsite power is the pattern where a data-center developer generates, stores, or delivers electricity at or near the facility instead of waiting for a full grid connection. [[tech-20260216-0216-mp-tech-pod-128-tech-20260216-0216-mp-tech-pod-128]] adds this concept through [[Caterpillar]] natural gas generators being used as primary power for some AI data centers.

The concept extends [[AIEnergyBottleneck]]. Earlier wiki sources emphasize utility approvals, rate design, tax incentives, and grid upgrades. This source adds the workaround: when interconnection queues take years, developers may buy generators and fuel to move faster. That can speed deployment, but it shifts the constraint to equipment supply, fuel availability, emissions, local siting, and generator maintenance.

[[tech-20260129-0129-mp-tech-pod-128-tech-20260129-0129-mp-tech-pod-128]] adds the storage version through [[RedwoodMaterials]] and [[SecondLifeEVBatteryStorage]]. Redwood's [[Nevada]] project uses reused EV batteries to power a data center disconnected from the grid, showing that onsite power can include storage systems as well as generation equipment.

The source also changes [[DataCenterPhysicalResilience]]. Backup power equipment is not only a failover layer; in some projects it becomes the main operating power system. That makes generator capacity part of [[AIComputeContinuity]] and [[MaaSInfrastructure]], because model-serving capacity depends on whether dense facilities can keep drawing power under real deployment pressure.

[[tsr-s5-davidkirtley-v2-audio-tsr-s5-davidkirtley-v2-audio]] adds a speculative clean-power extension through [[Helion]]. [[DavidKirtley]] says Helion wants future generators placed directly at data centers, factories, and manufacturing sites where power can be tailored to customer needs. Unlike the Caterpillar natural-gas case, this remains a source-described future route tied to [[CommercialFusionPower]] rather than a current workaround.

## Key Claims
- Onsite power can reduce dependence on slow grid interconnection queues, but it does not make electricity demand disappear.
- Natural gas generators can win over solar or geothermal options when the highest-priority variable is speed to operation.
- Battery storage can also become onsite power infrastructure when a data center needs fast electricity access, but it must still be charged, controlled, cooled, and maintained.
- Generator suppliers become part of the AI infrastructure supply chain when data centers use them for primary power.
- A data-center generator boom can crowd out traditional backup-power customers, such as hospitals, if production capacity is tight.
- Onsite power turns the energy bottleneck into a mixed industrial, fuel, regulatory, reliability, and climate problem.
- Fusion onsite power would still be industrial-scale infrastructure, not a residential appliance; it would require buildings, substations, safety controls, and power-market integration.
- The All-In source adds behind-the-meter generation as a national AI competitiveness tool, but its ratepayer claim depends on projects creating net capacity instead of shifting costs or emissions elsewhere.
- Crusoe adds that onsite power is also a financing and supply-chain problem: gas turbines, battery systems, substations, skilled labor, and long-term customer leases all shape whether a site can operate.

## Connections
- [[Caterpillar]] - central company case in the source.
- [[DanAckerman]] and [[DavidVictor]] - named commentators explaining demand and speed pressure.
- [[RedwoodMaterials]], [[ColinCampbell]], and [[SecondLifeEVBatteryStorage]] - reused-battery storage route added by Marketplace Tech.
- [[AIEnergyBottleneck]] - bottleneck that onsite power tries to bypass or compress.
- [[AIComputeContinuity]] and [[MaaSInfrastructure]] - downstream service reliability that depends on available facility power.
- [[DataCenterPhysicalResilience]] - generator role shifts from backup to primary operation.
- [[PublicUtilityCommissions]] and [[DataCenterCostShifting]] - grid-regulation path that onsite power may partly route around.
- [[AIMetabolicInfrastructure]] and [[DataCenterBacklash]] - adjacent resource, emissions, and public-permission risks.
- [[Helion]], [[CommercialFusionPower]], and [[Nucor]] - future large-site clean-power route added by The Social Radars.
- [[AmericanAIStackStrategy]], [[DataCenterCostShifting]], and [[DataCenterPowerBottleneck]] - behind-the-meter AI policy branch added by All-In.
- [[Crusoe]], [[EnergyFirstNeocloud]], [[AIInfrastructureDebtFinancing]], [[SecondLifeEVBatteryStorage]], and [[RedwoodMaterials]] - energy-first neocloud branch added by the January 25 All-In episode.
