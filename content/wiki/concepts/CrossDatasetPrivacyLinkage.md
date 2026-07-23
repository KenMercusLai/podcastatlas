---
title: "Cross-Dataset Privacy Linkage"
type: concept
tags: [privacy, data, surveillance]
sources: [tech-20260108-0108-mp-tech-pod-128-tech-20260108-0108-mp-tech-pod-128]
last_updated: 2026-07-23
---

# Cross-Dataset Privacy Linkage

Cross-dataset privacy linkage is the risk that one exposed or ordinary data source becomes identifying when combined with another dataset. In [[tech-20260108-0108-mp-tech-pod-128-tech-20260108-0108-mp-tech-pod-128]], [[BenJordan]] says a license plate visible in exposed [[FlockSafety]] footage could be cross-referenced with [[ParkMobile]] breach data to infer where someone lives or when they might be home.

The concept explains why surveillance risk is not limited to what a camera directly shows. A plate, face, route, timestamp, phone view, or home-adjacent activity can become more revealing when connected to breached data, data brokers, public records, or other commercial datasets.

## Key Claims
- A single data point can become sensitive when another dataset supplies identity, address, schedule, or context.
- License-plate capture is especially linkable because it sits between vehicle identity, location, and public movement.
- Breached datasets can continue creating risk after the original incident when they are reused as lookup tables for new exposures.
- Cross-dataset linkage makes [[SurveillanceCameraExposure]] and [[PublicSpaceRoutineTracking]] more dangerous than isolated video access.
- The issue overlaps with data-broker governance, but it can also arise from leaked or breached records outside formal brokerage markets.

## Connections
- [[FlockSafety]] - source camera network.
- [[ParkMobile]] - breach example named by Jordan.
- [[BenJordan]] - source speaker.
- [[SurveillanceCameraExposure]] and [[PublicSpaceRoutineTracking]] - exposure and temporal-pattern risks that linkage can amplify.
- [[DataBrokerLoophole]], [[GovernmentDataBrokerAccess]], and [[ConsumerDataDeletion]] - adjacent data-reuse and governance branches.
