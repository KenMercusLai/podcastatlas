---
title: "Consent-Based Recording"
type: concept
tags: [privacy, ai, wearables, governance]
sources: [tsr-s3-dansiroker-v3-tsr-s3-dansiroker-v3]
last_updated: 2026-07-23
---

# Consent-Based Recording

Consent-based recording is the privacy pattern [[DanSiroker]] describes for the [[Limitless]] pendant in [[tsr-s3-dansiroker-v3-tsr-s3-dansiroker-v3]]. Dan says the device should include consent mode, where it records only voices that have verbally opted in and avoids capturing a newly heard voice until consent is given.

The concept matters because [[PersonalAIMemory]] moves AI assistants from a user's screen into shared physical space. A wearable may be owned by one person but capture other people's speech, social expectations, workplace context, and legally protected conversations. Consent-based recording is one proposed boundary for making [[WearableAIAssistant]] products less invasive, though the source does not independently verify the implementation.

## Key Claims
- Recording consent has to account for bystanders, not only the person wearing or owning the device.
- Voice-level opt-in can make consent more granular than a room-level warning, but it also creates implementation and reliability demands.
- Legal compliance and social comfort are separate problems; a product can be legally allowed yet still feel creepy or hostile.
- Consent boundaries need to work in live interaction without making every meeting or conversation unusably awkward.
- The approach should be evaluated alongside retention, deletion, encryption, audit, and user-control policies.

## Connections
- [[Limitless]], [[DanSiroker]], and [[PersonalAIMemory]] - source case and memory-product context.
- [[WearableAIAssistant]], [[OSLevelContext]], [[AgentPermissionBoundaries]], and [[ApplePrivacy]] - adjacent privacy and permission concepts.
- [[ConsumerCameraSurveillance]] - related bystander-consent problem for consumer sensing devices.
