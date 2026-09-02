---
title: "To-Agent Distribution"
type: concept
tags: [agents, distribution, ai, platforms]
sources:
  - 263-sora-si-le-adobe-die-le-meitu-he-qu-he-cong-lgjmyveooc8wpzr0yviggvzvdyfs
  - ba044533d184-ba044533d184
knowledge_schema: synthesis-v1
last_updated: 2026-09-03
---

# To-Agent Distribution

## Definition
To-agent distribution is the route where products expose content, capabilities, data, or transactions so AI agents can discover and use them on behalf of people or organizations. It sits beside To C and To B distribution: the customer may still be human, but the immediate reader, chooser, or operator can be an agent.

## Current Synthesis
The concept began as a capability-node strategy. A product such as [[Meitu]] can package image and video functions as [[AISkills]] or agent-callable tools so agents invoke the capability inside a wider task flow rather than sending a user to the original app first.

The new source broadens the route from tools to websites and information surfaces. If agents become the first researcher or buyer-facing intermediary, public product pages, documentation, and service descriptions must be complete and retrievable enough for agents to understand them. That makes [[AgentReadableWeb]] a distribution requirement, not only a technical rendering preference.

To-agent distribution has a control tradeoff. Opening content or tools can create incremental demand if agents bring users to a service at the right moment, but it can also weaken the original front door, reduce human page views, and expose data to scraping. Durable versions therefore need [[AgentFacingInterfaces]], [[AgentPaymentInfrastructure]], permission rules, and clear public-versus-protected data boundaries.

## Key Claims
- To-agent distribution turns a product from a destination app into a capability or information source that can be selected during an agent workflow.
- Agent-readable public content can become as important as callable APIs when agents research, compare, summarize, or recommend services.
- The route differs from traditional developer APIs because the agent may invoke the service close to user intent without a third-party developer building a full product first.
- Opening agent access can expand demand, but it can also reduce platform control over attention, ranking, ads, and the front-end session.
- Practical monetization may require per-use fees, bundles, tokens, paid data access, or agent payment mandates rather than only ads or subscriptions.
- Public information should be easy for agents to read, while protected data and high-impact actions need authentication, payment, and permissions.

## Evidence
- Capability-node evidence: [[263-sora-si-le-adobe-die-le-meitu-he-qu-he-cong-lgjmyveooc8wpzr0yviggvzvdyfs]] describes [[Meitu]] packaging image and video capabilities for external agents as a possible route beyond direct consumer apps and enterprise sales.
- Application-layer evidence: [[263-sora-si-le-adobe-die-le-meitu-he-qu-he-cong-lgjmyveooc8wpzr0yviggvzvdyfs]] ties to-agent exposure to [[AIApplicationLayerMoat]], where workflow fit, quality control, and product details can survive model-provider pressure.
- Agent-readable content evidence: [[ba044533d184-ba044533d184]] argues that websites and product descriptions may need fuller information, server-rendered content, or Markdown responses if agents become the first reader.
- Control-tradeoff evidence: [[ba044533d184-ba044533d184]] distinguishes public information that agents should read from data assets that should not simply be exposed to competitors or crawlers.
- Monetization evidence: [[ba044533d184-ba044533d184]] links agent distribution to payment protocols and authenticated tokens when agents call protected services or retrieve paid data.

## Counterevidence & Qualifications
- To-agent distribution is still early; the sources do not prove which interface form, pricing model, or marketplace structure will dominate.
- Some products still need human-facing UI for trust, taste, inspection, social proof, and confirmation.
- Agent access can be blocked by platform incentives when apps depend on dwell time, advertising, data control, or closed transaction flows.
- Being readable or callable by agents does not guarantee recommendation, usage, payment, or durable customer ownership.

## What Changed
- Migrated the page to `synthesis-v1` from the complete prior source set.
- Expanded the concept from packaged tool capabilities to public web content and documentation designed for agent discovery.
- Added payment and authorization as necessary boundaries when to-agent distribution reaches protected data or services.

## Related Concepts
- [[AgentReadableWeb]] - content and rendering pattern that makes public information legible to agents.
- [[AgentFacingInterfaces]] - callable tool, API, CLI, and protocol layer for agent execution.
- [[AISkills]] - procedural packaging that lets agents reuse product capabilities.
- [[AgentPaymentInfrastructure]] - monetization and authorization layer for paid agent access.
- [[AIAssistantServiceEntry]] - user-entry shift when assistants mediate service choice and fulfillment.
- [[AgenticCommerce]] - buying and booking workflows that to-agent distribution can feed.
- [[AIApplicationLayerMoat]] - application defensibility that may improve when workflows become agent-callable.
