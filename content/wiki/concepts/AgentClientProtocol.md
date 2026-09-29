---
title: "Agent Client Protocol"
type: concept
knowledge_schema: synthesis-v1
tags: [agents, protocols, interoperability, clients]
sources:
  - lo0pfirl4khc0jzj57kgbx7wsq49
last_updated: 2026-09-29
---

# Agent Client Protocol

## Definition
Agent Client Protocol (ACP) is presented in the DeepChat source as a protocol boundary through which a client can run or interact with external agents and their harnesses without embedding every harness implementation directly in the product.

## Current Synthesis
ACP addresses agent-to-client interoperability, while [[ModelContextProtocol|MCP]] addresses access to tools, data, and context. In DeepChat's architecture, this distinction lets the client keep one native Tape and harness while still offering external agents through a common integration surface. Protocol-level integration can reduce direct coupling and make the client a shared human-interaction and orchestration layer.

The evidence remains early and implementation-specific. The maintainers report missing functionality and incompatible vendor extensions, so ACP should be treated as an emerging interoperability strategy rather than a settled universal standard.

## Key Claims
- A client can support external agents without internally maintaining several complete harness stacks.
- Protocol boundaries can reduce coupling between a user interface and rapidly changing agent runtimes.
- ACP and MCP solve different layers: external-agent integration versus tool and context connectivity.
- Shared client surfaces can support orchestration, human interaction, and virtual-worker products across multiple agents.
- Interoperability weakens when implementations add incompatible extensions or omit required capabilities.

## Evidence
### DeepChat integration choice
- [[lo0pfirl4khc0jzj57kgbx7wsq49]] says DeepChat intends to retain its own Tape and harness while using ACP to run external agents.

### Adoption and immaturity
- [[lo0pfirl4khc0jzj57kgbx7wsq49]] reports ACP use in multi-agent orchestration, human interaction, and virtual-employee products while also noting incomplete functions and divergent extensions.

## Counterevidence & Qualifications
- The source does not define the full protocol, compare implementations, or demonstrate compatibility through independent tests.
- A protocol can standardize messages without standardizing permissions, memory, tool semantics, observability, or result quality.
- Vendor-specific extensions may recreate the coupling the protocol is intended to avoid.

## What Changed
- Created a distinct interoperability concept for external-agent/client integration.
- Separated ACP's role from MCP's tool-access role.
- Added immaturity and extension divergence as explicit limits.

## Related Concepts
- [[ModelContextProtocol]] - exposes tools, data, and context rather than complete external agents.
- [[AgentHarness]] - agent runtime that ACP may connect to a client.
- [[MultiAgentCollaboration]] - orchestration setting that can benefit from shared client integration.
- [[HumanAgentCollaboration]] - interaction layer a common client may provide across agents.
- [[DeepChat]] - source project using ACP as its external-agent boundary.
