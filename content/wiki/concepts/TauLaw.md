---
title: "Tau Law"
type: concept
tags: [semiconductors, strategy, engineering, huawei]
sources: [dang-huawei-paochu-tao-dinglv-women-gai-xin-ta-dao-na-yibu-keji-luandun, huawei-de-tao-dinglv-shi-chuangxin-haishi-xuetou-bonus-e471f937-616b-4f49-a7ae-49137d32dbe5]
last_updated: 2026-08-05
---

# Tau Law

Tau Law is the semiconductor and organization idea evaluated in [[dang-huawei-paochu-tao-dinglv-women-gai-xin-ta-dao-na-yibu-keji-luandun]]. The source describes it as [[Huawei]]'s attempt to reframe chip progress around tau, signal delay, and end-to-end system speed rather than only around smaller process nodes.

The hosts' main position is cautious: [[TauLaw]] should not be read as a new natural law that replaces Moore's Law. It is more defensible as a KPI-like engineering metric that can align devices, process, circuits, architecture, systems, and software around lower latency. Its credibility depends on whether [[Huawei]] can produce measurable, repeatable gains in performance, cost, and energy efficiency.

[[huawei-de-tao-dinglv-shi-chuangxin-haishi-xuetou-bonus-e471f937-616b-4f49-a7ae-49137d32dbe5]] sharpens the implementation boundary through [[ZhangHaijun]]'s explanation of [[CellToCellLogicStacking]]. The bonus episode treats the time metric as meaningful and not merely marketing, but says full logic-cell stacking would need new [[ElectronicDesignAutomation|EDA]] flows and public product proof; Huawei's "381 chips" claim is therefore broader methodology evidence, not proof that the hardest cell-level route has shipped.

## Key Claims
- Tau is treated as a time-constant and delay-oriented metric: smaller tau means faster switching and shorter effective communication paths.
- The episode frames the first move as changing the goal from "smaller" to "faster."
- [[Semiconductor3DStacking]] and "logic folding" are the technical routes named in the source, but the hosts say the details of logic folding remain unclear from public information.
- The What's Next source narrows "logic folding" into [[CellToCellLogicStacking]], distinguishing it from die-to-die stacking such as HBM, CoWoS-style packaging, or cache stacking.
- The same source treats EDA readiness as a gating test for whether [[TauLaw]] can become a practical design flow rather than only a system-performance frame.
- [[TauLaw]] has an internal organization role: it can give [[HiSilicon]] and adjacent teams a shared measure across device, circuit, architecture, system, and software layers.
- The public word "law" is treated as a communication and mobilization choice, not proof that the idea has the status of physics.
- To become an industry law, it would need the kind of long-term, measurable, ecosystem-coordinating proof that Moore's Law once provided.

## Connections
- [[Huawei]] — origin and main strategic context.
- [[HiSilicon]] — chip-design capability that would have to help implement the metric.
- [[RenZhengfei]] and [[HuaweiOrganizationalMethodology]] — organization background for why a KPI-like technical doctrine fits Huawei.
- [[Semiconductor3DStacking]] — key technical route for reducing signal distance and latency.
- [[CellToCellLogicStacking]] and [[ElectronicDesignAutomation]] — What's Next's toolchain-specific implementation boundary.
- [[ConstraintDrivenEngineeringStrategy]] — strategic reason Huawei would emphasize a route beyond pure lithography scaling.
- [[LargeCompanyOrganizationalInertia]] — contrast case: tau-law framing attempts to coordinate a large organization around one metric rather than let scale fragment effort.
