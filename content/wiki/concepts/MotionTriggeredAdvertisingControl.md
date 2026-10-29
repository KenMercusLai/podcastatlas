---
title: "Motion-Triggered Advertising Control / 摇一摇广告控制"
type: concept
tags: [advertising, mobile, privacy, sensors, platform-governance]
sources:
  - dafeixin-pingguo-xin-xitong-keyi-jinzhi-yaoyiyao-guanggao-zhangyiming-zai-deng-hurun-baifu-bangshou-gkwridoot6kmafx6cwtxdrfn
last_updated: 2026-10-29
knowledge_schema: synthesis-v1
---

# Motion-Triggered Advertising Control / 摇一摇广告控制

## Definition
Motion-triggered advertising control is operating-system governance that lets users deny apps access to motion sensors when those sensors are used to initiate advertising redirects rather than a user-requested fitness or motion function.

## Current Synthesis
The reported iOS control treats sensor permission as an interaction-integrity boundary. Blocking motion access removes an app's ability to infer a shake and trigger a jump, reducing accidental activation without banning all advertising. The mechanism also illustrates platform power: enforcement depends on permission granularity, defaults, developer compliance, and whether apps substitute other attention-capture techniques.

## Key Claims
- Motion sensors can be repurposed from device functionality into advertising triggers.
- Accidental physical movement makes intent ambiguous and increases unwanted redirects.
- Per-app permission controls can remove the trigger capability at the operating-system layer.
- Interface governance is stronger when permissions align with the declared purpose of an API.
- Blocking one trigger does not eliminate deceptive or coercive advertising design.

## Evidence
- **Permission mechanism:** [[dafeixin-pingguo-xin-xitong-keyi-jinzhi-yaoyiyao-guanggao-zhangyiming-zai-deng-hurun-baifu-bangshou-gkwridoot6kmafx6cwtxdrfn]] says a new China-region iOS version lets users deny selected apps access to motion data.
- **Intent problem:** [[dafeixin-pingguo-xin-xitong-keyi-jinzhi-yaoyiyao-guanggao-zhangyiming-zai-deng-hurun-baifu-bangshou-gkwridoot6kmafx6cwtxdrfn]] cites more than a thousand complaints on a third-party platform about easy accidental activation.
- **Purpose boundary:** [[dafeixin-pingguo-xin-xitong-keyi-jinzhi-yaoyiyao-guanggao-zhangyiming-zai-deng-hurun-baifu-bangshou-gkwridoot6kmafx6cwtxdrfn]] says Apple's developer agreement limits the relevant interface to health, motion, and fitness services rather than advertising.

## Counterevidence & Qualifications
The source does not name the iOS version, document rollout coverage, test enforcement, or compare default settings. Complaint volume is not a population-level incidence rate, and apps may redesign prompts or use other triggers.

## What Changed
- Added an operating-system control concept for sensor-driven ad redirects.
- Preserved platform enforcement and substitution as explicit limitations.

## Related Concepts
- [[ApplePrivacy]] - device-permission and data-minimization relationship.
- [[AgentPermissionBoundaries]] - permission granularity and delegated-action relationship.
- [[AIConsumerProtectionEnforcement]] - platform and regulator enforcement relationship.
- [[PlatformAdvertisingMonetization]] - attention capture and advertising-revenue relationship.
