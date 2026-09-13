---
title: "NeMoClaw"
type: entity
knowledge_schema: synthesis-v1
tags: [ai, agents, nvidia, security]
sources:
  - ep-38-the-local-ai-stack-nobody-talks-about-but-should
last_updated: 2026-09-13
---

# NeMoClaw

## Overview
NeMoClaw is mentioned in [[ep-38-the-local-ai-stack-nobody-talks-about-but-should]] as an Nvidia-associated, more security-first variation in the local-agent discussion.

## Current Profile
The episode contrasts NeMoClaw with [[OpenClaw]] through default permissions. NeMoClaw is described as starting with nothing allowed and requiring explicit configuration before the agent can act, making it a useful anchor for enterprise-safe agent setup.

## Key Characteristics
- Security-first local-agent variation in the source account.
- Starts from a deny-by-default permission posture as described in the episode.
- Illustrates the enterprise tradeoff between safety, setup burden, and agent usefulness.

## Evidence
### Permission model
- [[ep-38-the-local-ai-stack-nobody-talks-about-but-should]] says NeMoClaw starts with nothing allowed and requires users to explicitly configure what the agent can do.

### Enterprise safety framing
- [[ep-38-the-local-ai-stack-nobody-talks-about-but-should]] presents NeMoClaw as potentially safer for enterprise settings, while warning that it adds setup and friction.

## Qualifications
- The source does not provide product documentation, release status, or independent security assessment.
- The page should keep NeMoClaw source-scoped until later sources corroborate details.

## What Changed
- Created NeMoClaw as the security-first local-agent comparison point.

## Relationships
- [[OpenClaw]] - local-agent comparison in the source.
- [[AgentPermissionBoundaries]] - permission model NeMoClaw illustrates.
- [[AgentEnvironmentIsolation]] - safety pattern adjacent to the source's warning.
- [[Nvidia]] - ecosystem affiliation named in the episode.
