---
title: "Robot Evaluation Problem"
type: concept
tags: [robotics, evaluation, embodied-ai]
sources: [146-dui-physical-intelligence-ke-li-yiming-4-xiaoshi-fangtan-pi-de-kaiyuan-moxing-yanjiu-jiqiren-de-jianghu-zupu-yu-zhujiao-ljmazvdvad7o5md-nuiompd6-1nv]
last_updated: 2026-07-18
---

# Robot Evaluation Problem

Robot evaluation problem is the difficulty of comparing real-world robot systems that K emphasizes in [[146-dui-physical-intelligence-ke-li-yiming-4-xiaoshi-fangtan-pi-de-kaiyuan-moxing-yanjiu-jiqiren-de-jianghu-zupu-yu-zhujiao-ljmazvdvad7o5md-nuiompd6-1nv]]. Unlike language models, robots cannot be cleanly ranked by a single public leaderboard because evaluation has to happen on real or realistic machines in variable physical scenes.

The source lists many confounders: lighting, position, background, table height, object angle, hardware state, and task definition can all change results. That makes private company evals useful internally but hard to compare externally, and it makes public demos a weak proxy for frontier status.

## Key Claims
- A task's success definition matters as much as the model architecture when judging progress.
- Real-machine evaluation is expensive, slow, and hardware-dependent.
- Throughput can combine speed and quality, but only for tasks whose success and time windows are clearly defined.
- Company demos should be read as evidence of capability, not as a complete frontier ranking.
- The problem connects to simulation because scalable evaluation may need repeatable simulated or semi-simulated testbeds.

## Connections
- [[RoboticsSimulationEvaluation]] — scalable evaluation infrastructure that can complement real-machine tests.
- [[RobotGeneralizationPerformanceTradeoff]] — tradeoff that evaluation is supposed to measure.
- [[PhysicalIntelligencePiSeries]] — Pi sequence and π0.6* throughput example.
- [[OpenWorldRobotManipulation]], [[Structured3DRobotData]], and [[Sim2Real]] — adjacent route for testing unseen-object manipulation.
- [[FigureAI]], [[Generalist]], [[SkildAI]], and [[PhysicalIntelligence]] — companies whose public claims and demos need evaluation discipline.
