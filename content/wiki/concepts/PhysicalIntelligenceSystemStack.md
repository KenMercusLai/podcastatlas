---
title: "Physical Intelligence System Stack"
type: concept
knowledge_schema: synthesis-v1
tags: [physical-ai, robotics, embodied-ai, systems]
sources:
  - 173-duihua-yao-song-shenjian-dongfang-kongjian-zaichufa-tiancai-shaonian-shinian-hou-1-173-1
  - tefan-cong-hui-kaiche-dao-hui-zuoshi-ai-ruhe-jinru-zhenshi-shijie-gkwrijeopcilaoo4hwtn2dns
  - 187-duihua-liberai-liu-songming-astra-lai-xi-00-hou-wuli-ai-chuangshiren-kandao-de-shenglv-ad3b421a
last_updated: 2026-11-13
---

# Physical Intelligence System Stack

## Definition
Physical intelligence system stack is the complete set of data, compute, models, algorithms, chips, software, hardware, sensors, controls, scenes, solutions, operations, and feedback needed for an intelligent machine to perceive, decide, and act reliably in the physical world.

## Current Synthesis
The bounded sources reject reducing physical intelligence to a model or robot body. [[YaoSong]] emphasizes vertical system coverage from data and compute through hardware, scene access, solutions, and remote operation. [[HorizonRobotics|地平线]] adds a time-coupling constraint: algorithms can change quickly, while chips take years to define and must operate within edge power, heat, space, and latency limits. [[LiberAI]] adds a competitive boundary: general foundation models may absorb more semantic understanding and planning, while action generation, contact feedback, motion control, embodiment, hardware reliability, and scene delivery remain specialized. System performance therefore depends on interfaces and co-design across layers, not simply owning every layer.

Cars and robots instantiate the stack differently. Vehicles offer scaled production and tight real-time safety requirements; robots add varied bodies, joint control, contact, manipulation, and task-dependent thinking time. A platform can reuse design and data-loop methods across them, but must still adapt hardware, control, and evidence to each embodiment. Vertical integration is therefore selective rather than absolute: control the layers whose interfaces materially affect learning or reliability, and use mature suppliers where ownership would add cost without improving the system.

## Key Claims
- Space perception, body motion, manipulation, and remote operation are all parts of physical intelligence rather than separate afterthoughts.
- [[VisionLanguageActionModels]], [[WorldModels]], [[WorldActionModels]], and [[RobotReinforcementLearning]] are route components, not complete company definitions by themselves.
- Scenario access matters because physical-world data and commercial value appear only when robots act in real settings.
- Early vertical integration can be rational when standard interfaces, mature suppliers, and stable form factors have not yet formed.
- The stack view supports [[MilestoneCommercialization]]: each technical step should be linked to a deployable service or customer value where possible.
- Chip roadmaps and model roadmaps must be coordinated because silicon decisions precede the software workloads they will eventually run.
- Edge power, heat, space, latency, safety, and embodiment constraints determine which nominal capability becomes usable action, so general models can move deeper into planning without eliminating specialized policies, low-level control, sensors, hardware adaptation, or customer delivery.

## Evidence
### Full-stack scope and scene access
- [[173-duihua-yao-song-shenjian-dongfang-kongjian-zaichufa-tiancai-shaonian-shinian-hou-1-173-1]] defines physical intelligence through data, compute, models, algorithms, software, hardware, scenarios, solutions, and remote systems, and connects scenario access to both learning and commercial value.

### Hardware–software time coupling
- [[tefan-cong-hui-kaiche-dao-hui-zuoshi-ai-ruhe-jinru-zhenshi-shijie-gkwrijeopcilaoo4hwtn2dns]] says vehicle chips may take three to four years from definition to deployment, so algorithm teams must anticipate future model characteristics while chip constraints bound later software capability.

### Embodiment-specific system design
- [[tefan-cong-hui-kaiche-dao-hui-zuoshi-ai-ruhe-jinru-zhenshi-shijie-gkwrijeopcilaoo4hwtn2dns]] contrasts edge vehicle requirements with data-center compute and distinguishes robot high-level decisions from joint-level control, balance, tactile feedback, and body limits.

### Layer boundary and selective integration
- [[187-duihua-liberai-liu-songming-astra-lai-xi-00-hou-wuli-ai-chuangshiren-kandao-de-shenglv-ad3b421a]] divides the robot stack into System 2 planning, System 1 action, and System 0 motion control, then argues for owning model-relevant data, hardware, control, and deployment links while sourcing mature components elsewhere.

## Counterevidence & Qualifications
- Full-stack thinking does not prove that one firm should vertically own every component; modular suppliers and standards can outperform integration when interfaces mature.
- The sources are founder or company accounts and do not independently compare stack ownership, platform economics, or performance.
- Co-design can improve fit while increasing capital intensity, roadmap lock-in, organizational complexity, and exposure to wrong long-range forecasts.
- The System 2/System 1/System 0 boundary is a useful engineering and company heuristic, not a stable industry standard; general models, specialized policies, and control systems may change their division of labor.
- Liber AI's reported model, hardware, and deployment advantages are founder claims and do not establish that vertical integration will outperform modular competitors at scale.

## What Changed
- Added the System 2/System 1/System 0 division and the competitive boundary between general models and physical execution.
- Clarified selective vertical integration: own interfaces that determine learning and reliability, not necessarily every component.
- Added customer delivery and scene infrastructure as durable stack layers alongside models and hardware.

## Related Concepts
- [[PhysicalAI]] - broader physical-world intelligence category instantiated by the system stack.
- [[EmbodiedAIValueChain]] - distribution of value across the stack's commercial layers.
- [[PhysicalWorldDataFlywheel]] - feedback mechanism connecting deployed action to later improvement.
- [[ProductionRobotScenarioSelection]] - scene choice that determines useful data and customer value.
- [[HardwareSoftwareIterationAsymmetry]] - timing and reversibility difference between physical and digital layers.
- [[EmbodiedIntelligenceVehiclePath]] - vehicle-first route for scaling and financing the stack.
- [[RobotFormFactorPragmatism]] - body-selection rule that can reduce unnecessary stack complexity.
- [[GeneralModelRobotBoundary]] - changing division of labor between broad foundation models and embodied specialization.
- [[LayeredRobotArchitecture]] - technical separation of slower planning from low-latency physical execution.
