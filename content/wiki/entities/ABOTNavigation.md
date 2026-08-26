---
title: "A-BOT Navigation"
type: entity
tags: [robotics, navigation, maps, embodied-ai]
sources:
  - dang-jiqiren-xuehui-renlu-wuli-shijie-cai-zhenzheng-jieshangle-ai-658f592c4a52
last_updated: 2026-08-27
knowledge_schema: synthesis-v1
---

# A-BOT Navigation

## Overview
A-BOT Navigation is the Gaode robot-navigation model or product line discussed in [[dang-jiqiren-xuehui-renlu-wuli-shijie-cai-zhenzheng-jieshangle-ai-658f592c4a52]]. The episode says it is part of Gaode's A-BOT series and had reached version 1.5, with a focus on visual navigation across indoor, outdoor, campus, office, and city contexts.

## Current Profile
Within the wiki, A-BOT Navigation is the concrete technical handle for Gaode's [[RobotNavigationInfrastructure]] strategy. It turns maps from a human phone-navigation service into robot-facing guidance: fine-grained routes, passability judgments, local memory, and shared learned layouts become part of how robots decide where to move.

## Key Characteristics
- It is framed as a pure-visual navigation model in the episode.
- It extends ordinary car-lane or road-map data toward pedestrian, campus, indoor, and robot-passability detail.
- It can learn private or semi-private spaces by walking a robot through an office, then reuse that layout across robots.
- It supports [[GuideRobotDogs]], delivery, and inspection scenarios where movement is the first bottleneck.
- Its practical value depends on privacy, safety, road rights, and real-world task feedback.

## Evidence
- Product evidence: [[dang-jiqiren-xuehui-renlu-wuli-shijie-cai-zhenzheng-jieshangle-ai-658f592c4a52]] names A-BOT Navigation as part of Gaode's A-BOT series and says Navigation had reached version 1.5.
- Model evidence: [[dang-jiqiren-xuehui-renlu-wuli-shijie-cai-zhenzheng-jieshangle-ai-658f592c4a52]] describes Gaode's approach as pure-visual navigation rather than only static map lookup.
- Map-granularity evidence: [[dang-jiqiren-xuehui-renlu-wuli-shijie-cai-zhenzheng-jieshangle-ai-658f592c4a52]] contrasts car-lane maps with robot needs such as sidewalks, ramps, stairs, curbs, passage width, and overpasses.
- Indoor evidence: [[dang-jiqiren-xuehui-renlu-wuli-shijie-cai-zhenzheng-jieshangle-ai-658f592c4a52]] says a robot can be walked through an office to remember desks, offices, and bathrooms.
- Application evidence: [[dang-jiqiren-xuehui-renlu-wuli-shijie-cai-zhenzheng-jieshangle-ai-658f592c4a52]] connects the navigation stack to guide dogs, last-mile delivery, and patrol or inspection use cases.

## Qualifications
The episode does not provide benchmark results, deployment counts, independent safety testing, or details about how A-BOT Navigation handles privacy-sensitive indoor maps. Its current wiki status is therefore a source-scoped product profile rather than verified market adoption.

## What Changed
- Initial profile: A-BOT Navigation becomes Gaode's named robot-navigation layer in the wiki.
- The current judgment treats it as a robot-facing map/model interface, not simply as a human navigation feature.

## Relationships
- [[Gaode]] - company building and presenting the A-BOT Navigation route.
- [[TangWenbin]] - speaker explaining the model and its use cases.
- [[RobotNavigationInfrastructure]] - broader concept that A-BOT Navigation instantiates.
- [[GuideRobotDogs]] - assistive-robot application that depends on the navigation layer.
- [[LastMileRobotDelivery]] - delivery application that needs sidewalk, campus, building, and elevator-aware routing.
- [[IndustrialInspectionRobotics]] - inspection application where route stability and localization matter in changing or open sites.
