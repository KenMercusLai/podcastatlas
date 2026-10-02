---
title: "Structured Decision Model"
type: concept
tags: [ai, structured-output, classification, routing]
sources:
  - vol-175-gpt-6-astra-opus-5-5-jev-zhu-moxing-hunzhan-1-6700-1
  - ai-jibao-26q3-muse-yinbao-geren-zhuli-astra-jinru-jiqiren-openai-shouru-mengzeng-1-183-1
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

# Structured Decision Model

## Definition
A structured decision model is an AI component optimized to return bounded choices, classifications, scores, probabilities, or schema-conforming objects when an application needs a reliable machine-readable decision more than free-form prose.

## Current Synthesis
The sources use [[Jev]] and OpenAI's reported Decisions API to illustrate a broader architecture choice: not every agent step needs the strongest conversational model. A narrow, fast model can sit in a routing, advertising, recommendation, or action-selection loop, reduce output-parsing failures, and improve responsiveness, while stronger models handle ambiguous planning or consequential reasoning. This is a systems claim, not an assertion that constrained output guarantees correct judgment.

## Key Claims
- Output shape can be a first-class capability rather than a formatting instruction added to a general model.
- Classification, scoring, intent recognition, and routing benefit from low latency and predictable schemas.
- Structured models can reduce malformed output, missing fields, and compatibility branches in application code.
- Narrow decision components complement rather than replace frontier models in mixed-model workflows.
- Accuracy, calibration, abstention, and error costs remain essential even when format compliance is high.
- Provider entry can quickly compress differentiation for startups unless their advantage extends beyond the model endpoint.

## Evidence
- Structured-output case: [[vol-175-gpt-6-astra-opus-5-5-jev-zhu-moxing-hunzhan-1-6700-1]] describes Jev returning selections, scores, classifications, and JSON-like structures.
- Latency case: [[vol-175-gpt-6-astra-opus-5-5-jev-zhu-moxing-hunzhan-1-6700-1]] reports roughly two thousand probability judgments in about 1.6 seconds in one host's use.
- Integration case: [[vol-175-gpt-6-astra-opus-5-5-jev-zhu-moxing-hunzhan-1-6700-1]] contrasts the approach with forcing a general model into JSON and handling format or missing-result failures.
- Category confirmation: [[ai-jibao-26q3-muse-yinbao-geren-zhuli-astra-jinru-jiqiren-openai-shouru-mengzeng-1-183-1]] describes OpenAI's reported Decisions API for text, structured data, and image inputs and compares it with startup products that return scores and confidence values.

## Counterevidence & Qualifications
The sources supply no controlled accuracy comparison, calibration results, schema-failure rate, reproducible latency setup, pricing comparison, or primary documentation here. A fast wrong classification can amplify errors at scale, and tasks with ambiguous goals or high consequences may need stronger reasoning, retrieval, human review, or an abstention path. The claimed financing pressure on specialized startups is an inference, not an observed market outcome.

## What Changed
- Added a second provider and multimodal input case, strengthening the concept beyond one product example.
- Added provider-entry pressure as a qualified market implication.

## Related Concepts
- [[ModelRoutingCostControl]] - architectural relationship because structured models can handle cheap routine decisions.
- [[Jev]] - product example described by the source.
- [[AgentHarness]] - integration relationship because schemas, retries, validation, and fallbacks belong in the execution layer.
- [[AgentTrustCalibration]] - evaluation relationship because predictable format should not be mistaken for reliable judgment.
- [[ComputerUseAgent]] - application relationship where low-latency intent and action decisions can improve responsiveness.
