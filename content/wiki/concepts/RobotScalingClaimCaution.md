---
title: "Robot Scaling Claim Caution / 幂律现象与 scaling law 谨慎"
type: concept
tags: [robotics, data, scaling, embodied-ai]
sources:
  - yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr
  - wo-kandao-le-scaling-law-de-xinhao-duitan-qinghua-chayuan-zhuli-jiaoshou-xu-mengdi-jushen-zhineng-shijie-moxing-zhenzheng-de-fanhua-ltdn8trgg55fluenullokxdiz1y5
last_updated: 2026-09-21
knowledge_schema: synthesis-v1
---

# Robot Scaling Claim Caution / 幂律现象与 scaling law 谨慎

## Definition
Robot scaling claim caution is the discipline of separating suggestive improvements in training or held-out loss from a validated law connecting more data and larger models to safe, reliable success on unseen physical tasks.

## Current Synthesis
Both bounded sources report early scaling-like signals while refusing the strongest conclusion. The Shenpu interview calls its internal observation a power-law phenomenon rather than a scaling law because sufficient controlled experiments and public evaluation are missing. Xu Mengdi points to source-reported held-out-loss improvement as pretraining data grows from roughly one hundred thousand to one million hours, but adds the decisive robotics qualification: lower average loss may not improve task success when a small error at a contact-critical step can break a long-horizon action. A meaningful embodied scaling law would therefore connect model and data growth to sustained unseen-task success under disclosed task, data, safety, and latency conditions.

## Key Claims
- Power-law-like improvement and held-out-loss reduction are signals, not by themselves validated robot scaling laws.
- The most meaningful outcome variable is success on unseen tasks, not average prediction loss alone.
- Contact-critical and long-horizon tasks can amplify small local errors into complete task failure.
- Controlled scaling experiments require known data quality, cost, usability, diversity, and data-to-model ratios.
- Large human or egocentric data collections can be cheap to record but expensive to annotate, train, and validate for robot use.
- Zero-shot results should disclose task difficulty and data exposure rather than stand alone as general-capability claims.

## Evidence
- Claim-discipline evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] says the team observes power-law phenomena but lacks the experiments needed to claim a scaling law.
- Controlled-data evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] connects controlled parameter and data-ratio experiments to self-collected, cost-known UMI data reported as over 90% usable.
- Loss-signal evidence: [[wo-kandao-le-scaling-law-de-xinhao-duitan-qinghua-chayuan-zhuli-jiaoshou-xu-mengdi-jushen-zhineng-shijie-moxing-zhenzheng-de-fanhua-ltdn8trgg55fluenullokxdiz1y5]] reports seeing lower unseen-test loss as some companies move from roughly one hundred thousand to one million hours of pretraining data.
- Success-rate qualification: [[wo-kandao-le-scaling-law-de-xinhao-duitan-qinghua-chayuan-zhuli-jiaoshou-xu-mengdi-jushen-zhineng-shijie-moxing-zhenzheng-de-fanhua-ltdn8trgg55fluenullokxdiz1y5]] argues that critical contact errors can break a whole long-horizon task and defines the desired law through unseen-task success.
- Cost and disclosure evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] distinguishes cheap raw egocentric footage from annotation and training cost and calls for disclosure around zero-shot and few-shot data use.

## Counterevidence & Qualifications
Neither source supplies audited scaling curves, model sizes, complete data composition, confidence intervals, or reproducible cross-company tests. The million-hour comparison is reported as an observation from company releases rather than an independent experiment. The current evidence supports a research signal and a measurement standard, not the existence, exponent, or commercial implication of a robot scaling law.

## What Changed
- Added held-out-loss improvement as a stronger early signal while preserving the distinction between signal and validated law.
- Made unseen-task success the required outcome and added the contact-critical reason loss can diverge from success.
- Broadened the validation boundary to include task disclosure, safety, and latency alongside data and model scale.

## Related Concepts
- [[RobotDataScaleUp]] - broader data-scaling bottleneck this concept qualifies.
- [[RobotGeneralizationPerformanceTradeoff]] - capability tension a useful scaling law must measure.
- [[EgocentricRobotData]] - large-scale first-person route whose total cost and transfer value remain uncertain.
- [[RobotEvaluationProblem]] - benchmark and disclosure layer required to test the scaling claim.
- [[CapabilityDrivenRobotDataDesign]] - reminder that capability-relevant data composition matters alongside hours.
- [[FrontierModelScaling]] - language-model scaling discourse that cannot be imported into robotics without embodied outcome evidence.
