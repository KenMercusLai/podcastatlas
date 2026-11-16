---
title: "Delegated AI Agent Consent"
type: concept
tags: [ai-agents, consent, authorization, privacy, platform-access]
sources:
  - tech-20261116-1116-mp-tech-pod-128-tech-20261116-1116-mp-tech-pod-128
last_updated: 2026-11-16
knowledge_schema: synthesis-v1
---

# Delegated AI Agent Consent

## Definition
Delegated AI agent consent is the unresolved question of when an AI agent may validly accept data, privacy, access, or transaction terms on a person's behalf and when a website may reject or constrain that delegation.

## Current Synthesis
An agent can mechanically click or transmit assent, but legally and practically meaningful consent requires more: attributable user authority, understandable scope, current intent, records, revocation, and a way to distinguish authorized agents from bots or adversaries. [[tech-20261116-1116-mp-tech-pod-128-tech-20261116-1116-mp-tech-pod-128]] introduces the issue without resolving it, noting both the possibility of agent-provided consent and businesses' existing interest in restricting agent access.

## Key Claims
- Mechanical acceptance by an agent does not alone establish informed or authorized user consent.
- Delegation needs a traceable link among the user, agent, requested action, data practice, and applicable terms.
- Consent scope should be limited by purpose, time, resource, and revocability rather than treated as blanket authority.
- Platforms have legitimate security and policy interests in identifying or restricting agents, but broad bans can also prevent users from exercising delegated choice.
- Privacy notices designed for human reading may not provide a reliable machine-actionable basis for agent decisions.

## Evidence
- Emerging legal question - [[tech-20261116-1116-mp-tech-pod-128-tech-20261116-1116-mp-tech-pod-128]] asks whether agents acting online can consent for users.
- Platform boundary - [[tech-20261116-1116-mp-tech-pod-128-tech-20261116-1116-mp-tech-pod-128]] reports Goldman saying that businesses are already restricting agents and names Amazon and Williams-Sonoma as examples.
- Privacy setting - [[tech-20261116-1116-mp-tech-pod-128-tech-20261116-1116-mp-tech-pod-128]] ties the question to consent for analytics and targeted advertising rather than only purchasing or enterprise access.

## Counterevidence & Qualifications
The episode raises the agent-consent problem only briefly. It does not identify a governing doctrine, technical standard, company policy text, court ruling, identity mechanism, or tested consent interface. The concept therefore states requirements and tensions as a synthesis boundary, not as settled law or proof that named companies impose identical restrictions.

## What Changed
- Established privacy and advertising consent as a distinct branch of delegated agent authority.

## Related Concepts
- [[AgentPermissionBoundaries]] - defines the maximum authority an agent may exercise for a user.
- [[ContextualAgentAuthorization]] - evaluates whether a particular action is authorized in its current context.
- [[VideoPrivacyProtectionAct]] - live privacy setting in which delegated consent becomes relevant.
- [[AgentReadableWeb]] - technical-access model that must coexist with authorization and site policy.
