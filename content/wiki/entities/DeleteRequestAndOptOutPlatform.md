---
title: "Delete Request and Opt Out Platform"
type: entity
tags: [platform, privacy, data-brokers, consumer-protection]
sources:
  - tech-20260309-0309-mp-tech-pod-128-tech-20260309-0309-mp-tech-pod-128
  - tech-20260825-mp-tech-pod-128-tech-20260825-mp-tech-pod-128
last_updated: 2026-08-26
knowledge_schema: synthesis-v1
---

# Delete Request and Opt Out Platform

## Overview
The Delete Request and Opt Out Platform is California's centralized deletion-request system for residents who want registered data brokers to delete personal information. The wiki treats DROP and DROPS as naming variants for the same California data-broker deletion infrastructure.

## Current Profile
The platform turns the [[CaliforniaDeleteAct]] into a practical [[ConsumerDataDeletion]] workflow: residents can make one request instead of contacting data brokers one by one. Its significance is operational rather than symbolic. The March source presents the platform as a way to reduce broker-held data and downstream harms; the August source adds that usefulness depends on whether brokers actually register, report statistics, check the system every 45 days, and remove friction from consumer-rights workflows.

## Key Characteristics
- Centralizes deletion requests that would otherwise have to be sent to individual data brokers.
- Implements a state-law privacy right rather than a voluntary industry opt-out.
- Reduces but does not eliminate consumer exposure because data can still exist in cookies, government systems, dark-web copies, unregistered flows, or platform behavior trails.
- Depends on broker compliance, reporting, enforcement, public awareness, and usability.
- Creates scale effects because a persistent, one-time consumer sign-up can force repeated broker checks.

## Evidence
- Centralized workflow: [[tech-20260309-0309-mp-tech-pod-128-tech-20260309-0309-mp-tech-pod-128]] says DROP lets [[California]] residents request deletion from registered data brokers through a state platform; [[tech-20260825-mp-tech-pod-128-tech-20260825-mp-tech-pod-128]] says the DROPS system avoids broker-by-broker deletion requests.
- Operational limits: [[tech-20260309-0309-mp-tech-pod-128-tech-20260309-0309-mp-tech-pod-128]] says deletion does not cover all cookies, government systems, behavioral data trails, or unregistered data flows.
- Compliance dependence: [[tech-20260825-mp-tech-pod-128-tech-20260825-mp-tech-pod-128]] says brokers must check the system every 45 days and that some brokers add friction or fail to report required statistics.
- Scale potential: [[tech-20260825-mp-tech-pod-128-tech-20260825-mp-tech-pod-128]] says more than 450,000 people had registered after sign-ups began in January and frames millions of registrations as potentially material to broker-held data supply.

## Qualifications
The platform is not a universal erasure tool. It addresses registered data brokers, not every collector or downstream holder of personal information. The name appears as DROP in the March episode and DROPS in the August episode; the current synthesis treats that as a naming variant unless future sources distinguish separate systems.

## What Changed
- Added the compliance and scale layer: the platform's promise now depends on broker behavior, required 45-day checks, and enforcement capacity.
- Added the DROP/DROPS naming qualification.

## Relationships
- [[CaliforniaDeleteAct]] - legal mandate implemented by the platform.
- [[ConsumerDataDeletion]] - privacy mechanism operationalized through the platform.
- [[DataBrokerComplianceGap]] - failure mode when brokers make the platform or related rights hard to use.
- [[CaliforniaPrivacyProtectionAgency]] - regulator whose enforcement capacity shapes platform effectiveness.
- [[AIDataBrokerDemand]] - downstream demand that makes deletion and broker disclosure more consequential.
