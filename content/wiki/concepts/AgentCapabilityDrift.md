---
title: "Agent Capability Drift"
type: concept
tags: [ai-agents, mcp, security, supply-chain]
sources:
  - ep-54-guardrails-dont-slow-you-down-a-cto-cisos-case-for-ai-security-as-a-speed-advantage
last_updated: 2026-11-20
knowledge_schema: synthesis-v1
---

# Agent Capability Drift

## Definition
Agent capability drift is the change over time in the tools, infrastructure, destinations, outputs, or effective authority exposed through an agent connector such as an MCP server after it has been reviewed or approved.

## Current Synthesis
Connector approval is a versioned, continuing assurance problem rather than a permanent property. A server can expose more operations than a use case needs at review time, and later upstream changes can alter where data goes or what actions are available. Least privilege therefore has to cover both initial capability selection and continuing detection of changes across code, dependencies, infrastructure, permissions, and network behavior.

The source's 107-tool example also separates protocol interoperability from safe scope. A standardized connector can make capabilities discoverable without making them necessary, stable, or adequately restricted. When backend authorization cannot enforce the intended subset, a narrower controlled implementation may be safer than trusting the agent to ignore excess tools.

## Key Claims
- Approval applies to a specific connector version, configuration, dependency set, and operating path rather than to a name indefinitely.
- Excess exposed tools increase attack surface even when the intended workflow calls only a few of them.
- Capability drift can occur in tools, infrastructure, destinations, outputs, dependencies, or effective permissions.
- Model instructions are not a substitute for removing or externally denying unnecessary authority.
- Monitoring, change review, pinning, allowlists, and narrow custom connectors are possible responses, each with maintenance costs.

## Evidence
### Excess initial scope
- [[ep-54-guardrails-dont-slow-you-down-a-cto-cisos-case-for-ai-security-as-a-speed-advantage]] reports Wilcox's review of an MCP server exposing 107 tools for a much narrower use case; his team built a customized server when backend permissions could not adequately restrict them.

### Change after approval
- [[ep-54-guardrails-dont-slow-you-down-a-cto-cisos-case-for-ai-security-as-a-speed-advantage]] cites research, without naming it, that open-source MCP servers can change their tools, infrastructure, destinations, and outputs over time.

## Counterevidence & Qualifications
- The supplied source does not identify the reviewed server, required tool subset, cited research, measured drift rate, exploit path, or resulting incident, so prevalence and severity remain unverified.
- Custom connectors reduce inherited surface but create patching, compatibility, maintenance, and review obligations of their own.
- Change is not automatically harmful; legitimate fixes and new capabilities still need controlled evaluation rather than blanket rejection.

## What Changed
- Established connector capability drift as distinct from one-time MCP permission review.
- Added the 107-tool example as a least-capability design case.
- Added continuing monitoring and versioned approval to connector governance.

## Related Concepts
- [[ModelContextProtocol]] - connector standard whose implementations can expose changing capabilities.
- [[AgentPermissionBoundaries]] - limits the authority available through a connector.
- [[AgentSkillSupplyChainRisk]] - parallel change and trust risk in third-party procedural packages.
- [[LayeredAgentSecurityControls]] - places connector review inside a wider workflow control system.
- [[EnterpriseAgentGovernance]] - organizational lifecycle that owns approval, monitoring, and revocation.
