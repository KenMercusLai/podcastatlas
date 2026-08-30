---
title: "PyroDash"
type: entity
tags: [ai, inference, model-routing, privacy, cost-control]
sources:
  - ai-xia-banchang-buhui-zhisheng-yige-chaoji-moxing-duitan-kevin-ding-pyromind-chuangshiren-ceo-lsq-rke8nfrbi5xalgst3a8uncfd
last_updated: 2026-08-31
knowledge_schema: synthesis-v1
---

# PyroDash

## Overview
PyroDash is described as [[Pyromind]]'s collaborative inference engine that routes requests between a small local worker model and a larger base model.

## Current Profile
PyroDash connects a roughly 4B-size worker model running locally, such as on a Mac, with a base model that handles harder requests. The source presents it as a cost, correctness, and privacy architecture: easy tasks can be handled locally, hard tasks are routed outward, and sensitive tokens can be masked or processed by the worker before base-model routing.

## Key Characteristics
- Uses a worker/base split rather than a single-model inference path.
- Routes easy requests to a small local model and hard requests to a larger base model.
- Applies correctness and cost rewards, with the episode reporting benchmark gains and cost savings under certain Lambda settings.
- Adds a privacy reward so the worker can mask or process sensitive tokens before routing.
- Differs from LoRA-style adaptation because the worker and base model are connected mainly through context rather than weight updates tied to one base model.
- Benefits from stronger base models because the worker's burden can fall as the base improves.

## Evidence
Worker/base routing:
- [[ai-xia-banchang-buhui-zhisheng-yige-chaoji-moxing-duitan-kevin-ding-pyromind-chuangshiren-ceo-lsq-rke8nfrbi5xalgst3a8uncfd|AI 下半场，不会只剩一个超级模型]] describes PyroDash as a collaborative inference engine with a local 4B worker and a base model.

Cost and correctness:
- [[ai-xia-banchang-buhui-zhisheng-yige-chaoji-moxing-duitan-kevin-ding-pyromind-chuangshiren-ceo-lsq-rke8nfrbi5xalgst3a8uncfd|AI 下半场，不会只剩一个超级模型]] reports GRPO training with correctness and cost rewards, about 10% benchmark improvement, and about 20% cost savings when Lambda is small.

Privacy and LoRA boundary:
- [[ai-xia-banchang-buhui-zhisheng-yige-chaoji-moxing-duitan-kevin-ding-pyromind-chuangshiren-ceo-lsq-rke8nfrbi5xalgst3a8uncfd|AI 下半场，不会只剩一个超级模型]] says harnesses help flow and speed but not privacy, while PyroDash adds privacy rewards and is less tied to a single base model than LoRA.

## Qualifications
Benchmark, cost-saving, and privacy claims are source-scoped. The episode does not provide the benchmark name, full evaluation method, deployment security design, or the exact training setup.

## What Changed
- Added PyroDash as Pyromind's worker/base collaborative inference product.
- Added local-worker routing, cost/correctness reward training, and privacy masking as source-scoped characteristics.
- Added its distinction from LoRA-style base-model-bound adaptation.

## Relationships
- [[Pyromind]] - parent company and product owner.
- [[WorkerBaseModelRouting]] - architecture pattern represented by PyroDash.
- [[ModelRoutingCostControl]] - cost-control logic PyroDash uses.
- [[AIModelOrchestration]] - broader coordination problem PyroDash addresses through routing.
- [[LocalAgentExecution]] - local execution layer represented by the worker model.
- [[OnDeviceAI]] - endpoint deployment pattern implied by a Mac-runnable worker model.
- [[ModelFungibility]] - related because PyroDash is framed as less bound to one base model than LoRA.
