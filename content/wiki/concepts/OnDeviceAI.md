---
title: "On-Device AI"
type: concept
tags: [ai, edge-ai, smartphones, systems]
sources: [ai-shidai-de-chaoji-rukou-haishi-shouji-ma-s10e17-523a0d42-4c16-4dd6-a2ab-9277fec1a731, 268-ai-shidai-geren-gongzuotai-hui-zhongxin-huidao-shouji-ma-lgprs5juhhrjykbzasaqvdlzx8fs]
last_updated: 2026-07-09
---

# On-Device AI

On-Device AI is the implementation frame in [[ai-shidai-de-chaoji-rukou-haishi-shouji-ma-s10e17-523a0d42-4c16-4dd6-a2ab-9277fec1a731]] for running useful AI behavior on phones rather than treating the handset only as a remote display for cloud models. The episode stresses that this is not a matter of copying a large cloud model onto a phone: it requires hardware compute, model adaptation, NPU execution tools, power management, thermal limits, foreground smoothness, privacy choices, and application design.

[[ChenYiqiang]] describes the chip-side stack as hardware investment, software development architecture, and system-level energy scheduling. [[HanBoxiao]] describes the terminal-side stack as hardware, model, system, and application layers. Together, their account makes on-device AI a systems problem rather than only a model-size problem.

[[268-ai-shidai-geren-gongzuotai-hui-zhongxin-huidao-shouji-ma-lgprs5juhhrjykbzasaqvdlzx8fs]] adds the user-context and workbench version. Local AI becomes a stronger upgrade reason when it can handle privacy-sensitive files, meeting records, screenshots, habits, and assistant memory on the device instead of functioning only as a cloud-chat shortcut.

## Key Claims
- The terminal needs enough AI compute before applications are fully known because smartphone chips are planned years ahead.
- NPU hardware behaves more like specialized acceleration than a general computer, so model vendors and handset makers need middleware and adaptation layers to run models efficiently.
- Model compression and smaller local models matter because phones face battery, heat, memory, and price constraints.
- On-device AI must coexist with everyday workloads such as meetings, videos, games, display refresh, image processing, and foreground app responsiveness.
- Useful local tasks include speech transcription, role-separated meeting notes, file grouping and analysis, preference learning, recognition, memory, and simpler image enhancement.
- Heavy long-context understanding, complex generation, and advanced image/video effects may remain cloud-heavy until terminal hardware and models improve.
- Local AI can differentiate new phones when it supports [[AIFileManagement]], meeting assistants, and low-latency context understanding that a generic cloud app cannot fully own.

## Connections
- [[Vivo]], [[HanBoxiao]], [[MediaTek]], [[ChenYiqiang]], and [[Dimensity9500]] — source actors and platform case.
- [[OnDeviceModelHierarchy]] — broader hierarchy of endpoint and local model sizes.
- [[EdgeCloudAIBoundary]] — boundary between terminal-side and cloud-side work.
- [[HandsetChipCoDesign]] — planning process needed to make terminal AI possible.
- [[SmartphoneAIHub]] and [[FoldablePhoneProductivity]] — product surfaces where on-device AI becomes visible.
- [[MobileAIWorkstation]] and [[AIFileManagement]] — workbench and personal-file contexts added by Luanfanshu 268.
- [[OSLevelContext]], [[ContextEngineering]], and [[AgentPermissionBoundaries]] — adjacent context, privacy, and permission issues once local devices sense and remember more.
