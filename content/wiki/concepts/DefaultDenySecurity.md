---
title: "Default Deny Security"
type: concept
tags: [cybersecurity, access-control, zero-trust]
sources: [how-danny-jenkins-bootstrapped-threatlocker-from-150k-debt-to-200m]
last_updated: 2026-07-06
---

# Default Deny Security

Default deny security is the control pattern of blocking software or behavior unless it has been explicitly approved. In [[how-danny-jenkins-bootstrapped-threatlocker-from-150k-debt-to-200m]], [[DannyJenkins]] describes [[ThreatLocker]] as hardening customer environments by controlling what can run, rather than depending mainly on detection of known threats.

## Key Claims
- The episode presents default-deny controls as a response to ransomware cases where backups, databases, servers, and endpoints could be encrypted after unauthorized execution.
- Jenkins argues that earlier whitelisting and application-control products were difficult to operate, making usability central to adoption.
- The first customer trial required fast code changes and real deployment, showing that default-deny products may be hard to validate without live customer environments.
- Default deny is related to [[ZeroTrustSecurity]] but more concrete: it is one mechanism for enforcing least privilege and explicit approval.
- The pattern can create sales resistance because buyers may fear blocking legitimate work unless the product makes approval and maintenance practical.

## Connections
- [[ThreatLocker]] and [[DannyJenkins]] - product and founder case.
- [[ZeroTrustSecurity]] - broader security philosophy.
- [[CategoryCreation]] - market-education challenge when buyers are used to default-allow and detection-oriented security.
- [[ProductLedWillingnessToPay]] - payment signal when customers accept deployment friction because the control solves an urgent risk.
