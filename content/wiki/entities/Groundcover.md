---
title: "Groundcover"
type: entity
knowledge_schema: synthesis-v1
tags: [company, observability, cloud-infrastructure]
sources:
  - d5efc401
last_updated: 2026-10-01
---

# Groundcover

## Overview
Groundcover is a full-stack observability company co-founded by [[ShaharAzulay]]. It combines an [[EBPFObservability|eBPF sensor]] with a managed backend deployed in the customer's environment.

## Current Profile
The available source presents Groundcover as a technical and commercial challenger in a mature, mission-critical category. Its architecture keeps the data plane with the customer and prices mainly by monitored infrastructure instead of telemetry volume. Its go-to-market path moved from a UI-light complementary tool to a fuller replacement proposition, making [[FounderLedSales]] and [[IncumbentReplacementMigration]] as important to the case as the sensor itself.

## Key Characteristics
- Uses eBPF to collect logs, metrics, traces, network traffic, and system-call telemetry with limited application-code instrumentation.
- Runs the managed data plane in the customer's environment rather than requiring the vendor to host and mark up all telemetry.
- Prices primarily by monitored infrastructure, such as hosts, rather than ingestion volume.
- Entered accounts first through greenfield or complementary use cases and later pursued full Datadog and New Relic replacement.
- Grew through founder-run prospecting, demonstrations, proofs of concept, negotiation, and product feedback before specializing the sales organization.
- Treats migration completion and incumbent retirement as part of commercial execution.

## Evidence
Architecture and economics:
- [[d5efc401]] connects eBPF collection, a customer-hosted data plane, and host-based pricing to the goal of retaining higher-fidelity telemetry without volume-linked vendor charges.

Early product and customers:
- [[d5efc401]] says the first product used open-source Grafana rather than its own interface and won an initial complementary deployment roughly three months after company formation.

Commercial scale and evolution:
- [[d5efc401]] reports approximately $20 million in ARR, 250 customers, and 150 employees, and traces the shift from early discounted contracts to larger incumbent-displacement deals.

## Qualifications
The page reflects one company-founder interview. Scale, technical-performance, pricing, customer, and timing claims are source-scoped. The source respects incumbent products as technically strong and attributes Groundcover's opening to consumption economics, architecture, and migration execution rather than claiming incumbents lack capability.

## What Changed
- Created the company profile around the combined architecture, pricing, founder-sales, and migration system.
- Distinguished early complementary use from the later full-replacement position.

## Relationships
- [[ShaharAzulay]] - co-founder and CEO presenting Groundcover's history.
- [[EBPFObservability]] - kernel-level collection method at the product's technical core.
- [[ObservabilityCostArchitecture]] - economic and architectural logic behind customer-hosted data and infrastructure-based pricing.
- [[Observability]] - operating category in which Groundcover competes.
- [[FounderLedSales]] - early customer-acquisition and learning method.
- [[IncumbentReplacementMigration]] - commercial and post-sales discipline required for displacement.
