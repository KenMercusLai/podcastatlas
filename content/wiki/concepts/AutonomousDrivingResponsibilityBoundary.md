---
title: "Autonomous Driving Responsibility Boundary"
type: concept
tags: [autonomous-driving, safety, liability, robotaxi]
sources: [acc532947b65-acc532947b65]
last_updated: 2026-08-12
---

# Autonomous Driving Responsibility Boundary

Autonomous driving responsibility boundary is the distinction between systems that assist a human driver and systems that assume the driving task. [[acc532947b65-acc532947b65]] adds the concept through [[ZhangNingPonyAI|张宁]]'s explanation of L2, L3, and L4: L2 may handle lateral and longitudinal control, but the driver remains responsible; L4 makes the in-car humans passengers and shifts responsibility toward the system and operator.

The concept is useful because feature names can hide liability. Higher-end L2 functions can feel impressive, but they still depend on human supervision. L3 creates the hardest mixed state because the system may drive only inside conditions and then request handoff when the human is no longer alert enough to respond. L4 Robotaxi avoids that handoff ambiguity only by making the autonomous system and service operator responsible for fallback, safety, and operations.

## Key Claims
- Autonomy levels should be read through responsibility and fallback, not only through driving-feature richness.
- L2 remains a driver-responsibility product even when it includes lane keeping, following, LCC, NOA-style navigation, or other advanced assistance.
- L3 is commercially and legally hard because control may move from system to human at the exact moment the human is least ready.
- L4 creates a different business model because the passenger is no longer the fallback driver.
- The responsibility boundary connects technical design to regulation, insurance, public trust, and service operations.

## Connections
- [[PonyAI|Pony.ai]] and [[ZhangNingPonyAI]] - source company and speaker.
- [[RobotaxiEconomics]] - business consequences of removing the driver.
- [[RobotaxiFleetOperations]] - operational responsibilities that replace driver labor.
- [[AutonomousVehicleSafetyBenchmark]] - safety-evidence frame needed when the system becomes responsible.
- [[AutonomousVehicleRegulatoryPatchwork]] - legal and policy context around L4 deployment.
- [[RobotaxiLocalAcceptance]] - passenger and city trust consequences.
