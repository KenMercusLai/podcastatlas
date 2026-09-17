---
title: "Small Brain Action Layer / 小脑（Action Policy）"
type: concept
tags: [robotics, architecture, embodied-ai, control]
sources:
  - yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

# Small Brain Action Layer / 小脑（Action Policy）

## Definition
The action policy, or "small brain," is the lower layer of an embodied system that turns high-level intent into fast, stable, controllable physical action in real time, as distinct from the upper brain that reasons, plans, and interprets the world.

## Current Synthesis
The source's central architecture claim is that a general model is not enough for a robot. [[ChatGPT6Astra]] driving a robot arm impressed on grasping and on multi-step spatial and task planning, including a pen drawing of the Golden Gate Bridge that improved over repeated attempts. But the source notes that demonstration videos are often sped up, that a single model inference takes a long time, that success in a static scene does not transfer to a dynamic one, and that a tilted cup may not be recovered fast enough. Those gaps define the small brain: a layer that can react, adjust, and keep the body controllable while the upper brain plans. The same split appears in the company's System 2 planner and System 1 executor, and it explains why a compute-constrained startup may prioritize Action pretraining over the upper model.

## Key Claims
- Grasping and task-planning success does not establish real-time physical control, because recovery from disturbance is a different capability.
- Sped-up demonstration video can hide inference latency, and single-pass inference time is a first-order constraint for physical tasks.
- The small-brain layer exists to provide fast, stable, controllable reactions that a reasoning model cannot guarantee.
- The brain/small-brain division maps onto System 2 intent understanding and planning versus System 1 fast fine execution, mediated by a harness.
- A startup may allocate scarce compute to Action pretraining while borrowing a fast-improving upper foundation model.
- The source thinks the lower layer eating the upper layer is unlikely, while the upper layer absorbing System 1 is possible with uncertain timing; a unified very-large embodied model is theoretically imaginable but cannot skip the intermediate system work.

## Evidence
- Astra boundary evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] describes the robot-arm demonstration, the sped-up video, the long single-pass inference, and the static-versus-dynamic gap.
- Disturbance evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] uses the tilted cup as the case where a general model may not recover quickly enough without a reactive lower layer.
- Architecture evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] names the Action Policy or "small brain" as the lower layer and System 1/System 2 as the company's operating split.
- Compute-priority evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] says startup compute is scarce and may go to Action pretraining because upper-layer foundation models are still moving fast.
- Convergence evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] gives the "below cannot eat above, above may eat System 1" judgment and the 10T unified-model thought experiment.

## Counterevidence & Qualifications
The claim that the upper layer could eventually absorb System 1 is the source's own caveat against a hard architectural separation, and the source gives no timing. The page also lacks model architecture, latency numbers, and success rates, so it records an argument structure rather than a measured comparison, and part of the demonstration evidence comes from public video that the source itself says is sped up.

## What Changed
- Created the concept to hold the source's brain/small-brain distinction separately from general layered-robotics discussion.
- Added the real-time disturbance-recovery boundary as the reason a general model cannot be the whole embodied system.

## Related Concepts
- [[LayeredRobotArchitecture]] - broader upper-planning and lower-manipulation split into which this concept fits.
- [[RobotResponseLatency]] - latency constraint that makes a reactive lower layer necessary.
- [[GeneralModelRobotBoundary]] - boundary that this concept draws at real-time recovery rather than at semantics.
- [[RobotAgenticOS]] - system layer that schedules the small brain and mediates the brain-to-body interaction.
- [[VisionLanguageActionModels]] - model family that supplies action prediction but does not by itself settle the real-time control question.
