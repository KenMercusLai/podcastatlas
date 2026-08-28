---
title: "Silent SQL Failure"
type: concept
tags: [ai, sql, data-engineering, reliability]
sources:
  - ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack
last_updated: 2026-08-29
knowledge_schema: synthesis-v1
---

# Silent SQL Failure

## Definition
Silent SQL failure is the data-agent failure mode where generated SQL compiles, runs, and returns plausible results but is semantically wrong because it uses nonexistent tables, wrong joins, incomplete context, or an incorrect interpretation of the task.

## Current Synthesis
The EP45 source makes silent SQL failure a sharper version of the wiki's general [[AIHallucination]] and [[AIVerification]] concerns. In data environments, the dangerous output is not always an error message; it can be a clean result set that answers the wrong question and gets accepted because it looks operationally valid.

The current synthesis is that SQL execution is a weak verifier. Data agents need schema grounding, lineage context, relationship knowledge, and deterministic checks that inspect whether the query and result match the intended business question.

## Key Claims
- SQL that compiles and runs can still be wrong enough to mislead a user or business workflow.
- Hallucinated tables and wrong joins are central data-agent failure modes.
- Silent failures are more dangerous than syntax errors because they can pass ordinary execution checks.
- Missing table, relationship, and lineage context should be treated as a harness failure, not only as an LLM flaw.
- Validation should inspect semantic fit, not only whether the warehouse accepted the query.
- Human review remains necessary when the ground truth or business definition is ambiguous.

## Evidence
- Executable wrongness: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] cites six in ten AI-generated Cortex Analyst queries as wrong while still compiling and running.
- Hallucinated tables: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] cites figures that 27 to 33 percent of AI-generated SQL references nonexistent tables.
- Wrong joins: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] cites 78 percent of errors as silent wrong joins.
- Context failure: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] says agents can assume a table exists or use only a subset of data when humans fail to provide correct context.
- Validation need: [[ep-45-why-ai-agents-break-in-production-the-missing-harness-in-your-data-stack]] says a validation layer is needed to check whether the agent performed the task correctly.

## Counterevidence & Qualifications
The cited error percentages are episode-level claims and should not be generalized across every SQL agent, warehouse, benchmark, or deployment without additional sources. Some generated-SQL failures are visible syntax errors, permission errors, or ambiguous-question failures rather than silent semantic failures. The page captures the risk pattern, not a universal rate.

## What Changed
- Initial concept created to capture the episode's executable-but-wrong SQL failure mode.

## Related Concepts
- [[DeterministicDataAgentValidation]] - control layer designed to catch silent SQL failure.
- [[AgenticDataEngineeringHarness]] - broader operating environment needed to prevent the failure.
- [[AIDataReadiness]] - data-context foundation that reduces hallucinated tables and joins.
- [[AIVerification]] - general AI correctness problem specialized here to SQL.
- [[AIHallucination]] - broader model failure that can appear as fabricated tables or relationships.
- [[HumanJudgmentUnderAI]] - review boundary when correctness depends on business meaning.
- [[SnowflakeCortexAnalyst]] - product example used by the source to introduce the failure mode.
