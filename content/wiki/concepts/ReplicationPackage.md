---
title: "Replication Package"
type: concept
tags: [research-methods, data, code, reproducibility]
sources: [dont-hate-the-replicator-hate-the-game]
last_updated: 2026-07-24
---

# Replication Package

A replication package is the data-and-code bundle behind a published paper. In [[dont-hate-the-replicator-hate-the-game]], some top journals require these packages so other researchers can rerun the analysis and check whether the published tables and results are reproducible.

The episode shows why the package is necessary but insufficient. A folder may exist, code may run, and tables may reproduce, yet the underlying raw data, cleaning steps, missing variables, or modeling choices can still create uncertainty. That is why [[ReplicationGames]] move from reproduction into [[RobustnessChecks]].

## Key Claims
- Replication packages make research claims inspectable by linking published results to code and data.
- The first replication task is often mechanical: run the authors' code and check whether outputs match the paper.
- Package quality depends on documentation, file provenance, raw-data clarity, and executable code.
- A package can reproduce reported numbers while leaving [[PHacking]] or fragile specification choices unresolved.
- [[CrowdsourcedAcademicAuditing]] increases the value of packages by making it more likely someone will actually inspect them.

## Connections
- [[ReplicationGames]] and [[InstituteForReplication]] - setting where packages are used.
- [[ReplicationCrisis]] - problem the package is meant to address.
- [[RobustnessChecks]], [[Preregistration]], and [[ResearchIntegrityIncentives]] - adjacent reproducibility tools and incentives.
- [[ScientificSelfCorrection]] - broader correction mechanism.
