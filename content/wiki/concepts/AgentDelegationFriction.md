---
title: "Agent Delegation Friction / 智能体委托摩擦"
type: concept
tags: [ai, agents, product-design, delegation]
sources:
  - 277-cong-tixing-ni-dao-ti-ni-ban-today-xiang-ba-personal-ai-dai-dao-na-yibu-lub_xekqnxjr6psdo-utmiuig6m6
  - yi-ge-personal-agent-chuangyezhe-de-sikao-duitan-ambi-chuangshiren-zihao-lkr2rf-l-ft-p-i6f-tay5vlnt6e
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

# Agent Delegation Friction / 智能体委托摩擦

## Definition
Agent delegation friction is the explanation, configuration, supervision, confirmation, and correction effort a user must spend before an AI agent can complete a task well enough that delegation is cheaper than doing it personally.

## Current Synthesis
The Today episode argues that many small tasks remain undelegated not because an agent cannot perform their individual steps, but because the user must restate preferences, relationships, schedules, history, and desired style each time. [[PersonalAIMemory|Long-term memory]] can lower that setup cost, while a [[PersonalAgentUnderstandingLayer|personal understanding layer]] determines which retained facts actually matter now.

Lower friction does not mean removing all confirmation. The useful design target is risk-adjusted delegation: prepare or complete low-impact, familiar work with little interruption; ask when identity, intent, money, health, external communication, or irreversible consequences are uncertain. An agent creates negative value when its reminders, verbose explanations, generated to-do lists, or coordination demands add more work than the task it removes.

The Ambi interview extends the cost model beyond digital setup. If the user must find a device, open an app, wake the assistant, and restate a conversation or physical situation the system could already know, useful but infrequent needs may never become expressed demand. Ambient access can lower that threshold, but continuous capture is not free: privacy, false triggers, battery, inference cost, and socially necessary confirmation remain part of the total delegation cost.

## Key Claims
- Delegation is worthwhile only when explanation and supervision cost less than direct completion.
- Persistent, current context can reduce repeated briefing for recurring small tasks.
- Generated plans and reminders can increase friction when they leave all execution to the user.
- Confirmation should vary with consequence, uncertainty, learned authorization, and reversibility.
- One continuous front agent can reduce context-management burden even when specialists work behind it.
- Concise result delivery matters because excess output consumes attention after the task is done.
- Interface access and context restatement are delegation costs, not merely usability details.

## Evidence
- Repeated-briefing cost: [[277-cong-tixing-ni-dao-ti-ni-ban-today-xiang-ba-personal-ai-dai-dao-na-yibu-lub_xekqnxjr6psdo-utmiuig6m6]] says conventional agents often require enough background that users prefer to finish small tasks themselves.
- Memory mechanism: [[277-cong-tixing-ni-dao-ti-ni-ban-today-xiang-ba-personal-ai-dai-dao-na-yibu-lub_xekqnxjr6psdo-utmiuig6m6]] links learned contacts, preferences, relationships, and ongoing goals to lower-cost scheduling, messaging, research, and long-term support.
- Execution boundary: [[277-cong-tixing-ni-dao-ti-ni-ban-today-xiang-ba-personal-ai-dai-dao-na-yibu-lub_xekqnxjr6psdo-utmiuig6m6]] contrasts producing more to-do items with completing executable work and leaving the user mainly to verify results.
- Attention cost: [[277-cong-tixing-ni-dao-ti-ni-ban-today-xiang-ba-personal-ai-dai-dao-na-yibu-lub_xekqnxjr6psdo-utmiuig6m6]] treats excessive model speech and poorly timed initiative as additional cognitive burden rather than service.
- Ambient-access cost: [[yi-ge-personal-agent-chuangyezhe-de-sikao-duitan-ambi-chuangshiren-zihao-lkr2rf-l-ft-p-i6f-tay5vlnt6e]] argues that app opening, wake-up, repeated context, and operational steps suppress even valuable low-frequency requests.
- Trigger-cost boundary: [[yi-ge-personal-agent-chuangyezhe-de-sikao-duitan-ambi-chuangshiren-zihao-lkr2rf-l-ft-p-i6f-tay5vlnt6e]] contrasts meaningful environmental triggers with costly repeated scans and low-relevance proactive alerts.

## Counterevidence & Qualifications
The sources supply product frameworks, not measured delegation-cost or completion-rate data. Long-term memory and ambient sensing can reduce briefing while increasing privacy, bystander, misattribution, stale-context, and overreach risks. Some tasks remain faster to do manually, and consequential tasks may rationally require more explanation or confirmation even when that preserves friction. Removing visible user effort can also shift cost into battery, inference, review, recovery, or surveillance rather than eliminate it.

## What Changed
- Expanded delegation cost from briefing and supervision to access, wake-up, context restatement, and trigger quality.
- Added the boundary that invisible compute, privacy, and recovery costs still count even when interaction becomes easier.

## Related Concepts
- [[PersonalAIMemory]] - retained context that can reduce repeated briefing.
- [[PersonalAgentUnderstandingLayer]] - selects the retained context relevant to the current task.
- [[AgentTrustCalibration]] - determines how autonomy can expand after reliable performance.
- [[AgentPermissionBoundaries]] - preserves necessary friction for risky or consequential action.
- [[ProactiveAgents]] - can reduce or increase friction depending on timing and relevance.
- [[MultiAgentCollaboration]] - hidden specialization can help, while visible coordination can shift management work back to the user.
- [[AmbientAIInterface]] - can lower access and context-restatement cost while increasing continuous-sensing risk.
- [[EnvironmentTriggeredAgentProactivity]] - event-based trigger design intended to reduce speculative scanning and interruption.
