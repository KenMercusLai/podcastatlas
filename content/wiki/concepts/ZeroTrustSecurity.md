---
title: "Zero Trust Security"
type: concept
tags: [cybersecurity, security, saas]
sources: [how-danny-jenkins-bootstrapped-threatlocker-from-150k-debt-to-200m]
last_updated: 2026-07-06
---

# Zero Trust Security

Zero trust security is the security idea that systems should not automatically trust software, access, or activity simply because it appears inside an environment. In [[how-danny-jenkins-bootstrapped-threatlocker-from-150k-debt-to-200m]], [[DannyJenkins]] frames zero trust as an idea rather than a product, and presents [[ThreatLocker]] as a practical implementation through least privilege, explicit approval, and [[DefaultDenySecurity]].

## Key Claims
- The episode contrasts default-allow security with systems that allow only explicitly approved software or behavior.
- Jenkins argues that the idea is simple but hard to implement well, especially for smaller companies that lack large security teams.
- The category was controversial because it challenged a security industry built around antivirus, EDR, threat hunting, SIEM, SOC services, and other detection-oriented tools.
- Practical zero trust adoption depends on usability; if control systems are too hard to maintain, customers will not sustain them.
- [[ThreatLocker]] used product capability plus market education to turn application control and whitelisting into a broader [[CategoryCreation]] effort.

## Connections
- [[ThreatLocker]] and [[DannyJenkins]] - company and founder case.
- [[DefaultDenySecurity]] - concrete control pattern within the episode's zero trust framing.
- [[MSPChannelDistribution]] - route for bringing zero trust controls to smaller businesses.
- [[SaaSTrustMoat]] - adjacent SaaS strategy concept where security and reliability create defensibility.
