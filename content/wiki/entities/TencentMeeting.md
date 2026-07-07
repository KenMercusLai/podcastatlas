---
title: "Tencent Meeting"
type: entity
tags: [product, collaboration, saas, video]
sources: [vol-164-cong-pingguo-liaodao-ruanjian-weilai-agentic-software-zhende-yaolaile-1-6639-1]
last_updated: 2026-07-07
---

# Tencent Meeting

Tencent Meeting is used in [[vol-164-cong-pingguo-liaodao-ruanjian-weilai-agentic-software-zhende-yaolaile-1-6639-1]] as the episode's concrete example for imagining [[AgenticSoftware]]. The hosts ask what would happen if a familiar meeting product stopped being only a fixed application and became a set of callable video, audio, recording, storage, interface, and media capabilities that agents could assemble for a scene such as podcast recording.

The source does not analyze Tencent Meeting as a market case in detail. Its role is architectural: it makes [[AtomicCapabilityServices]] easier to see because a meeting product already contains multiple useful primitives that can be recombined for calls, recordings, virtual studios, storage, and workflow-specific review surfaces.

## Source Position
- Meeting software can be decomposed into communication, media, storage, recording, and interface atoms.
- A user may describe a desired workflow such as podcast recording, while an agent assembles a more specific interface from the available capabilities.
- The resulting product might no longer look like one universal meeting app; it could become many scene-specific views backed by the same infrastructure.
- This thought experiment illustrates why [[AgenticSoftware]] challenges conventional SaaS packaging and platform review assumptions.

## Connections
- [[Tencent]] — company context.
- [[AgenticSoftware]] — broader software form discussed through the example.
- [[AtomicCapabilityServices]] — concept extracted from the Tencent Meeting thought experiment.
- [[AgentFacingInterfaces]], [[HeadlessSoftware]], and [[GeneratedWorkInterfaces]] — interface patterns implied by making meeting capabilities callable and recombinable.
