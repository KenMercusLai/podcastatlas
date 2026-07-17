---
title: "Robot Experience Data"
type: concept
tags: [robotics, data, reinforcement-learning]
sources: [146-dui-physical-intelligence-ke-li-yiming-4-xiaoshi-fangtan-pi-de-kaiyuan-moxing-yanjiu-jiqiren-de-jianghu-zupu-yu-zhujiao-ljmazvdvad7o5md-nuiompd6-1nv]
last_updated: 2026-07-18
---

# Robot Experience Data

Robot experience data is the self-generated robot data described by [[KPhysicalIntelligence|K]] in [[146-dui-physical-intelligence-ke-li-yiming-4-xiaoshi-fangtan-pi-de-kaiyuan-moxing-yanjiu-jiqiren-de-jianghu-zupu-yu-zhujiao-ljmazvdvad7o5md-nuiompd6-1nv]]. It differs from pure human teleoperation data because the robot acts in the environment, records its own successes and failures, and produces correction traces that can support [[RobotReinforcementLearning]].

The source treats experience data as necessary when a robot must improve beyond human demonstration. Human data can provide an initial policy, but flexible physical tasks such as clothes, friction, and manipulation of messy objects require the robot to discover what actually happens when its own body moves in the world.

## Key Claims
- Experience data makes failure informative instead of only discarded noise.
- It links action, outcome, and correction in the robot's own embodiment.
- It is especially important when imitation learning reaches a ceiling and the model needs active exploration.
- It is expensive because it depends on real machines, hardware uptime, task setup, and evaluation.

## Connections
- [[PhysicalIntelligencePiSeries]] — π0.6* is the main source case for experience-data use.
- [[RobotReinforcementLearning]] — training route that consumes experience data.
- [[RealRobotDataStrategy]] and [[PhysicalWorldDataFlywheel]] — broader data strategy and deployment loop.
- [[RobotEvaluationProblem]] — measurement bottleneck that determines whether experience data is improving real behavior.
