---
title: "Threat-Channel Blindness"
type: concept
tags: [cybersecurity, risk, threat-modeling, geopolitics]
sources:
  - the-sony-hack-the-mistakes-series-the-sony-hack-the-mistakes-series
last_updated: 2026-11-15
knowledge_schema: synthesis-v1
---

# Threat-Channel Blindness

## Definition

Threat-channel blindness is the failure to evaluate an adversary's credible means of retaliation because risk analysis concentrates on a more familiar channel such as physical violence, legal action, or conventional military force.

## Current Synthesis

In [[the-sony-hack-the-mistakes-series-the-sony-hack-the-mistakes-series]], [[MichaelLynton]] sought expert advice after threats concerning [[TheInterviewFilm|The Interview]]. He reports being told that [[NorthKorea]] lacked a meaningful way to harm [[SonyPictures]], but his own interpretation focused chiefly on physical retaliation while the state possessed substantial cyber capability. The resulting lesson is not that expert advice is useless; it is that both the question and the answer must enumerate channels rather than treat “can they hurt us?” as a single undifferentiated judgment.

Threat modeling should separate actor, motive, access, capability, target surface, and consequence across physical, cyber, legal, economic, information, and proxy routes. Low confidence in one route does not transfer automatically to the others.

## Key Claims

- Threat likelihood must be assessed separately for each plausible channel of action.
- Familiarity with physical security can conceal cyber exposure even when the same adversary is being discussed.
- Expert confidence is only as useful as the threat categories and assumptions included in the question.
- State actors can impose asymmetric harm without matching the target in conventional power.
- Warnings should trigger adversarial capability mapping, not only literal interpretation of the most visible threat.
- Attribution uncertainty does not remove the value of closing channel-specific defensive gaps.

## Evidence

### Physical frame versus cyber capability

- [[the-sony-hack-the-mistakes-series-the-sony-hack-the-mistakes-series]] reports that Lynton understood retaliation mainly as physical harm while North Korea had meaningful cyber capability.

### Expert advice boundary

- [[the-sony-hack-the-mistakes-series-the-sony-hack-the-mistakes-series]] reports that consulted RAND Corporation and U.S. State Department experts discounted the threats, yet the supplied account does not show whether cyber scenarios were explicitly tested.

### Asymmetric consequence

- [[the-sony-hack-the-mistakes-series-the-sony-hack-the-mistakes-series]] describes a remote attack that disabled systems, exposed confidential information, and disrupted distribution without physical assault on the studio.

## Counterevidence & Qualifications

The supplied file does not provide the experts' wording, scope, assumptions, or response, so it cannot establish that they ignored cyber risk rather than that their advice was misunderstood, compressed, or overtaken by later events. It also does not independently establish attribution or show which defensive measures could have prevented the breach. The concept is a planning discipline, not proof that every threat is credible across every channel.

## What Changed

- Created a channel-specific threat-modeling concept from the Sony case.
- Distinguished expert error from question-framing, interpretation, and retrospective compression.

## Related Concepts

- [[StateCyberActorThreatModel]] - broader classification of state, criminal, and activist capabilities and motives.
- [[DecisionGuardrailBypass]] - earlier governance failure that prevented full geopolitical review.
- [[SchemaContextMismatch]] - parallel case of a familiar frame being applied to the wrong context.
- [[SonyPicturesHack2014]] - cyberattack illustrating remote asymmetric harm.
