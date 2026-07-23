---
title: "Surveillance as a Service"
type: concept
tags: [surveillance, privacy, law-enforcement, data]
sources: [tech-20260108-0108-mp-tech-pod-128-tech-20260108-0108-mp-tech-pod-128, tech-20260302-0302-mp-tech-pod-128-tech-20260302-0302-mp-tech-pod-128]
last_updated: 2026-07-23
---

# Surveillance as a Service

Surveillance as a service is [[JeremyScott]]'s category in [[tech-20260302-0302-mp-tech-pod-128-tech-20260302-0302-mp-tech-pod-128]] for companies that build surveillance infrastructure, aggregate data, and sell searchable access or analytical tools to law enforcement. The episode uses [[FlockSafety]] license-plate-reader networks as the concrete example.

The concept differs from a single camera or database because the vendor packages collection, storage, search, and analysis as an ongoing service. That moves surveillance from a government-owned asset into a private infrastructure market, while still letting agencies such as [[USDepartmentOfHomelandSecurity]] and [[USImmigrationAndCustomsEnforcement]] query the resulting records.

[[tech-20260108-0108-mp-tech-pod-128-tech-20260108-0108-mp-tech-pod-128]] adds the operational-security failure mode. If service-managed cameras are exposed online, outsiders may see live feeds, archives, or controls even outside the contracted law-enforcement use case. In that episode, [[FlockSafety]] says the issue was a limited misconfiguration affecting a very small number of devices and had been remedied.

## Key Claims
- Private companies can build the data-collection layer before government agencies request access.
- The searchable database and analytics interface are as important as the raw sensor or record.
- Law-enforcement access can make private infrastructure function like public surveillance capacity.
- The issue connects device networks, data brokers, and constitutional process into one governance problem.
- The service model also creates vendor-security and configuration obligations because a single platform failure can expose many camera endpoints or archives.

## Connections
- [[FlockSafety]] - source example of license-plate-reader infrastructure.
- [[SurveillanceCameraExposure]], [[Shodan]], and [[BenJordan]] - exposed-device branch added by the January 8, 2026 Marketplace Tech episode.
- [[GovernmentDataBrokerAccess]], [[DataBrokerLoophole]], and [[AdministrativeSubpoenaDataAccess]] - adjacent access routes.
- [[FourthAmendmentDigitalPrivacy]], [[ThirdPartyDoctrine]], and [[CivilLibertiesSurveillanceRisk]] - legal and democratic-risk frame.
- [[ConsumerCameraSurveillance]] - related camera-network concern already present in the wiki.
