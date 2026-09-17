---
title: "深普智能 / Shenpu Intelligence"
type: entity
tags: [robotics, embodied-ai, physical-ai, startup, company]
sources:
  - yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

# 深普智能 / Shenpu Intelligence

## Overview
[[ShenpuIntelligence|深普智能]] is the home-facing general embodied-intelligence company where [[WangJiawei|王家伟]] is chief scientist, described in one [[ShizilukouCrossing]] interview. The episode presents it as a terminal company that builds data collection, pretraining, an agentic system, and its own evaluation as one product chain rather than as a data vendor or a model vendor.

## Current Profile
The company's stated goal is a general embodied system for the home, with an English name the source associates with "Simple AI" and the slogan "Keep the world simple." It reports roughly 70 employees, a 9:30-to-18:30 schedule with no forced overtime, self-directed work, an effectively unlimited AI-tool budget with [[Codex]] as the main tool, and planning that runs top-down from the CEO and technical leads on definitions, data, and compute. Technically it is building a pretrained action model plus an Agentic OS, while relying on self-built UMI-style collection hardware and on external upper-layer models where they are still improving fastest.

## Key Characteristics
- It is a full-stack terminal company: data, pretraining, deployment, and the robot body are treated as one value chain, and the source argues full-stack depth can become the moat.
- Its data position rests on a self-built six-camera UMI-style glove that removes the base station, localizes by camera at millimeter scale, and synchronizes at microsecond scale; a replay test put over 95% of collected trajectories back on the body.
- It open-sourced about 2,000 hours of data, reports internal data in the tens of thousands of hours, and cites cumulative downloads above 500,000 across Hugging Face and ModelScope.
- Its model program is described as zero-shot-capable on many tasks before release, with the first model planned for the end of 2026, selective borrowing from world-model and VLA work, and an explicit refusal to claim a validated scaling law.
- Its system architecture separates System 2 intent understanding and planning from System 1 fast fine execution, linked by a harness for context management and brain-to-small-brain scheduling.
- It stages tactile sensing instead of scaling it, keeps hardware and data-format options open, and treats vision plus upper/lower wrist cameras as enough for many two-finger grip judgments.
- Its organization is presented as flat and research-driven, with output tied to problem definition, shared context, and tool leverage rather than hours worked.

## Evidence
- Company positioning and organization: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] describes the home-facing terminal-company framing, the roughly 70-person team, the fixed non-overtime schedule, the unlimited AI-tool budget, and the top-down planning cadence.
- Data-collection evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] gives the six-camera glove design, base-station removal, millimeter localization, microsecond synchronization, the over-95% trajectory-replay result, the 2,000 open-sourced hours, the tens-of-thousands-of-hours internal scale, and the 500,000-plus downloads.
- Model and architecture evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] reports the planned end-of-year release, zero-shot task performance, the power-law-not-scaling-law caution, and the System 1/System 2 Agentic OS with an upper model that may start on an external model.
- Tactile and evaluation evidence: [[yushi-zhuan-shen-xiang-jushen-zouqu-duitan-wangjiawei-24-sui-de-jushen-zhineng-shouxi-kexuejia-litrgtfozrerillt7mtumknilr]] records the no-touch open dataset, the sensor-convergence worry, and the plan to publish a company-run evaluation that discloses zero-shot versus few-shot data use.

## Qualifications
The page rests on one chief-scientist interview, so its numbers, roadmap, and capability claims are company statements rather than independently verified facts. The source does not disclose model architecture, training cost, concrete success rates, revenue, or customer details. The name is kept as 深普智能 because that is what the episode reports; the "Simple AI" English association is the source's hint rather than a confirmed brand name. The end-of-year model release is a plan, not a shipped result.

## What Changed
- Created the entity page from the Shizilukou Crossing interview with [[WangJiawei]], separating the company's data, model, system, and organization claims into one bounded profile.
- Recorded the terminal-company positioning, the six-camera UMI-style data pipeline, the System 1/System 2 architecture, and the staged tactile position.

## Relationships
- [[WangJiawei]] - chief-scientist relationship; the source introduces the company through his background and role.
- [[ShizilukouCrossing]] - media-appearance relationship; the interview is the company's only wiki source so far.
- [[ChatGPT6Astra]] - evidence relationship; Astra's robot-arm demonstration is the general-model trigger the company interprets.
- [[SmallBrainActionLayer]] - architecture relationship; the company's stated differentiator is the lower real-time action layer.
- [[UMIGloveDataCollection]] - data-infrastructure relationship; the self-built glove is the company's claimed collection moat.
- [[RobotAgenticOS]] - product/system relationship; the Agentic OS is how the company connects planning to execution.
- [[HomeServiceRobots]] - product-direction relationship; the stated goal is a home robot that helps with everyday chores.
