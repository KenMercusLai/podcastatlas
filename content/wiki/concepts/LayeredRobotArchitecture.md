---
title: "Layered Robot Architecture"
type: concept
tags: [robotics, architecture, embodied-ai]
sources:
  - e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e
  - 146-dui-physical-intelligence-ke-li-yiming-4-xiaoshi-fangtan-pi-de-kaiyuan-moxing-yanjiu-jiqiren-de-jianghu-zupu-yu-zhujiao-ljmazvdvad7o5md-nuiompd6-1nv
  - 184-yu-chenzhe-de-jushen-jibao-26q3-astra-chongji-hou-tongyong-moxing-hui-chidiao-robotics-ma-1ba74c4b-43e4-416c-aafe-f191fcb44898
  - e256-agent-jiqiren-yu-zhiyao-shui-xian-bei-gpt-6-astra-gaixie-9e6e1db1-f30b-492d-8a09-d8756b9df700
last_updated: 2026-10-20
knowledge_schema: synthesis-v1
---

# Layered Robot Architecture

## Definition
Layered robot architecture separates slower high-level understanding, planning, and supervision from faster low-level perception-action and control, while allowing training or deployed behavior to remain learned and partly end-to-end.

## Current Synthesis
The complete source set converges on layering for different reasons. The Sudu interview argues that scarce real-robot data and weak open-world manipulation favor an upper planner plus reliable lower-level skills trained with structured 3D information and simulation. The Physical Intelligence interview keeps learned policies and real-machine experience central, but shows that traditional planning, control, and performance discipline remain part of modern robot learning.

The Q3 review makes the upper layer more general. [[ChatGPT6Astra|Astra]] can reason about changed scenes, generate end-effector targets, supervise a specialized policy, and call simulation tools, while a local action model handles speed, precision, contact, and continuous feedback. Episode 256 adds a clearer timescale boundary: quasi-static work may tolerate hundreds of milliseconds or cloud reasoning, while high-dynamic action needs a small local model; slow reflection can diagnose one failure yet remain too expensive for fluent repetition.

Layering is therefore not a retreat to brittle hand-coded pipelines. It allocates timescales, data types, and reliability requirements to the components best able to meet them, with an interface that must translate general-model plans into fast physical control and return failures for revision.

## Key Claims
- The upper layer interprets the environment, decomposes tasks, chooses strategies, and can supervise or correct execution.
- The lower layer performs fast, contact-rich skills such as grasping, insertion, pouring, turning, and disturbance recovery.
- Layering can use learned geometry, material, kinematic, future-state, and action representations rather than fixed rules alone.
- Reliable short skills remain prerequisites for long tasks because serial failures compound.
- A general foundation model can deepen the upper layer without eliminating embodiment-specific policies, controllers, sensors, or hardware validation.
- Deployment may appear end-to-end even when pretraining and system design expose interpretable intermediate structure.
- The layer boundary should move with task dynamics: slow reasoning can serve quasi-static work, while high-frequency and safety-critical response stays local.

## Evidence
### Structured manipulation and simulation
- [[e244-duan-dao-duan-vs-shangxia-fenceng-jiqiren-lujing-zhizheng-zhengzai-zhuanxiang-fc9a3737-81a9-49cf-a7d6-530c77df836e]] defines the upper planning layer and lower manipulation layer and argues that structured 3D data, [[Sim2Real]], and hardware/software co-design can improve open-world reliability.

### Learned-policy continuity
- [[146-dui-physical-intelligence-ke-li-yiming-4-xiaoshi-fangtan-pi-de-kaiyuan-moxing-yanjiu-jiqiren-de-jianghu-zupu-yu-zhujiao-ljmazvdvad7o5md-nuiompd6-1nv]] connects contemporary imitation, reinforcement learning, and VLA policies to traditional robotics concerns about planning, control, and real-machine performance.

### General-model upper layer
- [[184-yu-chenzhe-de-jushen-jibao-26q3-astra-chongji-hou-tongyong-moxing-hui-chidiao-robotics-ma-1ba74c4b-43e4-416c-aafe-f191fcb44898]] reports Astra generating end-effector targets and supervising another action model while specialized local policies retain an advantage in precise, high-frequency contact tasks.
- [[e256-agent-jiqiren-yu-zhiyao-shui-xian-bei-gpt-6-astra-gaixie-9e6e1db1-f30b-492d-8a09-d8756b9df700]] reports action reflection and lower-level directional commands while preserving slow repetition, intuitive-physics, bimanual, alignment, and dynamic-control limits.

## Counterevidence & Qualifications
The sources do not establish one universally optimal boundary between layers. Extra interfaces can introduce latency, error propagation, and integration complexity, while end-to-end training may discover useful representations that designers omit. The reported Astra success figures lack common protocols and remain far below production proof. The episode 256 estimate that a sub-10B local model is comfortable is practitioner judgment rather than a universal threshold. Hardware, task, safety, and available data can shift which functions belong in each layer.

## What Changed
- Added an explicit quasi-static-versus-dynamic timescale boundary for cloud and local control.
- Added reflection as useful upper-layer diagnosis whose latency prevents it from replacing fluent repeated execution.

## Related Concepts
- [[GeneralModelRobotBoundary]] - determines which responsibilities can move into a general upper layer.
- [[SmallBrainActionLayer]] - local real-time execution layer beneath slower reasoning.
- [[VisionLanguageActionModels]] - learned policy family that can occupy or bridge layers.
- [[OpenWorldRobotManipulation]] - reliability bar for lower-level skills outside rehearsed scenes.
- [[Structured3DRobotData]] - intermediate physical representation used by one layered route.
- [[RobotResponseLatency]] - timing constraint that motivates separating slow reasoning from fast action.
- [[PhysicalRecursiveSelfImprovement]] - tool-using simulation loop that may improve policies across the architecture.
- [[RealWorldAIValidationLatency]] - feedback relationship between fast planning and slower physical proof.
