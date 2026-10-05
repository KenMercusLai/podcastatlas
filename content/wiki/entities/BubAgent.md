---
title: "Bub"
type: entity
knowledge_schema: synthesis-v1
tags: [ai-agent, coding-agent, group-chat]
sources:
  - 8226494223-026583
last_updated: 2026-10-06
---

# Bub

## Overview
Bub is an AI-agent project described in the source as beginning with a thin coding-agent loop and later being adapted for persistent participation in group chat.

## Current Profile
Bub combines basic coding tools with channels, identity-aware group interaction, an append-only tape, anchors and handoffs, searchable history, skills, and self-written capabilities. Its design goal is not constant responsiveness: it tries to participate when socially activated, preserve long-running history, and let components be replaced or extended. The same flexibility creates cost, retrieval, silence, permission, formatting, and verification problems that still require human engineering.

## Key Characteristics
- Began with file read, write, edit, Bash, and an agent loop as its minimal coding substrate.
- Uses mentions and a configurable activity window to decide when group-chat messages enter its working interaction.
- Records messages, tool calls, state, intermediate events, and feedback in an append-only tape.
- Uses anchors and handoffs to change the visible working context without deleting older history.
- Can retrieve older tape content and package repeated work as skills or deterministic code.
- Is moving toward replaceable cores, tape implementations, and channels so other agents can be “Bubified.”

## Evidence
### Coding substrate and group-chat behavior
- [[8226494223-026583]] describes Bub's four-tool coding-agent origin and its later mention, reply, identity, activity-window, and silence behavior in Telegram groups.

### Context and capability architecture
- [[8226494223-026583]] describes tape, anchors, handoffs, selective history search, reviewed facts, skills, self-written I/O, and replaceable components.

### Operational boundaries
- [[8226494223-026583]] reports non-response, context flooding, formatting mistakes, token cost, permission risk, and verification failure as continuing constraints.

## Qualifications
- The profile rests on one interview with project builders rather than independent code review, benchmarks, security analysis, or controlled comparisons.
- “Self-evolution” here means accumulating skills, code, context, and operating methods; it does not establish autonomous model improvement.
- The transcript does not fully specify Bub's implementation, licensing, deployment footprint, or separation from the speakers' individual forks and experiments.

## What Changed
- Established Bub as a distinct agent project rather than treating it as another name for OpenClaw.
- Identified selective group-chat participation and tape-based context as its defining source-backed features.

## Relationships
- [[FrostMing]] - builder and interview guest describing Bub's I/O and self-extension experiments.
- [[ZhuoranBub]] - builder and interview guest explaining tape, anchors, handoffs, and channel abstraction.
- [[GroupChatAgentParticipation]] - social interaction problem Bub is designed to address.
- [[AgentTapeSystem]] - append-only context architecture used to preserve and revisit history.
- [[AgentHarness]] - broader runtime layer containing tools, channels, context, skills, and permissions.
- [[OpenClaw]] - adjacent personal-agent form that motivated Bub's expansion beyond coding.
