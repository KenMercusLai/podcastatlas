---
title: "Robot Evaluation Problem"
type: concept
tags: [robotics, evaluation, embodied-ai]
sources:
  - 146-dui-physical-intelligence-ke-li-yiming-4-xiaoshi-fangtan-pi-de-kaiyuan-moxing-yanjiu-jiqiren-de-jianghu-zupu-yu-zhujiao-ljmazvdvad7o5md-nuiompd6-1nv
  - jushen-zhineng-de-jinqian-youxi-jinzhan-nance-shouru-cuishu-yu-ipo-jingsu-1-180-1
  - yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr
  - wo-kandao-le-scaling-law-de-xinhao-duitan-qinghua-chayuan-zhuli-jiaoshou-xu-mengdi-jushen-zhineng-shijie-moxing-zhenzheng-de-fanhua-ltdn8trgg55fluenullokxdiz1y5
last_updated: 2026-09-21
knowledge_schema: synthesis-v1
---

# Robot Evaluation Problem

## Definition
The robot evaluation problem is the difficulty of comparing embodied systems when success depends on task definitions, physical scenes, hardware state, prior data exposure, autonomy boundaries, failure consequences, and response time.

## Current Synthesis
The bounded sources agree that robotics lacks a public, reproducible evaluation regime comparable to language-model benchmarks. Real-machine results vary with lighting, object angle, table height, hardware condition, and success definition; simulation is repeatable but can reward post-training against the benchmark rather than robust physical ability. Weak observability then creates a market problem, allowing demos, fundraising, revenue, and route narratives to substitute for deployment evidence.

Physical embodiment adds two requirements. Evaluation must characterize how a robot fails and where risk becomes unacceptable, not merely average success, because errors can damage people or property. It must also measure real-time interaction: a system that eventually returns a strong answer may still be unusable if the physical world changes while it reasons. The emerging standard is therefore a disclosed suite spanning unseen-task success, task difficulty, scene and object variation, autonomy, data exposure, speed or throughput, recovery, failure modes, and safety boundaries.

## Key Claims
- Task and success definitions are as important as model architecture when judging robot progress.
- Real-machine evaluation is expensive, slow, hardware-dependent, and difficult to reproduce across sites.
- Simulation can improve repeatability but may be gameable and can omit physical noise, contact, and risk.
- Results are not comparable without disclosure of autonomy, task difficulty, scene variation, and zero-shot or few-shot data exposure.
- Speed, latency, or throughput must be included because robots interact continuously with changing environments.
- Safety evaluation must cover failure modes and operational risk boundaries, not only mean success rate.
- Weak technical observability lets capital-market and revenue signals stand in for capability evidence.

## Evidence
- Physical-confounder and throughput evidence: [[146-dui-physical-intelligence-ke-li-yiming-4-xiaoshi-fangtan-pi-de-kaiyuan-moxing-yanjiu-jiqiren-de-jianghu-zupu-yu-zhujiao-ljmazvdvad7o5md-nuiompd6-1nv]] lists lighting, background, object pose, table height, hardware condition, and task definition as confounders and uses throughput to join speed with successful work.
- Market-observability evidence: [[jushen-zhineng-de-jinqian-youxi-jinzhan-nance-shouru-cuishu-yu-ipo-jingsu-1-180-1]] says benchmark scarcity allows demos, founder background, fundraising, revenue, and listing plans to become substitute signals.
- Benchmark and disclosure evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] describes simulation-heavy and post-training-gameable benchmarks, third-party real-machine testing resistance, and evaluation across difficulty, generalization, and zero-shot or few-shot data budgets.
- Safety and failure evidence: [[wo-kandao-le-scaling-law-de-xinhao-duitan-qinghua-chayuan-zhuli-jiaoshou-xu-mengdi-jushen-zhineng-shijie-moxing-zhenzheng-de-fanhua-ltdn8trgg55fluenullokxdiz1y5]] argues that embodied benchmarks must communicate what a robot can and cannot safely do before deployment.
- Latency evidence: [[wo-kandao-le-scaling-law-de-xinhao-duitan-qinghua-chayuan-zhuli-jiaoshou-xu-mengdi-jushen-zhineng-shijie-moxing-zhenzheng-de-fanhua-ltdn8trgg55fluenullokxdiz1y5]] distinguishes robots from systems that can wait minutes for an answer because physical interaction is continuous.

## Counterevidence & Qualifications
The absence of one universal benchmark does not make internal tests, customer pilots, long-duration demos, competitions, or deployment metrics meaningless. Each can supply evidence if the task, body, environment, autonomy, speed, failure handling, data budget, and business relevance are explicit. Company-run tests remain vulnerable to selection effects, while simulation and real-machine evaluation have complementary rather than mutually exclusive strengths. BEHAVIOR is recommended in the newest source for long-horizon household tasks, but its simulation-to-reality gap remains explicit.

## What Changed
- Added failure-mode and safety-boundary evaluation as requirements created by physical embodiment.
- Added latency and continuous interaction to the comparison standard.
- Clarified that long-horizon household simulation is useful while still limited by the sim-to-real gap.

## Related Concepts
- [[RoboticsSimulationEvaluation]] - repeatable infrastructure that complements rather than replaces real-machine tests.
- [[RobotGeneralizationPerformanceTradeoff]] - breadth, reliability, speed, and success tension evaluation should expose.
- [[RobotScalingClaimCaution]] - scaling claims depend on valid embodied outcome measurement.
- [[OpenWorldRobotManipulation]] - unseen-object and unseen-environment capability target.
- [[RobotDemoAuthenticity]] - disclosure problem around visible demos and autonomy.
- [[RobotExperienceData]] - attempts and failures that can support recovery-focused evaluation.
- [[Sim2Real]] - transfer boundary behind the benchmark's simulation limitation.
