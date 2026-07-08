---
title: "On-Device Model Hierarchy"
type: concept
tags: [ai, edge-ai, hardware, model-architecture]
sources: [144-dui-yang-meng-de-4-xiaoshi-fangtan-xiaofei-dianzi-si-yu-sheng-di-san-lei-gongsi-duan-ce-moxing-chanpin-fangfa-youxi-moshi-lnjleqjgjo1txupouvygmdv7oo8b, ai-shidai-de-chaoji-rukou-haishi-shouji-ma-s10e17-523a0d42-4c16-4dd6-a2ab-9277fec1a731]
last_updated: 2026-07-09
---

# On-Device Model Hierarchy

On-Device Model Hierarchy is [[YangMeng]]'s distributed-intelligence frame in [[144-dui-yang-meng-de-4-xiaoshi-fangtan-xiaofei-dianzi-si-yu-sheng-di-san-lei-gongsi-duan-ce-moxing-chanpin-fangfa-youxi-moshi-lnjleqjgjo1txupouvygmdv7oo8b]]. He expects future AI systems to combine trillion-scale cloud "brains," billion- to ten-billion-scale endpoint models, and million- to ten-million-scale perception/control models inside sensors, actuators, and small devices.

The analogy is biological: a human body does not send every signal to one central super-brain. Eyes, ears, muscles, and other organs perform local processing while higher-level planning happens elsewhere. In product terms, the model size should match the problem's complexity, latency, privacy, and power constraints.

[[ai-shidai-de-chaoji-rukou-haishi-shouji-ma-s10e17-523a0d42-4c16-4dd6-a2ab-9277fec1a731]] adds the smartphone implementation version. [[HanBoxiao]] says [[Vivo]] adapts smaller models to phone platforms and special foldable system versions, while [[ChenYiqiang]] explains why [[MediaTek]] needs NPU architecture, middleware, and scheduling so endpoint models can run efficiently inside everyday phone workloads.

## Key Claims
- Hardware AI should not be reduced to one giant model controlling every device from the cloud.
- Different tasks need different model scales: speech separation, local video search, robot control, and general planning do not have the same compute requirements.
- Endpoint and local models can improve privacy, latency, and reliability when continuous cloud access is undesirable.
- The hierarchy makes hardware more than a model-company accessory; devices become distributed organs of perception and control.
- It also changes product design: the user cares about smoother experience, not whether intelligence came from a cloud model, base station, chip, or tiny local model.
- The smartphone version adds a system constraint: local models must share battery, heat, memory, display, CPU, GPU, and NPU budgets with the rest of the phone experience.

## Connections
- [[YangMeng]] and [[AnkerInnovations]] — source speaker and company case.
- [[InMemoryComputingForEdgeAI]] — chip route for the smaller levels of the hierarchy.
- [[TrueSmartHome]] and [[HouseholdSecurityRobots]] — home examples where local perception and control matter.
- [[AIPlusTerminals]], [[PhysicalAI]], and [[EmbodiedAI]] — broader terminal and physical-intelligence context.
- [[WorldModels]] and [[VisionLanguageActionModels]] — higher-level model directions that may coordinate with local models.
- [[Vivo]], [[MediaTek]], [[Dimensity9500]], [[OnDeviceAI]], and [[EdgeCloudAIBoundary]] — phone-specific extension from S10E17.
