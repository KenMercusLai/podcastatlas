---
title: "System-Level Vehicle Agent Architecture"
type: concept
tags: [automotive, agents, autonomous-driving, ai]
sources:
  - lixiang-luoyonghao-lixiang-de-lixiang-ai-jishu-fuhao-shenghuo-lify6z4xnd4-vt9qqvxv-pccs7fp
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

# System-Level Vehicle Agent Architecture

## Definition
System-level vehicle agent architecture is a design pattern that separates generalized AI tasks, information retrieval, deterministic vehicle control, records, and personalization inside a car rather than routing every user request through one agent.

## Current Synthesis
The current synthesis is a safety-conscious vehicle-agent frame. In response to [[LuoYonghao]]'s desire for deeper car AI, [[LiXiangLiAuto|李想]] says in [[lixiang-luoyonghao-lixiang-de-lixiang-ai-jishu-fuhao-shenghuo-lify6z4xnd4-vt9qqvxv-pccs7fp]] that [[LiAutoL9Levius|L9 LEVIUS]] will use a system-level architecture for five needs: generalized tasks, generalized information access, precise vehicle control, necessary record keeping, and personalization. The important boundary is that not every function should be an agent; high-certainty vehicle control should use more deterministic representations.

## Key Claims
- Vehicle AI should be layered because car control, records, personalization, and open-ended tasks have different risk and latency profiles.
- Agents are useful for generalized tasks but can be inefficient or risky for precise control.
- Knowledge graphs, RAG, and parameterized personalization can coexist with agentic components.
- A car AI assistant becomes a systems problem rather than a single chatbot feature.

## Evidence
- Five needs: [[lixiang-luoyonghao-lixiang-de-lixiang-ai-jishu-fuhao-shenghuo-lify6z4xnd4-vt9qqvxv-pccs7fp]] lists generalized tasks, generalized information acquisition, precise vehicle control, necessary information recording, and personalization.
- Layering rule: [[lixiang-luoyonghao-lixiang-de-lixiang-ai-jishu-fuhao-shenghuo-lify6z4xnd4-vt9qqvxv-pccs7fp]] says vehicle control is better suited to knowledge graphs, records to RAG, and personalization to parameterized processing.
- Product context: [[lixiang-luoyonghao-lixiang-de-lixiang-ai-jishu-fuhao-shenghuo-lify6z4xnd4-vt9qqvxv-pccs7fp]] ties the architecture to L9 LEVIUS delivery.

## Counterevidence & Qualifications
The source explains intended architecture, not shipping behavior. It does not show how safety cases, latency, fallback, privacy, and user override will work in practice.

## What Changed
- Added a vehicle-agent architecture concept from the Li Auto interview.

## Related Concepts
- [[AgenticWorkflow]] - broad agent workflow context.
- [[AgentHarness]] - execution and tool layer for agent systems.
- [[AutonomousDrivingResponsibilityBoundary]] - safety and legal boundary for vehicle autonomy.
- [[HumanAgentCollaboration]] - user-agent interaction context.
- [[LiAutoL9Levius|理想 L9 LEVIUS]] - product where the architecture is promised.
