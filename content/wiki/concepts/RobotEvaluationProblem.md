---
title: "Robot Evaluation Problem"
type: concept
tags: [robotics, evaluation, embodied-ai]
sources:
  - 146-dui-physical-intelligence-ke-li-yiming-4-xiaoshi-fangtan-pi-de-kaiyuan-moxing-yanjiu-jiqiren-de-jianghu-zupu-yu-zhujiao-ljmazvdvad7o5md-nuiompd6-1nv
  - jushen-zhineng-de-jinqian-youxi-jinzhan-nance-shouru-cuishu-yu-ipo-jingsu-1-180-1
  - yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

# Robot Evaluation Problem

## Definition
Robot evaluation problem is the difficulty of comparing real-world robot systems when results depend on task definitions, physical scenes, hardware condition, data access, autonomy boundaries, and private test setups.

## Current Synthesis
The bounded sources agree that robotics lacks a public, reproducible evaluation regime comparable to language-model benchmarks. K's Physical Intelligence interview emphasizes real-machine confounders such as lighting, object angle, table height, hardware state, and task definition. The LateTalk industry episode adds the market consequence: when progress is hard for outsiders to observe, fundraising, founder background, route changes, demos, revenue, and listing plans can become substitute signals even though they may say little about deployable capability.

The Shenpu Intelligence interview adds the model-builder side of the same problem. [[WangJiawei]] says past embodied benchmarks skew to simulation, that some simulation benchmarks can be raised with post-training, and that the abilities a benchmark defines may not be the abilities a company cares about. Real-machine benchmarking is harder because it is not fully reproducible and often requires handing the model to a third party, which companies resist. His response is company-run evaluation of whole-chain stability and success rate, published with simple, medium, and hard tasks, scene and object generalization, and an explicit statement of how much data a zero-shot or few-shot result used. The same source says cross-model comparison stays difficult because outside data and outside embodiments are unknown, and that open-sourcing the model is still under discussion.

## Key Claims
- A task's success definition matters as much as the model architecture when judging progress.
- Real-machine evaluation is expensive, slow, and hardware-dependent.
- Throughput can combine speed and quality, but only for tasks whose success criteria and time windows are clear.
- Public demos and controlled scenes should be read as capability evidence, not as complete frontier rankings.
- Weak observability can make both underestimation and overestimation plausible, creating space for bubbles, story-telling, and route mimicry.
- The problem connects to simulation because scalable evaluation may need repeatable simulated or semi-simulated testbeds.
- Disclosure matters as much as scoring: a robot result is not comparable unless it states the autonomy boundary, task difficulty, scene variation, and how much data a zero-shot or few-shot claim used.

## Evidence
- Confounder evidence: [[146-dui-physical-intelligence-ke-li-yiming-4-xiaoshi-fangtan-pi-de-kaiyuan-moxing-yanjiu-jiqiren-de-jianghu-zupu-yu-zhujiao-ljmazvdvad7o5md-nuiompd6-1nv]] lists lighting, background, object angle, table height, hardware condition, and task definition as reasons robot evaluations are hard to compare.
- Throughput evidence: [[146-dui-physical-intelligence-ke-li-yiming-4-xiaoshi-fangtan-pi-de-kaiyuan-moxing-yanjiu-jiqiren-de-jianghu-zupu-yu-zhujiao-ljmazvdvad7o5md-nuiompd6-1nv]] uses π0.6* throughput as a way to combine speed and quality for bounded tasks.
- Benchmark-gap evidence: [[jushen-zhineng-de-jinqian-youxi-jinzhan-nance-shouru-cuishu-yu-ipo-jingsu-1-180-1]] contrasts robotics with large-language-model progress, where public leaderboards, open models, and direct user experience make capability easier to observe.
- Market-consequence evidence: [[jushen-zhineng-de-jinqian-youxi-jinzhan-nance-shouru-cuishu-yu-ipo-jingsu-1-180-1]] says hard-to-observe progress can leave room for route switching, story-telling, and capital-market signals to stand in for technical proof.
- Task-fit evidence: [[jushen-zhineng-de-jinqian-youxi-jinzhan-nance-shouru-cuishu-yu-ipo-jingsu-1-180-1]] describes a robot taking roughly 70 seconds to pick an axle bearing into a box, making it hard to translate a demo into labor-replacement ROI.
- Disclosure and benchmark-critique evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] describes simulation-heavy and post-training-gameable benchmarks, the third-party real-machine testing problem, a company-run evaluation across difficulty and generalization, disclosure of zero-shot versus few-shot data, and uncertainty about cross-model comparison and open-sourcing.

## Counterevidence & Qualifications
The absence of a universal benchmark does not make all public robotics progress meaningless. Internal tests, customer pilots, long-duration demos, competitions, and deployment metrics can each show something. The qualification is that each metric must name its task, hardware, environment, autonomy boundary, speed, failure handling, and business relevance before it can support cross-company comparison. Company-run evaluation does not solve that problem by itself: the Shenpu source's own numbers are self-reported, and a house evaluation can still be selective unless its protocol and data budget are published.

## What Changed
- Migrated the page to the synthesis-first concept schema.
- Added progress observability as a market and valuation problem, not only a technical-evaluation issue.
- Connected benchmark gaps to route mimicry, demos, fundraising, revenue, and IPO pressure.
- Added the model-builder response: simulation-gameable benchmarks, third-party real-machine testing, company-run difficulty and generalization suites, and mandatory zero-shot versus few-shot disclosure.

## Related Concepts
- [[RoboticsSimulationEvaluation]] - scalable evaluation infrastructure that can complement real-machine tests.
- [[RobotGeneralizationPerformanceTradeoff]] - tradeoff that evaluation is supposed to measure.
- [[PhysicalIntelligencePiSeries]] - Pi sequence and π0.6* throughput example.
- [[OpenWorldRobotManipulation]] - capability target that needs stronger public testing.
- [[RobotDemoAuthenticity]] - related problem of whether a visible demo discloses autonomy boundaries.
- [[RoboticsRevenuePullForward]] - business-side consequence when revenue substitutes for technical observability.
- [[HumanoidRobotCommercialization]] - commercialization frame that depends on reliable evaluation.
- [[UMIGloveDataCollection]] - data-collection and replay-validation route that a company can fold into its own evaluation loop.
