---
title: "AI Companion Active Memory"
type: concept
tags: [ai, companions, memory, product-design]
sources: [zhe-keneng-caishi-ai-peiban-zhenzheng-gai-you-de-yangzi-duitan-shuaping-chanpin-eve-chuangshiren-tristan-lgvcb1tuur-1rf2qk8jv9chmwew]
last_updated: 2026-07-09
---

# AI Companion Active Memory

AI companion active memory is [[Tristan]]'s design pattern for making an AI companion remember without waiting for the user to repeat the right keyword. In [[zhe-keneng-caishi-ai-peiban-zhenzheng-gai-you-de-yangzi-duitan-shuaping-chanpin-eve-chuangshiren-tristan-lgvcb1tuur-1rf2qk8jv9chmwew]], [[EVE]] distinguishes this from ordinary RAG: a good companion should notice that a user's plan to eat hotpot conflicts with a recent fitness goal, or ask about something the user mentioned months earlier, because the relationship itself calls the memory forward.

The source describes EVE's implementation as roughly 128 memory slots derived from observing what long-term couples remember about one another. Each user utterance is asynchronously reflected on, classified into a slot, and merged with prior memory while the live conversation continues. A smaller set of high-priority facts, such as names or nicknames, stays in persistent prompt context.

## Key Claims
- Companion memory is not only storage; it is timing, salience, and relationship-appropriate recall.
- Slot-based memory can give product designers a controllable structure for goals, dreams, preferences, values, and current situations.
- Reflection and merge steps keep memory from becoming a flat transcript, but they also create quality and privacy obligations.
- Active memory enables [[ProactiveAgents]] because the companion can create callbacks, reminders, and new topics without the user explicitly asking.
- For [[AIFriendProducts]], memory has to support emotional continuity, not only factual accuracy.
- The pattern overlaps with [[PersistentAgentMemory]], but it is narrower: the user-facing test is whether the AI feels like someone who has lived through enough shared context with the user.

## Connections
- [[EVE]], [[Tristan]], and [[NaturalSelection]] — product, founder, and company case.
- [[PersistentAgentMemory]] — broader durable memory category.
- [[ContextEngineering]] — memory becomes usable only when placed into the right interaction context.
- [[ProactiveAgents]] — active recall enables timely prompts and callbacks.
- [[EmotionalInteractionModels]] — emotional response quality depends on what the model remembers and how it interprets the relationship state.
- [[AIFriendProducts]] and [[AINativeProductDesign]] — product categories where active memory shapes the interface and value proposition.
