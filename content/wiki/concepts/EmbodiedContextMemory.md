---
title: "Embodied Context & Memory / 具身上下文与记忆"
type: concept
tags: [robotics, embodied-ai, memory, context]
sources:
  - yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

# Embodied Context & Memory / 具身上下文与记忆

## Definition
Embodied context and memory is the temporal and causal state a robot must carry across short, medium, and long horizons so its actions depend on what just happened, what it has learned about similar situations, and what it remembers about places and people.

## Current Synthesis
The source argues that context is one of the most important parts of an agent and that embodied work often focuses on the current observation instead of native context and causality. It splits the problem into three scales: short-term context can unfold inside a single second, as when a grip loosens, a cup slides, and the robot re-tightens; medium-term context carries information such as the sizes of several identical cups so that knowledge transfers; long-term context is memory about where an object is kept or how a human partner will later look for it. The source says both data and model design have to solve this, because more context tokens raise inference latency and robot execution is latency-sensitive. That makes context a capability with a cost rather than a free addition to the prompt.

## Key Claims
- Embodied systems often underweight native context and causal information relative to the current observation.
- Short-horizon context can be a sub-second causal chain rather than a long conversation history.
- Medium-horizon context supports transfer across similar objects, scenes, or deployments.
- Long-horizon context is episodic memory about locations, ownership, and human partners.
- Context length and real-time control conflict because additional tokens increase inference latency.
- Solving context requires data that rewards context use as well as model designs that can represent it efficiently.

## Evidence
- Neglect evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] says many embodied projects act on the current observation and pay insufficient attention to native context and causality.
- Horizon evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] gives the grip-loss example for short context, the several-identical-cups example for medium context, and the drawer-location and human-partner example for long context.
- Data-and-model evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] says context has to be addressed both by designing data that elicits context use and by modeling context efficiently.
- Latency evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] ties growing token counts to inference delay and notes that robot execution is highly sensitive to real-time behavior.

## Counterevidence & Qualifications
The source gives no architecture, memory benchmark, or deployment evidence, so the three-horizon split should not be read as proof that robot memory is solved or that the horizons are exhaustive. The page is adjacent to broader agent-memory work, where context management, retrieval, and persistence remain contested and system-specific.

## What Changed
- Created the concept from the interview's three-horizon context model and its sub-second causal example.
- Added the context-length-versus-latency tension as an embodied-specific constraint.

## Related Concepts
- [[AgentHarness]] - harness layer where context management and memory scheduling are implemented.
- [[PersistentAgentMemory]] - general agent-memory work that the embodied case extends with physical and partner state.
- [[ContextEngineering]] - adjacent practice of designing what context an agent receives and carries.
- [[SmallBrainActionLayer]] - execution layer that must act while context is still being represented.
- [[RobotResponseLatency]] - latency constraint that makes long context expensive in embodied settings.
- [[EmbodiedCapabilityFramework]] - framework in which context understanding is one of the three capability axes.
