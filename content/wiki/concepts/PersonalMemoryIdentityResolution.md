---
title: "Personal Memory Identity Resolution / 个人记忆身份解析"
type: concept
tags: [ai, memory, identity, context]
sources:
  - 277-cong-tixing-ni-dao-ti-ni-ban-today-xiang-ba-personal-ai-dai-dao-na-yibu-lub_xekqnxjr6psdo-utmiuig6m6
last_updated: 2026-09-24
knowledge_schema: synthesis-v1
---

# Personal Memory Identity Resolution / 个人记忆身份解析

## Definition
Personal memory identity resolution is the process of determining which person, relationship, and time a captured fact concerns before storing or recalling it as part of a personal AI's memory.

## Current Synthesis
Personal-agent inputs routinely mention multiple people. A health question may concern the user, a child, or a parent; an email or recording can mix the user's preferences with a colleague's statements; an old fact may be true of the same person only at an earlier time. Treating every sentence as a permanent fact about the account owner produces a coherent-looking but false profile.

The Today episode therefore frames memory as structured interpretation rather than accumulation. Identity and time need to travel with the fact, uncertainty should remain visible, and the system must be able to correct, supersede, decay, or delete earlier inferences. Graph-like relationship structure can help represent people, while event sequences need temporal structure; neither storage model eliminates the need for query-time judgment.

## Key Claims
- Personal context often contains facts about people other than the account owner.
- Memory must distinguish event time from capture time and current state from historical state.
- Relationship facts and event sequences may need different representations.
- Uncertain attribution should not silently become a durable user-profile claim.
- Recall must select the right person's information for the current query, not merely retrieve similar text.
- Inspection, correction, deletion, and supersession are necessary recovery mechanisms.

## Evidence
- Person attribution: [[277-cong-tixing-ni-dao-ti-ni-ban-today-xiang-ba-personal-ai-dai-dao-na-yibu-lub_xekqnxjr6psdo-utmiuig6m6]] uses health questions about the user, a child, or parents to show why all remembered information cannot be assigned to one person.
- Temporal attribution: [[277-cong-tixing-ni-dao-ti-ni-ban-today-xiang-ba-personal-ai-dai-dao-na-yibu-lub_xekqnxjr6psdo-utmiuig6m6]] distinguishes when an event happened from when the system recorded it and argues that old preferences must yield to changed state.
- Representation and recall: [[277-cong-tixing-ni-dao-ti-ni-ban-today-xiang-ba-personal-ai-dai-dao-na-yibu-lub_xekqnxjr6psdo-utmiuig6m6]] contrasts relationship graphs with event timelines and discusses dynamic context construction versus model-selected memory infrastructure.
- User recovery: [[277-cong-tixing-ni-dao-ti-ni-ban-today-xiang-ba-personal-ai-dai-dao-na-yibu-lub_xekqnxjr6psdo-utmiuig6m6]] reports that Today exposes recorded memory for deletion and allows all memory to be cleared on exit.

## Counterevidence & Qualifications
The source identifies the problem but does not establish a solved architecture or evaluation benchmark. Graph, timeline, and query-time approaches create latency, compute, cache, and error tradeoffs. User inspection can mitigate mistaken attribution but cannot replace robust defaults, especially when sensitive health, family, workplace, or bystander information is involved.

## What Changed
- Created the concept to separate person-and-time attribution from generic memory storage and retrieval.

## Related Concepts
- [[PersonalAIMemory]] - broader memory system whose facts require identity and temporal attribution.
- [[PersonalAgentUnderstandingLayer]] - interpretation layer that resolves and updates personal evidence.
- [[ContextDecay]] - stale-context failure that identity and time metadata help expose.
- [[IdentityResolutionError]] - broader failure class for merging distinct real-world identities.
- [[AgentPermissionBoundaries]] - limits capture and use of sensitive family, health, and workplace information.
- [[ConsentBasedRecording]] - bystander-consent requirement when memory inputs include other people's speech.
