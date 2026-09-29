---
title: "Memory Box"
type: entity
knowledge_schema: synthesis-v1
tags: [product, ai, memory, local-ai, personal-data]
sources:
  - lsh8sdro6i9mkt5nug4zkibv95tn
last_updated: 2026-09-29
---

# Memory Box

## Overview
Memory Box is [[MemVerge]]'s consumer-facing personal AI memory application, described in [[lsh8sdro6i9mkt5nug4zkibv95tn]] as the first commercial product built on [[MemoryMachine]].

## Current Profile
The product aims to index scattered personal data and let users query it without manually finding and uploading individual files. Its proposed architecture combines an embedded chat agent, local models, selective remote inference, browser integration, and a planned [[ModelContextProtocol|MCP]] server. This is a product-team description; the source does not independently verify privacy, retrieval, or adoption outcomes.

## Key Characteristics
- Targets heavy AI users and some small-team use rather than developers alone.
- Connects local files, cloud storage, applications, email, chat history, and model conversations.
- Supports local and hybrid execution according to sensitivity and task difficulty.
- Aims to become a primary personal AI interface while remaining callable from other tools.
- Plans free and paid subscription tiers plus broader mobile availability.

## Evidence
### Personal-data interface
- [[lsh8sdro6i9mkt5nug4zkibv95tn]] says users should be able to ask about work, finance, or life data without knowing which file holds the answer.

### Hybrid execution
- [[lsh8sdro6i9mkt5nug4zkibv95tn]] describes local handling for private or easier tasks and external-model use for harder non-private work or constrained devices.

### Interoperability and commercialization
- [[lsh8sdro6i9mkt5nug4zkibv95tn]] mentions a browser extension, planned MCP server, PC and Mac support, planned mobile releases, and tiered subscriptions.

## Qualifications
- Retrieval quality, zero-retention claims, model routing, context limits, subscription details, and future releases are unverified product claims or plans.
- Centralizing personal information can increase the consequence of incorrect access control, stale memory, or compromised credentials.

## What Changed
- Created a product profile centered on personal-data access, hybrid inference, and interoperability.

## Relationships
- [[MemVerge]] - developer company.
- [[CharlesFan]] - CEO and product spokesperson.
- [[MemoryMachine]] - underlying memory layer.
- [[LocalFirstMemoryLayer]] - architectural pattern the product claims to implement.
- [[AIMemoryLifecycle]] - retrieval and long-term maintenance problem the product must address.
