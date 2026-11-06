---
title: "Makeboom"
type: entity
tags: [software, aerospace, simulation, design]
knowledge_schema: synthesis-v1
sources:
  - tsr-s6-blakescholl-v3-tsr-s6-blakescholl-v3
last_updated: 2026-11-07
---

# Makeboom

## Overview
Makeboom is [[BoomSupersonic]]'s source-described design and simulation software for evaluating an engine inside a complete aircraft and flight mission.

## Current Profile
The episode presents Makeboom as the computational layer for [[AircraftPropulsionCoDesign|aircraft–propulsion co-design]]. After a more ambitious cabin concept appeared to reduce [[OvertureSupersonicAirliner|Overture]]'s simulated range by about 1,000 miles, Boom used the tool to compare roughly a dozen buildable engine configurations. Scholl says one recovered most of the loss, making the software evidence of an integrated design process rather than independent proof of final aircraft performance.

## Key Characteristics
- Wraps an aircraft design around a candidate engine rather than evaluating propulsion in isolation.
- Simulates a complete flight mission to compare engine, airframe, cabin, and range tradeoffs.
- Supports exploration across multiple configurations that Boom describes as buildable.
- Keeps the design loop inside the company after its shift away from a supplier-controlled engine.

## Evidence
- Integrated configuration search: [[tsr-s6-blakescholl-v3-tsr-s6-blakescholl-v3]] describes the cabin-driven range loss, the roughly dozen modeled configurations, and Scholl's claim that one recovered most of the lost range.

## Qualifications
The source does not document the tool's models, validation data, uncertainty bounds, optimization method, or relationship to certification analysis. A simulated range recovery can direct engineering work but does not establish as-built aircraft performance.

## What Changed
- Created the profile from the Part 2 interview's engine–airframe–cabin design example.

## Relationships
- [[BoomSupersonic]] - company that developed and uses the tool.
- [[OvertureSupersonicAirliner]] - planned aircraft whose configuration the tool evaluates.
- [[AircraftPropulsionCoDesign]] - integrated design method the tool supports.
- [[BlakeScholl]] - founder describing the tool and its product-design role.
