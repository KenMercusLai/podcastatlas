---
title: "Offline Platform Safety Boundary / 线下平台安全边界"
type: concept
tags: [platforms, offline-services, safety, risk-management]
sources:
  - no-228-duihua-didi-quxiaonan-pa-ni-juede-women-bu-anquan-geng-pa-ni-juede-women-juedui-anquan-gkwriueor0j1ayqkyatbzbpi
last_updated: 2026-09-07
knowledge_schema: synthesis-v1
---

# Offline Platform Safety Boundary / 线下平台安全边界

## Definition
Offline platform safety boundary is the limit of a digital platform's ability to prevent or respond to harm once a service moves into physical space, off-platform communication, silent behavior, or post-transaction interaction.

## Current Synthesis
The [[Didi]] source shows that platform safety visibility is strongest while the service remains legible to the app: order state, driver identity, route, audio, video where available, phone contact, and in-app actions all help the platform infer risk. That visibility weakens when the ride is moved offline, when the passenger sleeps silently, when recording is closed, or when the driver and passenger remain near each other after the trip ends.

The boundary is not only technical. It is behavioral and contractual. Users who switch to offline rides remove the very signals that make safety operations possible; parents who call rides for children without proxy labeling hide the real passenger type; drunk passengers may appear to consent while lacking ordinary self-protection. The platform can reduce risk, but the safety envelope depends on user choices that keep the service visible.

## Key Claims
- Digital platforms lose safety capacity when users move physical services outside the tracked transaction.
- The app's order state can understate risk when people have not physically separated.
- Silent or ambiguous behavior can defeat audio and anomaly-based detection.
- Proxy-use labeling matters because the account holder may not be the actual passenger.
- Intoxication and age change how consent, self-protection, and service duty should be interpreted.
- User education is part of safety operations because user choices affect whether the platform can observe and intervene.

## Evidence
- Offline transaction gap - [[no-228-duihua-didi-quxiaonan-pa-ni-juede-women-bu-anquan-geng-pa-ni-juede-women-juedui-anquan-gkwriueor0j1ayqkyatbzbpi]] warns that moving a ride to direct driver-passenger contact makes platform route, recording, warning, and intervention capacity drop away.
- Post-order gap - [[no-228-duihua-didi-quxiaonan-pa-ni-juede-women-bu-anquan-geng-pa-ni-juede-women-juedui-anquan-gkwriueor0j1ayqkyatbzbpi]] says risk can continue if a drunk passenger remains in the car or if driver and passenger have not safely separated after order completion.
- Silent-risk gap - [[no-228-duihua-didi-quxiaonan-pa-ni-juede-women-bu-anquan-geng-pa-ni-juede-women-juedui-anquan-gkwriueor0j1ayqkyatbzbpi]] identifies sleeping drunk passengers and quiet cars as cases where audio cannot easily surface danger.
- Minor-passenger gap - [[no-228-duihua-didi-quxiaonan-pa-ni-juede-women-bu-anquan-geng-pa-ni-juede-women-juedui-anquan-gkwriueor0j1ayqkyatbzbpi]] says parents using an adult account for a child can hide the real passenger risk unless they use formal proxy-order functions.
- Drunk-passenger consent boundary - [[no-228-duihua-didi-quxiaonan-pa-ni-juede-women-bu-anquan-geng-pa-ni-juede-women-juedui-anquan-gkwriueor0j1ayqkyatbzbpi]] treats apparent willingness under intoxication as insufficient inside a driver-passenger service relationship.

## Counterevidence & Qualifications
The concept does not imply that platforms have no responsibility once a service is offline. It describes why technical visibility and intervention capacity weaken. The source remains platform-side evidence and does not independently establish the legal allocation of responsibility among platform, driver, passenger, and regulator.

## What Changed
- Created the concept from the [[Didi]] ride-hailing safety episode.

## Related Concepts
- [[RideHailingSafetyOperations]] - platform system whose reach is constrained by this boundary.
- [[HighRecallSafetyIntervention]] - intervention posture that still depends on observable signals.
- [[PublicSafetyPrivacyTradeoff]] - privacy controls around keeping physical services observable.
- [[OfflineAIImplementation]] - adjacent physical-world implementation frame where real operations expose requirements and limits.
- [[LocalLifePlatformDependency]] - platform-mediated local-service context where leaving the platform changes risk and leverage.
- [[ChildOnlineCommerceSafety]] - adjacent child-protection frame for platform-mediated services.
