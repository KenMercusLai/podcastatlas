---
title: "Cross-Device Personal Memory / 跨设备个人记忆"
type: concept
knowledge_schema: synthesis-v1
tags: [ai, memory, interoperability, privacy, edge-ai]
sources:
  - dang-yanjing-erji-shouji-dou-you-ai-shui-lai-tongyi-ni-de-di-er-danao-2026-gaotong-xiaolong-fenghui-s10e31-2d6bfcec-31c3-4ef2-981f-6dc2864cf92d
last_updated: 2026-09-30
---

# Cross-Device Personal Memory / 跨设备个人记忆

## Definition
Cross-device personal memory is a continuity layer that turns perception and activity from phones, glasses, earbuds, PCs, cars, pendants, rings, and other devices into user-governed context that can be retrieved and carried across hardware, brands, operating systems, and ongoing tasks.

## Current Synthesis
The source frames personal AI as a distributed system. Different devices have different advantages for sensing, interaction, display, compute, and mobility, while the phone remains the likely near-term holder of identity, private context, payment, permissions, and coordination. A coherent “second brain” therefore cannot be only a larger model or a synchronized folder. It needs multimodal indexing, salience and privacy judgment, identity resolution, task state, permission continuity, and interoperable protocols.

The safest architecture in the source is local-first but hybrid: sensitive raw perception and memory remain on trusted devices where possible, while harder reasoning can use cloud models under explicit authorization. This is still a proposal rather than a demonstrated standard. Qualcomm can improve interoperability within its hardware ecosystem, but durable cross-brand memory also requires operating-system, application, and device-maker cooperation.

## Key Claims
- Multiple AI devices make memory continuity a system problem rather than a feature of one assistant or one form factor.
- Raw video, audio, text, motion, and spatial data must be indexed and transformed before they become useful memory.
- The phone can remain the near-term identity, permission, connectivity, payment, and compute hub even when glasses or earbuds become more frequent interaction edges.
- Cross-device continuity must preserve task state and authorization, not only copy files or launch the same application.
- Local retention reduces some exposure of sensitive perception, while selective cloud reasoning remains useful for tasks beyond edge capability.
- Open protocols and portable memory are necessary if users are not to be trapped inside separate vendor-specific recollections of their lives.

## Evidence
- **Distributed sensing and coordination:** [[dang-yanjing-erji-shouji-dou-you-ai-shui-lai-tongyi-ni-de-di-er-danao-2026-gaotong-xiaolong-fenghui-s10e31-2d6bfcec-31c3-4ef2-981f-6dc2864cf92d]] describes glasses, earbuds, phones, PCs, pendants, rings, cars, and other endpoints gathering or using personal context.
- **Memory transformation:** [[dang-yanjing-erji-shouji-dou-you-ai-shui-lai-tongyi-ni-de-di-er-danao-2026-gaotong-xiaolong-fenghui-s10e31-2d6bfcec-31c3-4ef2-981f-6dc2864cf92d]] reports an indexing approach that converts video, audio, text, action, and 3D-space signals into retrievable representations.
- **Local-first privacy boundary:** [[dang-yanjing-erji-shouji-dou-you-ai-shui-lai-tongyi-ni-de-di-er-danao-2026-gaotong-xiaolong-fenghui-s10e31-2d6bfcec-31c3-4ef2-981f-6dc2864cf92d]] argues that sensitive perception and personal memory should stay on trusted local devices while complex reasoning may use the cloud.
- **Interoperability limit:** [[dang-yanjing-erji-shouji-dou-you-ai-shui-lai-tongyi-ni-de-di-er-danao-2026-gaotong-xiaolong-fenghui-s10e31-2d6bfcec-31c3-4ef2-981f-6dc2864cf92d]] reports Qualcomm's work on Snapdragon-device interoperability but gives no implementation detail for a cross-brand open standard.

## Counterevidence & Qualifications
The evidence comes from summit demonstrations, company interviews, and episode interpretation rather than a deployed cross-brand memory standard. Continuous capture may include bystanders and sensitive locations even when storage is local. Open protocols do not automatically provide consent, deletion, correction, security, accurate identity resolution, or protection from manipulation. A phone-centered architecture may also change if another device becomes the trusted identity and authorization anchor.

## What Changed
- Added a distinct continuity layer between single-device personal memory and proactive cross-device action.

## Related Concepts
- [[PersonalAIMemory]] - broader retained personal context that the cross-device layer must govern.
- [[MultimodalPersonalMemory]] - non-text perception that must be transformed and aligned.
- [[LocalFirstMemoryLayer]] - privacy-oriented storage and processing architecture.
- [[SmartphoneAIHub]] - likely near-term coordinator for identity, permissions, connectivity, and compute.
- [[EdgeCloudAIBoundary]] - task-by-task placement between trusted devices and remote models.
- [[RememberUnderstandActLoop]] - action progression that depends on coherent memory.
- [[AIHardwarePrivacyExchange]] - benefit, consent, and exposure tradeoff created by continuous sensing.
