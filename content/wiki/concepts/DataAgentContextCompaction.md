---
title: "Data Agent Context Compaction"
type: concept
tags: [ai, agents, context, data-engineering]
sources:
  - ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack
last_updated: 2026-08-29
knowledge_schema: synthesis-v1
---

# Data Agent Context Compaction

## Definition
Data agent context compaction is the domain-specific compression and retention strategy for long-running data-agent tasks, where schema, lineage, query plans, and data relationships must remain available when later steps depend on them.

## Current Synthesis
The EP45 source treats compaction as a correctness boundary rather than only a token-efficiency tactic. A generic summarizer may reduce context length, but if it removes schema or lineage details, the agent can fail later by joining incorrectly, hallucinating available fields, or forgetting why an earlier query result mattered.

The current synthesis is that data-agent harnesses need selective compaction. They should preserve facts that define the data environment while compressing lower-risk process chatter, duplicated reasoning, or already-validated intermediate steps.

## Key Claims
- Long-running data tasks need context strategy because later steps may depend on earlier schema or lineage details.
- Generic context compaction can damage data work when it removes metadata needed for correctness.
- Schema information should often be preserved more conservatively than ordinary conversation history.
- Context management affects reliability, not only token cost.
- Harnesses should distinguish compressible workflow state from non-compressible data-environment facts.
- Domain-aware compaction complements deterministic validation by keeping validators and model reasoning grounded.

## Evidence
- Long-task context: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] says Altimate has worked on context compaction for long-running tasks.
- Schema warning: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] says generic compaction can damage data tasks if it removes schema or lineage information.
- Disaster framing: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] calls compacting schema information a recipe for disaster.
- Preservation rule: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] says Altimate avoids compacting information that may be important for later data-engineering steps.
- Correctness link: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] presents context management as part of correctness rather than token efficiency alone.

## Counterevidence & Qualifications
The source does not specify an implementation algorithm for identifying which metadata must survive compaction. In some bounded tasks, compact summaries may be sufficient if validators, schemas, or catalogs remain available through tools. The stable claim is that compaction policy must be domain-aware, not that all raw context should be retained forever.

## What Changed
- Initial concept created to capture the episode's schema-preserving compaction warning for data agents.

## Related Concepts
- [[ContextEngineering]] - broader context-design field that this page specializes.
- [[AgenticDataEngineeringHarness]] - harness layer that should manage compaction policy.
- [[AIDataReadiness]] - metadata foundation that compaction must preserve.
- [[SilentSQLFailure]] - failure mode that can result when needed context disappears.
- [[DeterministicDataAgentValidation]] - validation layer that depends on preserved data context.
- [[AgentHarness]] - broader harness concept where compaction already appears.
- [[TokenEfficientAgentWorkflow]] - adjacent efficiency frame qualified by correctness needs.
