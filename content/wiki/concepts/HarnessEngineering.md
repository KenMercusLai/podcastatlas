---
title: "Harness Engineering"
type: concept
tags: [agents, infrastructure, software-engineering]
sources: [e238-liaoliao-harness-shidai-ai-first-de-zuzhi-jiagou-cong-xinren-ren-dao-xinren-ai-51260de8-60ef-4b76-b3e5-2e559c4a0923]
last_updated: 2026-07-23
---

# Harness Engineering

Harness engineering is the discipline of designing the model-external system that lets agents complete real work reliably. In [[e238-liaoliao-harness-shidai-ai-first-de-zuzhi-jiagou-cong-xinren-ren-dao-xinren-ai-51260de8-60ef-4b76-b3e5-2e559c4a0923]], [[PeterCreo|Peter]] of [[Creo]] contrasts it with prompt and [[ContextEngineering]]: prompt and context work improve interaction with a model, while harness work manages tools, runtime, sandboxing, security, latency, feedback, and production recovery.

The concept extends [[AgentHarness]] from a product/runtime layer into an engineering practice. [[Creo]]'s version is dynamic rather than static: the harness should absorb marketing, product, user, and infrastructure signals; observe failures; feed corrections back into agents; and gradually turn successful behavior into a more reliable system.

## Key Claims
- Harness engineering matters most once agents run for longer tasks, call more tools, use more context, and operate inside real workflows.
- The harness includes execution environment, tool access, sandbox and host-service boundaries, startup time, latency, cost, authentication, and observability.
- Self-healing and self-improvement are harness requirements because agent failures are system failures, not only bad answers.
- Verification tools, rollout/fallback logic, and bug triage can be part of the harness when AI-generated implementation outruns manual QA.
- Harness engineering still needs human architecture judgment because AI-generated solutions can hide security, latency, permission, or maintainability risks.
- When the harness works, AI can become production infrastructure inside an [[AIFirstOrganization]] rather than a per-person productivity accessory.

## Connections
- [[AgentHarness]] - broader concept for the model-external runtime and governance layer.
- [[ContextEngineering]] - predecessor discipline that shapes what information reaches the model.
- [[AgenticWorkflow]] - work pattern that exposes whether the harness can act, observe, and recover.
- [[AICodingVerification]] - engineering quality loop that becomes part of the harness in AI-driven development.
- [[AgentPermissionBoundaries]], [[AgentIdentityAndAuthentication]], and [[EnterpriseAgentGovernance]] - safety and accountability layer.
- [[AIOrganizationDesign]] and [[AIFirstOrganization]] - organizational consequences when harnesses become production systems.
- [[ModelHarnessCoEvolution]] - adjacent model-training view where real harness traces and failures improve future agents.
