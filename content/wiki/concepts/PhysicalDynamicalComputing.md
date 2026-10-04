---
title: "Physical Dynamical Computing"
type: concept
tags: [ai, computing, dynamical-systems, semiconductors]
knowledge_schema: synthesis-v1
sources:
  - all-in-with-chamath-jason-sacks-friedberg-naveen-rao-4d-computing-ais-energy-wall-beating-biology-42983573
last_updated: 2026-10-04
---

# Physical Dynamical Computing

## Definition
Physical dynamical computing is computation performed through the evolving state of coupled physical elements, here semiconductor oscillators, rather than by representing every operation as a sequence of conventional digital arithmetic instructions.

## Current Synthesis
The source presents physical dynamical computing as a locality-first AI architecture. Coupled oscillators influence one another over time, each element can retain state, and a trained system converges through physical interaction toward a useful output. [[UnconventionalAI|Unconventional AI]] calls its three-dimensional, time-evolving implementation "4D computing." [[UNO]] provides an early image-generation proof point, but the evidence does not yet establish general-purpose programmability, matched quality, production reliability, or rack-scale advantage.

## Key Claims
- Computation can be encoded in trajectories and convergence of a physical system rather than only in explicit digital instruction sequences.
- Combining state and computation at each element may reduce separate memory-interface traffic.
- Sparse coupling is necessary to avoid quadratic connection growth as systems scale.
- Time is an active computational dimension, while die stacking can shorten physical communication paths.
- A trainable simulation-to-circuit workflow can make a novel physical substrate accessible to model developers.
- Compatibility is not automatic because existing models must be ported to the substrate and its new programming abstractions.

## Evidence
- Physical mechanism: [[all-in-with-chamath-jason-sacks-friedberg-naveen-rao-4d-computing-ais-energy-wall-beating-biology-42983573]] uses synchronized metronomes to explain computation through coupled system dynamics.
- Trainability and sparsity: [[all-in-with-chamath-jason-sacks-friedberg-naveen-rao-4d-computing-ais-energy-wall-beating-biology-42983573]] presents [[UNO]] as a trained sparse oscillator model whose trajectories generate conditioned images.
- Hardware embodiment: [[all-in-with-chamath-jason-sacks-friedberg-naveen-rao-4d-computing-ais-energy-wall-beating-biology-42983573]] describes a fabricated prototype, local state, die stacking, temporal evolution, and a reported 500-nanojoule image result.
- Programming and migration: [[all-in-with-chamath-jason-sacks-friedberg-naveen-rao-4d-computing-ais-energy-wall-beating-biology-42983573]] says Python libraries expose stochastic time-varying elements while existing model families still require porting.

## Counterevidence & Qualifications
The source is a company presentation without independent replication or enough implementation detail to compare equivalent workloads. Oscillator dynamics may be mathematically describable with matrices without sharing the flexibility, precision, error behavior, toolchain maturity, or workload coverage of digital accelerators. Prototype energy at an unspecified quality level is not the same as end-to-end data-center efficiency, and stacking introduces thermal, yield, packaging, and manufacturing constraints.

## What Changed
- Created the concept and separated its physical mechanism from the company's "4D computing" label.
- Preserved model-porting, benchmark, reliability, and manufacturing gates around the prototype claim.

## Related Concepts
- [[AIDataMovementEnergyCost]] - architectural motivation for combining state and computation locally.
- [[IntelligencePerWatt]] - proposed objective for comparing useful AI output per unit power.
- [[MemoryWall]] - conventional bandwidth and latency bottleneck the architecture attempts to bypass.
- [[InMemoryComputingForEdgeAI]] - adjacent route that moves memory and computation closer without necessarily using temporal dynamics.
- [[Semiconductor3DStacking]] - spatial-integration route contributing to the 4D framing.
- [[AIChipSpecialization]] - broader tradeoff between workload-specific efficiency and flexibility.
