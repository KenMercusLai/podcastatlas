---
title: "Embodied Capability Framework / 具身智能三项能力"
type: concept
tags: [robotics, embodied-ai, capability, evaluation]
sources:
  - yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

# Embodied Capability Framework / 具身智能三项能力

## Definition
The embodied capability framework is [[ShenpuIntelligence|深普智能]]'s internal way of specifying what "intelligence" means for a physical agent, organized around three abilities: adaptability, steerability, and context understanding.

## Current Synthesis
The bounded source treats embodied intelligence as a capability profile rather than a model class or product category. Adaptability runs from zero-shot performance through few-shot adaptation into fully out-of-distribution scenes. Steerability covers control through language, images, and video, including following a demonstration video quickly. Context understanding requires world dynamics and causal information beyond the current observation, which the source says much embodied work underweights. The three axes then drive data choices, selective borrowing from world-model and VLA work, and evaluation design, so the framework functions as a route-selection filter rather than a public benchmark.

## Key Claims
- The source defines embodied intelligence by capability rather than by a single model family, demo, or hardware form.
- Adaptability is specified as zero-shot ability plus few-shot adaptation through fully out-of-distribution scenes.
- Steerability covers different control channels, including language, image, and video, and the ability to follow a video demonstration quickly.
- Context understanding requires world dynamics and causal information, not only the current observation or the most recent frame.
- The framework is used to select data, model components, and evaluation targets, which is why the company says it borrows only the parts of world models and VLA it needs.
- A capability missing from the framework tends to be under-instrumented in data collection and evaluation, so the framework shapes what the company can later measure.

## Evidence
- Framework definition: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] gives adaptability, steerability, and context understanding as the three abilities the company discusses when it asks where embodied intelligence actually resides.
- Adaptability and steerability evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] describes zero-shot performance and few-shot adaptation toward out-of-distribution scenes, and lists language, image, and video as control forms.
- Context evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] says many embodied systems act from the current observation and underweight native context and causal information.
- Route-selection evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] says the company reverse-engineers the model from its defined capabilities and borrows selectively from world models and VLA instead of aligning with a concept label.

## Counterevidence & Qualifications
The framework is a company-internal framing from one interview, not a validated evaluation standard. Its three terms are broad enough to overlap with existing generalization, steerability, and world-model discussion, and the source gives no measurements, success rates, or comparison with other frameworks. Read the page as a bounded statement of how one company organizes the problem rather than as evidence that these axes are complete or mutually exclusive.

## What Changed
- Created the concept from the interview's definition of embodied intelligence through adaptability, steerability, and context understanding.
- Connected the framework to data selection, model borrowing, and evaluation design as one internal filter.

## Related Concepts
- [[VisionLanguageActionModels]] - adjacent model family that the framework refuses to reduce embodied intelligence to.
- [[RobotGeneralizationPerformanceTradeoff]] - adaptability without reliable performance is the tradeoff this framework tries to separate.
- [[EmbodiedContextMemory]] - the context-understanding axis expressed as short, medium, and long memory.
- [[SmallBrainActionLayer]] - execution capability that adaptability and steerability ultimately have to reach.
- [[RobotEvaluationProblem]] - evaluation problem the framework would need observable metrics to solve.
- [[ChatGPT6Astra]] - general-model capability that the source evaluates through these axes rather than as a total solution.
