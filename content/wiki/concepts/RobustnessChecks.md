---
title: "Robustness Checks"
type: concept
tags: [research-methods, statistics, evidence, reproducibility]
sources: [dont-hate-the-replicator-hate-the-game]
last_updated: 2026-07-24
---

# Robustness Checks

Robustness checks are alternative analyses used to ask whether a published result still holds when reasonable modeling or data choices change. In [[dont-hate-the-replicator-hate-the-game]], [[ReplicationGames]] teams first reproduce author code and then, when possible, test robustness.

The episode stresses that robustness work is more judgment-heavy than simple reproduction. A model change can reveal fragility, but it can also miss what the original authors believed the study was actually testing. The cartel-paper dispute in the source shows this boundary: removing one cartel changed the result, while the authors argued that the removed case was the central object of the paper.

## Key Claims
- Robustness checks test whether a result is dependent on one narrow specification.
- They are essential for detecting [[PHacking]] and fragile conclusions.
- They require judgment about what alternatives are reasonable rather than arbitrary.
- A failed robustness check can expose a real weakness or a mismatch between replicators' interpretation and authors' intended hypothesis.
- Strong research needs both executable [[ReplicationPackage|replication packages]] and robustness work that is clearly documented.

## Connections
- [[ReplicationGames]] - main source setting.
- [[ReplicationCrisis]], [[PHacking]], and [[PublicationBias]] - problems robustness checks help detect.
- [[ResearchIntegrityIncentives]] and [[CrowdsourcedAcademicAuditing]] - institutional context for doing the work at scale.
- [[RationalHumility]] - posture needed when robustness evidence is ambiguous.
