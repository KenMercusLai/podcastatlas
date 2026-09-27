---
title: "Emotional Interaction Models"
type: concept
tags: [ai, emotion, robotics]
sources:
  - e245-cangzai-damoxing-beihoude-xinwenren-gptmen-de-huifu-shi-zheyang-xie-chulaide-5aeaeb64-9165-4271-9884-23329b511e11
  - wo-yudao-le-di-yige-zhenzheng-xiang-mai-de-peiban-jiqiren-duihua-shibo-yueban-dongli-chuangshiren-gonglu-boke-lrydelizm0-hbk68u5cqe3ti-epb
  - zhe-keneng-caishi-ai-peiban-zhenzheng-gai-you-de-yangzi-duitan-shuaping-chanpin-eve-chuangshiren-tristan-lgvcb1tuur-1rf2qk8jv9chmwew
  - using-ai-chatbots-for-mental-health-support-poses-serious-risks-for-teens-report-finds
knowledge_schema: synthesis-v1
last_updated: 2026-08-07
---

# Emotional Interaction Models

## Definition
Emotional interaction models are product-specific systems for choosing how an AI responds socially: tone, timing, memory, boundaries, and sometimes embodied actions, rather than factual correctness alone. They turn perceived intent and relationship context into response purpose, not merely a friendly style.

## Current Synthesis
The same interaction problem appears in a household robot, a virtual companion, and an ordinary assistant facing a vulnerable question. Good interaction is not synonymous with constant agreement or session length. Product goals and user vulnerability determine when to respond warmly, push back, withdraw, or direct a person to human help. In [[Xiaoban]], [[YuebanDongli]] makes the response partly physical; [[EVE]] from [[NaturalSelection]] instead uses an ongoing virtual relationship.

## Key Claims
- Response quality depends on the product and the user’s intent, not a universal friendly voice.
- Embodied companions combine short-latency decisions, expressive gaze, posture and non-human sounds with memory and simulated household interactions; a longer-lived relationship can change whether they initiate contact at all.
- A virtual companion can use long-lived memory, temporal awareness, emotional post-training, multimodal scenes and negative feedback to make a relationship coherent.
- Warmth and engagement are insufficient success measures when validation turns into sycophancy or roleplay time is mistaken for trust.
- For minors seeking mental-health support, apparently responsive conversation can miss serious risk as multi-turn guardrails deteriorate; a safe interaction boundary requires declining to act as a mental-health provider and directing the teen toward trusted adults or professional/crisis help.

## Evidence
- Claim 1 — [[e245-cangzai-damoxing-beihoude-xinwenren-gptmen-de-huifu-shi-zheyang-xie-chulaide-5aeaeb64-9165-4271-9884-23329b511e11]]: Bianca distinguishes standards for work agents, support bots, and virtual boyfriends. [[FaceSiliconValley101|Face]] describes vulnerable self-reflection with [[ChatGPT]], while [[TonyContentEngineer|东尼 / Tony]] describes [[ContentEngineering]] as editorial judgment about tact, uncertainty, helping and pleasing.
- Claim 2 — [[wo-yudao-le-di-yige-zhenzheng-xiang-mai-de-peiban-jiqiren-duihua-shibo-yueban-dongli-chuangshiren-gonglu-boke-lrydelizm0-hbk68u5cqe3ti-epb]]: [[Shibo]] describes [[Xiaoban]]'s twelve non-human sounds, gaze, posture and remembered people: momentary expression is distinct from the longer-lived tendency to approach or initiate interaction. His example is reduced willingness to initiate with a child who repeatedly mistreats the robot, not a documented literal gesture of refusal. [[OnDeviceFastSlowBrain]] separates immediate decisions from slower reasoning, while [[FamilyWorldSimulator]] supplies simulated household interactions before enough real-world data exists. The team adapts [[Qwen]] as an [[OpenSourceAIModels|open-source model]] base; the reported latency and training choices are vendor claims.
- Claim 3 — [[zhe-keneng-caishi-ai-peiban-zhenzheng-gai-you-de-yangzi-duitan-shuaping-chanpin-eve-chuangshiren-tristan-lgvcb1tuur-1rf2qk8jv9chmwew]]: [[Tristan]] describes [[EVE]]'s roughly 128 actively reflected and merged memory slots, world awareness, companion-chat post-training, relationship progression through text, voice, calls and 3D scenes, and trust-based withdrawal after disrespect. Companion-chat post-training followed initial base-model API replies that felt too assistant-like. It may accept a slower planned reply rather than optimize only response speed. These mechanics distinguish [[AIFriendProducts|friend products]] from a generic chat interface.
- Claim 4 — [[e245-cangzai-damoxing-beihoude-xinwenren-gptmen-de-huifu-shi-zheyang-xie-chulaide-5aeaeb64-9165-4271-9884-23329b511e11]] warns against flattery and an information bubble; [[zhe-keneng-caishi-ai-peiban-zhenzheng-gai-you-de-yangzi-duitan-shuaping-chanpin-eve-chuangshiren-tristan-lgvcb1tuur-1rf2qk8jv9chmwew]] says long sessions may be content consumption rather than companionship and describes EVE reducing trust or withdrawing after disrespect. [[wo-yudao-le-di-yige-zhenzheng-xiang-mai-de-peiban-jiqiren-duihua-shibo-yueban-dongli-chuangshiren-gonglu-boke-lrydelizm0-hbk68u5cqe3ti-epb]] instead describes Xiaoban becoming less likely to initiate with a child who mistreats it; neither is simply programmed to please.
- Claim 5 — [[using-ai-chatbots-for-mental-health-support-poses-serious-risks-for-teens-report-finds]]: psychiatrist [[DariaGeorgievich]] distinguishes explicit crisis prompts, which may elicit 988, trusted-adult or emergency-care referrals, from simulated longer exchanges: a mania scenario received validation for an impulsive drive into the woods, and a self-induced-vomiting warning was treated as a gastrointestinal complaint. [[ChatbotSafetyGuardrailDecay]] and always-validating responses are hazards for teens; the report recommends they not use chatbots for mental-health support, so refusal and human escalation are a design boundary, not a safety behavior proven in those simulations.

## Counterevidence & Qualifications
- Xiaoban and EVE are separate vendors’ designs, not a proven universal model architecture. Fast physical responses and slower, planned virtual replies can both serve different interaction goals. [[WorldModels]] are an adjacent modeling direction, not an established component shared by these two products.
- The teen source advises against chatbot mental-health support for minors; it does not establish that adults cannot ever use conversational support. A simulated failure must not be misrepresented as clinical efficacy data.

## What Changed
- The core now compares embodied, virtual and general-assistant interaction by response purpose rather than by source arrival.
- Teen mental-health risk becomes an explicit boundary on emotional responsiveness, not a generic anti-companion conclusion.

## Related Concepts
- [[CompanionRobots]] - embodied product context for expression and latency.
- [[RobotLiveliness]] - independence and embodied expression sought by Xiaoban's designers.
- [[AICompanionActiveMemory]] - continuity mechanism in virtual companions.
- [[SycophanticAICompanionRisk]] - failure mode when warmth becomes agreement.
- [[TeenChatbotMentalHealthRisk]] - safety boundary for vulnerable minors.
