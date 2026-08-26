---
title: "Gaode"
type: entity
tags: [maps, local-services, alibaba, china]
sources:
  - ep117-doubao-yuehuo-guoyi-ali-zaizao-qianwen-shibushi-wanle-lmp0pzdig2ijow5k3cnnnvvqq6sa
  - dang-jiqiren-xuehui-renlu-wuli-shijie-cai-zhenzheng-jieshangle-ai-658f592c4a52
last_updated: 2026-08-27
knowledge_schema: synthesis-v1
---

# Gaode

## Overview
Gaode is [[Alibaba]]'s map, local-service, and mobility surface in the wiki. Earlier material placed it behind [[Qwen]] as a fulfillment layer for [[AIAssistantServiceEntry]]; the Gaode robotics episode extends the same asset base into [[PhysicalAI]] by treating maps, spatiotemporal data, and navigation models as robot infrastructure.

## Current Profile
Gaode now sits at two adjacent entry points. In consumer AI, it helps an assistant connect recommendations to places, routes, and local decisions. In embodied AI, it can tell robots not only a destination but what kind of path, obstacle, passage, indoor layout, or body-specific constraint they may encounter. The current profile is therefore no longer just a map app inside Alibaba's service stack; it is a possible physical-world coordination layer.

## Key Characteristics
- Gaode supplies map and local-life context inside Alibaba's broader service ecosystem.
- It can function as a "hands and feet" layer for [[Qwen]] when assistant requests require routing, local recommendations, or service fulfillment.
- Its embodied-AI route starts from movement and navigation rather than full humanoid manipulation.
- Its robot strategy depends on fine-grained spatial data: sidewalks, campuses, office interiors, curbs, slopes, stairs, passage width, and robot passability.
- Its early robot use cases center on guide robot dogs, last-mile delivery, and inspection or patrol.
- Its physical-AI ambitions remain source-scoped because deployment scale, safety, road rights, cost, and privacy are not independently demonstrated in the current evidence.

## Evidence
- Assistant-entry evidence: [[ep117-doubao-yuehuo-guoyi-ali-zaizao-qianwen-shibushi-wanle-lmp0pzdig2ijow5k3cnnnvvqq6sa]] places Gaode among Alibaba services such as Taobao, Fliggy, Damai, and DingTalk that could let Qwen complete real-world requests rather than only answer questions.
- Local-service evidence: [[ep117-doubao-yuehuo-guoyi-ali-zaizao-qianwen-shibushi-wanle-lmp0pzdig2ijow5k3cnnnvvqq6sa]] uses maps, places, travel, food, and local services to explain why assistant value depends on fulfillment surfaces.
- Embodied-strategy evidence: [[dang-jiqiren-xuehui-renlu-wuli-shijie-cai-zhenzheng-jieshangle-ai-658f592c4a52]] says Gaode is using two decades of spatiotemporal data to help robots move from A to B and handle obstacles.
- Navigation-infrastructure evidence: [[dang-jiqiren-xuehui-renlu-wuli-shijie-cai-zhenzheng-jieshangle-ai-658f592c4a52]] describes A-BOT Navigation, pedestrian-level map needs, indoor memory, and robot-specific passability.
- Application evidence: [[dang-jiqiren-xuehui-renlu-wuli-shijie-cai-zhenzheng-jieshangle-ai-658f592c4a52]] names guide robot dogs, last-mile delivery, office or campus delivery, and dangerous-site inspection as near-term scenarios.

## Qualifications
Gaode's robotics evidence comes from a company-side conversation and is not yet matched by independent deployment data. The wiki should keep the Physical AI port claim separate from proven large-scale adoption, especially where public-space rights, safety, privacy-sensitive indoor maps, and cost payback remain unresolved.

## What Changed
- Gaode's profile expanded from Qwen service fulfillment into robot navigation and physical-world execution.
- The current judgment distinguishes map-data advantage from proof of robotics market adoption.
- The page was migrated to `synthesis-v1` while preserving the original source order.

## Relationships
- [[Alibaba]] - parent ecosystem connecting Gaode to Qwen, logistics, local services, and Physical AI strategy.
- [[Qwen]] - assistant surface where Gaode can support local-service fulfillment.
- [[AutoNavi]] - older wiki page for the same map brand in a Robotaxi partnership context.
- [[TangWenbin]] - Gaode embodied-business lead explaining the robotics route.
- [[GuoNing]] - Gaode CEO tied to the source-scoped Physical AI port framing.
- [[ABOTNavigation]] - Gaode's named robot-navigation model or product layer.
- [[RobotNavigationInfrastructure]] - concept capturing Gaode's map-to-robot infrastructure role.
- [[GuideRobotDogs]] - first core embodied application in the Gaode episode.
- [[LastMileRobotDelivery]] - adjacent delivery use case enabled by precise navigation and local-service integration.
