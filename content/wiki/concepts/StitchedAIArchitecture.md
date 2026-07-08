---
title: "Stitched AI Architecture"
type: concept
tags: [ai, autonomous-driving, robotics, technical-debt]
sources: [143-dui-he-xiaopeng-de-di-er-ci-fangtan-gengda-duzhu-renxing-jiqiren-iron-dansheng-nachang-yiwai-jishu-jubian-xia-ceo-gx-he-fengheguai-ljekstsafrj-ovtm2bpl92s4nwoc]
last_updated: 2026-07-08
---

# Stitched AI Architecture

Stitched AI architecture is the wiki name for [[HeXiaopeng]]'s "缝合怪" critique in [[143-dui-he-xiaopeng-de-di-er-ci-fangtan-gengda-duzhu-renxing-jiqiren-iron-dansheng-nachang-yiwai-jishu-jubian-xia-ceo-gx-he-fengheguai-ljekstsafrj-ovtm2bpl92s4nwoc]]. In the source, it means an autonomous-driving or robotics system built from heavy software rules plus partial AI modules, rather than a more unified model-driven physical-intelligence stack.

The critique is not that old systems are useless. The source says they can improve assisted driving and known scenarios, but their ceiling is limited when the system enters unfamiliar garages, rare environments, or robot tasks that require generalization. XPeng's strategic risk is therefore a route change: a new foundation-model-like approach may start with worse lower-bound behavior and many engineering problems, but the source argues that the old stitched route cannot reach full autonomy or general robots.

## Key Claims
- Rule-heavy systems can produce local product progress while hiding a long-term ceiling problem.
- Physical-world edge cases expose the limits of manually described scenes, memorized routes, and ad hoc software rules.
- Moving away from stitched architecture creates short-term regressions because the new stack may initially have lower reliability and many unresolved engineering details.
- The architecture critique links technical judgment to [[AIOrganizationDesign]] because old teams and processes may keep optimizing the legacy route.

## Connections
- [[PhysicalAI]] — strategic target that requires moving beyond stitched systems.
- [[XPeng]], [[HeXiaopeng]], [[XPengIron]], and [[XPengGX]] — source case and products affected by the architecture choice.
- [[EmbodiedAI]], [[WorldModels]], and [[PhysicalWorldDataFlywheel]] — technical directions that make the old-rule critique important.
- [[AIEngineeringThinking]] — need to redesign systems, tests, data, and feedback loops rather than only adopt tools.
- [[AIOrganizationDesign]] — organization change required to stop optimizing the old path.
