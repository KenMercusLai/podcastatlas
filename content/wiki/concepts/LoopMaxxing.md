---
title: "Loop Maxxing"
type: concept
tags: [ai, workflow, reasoning, agents]
sources: [all-in-with-chamath-jason-sacks-friedberg-open-source-wins-agi-is-here-and-scorseses-ai-toolkit-with-ceos-of-cerebras-black-forest-labs-42029880]
last_updated: 2026-08-20
---

# Loop Maxxing

Loop maxxing is [[JasonCalacanis|Jason Calacanis]]'s phrase in [[all-in-with-chamath-jason-sacks-friedberg-open-source-wins-agi-is-here-and-scorseses-ai-toolkit-with-ceos-of-cerebras-black-forest-labs-42029880]] for repeatedly feeding AI outputs back into an AI workflow. [[AndrewFeldman|Andrew Feldman]] treats the pattern as a possible source of recursive improvement: ask, learn from the answer, ask again, and continue until the answer improves or the loop plateaus.

The concept extends [[TokenMaxxing]] but changes the bottleneck. Instead of only spending more tokens, the user creates iterative reasoning loops that also require evaluation, stopping rules, model routing, and human judgment about whether the loop is discovering signal or amplifying error.

## Key Claims
- Recursive prompting can produce better answers when each pass introduces new checks, sources, decompositions, or questions.
- Loop value depends on verification because repeated generations can also reinforce weak assumptions.
- Faster inference makes loops more practical by reducing waiting time across many serial calls.
- The economic question is not just token volume; it is whether the loop produces accepted work, better decisions, or a solved task.

## Connections
- [[TokenMaxxing]] and [[UnlimitedTokenWorkflow]] - abundant-token and usage-growth context.
- [[AIInferenceCostStructure]] and [[LowLatencyInferenceChip]] - cost and latency constraints behind recursive workflows.
- [[ModelRoutingCostControl]] - choosing which model should handle each loop stage.
- [[RecursiveSelfImprovement]] - adjacent stronger claim about model or system self-improvement.
- [[AIVerification]] and [[HumanJudgmentUnderAI]] - review and stopping-rule requirements.
