---
title: "Shodan"
type: entity
tags: [search-engine, cybersecurity, internet-exposure]
sources: [tech-20260108-0108-mp-tech-pod-128-tech-20260108-0108-mp-tech-pod-128]
last_updated: 2026-07-23
---

# Shodan

Shodan appears in [[tech-20260108-0108-mp-tech-pod-128-tech-20260108-0108-mp-tech-pod-128]] as a search engine used for security checks, including finding exposed ports and internet-connected cameras. [[BenJordan]] says he used basic Shodan searches to find more than 60 exposed [[FlockSafety]] cameras.

The episode uses Shodan as discovery infrastructure rather than as the source of the underlying failure. The risk comes from [[SurveillanceCameraExposure]]: devices that are reachable online without adequate authentication can expose live footage, archived footage, and controls to people outside the intended customer or law-enforcement workflow.

## Connections
- [[BenJordan]] - technologist who used Shodan in the source.
- [[FlockSafety]] - camera company whose devices were found exposed.
- [[SurveillanceCameraExposure]] - misconfiguration pattern surfaced by Shodan searches.
- [[SurveillanceAsAService]] - broader vendor-infrastructure model whose devices may become visible if operational controls fail.
- [[CyberDataTheftAndLeakOperations]] - adjacent cybersecurity branch where exposed or stolen data can create downstream harm.
