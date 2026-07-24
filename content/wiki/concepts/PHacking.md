---
title: "P-Hacking"
type: concept
tags: [statistics, research-methods, incentives, reproducibility]
sources: [dont-hate-the-replicator-hate-the-game]
last_updated: 2026-07-24
---

# P-Hacking

P-hacking is the practice described in [[dont-hate-the-replicator-hate-the-game]] where researchers repeatedly adjust data choices, model specifications, sample definitions, or other analytical decisions until a result clears a [[StatisticalSignificanceThreshold]]. The episode grounds the problem in [[AbelBrodeur]]'s smoking-ban project, where repeated reshaping could have produced a publishable effect even though his straightforward analysis found none.

The concept is not presented as only fraud. The source emphasizes that [[PublicationBias]] and career pressure can make small defensible-looking choices accumulate into misleading certainty, especially when journals reward novel significant findings more than null or messy results.

## Key Claims
- P-hacking exploits analytical degrees of freedom around data, variables, samples, controls, and models.
- It becomes more tempting when a null result is hard to publish.
- A result can look statistically official while depending on a sequence of researcher choices that readers cannot easily see.
- [[ReplicationPackage|Replication packages]] and [[RobustnessChecks]] expose p-hacking risk by making the underlying workflow inspectable.
- [[Preregistration]] can reduce p-hacking by requiring hypotheses and analysis plans before the researcher sees all results.

## Connections
- [[AbelBrodeur]] - source case and researcher who turned the experience into a broader research agenda.
- [[ReplicationCrisis]] - wider problem that p-hacking contributes to.
- [[PublicationBias]], [[StatisticalSignificanceThreshold]], and [[ResearchIntegrityIncentives]] - incentive environment around the practice.
- [[ScientificSkepticism]] and [[RationalHumility]] - broader reasoning guardrails.
