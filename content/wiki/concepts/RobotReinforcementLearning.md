---
title: "Robot Reinforcement Learning"
type: concept
tags: [robotics, reinforcement-learning, embodied-ai]
sources: [146-dui-physical-intelligence-ke-li-yiming-4-xiaoshi-fangtan-pi-de-kaiyuan-moxing-yanjiu-jiqiren-de-jianghu-zupu-yu-zhujiao-ljmazvdvad7o5md-nuiompd6-1nv]
last_updated: 2026-07-18
---

# Robot Reinforcement Learning

Robot reinforcement learning is K's frame in [[146-dui-physical-intelligence-ke-li-yiming-4-xiaoshi-fangtan-pi-de-kaiyuan-moxing-yanjiu-jiqiren-de-jianghu-zupu-yu-zhujiao-ljmazvdvad7o5md-nuiompd6-1nv]] for robots improving through their own experience. He contrasts it with imitation learning: imitation can copy examples, while reinforcement learning lets a robot explore, receive reward or correction, assign credit, and improve a policy through interaction.

The source does not reduce reinforcement learning to reward-function design. K says the deeper problem is how humans communicate the intended task to an agent in a way that is generalizable and robust. This links robot RL to [[RobotExperienceData]], [[RobotEvaluationProblem]], and [[HumanJudgmentUnderAI]] rather than only to an optimization algorithm.

## Key Claims
- Exploration quality matters: what the agent tries determines how efficiently it learns.
- Reward is a communication problem, not only a scalar engineering detail.
- Real-machine RL can improve specific task performance but depends on hardware reliability, task setup, and measurement.
- The idea scales metaphorically to research itself: choosing which experiments to run is also an exploration problem.

## Connections
- [[RobotExperienceData]] — the data source robot RL turns into improvement.
- [[PhysicalIntelligencePiSeries]] — π0.6* as the source's main performance-improvement example.
- [[AgentRL]] — adjacent digital-agent reinforcement-learning page with a different environment structure.
- [[VisionLanguageActionModels]] — policy family that may be improved by post-training and experience.
- [[RobotGeneralizationPerformanceTradeoff]] — RL can improve performance, but the wiki should track whether that narrows or broadens generalization.
