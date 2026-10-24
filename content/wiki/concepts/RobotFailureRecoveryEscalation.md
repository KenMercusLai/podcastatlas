---
title: "Robot Failure-Recovery Escalation / 机器人失败恢复分层接管"
type: concept
knowledge_schema: synthesis-v1
tags: [robotics, embodied-ai, failure-recovery, model-routing, distillation]
sources:
  - shaoyou-de-tongshi-zuoguo-agent-duomotai-he-jushen-de-ren-duitan-qian-hunyuan-duomotai-rl-infra-fuzeren-haonan-lvbhcwvcteq4tvfmvcbkrubw0n82
last_updated: 2026-10-25
---

# Robot Failure-Recovery Escalation / 机器人失败恢复分层接管

## Definition
Robot failure-recovery escalation is a layered deployment pattern in which a fast, hardware-specific local policy performs routine actions, a stronger general model takes over difficult or failing steps, and a human intervenes only when both model layers cannot recover; successful recovery traces then train the local policy.

## Current Synthesis
The bounded source presents escalation as both an operating architecture and a data strategy. Giving every motor-control step to a large model is too slow and costly, while expecting a small policy to handle every tail case blocks deployment. Routing only impending failures upward preserves fast local execution and concentrates expensive intelligence where it is most informative. Captured recovery trajectories can then reduce later escalation, but the account remains a proposed flywheel rather than audited field evidence.

## Key Claims
- Routine control belongs close to the robot body because action frequency, latency, and hardware-specific parameters make continuous large-model control inefficient.
- Failure detection is the routing gate: escalation has value only if the system recognizes trouble early enough for a stronger controller to recover safely.
- Large-model takeover is most useful for review, correction, and rare difficult steps rather than every low-level action.
- Human intervention remains the final safety and data-quality fallback when model recovery fails.
- Recovery trajectories are more targeted than having a large model generate complete task histories, making intervention-based “soft distillation” cheaper than full-trajectory “hard distillation.”
- Falling intervention rates could improve deployment economics while expanding the local model's competence.

## Evidence
- Execution hierarchy: [[shaoyou-de-tongshi-zuoguo-agent-duomotai-he-jushen-de-ren-duitan-qian-hunyuan-duomotai-rl-infra-fuzeren-haonan-lvbhcwvcteq4tvfmvcbkrubw0n82]] proposes local-model execution, large-model takeover near failure, and human fallback.
- Cost and latency: [[shaoyou-de-tongshi-zuoguo-agent-duomotai-he-jushen-de-ren-duitan-qian-hunyuan-duomotai-rl-infra-fuzeren-haonan-lvbhcwvcteq4tvfmvcbkrubw0n82]] argues that using a large model for all mechanical control is slower and more expensive than reserving it for difficult steps.
- Learning mechanism: [[shaoyou-de-tongshi-zuoguo-agent-duomotai-he-jushen-de-ren-duitan-qian-hunyuan-duomotai-rl-infra-fuzeren-haonan-lvbhcwvcteq4tvfmvcbkrubw0n82]] says recovered failure trajectories can train the local model and progressively reduce both large-model calls and human supervision.
- Distillation boundary: [[shaoyou-de-tongshi-zuoguo-agent-duomotai-he-jushen-de-ren-duitan-qian-hunyuan-duomotai-rl-infra-fuzeren-haonan-lvbhcwvcteq4tvfmvcbkrubw0n82]] distinguishes costly full-trajectory generation from retaining only intervention and recovery traces.

## Counterevidence & Qualifications
The source supplies no failure detector, routing threshold, safety protocol, latency budget, model comparison, deployment population, learning curve, or measured reduction in interventions. Large-model takeover can also arrive too late, produce unsafe actions, or fail under the same distribution shift as the local policy. Human fallback introduces staffing, privacy, labor, and scalability constraints. The pattern should therefore be treated as a deployment hypothesis requiring scenario-specific validation.

## What Changed
- Created the concept to separate intervention-based recovery and distillation from the broader brain/small-brain architecture.
- Preserved human fallback and failure detection as necessary constraints rather than assuming two model tiers guarantee recovery.

## Related Concepts
- [[SmallBrainActionLayer]] - routine, fast control layer from which difficult cases escalate.
- [[LayeredRobotArchitecture]] - broader architectural family that separates planning from control.
- [[RobotDeploymentDataLoop]] - learning and economic loop fed by recovery trajectories.
- [[RobotExperienceData]] - robot attempts, failures, corrections, and recoveries captured during use.
- [[RobotTeleoperationAndRemoteTakeover]] - human-control fallback with related operational and privacy constraints.
- [[GeneralModelRobotBoundary]] - reason stronger semantic reasoning does not eliminate real-time control requirements.
