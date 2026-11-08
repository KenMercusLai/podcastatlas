---
title: "Apprentice Bench"
type: entity
knowledge_schema: synthesis-v1
tags: [ai, benchmark, continual-learning, agents]
sources:
  - lgbtk9xxwn5za0du2hfhatfphcjc-lgbtk9xxwn5za0du2hfhatfphcjc
last_updated: 2026-11-09
---

# Apprentice Bench

## Overview
Apprentice Bench is presented as a [[NewYorkCognition|New York Cognition]] benchmark for whether an agent learns from a sequence of production tasks after deployment.

## Current Profile
The source describes 100 ordered construction-accounting tasks involving company conventions, workflows, and approval rules. Unlike an independent-item test, later tasks can require feedback or knowledge acquired earlier. The benchmark therefore operationalizes long-horizon intelligence as development across work episodes, while leaving open whether performance generalizes beyond the benchmark's hidden scenarios.

## Key Characteristics
- Sequential benchmark rather than a collection of independent questions.
- Uses a construction-accounting setting with organizational rules and approvals.
- Tests whether earlier feedback improves later task performance.
- Targets continual learning as a meta-capability rather than memorization of one company's rules.
- Keeps some test content private and is reported to have a harder version planned.

## Evidence
### Task structure
- [[lgbtk9xxwn5za0du2hfhatfphcjc-lgbtk9xxwn5za0du2hfhatfphcjc]] describes 100 tasks that must be completed in order and may depend on prior feedback.

### Capability target
- [[lgbtk9xxwn5za0du2hfhatfphcjc-lgbtk9xxwn5za0du2hfhatfphcjc]] contrasts learning across production work with merely running one uninterrupted task for a long time.

### Evaluation boundary
- [[lgbtk9xxwn5za0du2hfhatfphcjc-lgbtk9xxwn5za0du2hfhatfphcjc]] says the target is a general learning capability and reports that the full test set is not public.

## Qualifications
- The supplied document does not include the benchmark paper, tasks, scoring rules, model table, leakage audit, statistical analysis, or independent replication.
- Hidden tests can reduce direct overfitting but do not by themselves prove cross-company or cross-domain generalization.
- A sequence score can mix memory, retrieval, instruction following, error correction, tool use, and underlying domain competence.

## What Changed
- Established Apprentice Bench as a sequential workplace-learning evaluation with explicit generalization limits.

## Relationships
- [[NewYorkCognition|New York Cognition]] - developing organization named in the source.
- [[GuYu|Gu Yu / 谷雨]] - co-founder explaining the benchmark.
- [[SequentialWorkplaceLearningEvaluation]] - evaluation pattern instantiated by the benchmark.
- [[ContinualLearning]] - target capability.
- [[EnvironmentBasedAgentBenchmarks]] - broader family of interactive agent evaluations.
