---
title: "Probabilistic Software"
type: concept
tags: [ai, agents, software-engineering, safety]
sources: [dang-kekaode-daima-biancheng-le-ou-er-fafeng-de-openclaw-women-weilai-de-gongzuo-fanshi-bianqian, moxing-nengli-yijing-goule-yao-juan-jiu-juan-infra-duitan-daiguanlan-runta-chuangshiren-lmjsnpp7d75yhqh7bovj1bv6yhbk]
last_updated: 2026-08-10
---

# Probabilistic Software

Probabilistic software is software whose behavior is partly mediated by model judgment rather than fully specified deterministic code. In [[dang-kekaode-daima-biancheng-le-ou-er-fafeng-de-openclaw-women-weilai-de-gongzuo-fanshi-bianqian]], [[KejiLuandun]] uses [[OpenClaw]] to show the shift: a local agent can search, operate accounts, call tools, write files, change configuration, and keep working, but it may also drift, misread instructions, follow injected prompts, or break its own environment.

The concept does not mean "unusable software." It means the engineering boundary changes. A probabilistic agent can be valuable when a task is fuzzy, low-risk, and reviewable, while the same agent becomes dangerous when it receives broad local permissions, runs on schedules, acts on money or accounts, or mutates durable state without a recovery path.

[[moxing-nengli-yijing-goule-yao-juan-jiu-juan-infra-duitan-daiguanlan-runta-chuangshiren-lmjsnpp7d75yhqh7bovj1bv6yhbk]] adds the infrastructure-first version through [[DaiGuanlan|戴冠兰]] and [[Runta]]. Dai argues that if the lowest execution unit becomes probabilistic, infrastructure has to restore determinism around permissions, isolation, migration, recovery, audit, and cost rather than expecting [[TransformerArchitecture|Transformer]] models to become fully predictable.

## Key Claims
- The user's mental model must shift from command execution to coworker management: specify goals, constrain authority, inspect intermediate work, and accept that retries or corrections may be part of the workflow.
- [[AgentHarness]] design becomes a reliability layer because tools, context, memory, sandboxes, trigger rules, and rollback paths decide how much model uncertainty can damage the environment.
- Deterministic subtools still matter. Stable conversion, export, validation, deployment, and audit steps should be handled by code or structured interfaces when possible, leaving model calls for interpretation and judgment.
- Long-running scheduled agents are riskier than one-shot assistant tasks because the same unclear instruction, stale memory, model update, or hidden prompt can repeat or compound.
- Local agents intensify the issue because [[LocalAgentExecution]] gives them access to browser state, files, accounts, passwords, and private data that a cloud chat bot normally cannot touch.
- Security review itself can be probabilistic when AI is used to judge AI output, so high-impact workflows still need human review, deterministic checks, or domain-specific controls.
- The product question becomes whether the system can expose uncertainty, ask clarifying questions, preserve logs, let users revoke permissions, and recover from wrong action.
- The Runta source adds that probabilistic execution should be treated as a platform assumption: production agents need an [[AgentRuntimeExecutionLayer]] that can bound and record action before the model is trusted with customer data or production writes.

## Connections
- [[OpenClaw]] — source case where probabilistic behavior becomes visible in local agent work.
- [[AgentPermissionBoundaries]] — practical control surface for limiting damage.
- [[LocalAgentExecution]] — local context and authority that increase both usefulness and risk.
- [[AgentHarness]] — tools, context, memory, and orchestration layer that contains model behavior.
- [[AICodingVerification]] — coding-specific response to cheap but uncertain generated output.
- [[HumanAgentCollaboration]] — user-facing relationship shift from operating tools to supervising agents.
- [[DeterministicAuditData]] — contrast with facts and evidence that should not be left to probabilistic output alone.
- [[RoutineAgentAutomation]] — recurring tasks where drift and repeated mistakes have higher blast radius.
- [[Runta]], [[DaiGuanlan]], and [[AgentRuntimeExecutionLayer]] — infrastructure-first response added by the Runta source.
