---
title: "Data Agent Benchmarks"
type: concept
tags: [ai, agents, benchmarks, data-engineering]
sources:
  - ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack
last_updated: 2026-08-29
knowledge_schema: synthesis-v1
---

# Data Agent Benchmarks

## Definition
Data agent benchmarks are evaluation suites that compare how model-and-harness systems perform on agentic data engineering or data-agent tasks, rather than judging a base model in isolation.

## Current Synthesis
The EP45 source uses ADE Bench and DAB to argue that harness quality is measurable. The benchmark frame matters because data-agent systems include context retrieval, tools, deterministic validation, governance, and execution environments; the model is only one component of the evaluated system.

The current synthesis is cautious. Benchmarks can reveal whether a harness helps agents complete realistic data tasks, but a ranking claim remains source-scoped unless the benchmark methodology, task mix, model choices, and evaluation rules are independently inspected.

## Key Claims
- Data-agent benchmarks compare harness-and-model behavior across agentic data tasks.
- Harness design can change outcomes enough to matter beside base-model selection.
- ADE Bench is presented as an industry benchmark for agentic data engineering.
- DAB is presented as another data-agent benchmark associated with people at Berkeley.
- Benchmark results are useful evidence only when methodology, task coverage, and model choices are visible.
- Product claims based on benchmark rank should remain source-attributed until corroborated.

## Evidence
- ADE Bench identity: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] says ADE Bench is an industry benchmark for agentic data engineering created by Ben Stansel and dbt Labs.
- Altimate result claim: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] says Altimate Code topped ADE Bench.
- Model comparison: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] says Altimate topped the benchmark using Sonnet while some other tools used Opus.
- DAB identity: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] says DAB is a data-agent benchmark from people at the University of Berkeley.
- Harness-evaluation frame: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] describes benchmark tasks as connecting a harness and evaluating agent behavior across different tasks.

## Counterevidence & Qualifications
The source does not include benchmark datasets, scoring rubrics, task examples, reproducibility details, or current leaderboard snapshots. The source's strongest durable contribution is the evaluation frame: data-agent benchmarks should evaluate the whole harnessed system, not only the LLM name.

## What Changed
- Initial concept created to capture ADE Bench and DAB as data-agent harness evaluation signals.

## Related Concepts
- [[AgentEvaluationBenchmarks]] - broader benchmark concept for agent systems.
- [[AgenticDataEngineeringHarness]] - system layer these benchmarks evaluate.
- [[DeterministicDataAgentValidation]] - validation layer that can affect benchmark performance.
- [[AIVerification]] - broader correctness problem benchmarks try to operationalize.
- [[AICodingVerification]] - adjacent benchmarkable domain with stronger external checks.
- [[AltimateCode]] - project positioned through the benchmark claims.
- [[UCBerkeley]] - institutional context mentioned for DAB in the source.
