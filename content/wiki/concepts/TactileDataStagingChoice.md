---
title: "Tactile Data Staging / 触觉数据暂缓采集"
type: concept
tags: [robotics, tactile, data, embodied-ai]
sources:
  - yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

# Tactile Data Staging / 触觉数据暂缓采集

## Definition
The tactile data staging choice is a robot-data strategy that keeps tactile sensing in experimentation but delays large-scale collection because sensor formats have not converged and early hardware commitments can strand data.

## Current Synthesis
The source says its open dataset carries no tactile signal and defends the omission on two grounds. First, a two-finger claw can often judge whether it has a grip from vision, especially when upper and lower wrist cameras reduce occlusion. Second, although touch can be predicted from video, the source expects that predicted precision may help pretraining while being insufficient for post-training. More importantly, the source treats tactile sensors as unsettled: different devices have different resolutions and placements, so if the company buys 100 sets and the results are poor, or a better sensor appears a few months later, it is unclear how the earlier data can be reused. Touch has not been abandoned; the company keeps experimenting, but does not scale collection until the hardware question stabilizes.

## Key Claims
- Vision alone is judged adequate for many two-finger grip judgments when wrist cameras reduce occlusion.
- Video-to-touch prediction is treated as potentially useful for pretraining but not reliable enough for post-training.
- Tactile hardware has not converged across resolution and placement, creating a data-format risk.
- A large hardware commitment before convergence can strand expensive data if the sensor choice turns out wrong.
- Staging is an option-preserving decision rather than a rejection of touch.
- The choice is consistent with the source's broader preference for validating data value before scaling collection.

## Evidence
- Dataset evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] says the open-sourced data does not include tactile signals.
- Vision-substitution evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] argues that a two-finger claw can often judge grip visually and that the upper and lower cameras reduce occlusion.
- Prediction evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] says touch can be predicted from video but that the precision may be enough for pretraining and not for post-training.
- Hardware-risk evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] describes differing sensor resolutions and placements, the possibility that 100 devices produce poor results, and the problem of reusing data after a better sensor appears.
- Staging evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] says the company has not abandoned touch and is still experimenting, but has not scaled it.

## Counterevidence & Qualifications
This is one company's current tradeoff and it runs against the [[TactileSensing]] argument that touch is core infrastructure for dexterous manipulation. The source gives no trial results, error rates, or cost figures, and its position could change quickly if a dominant tactile format emerges or if vision-based grip judgment fails on soft, slippery, or deformable objects.

## What Changed
- Created the concept to record a deliberate delay in tactile scaling rather than a settled judgment that touch does not matter.
- Added the data-format lock-in risk as the stated reason for keeping the option open.

## Related Concepts
- [[TactileSensing]] - contrasting position that treats touch as core robotic infrastructure.
- [[OpticalTactileSensing]] - one unsettled sensor route whose format variation drives the staging choice.
- [[DexterousManipulation]] - capability area where the missing tactile channel is most likely to matter.
- [[UMIGloveDataCollection]] - the vision-only collection pipeline this choice applies to.
- [[RobotDataScaleUp]] - data-scaling discipline that the staging choice follows.
- [[RobotScalingClaimCaution]] - same source's preference for validated scale over premature commitments.
