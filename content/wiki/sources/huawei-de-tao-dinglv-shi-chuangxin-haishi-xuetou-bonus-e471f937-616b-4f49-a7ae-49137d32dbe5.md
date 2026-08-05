---
title: "华为的「韬定律」，是创新还是噱头？｜ Bonus"
type: source
tags: [podcast, whats-next, semiconductors, huawei, eda]
sources: []
date: 2026-05-27
source_file: "/home/ken/repos/podcastatlas/content/episodes/华为的「韬定律」，是创新还是噱头？｜ Bonus [e471f937-616b-4f49-a7ae-49137d32dbe5].md"
source_url: "https://guiguzaozhidao.fireside.fm/20240426"
duration: "1027"
last_updated: 2026-08-05
---

## Summary
This [[WhatsNextKejiZaozhidao]] bonus episode has [[ZhangHaijun]] explain [[Huawei]]'s [[TauLaw]] as a shift from process-node and transistor-size language toward system-level time reduction. The episode is cautiously positive: it rejects the view that Tau Law is pure marketing, but it also says the most ambitious part, [[CellToCellLogicStacking]], is still unproven in shipped products. Its main addition to the wiki is the toolchain boundary: true cell-level logic folding would require new [[ElectronicDesignAutomation|EDA]] flows, packaging capability, and system engineering, not just a new slogan.

## Key Claims
- [[TauLaw]] is framed as replacing a pure nanometer-node metric with time, delay, and system-task completion speed as the practical measure of semiconductor progress.
- [[ZhangHaijun]] says the idea is system-level rather than a single device, process, or packaging technique; gate-level, chip-level, and system-level changes can all count if they reduce time.
- The episode distinguishes ordinary die-to-die [[Semiconductor3DStacking]] from [[CellToCellLogicStacking]], where logic-cell placement and vertical connection would be considered from the start of chip design.
- [[CellToCellLogicStacking]] is treated as the most distinctive technical idea in the episode, but Zhang says current public evidence does not show a real product using it.
- The claim that 381 Huawei chips were designed and produced "based on Tau Law" is interpreted broadly: those chips may follow the lower-time design methodology without necessarily using cell-to-cell stacking.
- [[ElectronicDesignAutomation|EDA]] is a central bottleneck because cell-level folding would need new design tools rather than only back-end packaging changes.
- [[AdvancedPackaging]] still matters after design because three-dimensional logic routes raise process, connection, and manufacturing requirements.
- The episode says 3D stacking itself is not unique to Huawei; [[TSMC]] CoWoS, AMD 3D V-Cache, [[Nvidia]] super-node designs, and [[Google]] [[TPU]] interconnect improvements are used as comparison points.
- The source treats the reported 2031 "equivalent 1.4 nm" target as a system-performance comparison rather than literal physical line width.
- Chinese constraint conditions make an alternate route more strategically attractive for Huawei, but the source still requires later proof through tools, chips, cost, power, and reliable production.

## Key Quotes
> "不是噱头" — Zhang's short answer to whether Tau Law is only marketing.

> "Cell-to-Cell 的堆叠" — the episode's distinction between Huawei's ambitious logic-folding idea and more common chip-to-chip stacking.

> "目前全球还没有哪个产品真正使用这种技术" — Zhang's caveat about public product evidence for cell-level stacking.

## Connections
- [[WhatsNextKejiZaozhidao]] — show context for the bonus episode.
- [[ZhangHaijun]] — guest and semiconductor engineer explaining the claim.
- [[Huawei]] and [[TauLaw]] — company and central doctrine under discussion.
- [[CellToCellLogicStacking]] — source-specific technical caveat around logic folding.
- [[Semiconductor3DStacking]] and [[AdvancedPackaging]] — broader packaging and vertical-integration context.
- [[ElectronicDesignAutomation]] and [[Synopsys]] — toolchain layer that would have to change for cell-level folding.
- [[MooreLaw]] and [[ConstraintDrivenEngineeringStrategy]] — incumbent scaling frame and constraint-driven alternate route.
- [[TSMC]], [[Nvidia]], [[Google]], and [[TPU]] — comparison cases for advanced packaging, system architecture, and interconnect improvement.

## Contradictions
- No direct contradiction found with the existing Huawei [[KejiLuandun]] source. This source supports the same cautious position that [[TauLaw]] is more defensible as a system metric than as a literal replacement for [[MooreLaw]].
- It narrows the existing interpretation by separating die-to-die stacking from [[CellToCellLogicStacking]] and by warning that "based on Tau Law" does not prove the most ambitious cell-level implementation has shipped.
- It also qualifies public hype around "domestic chip breakthrough" claims: the source sees a plausible technical direction, but not enough product, EDA, yield, cost, or power evidence for a final verdict.
