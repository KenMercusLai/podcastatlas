---
title: "Scale Up AI Interconnect"
type: concept
tags: [ai, networking, semiconductors, data-centers]
sources: [guochan-ai-suanli-neng-ping-chaojiedian-wandao-chaoche-ma-waic-shendu-guancha-s10e23-a6c6ab3e-72b2-470b-aefd-04b19679d37f]
last_updated: 2026-08-07
---

# Scale Up AI Interconnect

Scale Up AI interconnect is the low-latency, high-bandwidth connection layer that lets many AI accelerators operate as one software-visible domain. In [[guochan-ai-suanli-neng-ping-chaojiedian-wandao-chaoche-ma-waic-shendu-guancha-s10e23-a6c6ab3e-72b2-470b-aefd-04b19679d37f]], [[ZhangHaijun]] defines Scale Up less by cabinet boundary and more by whether software can run collective operations such as Reduce and All Gather across the domain as though it were one larger accelerator.

The concept links [[AIClusterNetworking]] to accelerator architecture. Scale Out networking connects many servers or clusters, while Scale Up tries to make the tightly coupled region fast enough that model parallelism and communication-heavy workloads do not leave chips idle.

## Key Claims
- Scale Up is a system and software boundary, not only a physical rack boundary.
- The same supernode can span multiple cabinets if interconnect latency, bandwidth, and software abstraction make it behave as one domain.
- Copper links remain attractive at short range because latency, cost, and power are lower; optical links become more useful across cabinets or longer distances.
- [[Huawei]]'s UB route is framed as a unified protocol attempt across NPU, CPU, storage, Scale Up, and Scale Out, while [[Nvidia]]'s comparison stack uses NVLink and InfiniBand-style layers.
- Interconnect choice affects [[TokenPerWatt]], cooling, model adaptation, and whether a supernode becomes useful capacity.

## Connections
- [[AIAcceleratorSupernode]] — system pattern Scale Up enables.
- [[AIClusterNetworking]], [[MemoryWall]], and [[HighBandwidthMemory]] — data movement and bandwidth context.
- [[HuaweiCM384]], [[NvidiaGB200NVL72]], and [[TPUPodSystemOptimization]] — different pod or supernode-style system cases.
- [[ProprietaryAIInterconnectFragmentation]] — ecosystem risk when each vendor's protocol is different.
