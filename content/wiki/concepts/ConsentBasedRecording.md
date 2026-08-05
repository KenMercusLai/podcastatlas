---
title: "Consent-Based Recording"
type: concept
tags: [privacy, ai, wearables, governance]
sources: [tech-20260109-0109-mp-tech-pod-128-tech-20260109-0109-mp-tech-pod-128, tech-20251225-1225-mp-tech-pod-128-tech-20251225-1225-mp-tech-pod-128, tsr-s3-dansiroker-v3-tsr-s3-dansiroker-v3]
last_updated: 2026-08-05
---

# Consent-Based Recording

Consent-based recording is the privacy pattern [[DanSiroker]] describes for the [[Limitless]] pendant in [[tsr-s3-dansiroker-v3-tsr-s3-dansiroker-v3]]. Dan says the device should include consent mode, where it records only voices that have verbally opted in and avoids capturing a newly heard voice until consent is given.

The concept matters because [[PersonalAIMemory]] moves AI assistants from a user's screen into shared physical space. A wearable may be owned by one person but capture other people's speech, social expectations, workplace context, and legally protected conversations. Consent-based recording is one proposed boundary for making [[WearableAIAssistant]] products less invasive, though the source does not independently verify the implementation.

[[tech-20251225-1225-mp-tech-pod-128-tech-20251225-1225-mp-tech-pod-128]] adds a contrast case through [[Meta]] AI glasses. [[WillGottsagen]] notes that a visible light can signal video recording, but the source still worries about always-on listening. That contrast shows why recording consent cannot be reduced to a camera indicator: microphones, contextual inference, retention, and bystander awareness all need separate treatment.

[[tech-20260109-0109-mp-tech-pod-128-tech-20260109-0109-mp-tech-pod-128]] reinforces the same distinction through stronger demand for updated [[RayBanSmartGlasses|Ray-Ban smart glasses]]. The source says the glasses have a small red light while recording, but [[MariaCurie|Maria Curi]] questions whether people nearby can reliably notice it, making [[SmartGlassesBystanderPrivacy]] a consent problem as well as a product-design problem.

## Key Claims
- Recording consent has to account for bystanders, not only the person wearing or owning the device.
- Voice-level opt-in can make consent more granular than a room-level warning, but it also creates implementation and reliability demands.
- Legal compliance and social comfort are separate problems; a product can be legally allowed yet still feel creepy or hostile.
- Consent boundaries need to work in live interaction without making every meeting or conversation unusably awkward.
- The approach should be evaluated alongside retention, deletion, encryption, audit, and user-control policies.
- A visible recording cue can improve notice for one modality while leaving other sensing channels, such as microphones and ambient inference, unresolved.
- Commercially successful smart glasses make consent norms more urgent because bystander exposure grows as the device becomes ordinary.

## Connections
- [[Limitless]], [[DanSiroker]], and [[PersonalAIMemory]] - source case and memory-product context.
- [[WearableAIAssistant]], [[OSLevelContext]], [[AgentPermissionBoundaries]], and [[ApplePrivacy]] - adjacent privacy and permission concepts.
- [[ConsumerCameraSurveillance]] - related bystander-consent problem for consumer sensing devices.
- [[Meta]], [[RayBanSmartGlasses|Ray-Ban smart glasses]], and [[WillGottsagen]] - always-on wearable privacy contrast added by Marketplace Tech.
- [[SmartGlassesBystanderPrivacy]], [[NeuralBand]], and [[ConsumerCameraSurveillance]] - January 2026 smart-glasses demand and notice problem.
