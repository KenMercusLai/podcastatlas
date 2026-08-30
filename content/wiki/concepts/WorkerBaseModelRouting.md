---
title: "Worker-Base Model Routing"
type: concept
tags: [ai, inference, model-routing, cost-control, privacy]
sources:
  - ai-xia-banchang-buhui-zhisheng-yige-chaoji-moxing-duitan-kevin-ding-pyromind-chuangshiren-ceo-lsq-rke8nfrbi5xalgst3a8uncfd
last_updated: 2026-08-31
knowledge_schema: synthesis-v1
---

# Worker-Base Model Routing

## Definition
Worker-base model routing is an inference architecture in which a smaller worker model handles simple or sensitive tasks locally and routes harder tasks to a larger base model.

## Current Synthesis
The pattern offers a model-plurality answer to enterprise AI economics. Instead of assuming every request should hit the largest model, the system can train routing, correctness, cost, and privacy behavior so a local worker handles cheap or sensitive work while the base model remains available for harder reasoning.

## Key Claims
- Small local workers can lower inference cost when they solve easy tasks without base-model calls.
- Routing quality depends on reward design, because the system must balance correctness, cost, latency, and privacy.
- A worker can act as a privacy boundary by masking or transforming sensitive tokens before external routing.
- The architecture is less base-model-bound than LoRA-style adaptation when worker and base communicate mainly through context.
- Base-model progress can strengthen the architecture by reducing pressure on the worker or improving the routed path.

## Evidence
Routing architecture:
- [[ai-xia-banchang-buhui-zhisheng-yige-chaoji-moxing-duitan-kevin-ding-pyromind-chuangshiren-ceo-lsq-rke8nfrbi5xalgst3a8uncfd|AI 下半场，不会只剩一个超级模型]] describes PyroDash as connecting a local 4B worker with a base model and routing based on task difficulty.

Cost and performance:
- [[ai-xia-banchang-buhui-zhisheng-yige-chaoji-moxing-duitan-kevin-ding-pyromind-chuangshiren-ceo-lsq-rke8nfrbi5xalgst3a8uncfd|AI 下半场，不会只剩一个超级模型]] reports correctness/cost reward training, about 10% benchmark improvement, and about 20% cost savings under a small-Lambda setting.

Privacy and base-model relationship:
- [[ai-xia-banchang-buhui-zhisheng-yige-chaoji-moxing-duitan-kevin-ding-pyromind-chuangshiren-ceo-lsq-rke8nfrbi5xalgst3a8uncfd|AI 下半场，不会只剩一个超级模型]] says the worker can include privacy rewards and mask sensitive tokens, while stronger base models help rather than threaten the architecture.

## Counterevidence & Qualifications
The source does not provide enough benchmark detail to judge generality. Routing errors could increase cost or degrade output quality, and privacy masking claims need implementation and threat-model detail before being treated as settled.

## What Changed
- Added worker-base model routing as a focused inference pattern from PyroDash.
- Added correctness, cost, privacy, and LoRA-independence as its source-scoped dimensions.
- Added the qualification that reported benchmark and cost figures need corroboration.

## Related Concepts
- [[ModelRoutingCostControl]] - economic objective that worker/base routing directly serves.
- [[AIModelOrchestration]] - broader coordination layer for deciding which model handles which task.
- [[ModelFungibility]] - related because context-linked workers are framed as less tied to one base model.
- [[LocalAgentExecution]] - local execution path represented by the worker model.
- [[OnDeviceAI]] - deployment pattern for small models running on endpoint devices.
- [[AIInferenceCostStructure]] - cost model that routing tries to improve.
- [[AgentHarness]] - adjacent production layer that helps flow and speed but is insufficient for privacy in the source's framing.
