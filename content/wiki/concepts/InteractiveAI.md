---
title: "Interactive AI / 交互式人工智能"
type: concept
tags: [ai, voice, multimodal, interaction]
sources:
  - lhhxptqoanrsmgih0htfelq-znbg-lhhxptqoanrsmgih0htfelq-znbg
last_updated: 2026-11-16
knowledge_schema: synthesis-v1
---

# Interactive AI / 交互式人工智能

## Definition

Interactive AI is a system designed for continuous, interruptible exchange, updating its perception and response as a person pauses, adds information, changes direction, or speaks over it.

## Current Synthesis

[[lhhxptqoanrsmgih0htfelq-znbg-lhhxptqoanrsmgih0htfelq-znbg]] distinguishes three routes: native full-duplex multimodal models that repeatedly read input and decide whether to emit output; turn-based audio models that preserve direct speech input and output but remain conversationally sequential; and modular cascades linking voice activity detection, ASR, an LLM, and TTS. These routes are likely to coexist because native interaction can reduce interface seams while cascades allow independent module replacement, debugging, and control. Product quality still depends on latency and output selection: a model trained to produce long coding answers may be a poor voice assistant, and asking a reasoning-heavy model to decide what TTS should read can make interaction too slow.

## Key Claims

- Natural interaction requires continuous input processing and interruption handling, not merely audio input and output.
- Native full-duplex, turn-based audio, and cascaded systems make different latency and modularity tradeoffs.
- Voice output should often summarize or select information rather than read every visible token.
- Stronger reasoning can improve tool selection while violating real-time response expectations.
- Model capability does not remove interaction design; it relocates the bottleneck.

## Evidence

### Architecture alternatives
- [[lhhxptqoanrsmgih0htfelq-znbg-lhhxptqoanrsmgih0htfelq-znbg]] describes native roughly 200-millisecond input polling, direct turn-based audio, and VAD-ASR-LLM-TTS cascades.

### Product bottlenecks
- [[lhhxptqoanrsmgih0htfelq-znbg-lhhxptqoanrsmgih0htfelq-znbg]] uses weather output and TTS tool-calling experiments to show why screen content, spoken content, reasoning delay, and turn timing cannot be treated as identical.

## Counterevidence & Qualifications

- The source provides a practitioner taxonomy, not controlled comparative latency, quality, interruption, or user-satisfaction results.
- The three routes can be hybridized, so the categories are design poles rather than permanent market boundaries.
- Always-listening or multimodal systems introduce privacy and consent questions not developed in detail by this episode.

## What Changed

- Added a three-route architecture map and made selective spoken output a first-class product constraint.

## Related Concepts

- [[VoiceInteraction]] - broader voice-interface and conversational modality context.
- [[VoiceInputWorkflow]] - speech-first composition and contextual correction rather than full assistant dialogue.
- [[AgentFacingInterfaces]] - interaction surfaces through which people direct and inspect AI systems.
- [[HumanAgentCollaboration]] - requires interruption, clarification, handoff, and shared control.
- [[ModelHarnessCoEvolution]] - connects model behavior to the surrounding real-time tools and orchestration.
