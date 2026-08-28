---
title: "EP 45: Why AI Agents Break in Production: The Missing Harness in Your Data Stack"
type: source
tags: [podcast, data-science, ai, agents, data-engineering]
sources: []
date: 2026-07-15
source_file: "/home/ken/repos/podcastatlas/content/episodes/D05B471446F1BB7AFE1E7B3E896EA3C~8584397_2026-08-10-213237-8787-0-0-10.128 [D05B471446F1BB7AFE1E7B3E896EA3C~8584397_2026-08-10-213237-8787-0-0-10.128.mp3？cdn_id=99&uuid=a07f8efa-15c7-ef48-fb69-9ef7dd58c617&wuuid=6a83aea8].md"
source_url: "https://pdcn.co/e/serve.castfire.com/audio/8584397/8584397_2026-08-10-213237.128.mp3?rssID=6736"
duration: "1953"
last_updated: 2026-08-29
---

## Summary
This [[DataScienceWithSam]] episode has [[SamDataScienceWithSam|Sam]] interview [[PradmeshPatil|Pradmesh Patil]] of [[AltimateAI|Altimate AI]] about why production data agents fail even when their base models are strong. The discussion uses [[SnowflakeCortexAnalyst|Snowflake Cortex Analyst]], hallucinated tables, silent wrong joins, expensive warehouse queries, and long-running data tasks to argue that data agents need a domain-specific [[AgenticDataEngineeringHarness]]. Its core synthesis is that reliable agentic data engineering depends on [[AIDataReadiness]], [[DeterministicDataAgentValidation]], [[DataAgentGovernance]], [[DataAgentContextCompaction]], and a human role shift toward [[DataEngineerAgentSupervision]].

## Key Claims
- The opening example cites an independent evaluation of [[SnowflakeCortexAnalyst|Snowflake Cortex Analyst]] where six in ten AI-generated queries were wrong while still compiling and running.
- [[PradmeshPatil]] argues that production failures are often harness failures: the model lacks enough domain context, ground truth, validation, governance, tools, or execution infrastructure.
- For data work, a harness should expose table schemas, lineage, query results, query profiles, query plans, tool access, workflow skills, sandboxes, and validation environments.
- [[SilentSQLFailure]] is more dangerous than syntax failure because hallucinated tables or wrong joins can produce plausible results that mislead users.
- [[DeterministicDataAgentValidation]] should check outputs where deterministic logic is available instead of sending every correctness decision back into the LLM reasoning loop.
- [[AltimateCode|Altimate Code]] is presented as an open-source harness for agentic data engineering, with source-scoped claims about more than one million downloads, thousands of users, and strong benchmark results.
- [[DataAgentBenchmarks]] such as ADE Bench and DAB are used to argue that harness quality can be measured and that a stronger harness can outperform reliance on a larger model alone.
- [[DataAgentGovernance]] includes cost controls, permission limits, PII boundaries, and cross-tool policy layers above fragmented warehouse, pipeline, and BI systems.
- [[DataAgentContextCompaction]] is treated as a correctness issue because generic compaction can drop schema or lineage details needed later in a long data task.
- The episode expects data engineers and data scientists to write less SQL or fewer dbt models manually while spending more effort directing, validating, and scaling fleets of agents.

## Key Quotes
> "6 in 10 AI-generated queries were wrong" - the opening evaluation example attached to Snowflake Cortex Analyst.

> "system prompt tells the model what to do" - Sam's contrast between prompt instruction and harness-grounded truth.

> "recipe for disaster" - Pradmesh's warning about compacting away schema context in long data-agent tasks.

## Connections
- [[DataScienceWithSam]], [[SamDataScienceWithSam]], [[PradmeshPatil]], [[AltimateAI]], and [[AltimateCode]] - show, host, guest, company, and open-source project context.
- [[Snowflake]], [[SnowflakeCortexAnalyst]], [[SilentSQLFailure]], and [[AIDataReadiness]] - data-platform and wrong-query failure branch.
- [[AgenticDataEngineeringHarness]], [[AgentHarness]], [[AgentRuntimeExecutionLayer]], and [[AgenticWorkflow]] - harness and execution-infrastructure context.
- [[DeterministicDataAgentValidation]], [[AIVerification]], [[AgentReliabilityVerification]], and [[OutputQualityGates]] - validation and correctness branch.
- [[DataAgentGovernance]], [[EnterpriseAgentGovernance]], [[AgentPermissionBoundaries]], and [[ModelRoutingCostControl]] - cost, permission, and policy-control branch.
- [[DataAgentContextCompaction]], [[ModelContextProtocol]], and [[ContextEngineering]] - context-delivery and compaction branch.
- [[DataEngineerAgentSupervision]], [[DataEngineeringForDataScience]], [[MLOps]], and [[MachineLearningEngineering]] - role-shift and production-data workflow context.
- [[DataAgentBenchmarks]] and [[UCBerkeley]] - benchmark context mentioned in the episode.

## Contradictions
- No direct contradiction found.
- The episode reinforces existing [[AIDataReadiness]], [[AgentHarness]], and [[EnterpriseAgentGovernance]] claims by specializing them to production data agents, where SQL can be syntactically valid but semantically wrong.
- Benchmark rankings, download counts, error-rate figures, and the expensive-query example remain source-scoped because the episode summary does not provide independent methodology or audit detail.
