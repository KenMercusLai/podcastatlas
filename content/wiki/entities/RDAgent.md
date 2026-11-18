---
title: "RDAgent"
type: entity
tags: [project, ai-research, agents, automation]
sources:
  - c11cceb2-07c2-4c2f-9124-95bd1187c7ec-c11cceb2-07c2-4c2f-9124-95bd1187c7ec
last_updated: 2026-11-18
knowledge_schema: synthesis-v1
---

# RDAgent

## Overview

RDAgent, expanded in the source as Research and Development Agent, is an automated research-agent system described by [[BianJiang|边疆]] in [[c11cceb2-07c2-4c2f-9124-95bd1187c7ec-c11cceb2-07c2-4c2f-9124-95bd1187c7ec]].

## Current Profile

RDAgent links research ideation with engineering execution and experimental feedback. A research agent proposes a direction, development agents implement and test it, results return to the research layer, and the system uses the evidence to continue, revise, or abandon the line of work. The episode positions this as an operational [[AutoResearch]] system and a possible component of [[RecursiveSelfImprovement|RSI]], not evidence of autonomous open-ended recursion.

## Key Characteristics

- Joins proposal generation, implementation, experimentation, result analysis, and iterative revision.
- Uses model knowledge, reasoning, and coding ability across both research and development roles.
- Depends on verifiable objectives and feedback rather than unconstrained idea generation.
- Can preserve successful and failed trajectories as skills or memory for later cycles.
- Operates under human-set goals, resource constraints, and broad research framing.

## Evidence

### Closed research loop
- [[c11cceb2-07c2-4c2f-9124-95bd1187c7ec-c11cceb2-07c2-4c2f-9124-95bd1187c7ec]] describes the proposal-to-experiment-to-analysis loop and its use in post-training and deep-search-agent work.

### Organizational use
- [[c11cceb2-07c2-4c2f-9124-95bd1187c7ec-c11cceb2-07c2-4c2f-9124-95bd1187c7ec]] says human researchers led specialized agent teams for analysis, ideation, implementation, monitoring, and feedback collection.

### RSI boundary
- [[c11cceb2-07c2-4c2f-9124-95bd1187c7ec-c11cceb2-07c2-4c2f-9124-95bd1187c7ec]] distinguishes reusing research memory from the stronger loop where the newly trained model becomes a better research agent for its successor.

## Qualifications

- The source supplies no repository, paper, architecture specification, benchmark table, or comparison against other research-agent systems.
- Reported scale and productivity should not be read as proof that each agent operated independently or that agent count maps directly to researcher-equivalent output.
- A faster loop can accelerate bad objectives or misleading metrics unless evaluation and human review remain strong.

## What Changed

- Created a project profile separating RDAgent's operational research loop from stronger RSI claims.

## Relationships

- [[BianJiang|边疆]] - speaker who explains the system in the source.
- [[AutoResearch]] - RDAgent is an implementation of iterative automated research.
- [[AIForAI]] - RDAgent applies models to improve model and agent development.
- [[RecursiveSelfImprovement]] - RDAgent may contribute to recursion when its outputs improve the next research system.
- [[AIVerification]] - feedback quality determines whether the loop measures real progress.
