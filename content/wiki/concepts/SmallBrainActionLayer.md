---
title: "Small Brain Action Layer / 小脑（Action Policy）"
type: concept
tags: [robotics, architecture, embodied-ai, control]
sources:
  - yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr
  - shaoyou-de-tongshi-zuoguo-agent-duomotai-he-jushen-de-ren-duitan-qian-hunyuan-duomotai-rl-infra-fuzeren-haonan-lvbhcwvcteq4tvfmvcbkrubw0n82
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

# Small Brain Action Layer / 小脑（Action Policy）

## Definition
The action policy, or "small brain," is the lower layer of an embodied system that turns high-level intent into fast, stable, controllable physical action in real time, as distinct from the upper brain that reasons, plans, and interprets the world.

## Current Synthesis
The bounded sources agree that a general model is not enough for every robot-control cycle. [[ChatGPT6Astra]] demonstrates grasping and multi-step planning, but sped-up video, slow inference, static-scene success, and disturbance recovery expose a separate latency and controllability problem. The small brain is therefore a body-specific layer that reacts, adjusts, and keeps execution stable while an upper model handles semantics, planning, review, and difficult cases. The newer source makes the operating split more concrete: a modest local control model can execute most actions, escalating likely failures to a stronger model and then a human, while recovery traces improve the local policy.

## Key Claims
- Grasping and task-planning success does not establish real-time physical control, because recovery from disturbance is a different capability.
- Sped-up demonstration video can hide inference latency, and single-pass inference time is a first-order constraint for physical tasks.
- The small-brain layer provides fast, stable, controllable reactions that a reasoning model cannot guarantee and should be co-designed with the robot body's joints and control parameters.
- The brain/small-brain division maps onto System 2 intent understanding and planning versus System 1 fast fine execution, mediated by a harness.
- A startup may allocate scarce compute to Action pretraining while borrowing a fast-improving upper foundation model; the newer source suggests roughly 7B-to-16B local control models as a source-scoped design range.
- The lower layer can learn from selectively captured failure-recovery trajectories, while eventual upper-model absorption of System 1 remains possible but unproven and does not remove today's integration work.

## Evidence
- Astra boundary evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] describes the robot-arm demonstration, the sped-up video, the long single-pass inference, and the static-versus-dynamic gap.
- Disturbance evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] uses the tilted cup as the case where a general model may not recover quickly enough without a reactive lower layer.
- Architecture evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] names the Action Policy or "small brain" as the lower layer and System 1/System 2 as the company's operating split.
- Compute-priority evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] says startup compute is scarce and may go to Action pretraining because upper-layer foundation models are still moving fast.
- Convergence evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] gives the "below cannot eat above, above may eat System 1" judgment and the 10T unified-model thought experiment.
- Body-specific design evidence: [[shaoyou-de-tongshi-zuoguo-agent-duomotai-he-jushen-de-ren-duitan-qian-hunyuan-duomotai-rl-infra-fuzeren-haonan-lvbhcwvcteq4tvfmvcbkrubw0n82]] argues that differing bodies, joints, and control parameters still require hardware-linked policies.
- Recovery evidence: [[shaoyou-de-tongshi-zuoguo-agent-duomotai-he-jushen-de-ren-duitan-qian-hunyuan-duomotai-rl-infra-fuzeren-haonan-lvbhcwvcteq4tvfmvcbkrubw0n82]] proposes local execution, strong-model takeover near failure, human fallback, and recovery-trace training.

## Counterevidence & Qualifications
The claim that the upper layer could eventually absorb System 1 is a caveat against hard architectural separation, and neither source gives a timing or controlled comparison. The page lacks disclosed model architecture, latency, success, failure-detection, or intervention-rate measurements; the 7B-to-16B range is a practitioner's recommendation, not a validated universal optimum. Part of the demonstration evidence also comes from public video that the earlier source says is sped up.

## What Changed
- Added body-specific policy co-design and a source-scoped 7B-to-16B local-model range.
- Extended the architecture from a static brain/small-brain split to failure-triggered escalation and recovery learning.
- Narrowed the evidence boundary around failure detection, intervention rates, and model-size guidance.

## Related Concepts
- [[LayeredRobotArchitecture]] - broader upper-planning and lower-manipulation split into which this concept fits.
- [[RobotResponseLatency]] - latency constraint that makes a reactive lower layer necessary.
- [[GeneralModelRobotBoundary]] - boundary that this concept draws at real-time recovery rather than at semantics.
- [[RobotAgenticOS]] - system layer that schedules the small brain and mediates the brain-to-body interaction.
- [[VisionLanguageActionModels]] - model family that supplies action prediction but does not by itself settle the real-time control question.
- [[RobotFailureRecoveryEscalation]] - routing and learning mechanism built on top of the fast local layer.
