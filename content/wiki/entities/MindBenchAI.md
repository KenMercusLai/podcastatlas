---
title: "MindBench.AI"
type: entity
tags: [ai, evaluation, mental-health, safety]
sources:
  - tech-20261104-1104-mp-tech-pod-128-tech-20261104-1104-mp-tech-pod-128
last_updated: 2026-11-04
knowledge_schema: synthesis-v1
---

# MindBench.AI

## Overview
MindBench.AI is a mental-health AI evaluation project described by [[JohnTorous]] in a [[MarketplaceTech]] interview as having been developed with the National Alliance on Mental Illness.

## Current Profile
The project's distinguishing feature in the bounded source is participation by actual AI users in creating evaluation cases. That design responds to a weakness in model-only pipelines, where one system generates test cases and another scores them without enough input from the people who experience the product over time.

MindBench.AI therefore represents a user-centered component of [[LongitudinalChatbotSafetyEvaluation]]. The source does not describe the full benchmark, its governance, dataset, scoring procedure, validation results, or public availability, so the page does not infer those details.

## Key Characteristics
- Focuses on AI behavior in mental-health-related use.
- Involves real users in constructing evaluation cases.
- Was developed with the National Alliance on Mental Illness according to the episode.
- Addresses practical harms and benefits that automated test generation may miss.

## Evidence
- User participation - [[tech-20261104-1104-mp-tech-pod-128-tech-20261104-1104-mp-tech-pod-128]] contrasts MindBench.AI with evaluations generated and scored mainly by other AI systems.
- Institutional context - [[tech-20261104-1104-mp-tech-pod-128-tech-20261104-1104-mp-tech-pod-128]] attributes its development partnership to the National Alliance on Mental Illness.
- Evaluation purpose - [[tech-20261104-1104-mp-tech-pod-128-tech-20261104-1104-mp-tech-pod-128]] places the project within concern about rapidly changing model behavior and long, emotionally significant conversations.

## Qualifications
The supplied episode summary is not the benchmark specification or a validation study. It does not establish representativeness, sample size, scoring reliability, model coverage, clinical oversight, or whether user-created cases predict real-world outcomes. Those questions remain open in this wiki evidence set.

## What Changed
- Created a bounded profile of the user-centered evaluation project.
- Recorded its contrast with model-only test generation and scoring.

## Relationships
- [[JohnTorous]] - psychiatrist who describes the project in the source.
- [[LongitudinalChatbotSafetyEvaluation]] - broader evaluation approach the project exemplifies.
- [[ChatbotSafetyGuardrailDecay]] - failure mode that user-centered, multi-turn cases may expose.
- [[SycophanticAICompanionRisk]] - relational safety problem requiring more than one-turn scoring.
