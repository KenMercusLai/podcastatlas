---
title: "Progress Visibility Design"
type: concept
tags: [user-experience, service-design, waiting, trust]
sources:
  - the-dominos-pizza-tracker-theory-of-everything
last_updated: 2026-09-19
knowledge_schema: synthesis-v1
---

## Definition

Progress visibility design is the practice of translating otherwise invisible service work into understandable stages, milestones, or movement so users can orient themselves during a wait.

## Current Synthesis

The [[DominosPizzaTracker|Domino's Pizza Tracker]] shows that waiting quality depends on uncertainty and perceived control as well as elapsed time. A useful tracker exposes credible operational state at a level customers can understand; the milestones create a route through the wait, while visible effort can increase confidence and perceived value. The design stops being transparent when its apparent precision or activity is not supported by system state.

## Key Claims

- A predictable journey can reduce anxiety even when it does not shorten actual service time.
- Operational telemetry becomes customer value only after it is translated into legible milestones.
- Familiar stages restore some of the observability lost when transactions move from physical counters to digital services.
- Accuracy matters most at consequential transitions, but cosmetic inaccuracies can still weaken trust in the whole interface.
- Progress visibility is distinct from [[SyntheticProgressIndicators]], which imply process or certainty beyond the available evidence.

## Evidence

### Uncertainty reduction

- [[the-dominos-pizza-tracker-theory-of-everything]] reports that Domino's customer research identified the invisible middle of the delivery wait as an anxiety problem.

### Operational-to-customer translation

- [[the-dominos-pizza-tracker-theory-of-everything]] links internal order-event systems and store dashboards to the later customer tracker.

### Useful but imperfect representation

- [[the-dominos-pizza-tracker-theory-of-everything]] reports that major order transitions were mostly accurate in a field test even though worker attribution and the quality-check stage were not literal.

## Counterevidence & Qualifications

- One observed order cannot establish general tracker accuracy.
- More milestones do not necessarily create more information; they can merely subdivide a wait.
- If users cannot tell which stages are measured, inferred, or decorative, visibility can create false confidence.

## What Changed

- Added a general design pattern derived from Domino's shift from speed guarantee to state visibility.
- Established truthful operational grounding as the boundary between useful reassurance and synthetic progress.

## Related Concepts

- [[LaborIllusion]] - visible effort can increase appreciation for a service.
- [[SyntheticProgressIndicators]] - deceptive or weakly grounded counterpart to truthful state visibility.
- [[SyncReliabilityAsUX]] - adjacent principle that a status cue creates value only when users can trust the underlying state.
- [[BankingProductDelight]] - adjacent case where immediacy and clarity reduce financial uncertainty.
