---
title: "Platform Rights Pre-Review / 平台权利前置审查"
type: concept
tags: [platform-governance, moderation, rights, ai, ecommerce]
sources:
  - no-224-yong-ai-tou-mingxing-shengyin-he-xingxiang-qinquan-maihuo-zhibojian-gai-zenme-guan-gkwrijioio1wawwtsasyzh1d
last_updated: 2026-09-08
knowledge_schema: synthesis-v1
---

# Platform Rights Pre-Review / 平台权利前置审查

## Definition
Platform rights pre-review / 平台权利前置审查 is a platform governance mechanism that uses rights-owner data and automated detection to identify likely rights misuse before content, accounts, products, or live-selling activity reaches consumers.

## Current Synthesis
The Douyin ecommerce source treats pre-review as a shift from purely reactive complaint handling toward active rights protection. Rights holders can provide portraits, names, nicknames, aliases, voice information, and authorization relationships so the platform can detect likely unauthorized use earlier.

The mechanism is useful but fragile. It can reduce the visibility of obvious impersonation and catch scaled AI misuse, but it depends on accurate reference data, model generalization, authorization maintenance, and appeal channels for people who look similar, are misidentified, or have real but unsubmitted authorization.

## Key Claims
- Pre-review turns rights protection into an upstream platform workflow instead of only a takedown process.
- Reference data is central: names, aliases, portraits, voices, and authorized accounts become governance inputs.
- AI-generated variation forces models to generalize across masks, cropping, age changes, body changes, face edits, and voice substitution.
- Human review and appeals remain necessary because automated detection can misidentify lawful users or miss novel evasion.
- Rights-holder authorization records must stay current or lawful content can be blocked.
- Pre-review protects consumers as well as rights holders because it reduces misleading endorsement signals before purchase.

## Evidence
- Active protection: [[no-224-yong-ai-tou-mingxing-shengyin-he-xingxiang-qinquan-maihuo-zhibojian-gai-zenme-guan-gkwrijioio1wawwtsasyzh1d]] describes Douyin ecommerce portrait protection for public figures and future voice-information recognition.
- Submitted identifiers: [[no-224-yong-ai-tou-mingxing-shengyin-he-xingxiang-qinquan-maihuo-zhibojian-gai-zenme-guan-gkwrijioio1wawwtsasyzh1d]] says rights holders can submit names, nicknames, aliases, portraits, and authorization relationships.
- Evasion pressure: [[no-224-yong-ai-tou-mingxing-shengyin-he-xingxiang-qinquan-maihuo-zhibojian-gai-zenme-guan-gkwrijioio1wawwtsasyzh1d]] lists masks, sunglasses, cropped faces, age changes, body changes, foreign-face changes, and voice substitution as detection challenges.
- False positives: [[no-224-yong-ai-tou-mingxing-shengyin-he-xingxiang-qinquan-maihuo-zhibojian-gai-zenme-guan-gkwrijioio1wawwtsasyzh1d]] identifies similarity without bad faith, model errors, and missing authorization records as mistaken-enforcement categories.

## Counterevidence & Qualifications
The source does not provide technical details for the models, matching thresholds, human-review staffing, privacy safeguards for stored biometric-like data, or appeal timelines. Enforcement figures are platform-reported within the episode.

## What Changed
- Created the concept to capture pre-review as a distinct platform-rights workflow.

## Related Concepts
- [[AIEcommerceInfringementGovernance]] - broader governance system where pre-review operates.
- [[PlatformModerationComplianceLabor]] - adjacent creator-side labor created by platform rule enforcement.
- [[AIContentProvenance]] - evidence layer that can support detection and dispute resolution.
- [[AIPublicLikenessGeneration]] - visual identity surface that pre-review tries to protect.
- [[AIVoiceCloningRights]] - voice identity surface that pre-review may extend to.
- [[HumanJudgmentUnderAI]] - need for appeal and specialist judgment around automated signals.
