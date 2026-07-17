---
title: "Marine Recovery Platform Control"
type: concept
tags: [aerospace, maritime, control-systems, reusable-rockets]
sources: [ruhe-douzhu-yike-huojian-s10e21-b66fdf0f-d428-4f0c-8412-b0c7581132d0]
last_updated: 2026-07-17
---

# Marine Recovery Platform Control

Marine recovery platform control is the problem of catching or landing a returning rocket stage on a sea platform that is moving in six degrees of freedom under waves, wind, and current. [[ruhe-douzhu-yike-huojian-s10e21-b66fdf0f-d428-4f0c-8412-b0c7581132d0]] introduces it through the [[LinghangzheRecoveryShip]] and [[LongMarch10B]] recovery.

The episode says the ship and rocket need to exchange position, attitude, velocity, and platform-state data at millisecond scale. Dynamic positioning, sea-state limits, ship structural motion, net damping, and guidance all become one coupled control problem: the rocket is not aiming at a fixed pad, and the recovery ship is not merely waiting passively.

## Key Claims
- Sea recovery turns platform motion into part of the flight-control boundary condition.
- A DP2-style positioning system can reduce but not eliminate motion; capture still depends on communication and final guidance tolerance.
- [[SeaNetRocketRecovery]] increases the importance of shipbuilding, offshore engineering, and tension-system control inside reusable launch.

## Connections
- [[LinghangzheRecoveryShip]] — source platform.
- [[LongMarch10B]] — returning rocket stage controlled against the moving platform.
- [[SeaNetRocketRecovery]] — recovery method that makes platform control central.
- [[RocketRecoveryRouteChoice]] and [[ReusableRocketEconomics]] — route and economic context.
