---
title: "Aircraft–Propulsion Co-Design"
type: concept
tags: [aerospace, engineering, product-design, simulation]
knowledge_schema: synthesis-v1
sources:
  - tsr-s6-blakescholl-v3-tsr-s6-blakescholl-v3
last_updated: 2026-11-07
---

# Aircraft–Propulsion Co-Design

## Definition
Aircraft–propulsion co-design is the practice of optimizing an aircraft, engine, cabin, and flight mission as one coupled system instead of fitting an externally fixed engine into a largely fixed airframe.

## Current Synthesis
The bounded case comes from [[BoomSupersonic]]. [[BlakeScholl]] says internal engine ownership let Boom optimize transonic performance for [[BoomlessCruise]] and use [[Makeboom]] to explore engine configurations after a better cabin concept appeared to cost about 1,000 miles of simulated range. The claimed recovery illustrates the value of moving constraints across subsystem boundaries, but it remains a simulation-led design account rather than evidence that the final [[OvertureSupersonicAirliner|Overture]] meets range, comfort, safety, cost, or certification targets.

## Key Claims
- Fixed supplier interfaces can prevent globally better solutions even when they reduce subsystem-development burden.
- Joint optimization can trade engine architecture, airframe shape, cabin choices, altitude, speed, and mission profile against one another.
- Integrated simulation makes ambitious product choices testable by exposing their system-level performance cost.
- Owning more of the design loop accelerates learning only if the company can absorb added engineering, manufacturing, and certification risk.

## Evidence
- Capability and performance coupling: [[tsr-s6-blakescholl-v3-tsr-s6-blakescholl-v3]] links internal engine control to transonic optimization and boomless operation.
- Cabin and range tradeoff: [[tsr-s6-blakescholl-v3-tsr-s6-blakescholl-v3]] says Makeboom compared roughly a dozen buildable configurations and found one that recovered most of a source-reported 1,000-mile range loss.

## Counterevidence & Qualifications
The episode gives Scholl's retrospective explanation without independent model validation, as-built results, fuel-burn analysis, certification evidence, or the final cabin and engine configuration. Integration can improve whole-product optimization while increasing organizational complexity and reducing the diversification benefit of an established supplier.

## What Changed
- Created the concept from Boom's engine–airframe–cabin configuration example.

## Related Concepts
- [[CrisisForcedVerticalIntegration]] - supplier crisis that moved the coupled design loop inside Boom.
- [[Makeboom]] - software used to compare integrated aircraft and engine configurations.
- [[BoomlessCruise]] - operating capability Scholl says improved transonic optimization enabled.
- [[ConstraintDrivenEngineeringStrategy]] - broader pattern of using hard constraints to redirect design.
- [[FirstPrinciplesManufacturing]] - adjacent discipline coupling product architecture to production capability.
