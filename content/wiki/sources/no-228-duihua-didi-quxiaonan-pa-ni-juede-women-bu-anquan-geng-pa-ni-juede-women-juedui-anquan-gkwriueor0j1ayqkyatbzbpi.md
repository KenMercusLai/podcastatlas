---
title: "No.228 对话滴滴曲晓楠：怕你觉得我们不安全，更怕你觉得我们绝对安全"
type: source
tags: [podcast, sanwuhuan, ride-hailing, safety, platform-governance]
sources: []
date: 2026-08-04
source_file: "/home/ken/repos/podcastatlas/content/episodes/GKwRIUEOR0J1AYQKYATBzBPI [GKwRIUEOR0J1AYQKYATBzBPI].md"
source_url: "https://tk.wavpub.com/WPDL_gzscFcjQdxQCbKAzNFKKLgseULkhVgYSLKJBGSBBKdPbagPBhRbFmcBhDx-01.m4a"
duration: "3142"
last_updated: 2026-09-07
---

# No.228 对话滴滴曲晓楠：怕你觉得我们不安全，更怕你觉得我们绝对安全

## Summary
This [[SanWuHuan|三五环]] episode has [[LiuFei|刘飞]] interviewing [[XuXiaonan|徐晓楠 / 曲晓楠]], described in the source body as [[Didi]]'s ride-hailing safety lead, about how the platform rebuilt safety work after the 2018 Hitch safety incidents. The conversation turns [[RideHailingSafetyOperations]] into a concrete operating system: driver admission, pre-shift verification and education, safety-aware dispatch, AI and human warning during trips, and post-trip responsibility handling.

The durable synthesis is that ride-hailing safety is an online-offline governance problem, not only an app feature. [[Didi]] can raise risk recall by using route, audio, video, and in-app signals, but [[HighRecallSafetyIntervention]] creates false alarms and user interruption, while [[OfflinePlatformSafetyBoundary]] leaves gaps around offline transactions, silent in-car risk, drunk passengers, minors, and post-order events. The source also extends [[PublicSafetyPrivacyTradeoff]] because risk detection depends partly on optional recording, model scanning, minimal-access review, and institutional controls over who can inspect trip data.

## Key Claims
- [[Didi]]'s internal safety boundary is described as starting when an order is matched and ending only when driver and passenger have safely separated, not merely when the paid trip ends.
- [[RideHailingSafetyOperations]] has multiple layers: driver qualification and background checks, driver and vehicle verification, safety education, risk-aware dispatch, in-trip AI and human warning, phone intervention, possible police contact, and post-trip adjudication.
- The source says [[Didi]] processes roughly 30 million daily orders through two AI screening layers, narrowing them to about 100,000 and then about 30,000 orders for specialist review, with several thousand interventions.
- [[HighRecallSafetyIntervention]] is explicit: [[XuXiaonan|徐晓楠 / 曲晓楠]] says safety models prioritize recall far above precision, accepting many false alarms to reduce missed severe incidents.
- Large-model audio reasoning is presented as an improvement over keyword matching because it can infer risk from contextually unusual speech, sounds, tone, or interaction patterns before sending cases to human review.
- Current recall is described as a little above 80%, with remaining gaps around offline transactions, quiet or sleeping passengers, events after the order, and very fast or premeditated incidents.
- Drunk passengers are treated as a high-risk scene because self-protection and meaningful consent can be impaired; the source says apparent willingness during intoxication should not automatically be treated as valid within the service relationship.
- The episode warns against minors riding alone, especially children under 14, and recommends formal proxy ordering because platform-visible labels can raise the order's service and safety level.
- Offline transactions are framed as making a platform-supervised ride resemble an unlicensed ride because route, recording, warning, intervention, and identity visibility drop away.
- Privacy is framed as a controlled-access tradeoff: recording can be opened or closed by the passenger, model scanning happens before human review, and human access is said to require risk signals and internal information-security controls.

## Key Quotes
> "从订单成交那一刻开始，到司机和乘客安全分离为止" - the source's longer safety-boundary definition.

> "召回率的重要性远大于准确率" - the source's high-recall safety priority.

> "不要线下切单" - the clearest passenger-side safety warning.

## Connections
- [[SanWuHuan|三五环]], [[LiuFei|刘飞]], and [[XuXiaonan|徐晓楠 / 曲晓楠]] - show, host, and guest.
- [[Didi]] - company whose ride-hailing safety system grounds the episode.
- [[RideHailingSafetyOperations]], [[HighRecallSafetyIntervention]], and [[OfflinePlatformSafetyBoundary]] - main operational concepts created from the source.
- [[PublicSafetyPrivacyTradeoff]], [[AIHardwarePrivacyExchange]], and [[HumanJudgmentUnderAI]] - privacy, recording, model review, and specialist judgment context.
- [[PlatformAgeEstimation]] and [[ChildOnlineCommerceSafety]] - adjacent child-safety and platform-rule contexts touched by the minor-passenger examples.
- [[RobotaxiFleetOperations]] and [[AutonomousVehicleSafetyBenchmark]] - adjacent mobility-safety concepts that differ because this source concerns human driver-passenger service risk.

## Contradictions
- No settled contradiction found. The source title names "曲晓楠", while the body consistently uses "徐晓楠"; this ingest creates [[XuXiaonan|徐晓楠 / 曲晓楠]] and keeps the mismatch source-scoped.
- Safety incident reduction, daily-order, screening, intervention, vehicle-video, and recall-rate figures are treated as guest-reported platform claims, not independently verified public metrics.
