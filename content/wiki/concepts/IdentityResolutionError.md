---
title: "Identity Resolution Error"
type: concept
tags: [privacy, data, matching, surveillance, bias]
sources:
  - default-mp3-ywr3ahjkcgo-8eb9e254581eaa220d9428df389214d5-27844515-default-mp3-ywr3ahjkcgo-8eb9e254581eaa220d9428df389214d5-27844515
last_updated: 2026-09-06
knowledge_schema: synthesis-v1
---

# Identity Resolution Error

## Definition
Identity resolution error is the failure mode where a data system links records, photos, names, locations, or attributes to the wrong person while still producing an actionable-looking profile.

## Current Synthesis
The Palantir dating event shows identity resolution error as both a data-quality problem and a privacy problem. Jeannie Chan predicts that her common name and a same-name professional in New York may confuse the system; the event then displays incorrect photos and an incorrect Indonesia Ministry of Agriculture connection. The episode's lesson is not simply that matching can be wrong, but that wrong matches can still create exposure, embarrassment, suspicion, or downstream decisions.

## Key Claims
- Common names, shared cities, similar occupations, and weak identifiers can cause data profiles to merge multiple people.
- A profile can feel invasive even when it is wrong because the person is still publicly associated with claims they did not make.
- Facial recognition can compound identity error, especially where the source notes that recognition systems have poorer performance for people of color.
- Error does not neutralize surveillance risk; a wrong profile may still be believed by an audience or later user.
- Identity-resolution failures are harder to correct when people do not know which databases or enrichment tools produced the match.

## Evidence
- Jeannie's prediction - [[default-mp3-ywr3ahjkcgo-8eb9e254581eaa220d9428df389214d5-27844515-default-mp3-ywr3ahjkcgo-8eb9e254581eaa220d9428df389214d5-27844515]] says Jeannie expected identification problems because a same-name, same-city, similar-profession person existed.
- Incorrect profile - [[default-mp3-ywr3ahjkcgo-8eb9e254581eaa220d9428df389214d5-27844515-default-mp3-ywr3ahjkcgo-8eb9e254581eaa220d9428df389214d5-27844515]] says the displayed Ministry of Agriculture connection and photos were not hers.
- Facial recognition qualification - [[default-mp3-ywr3ahjkcgo-8eb9e254581eaa220d9428df389214d5-27844515-default-mp3-ywr3ahjkcgo-8eb9e254581eaa220d9428df389214d5-27844515]] notes the host's point that facial recognition software is notoriously poor at recognizing people of color.
- Social exposure - [[default-mp3-ywr3ahjkcgo-8eb9e254581eaa220d9428df389214d5-27844515-default-mp3-ywr3ahjkcgo-8eb9e254581eaa220d9428df389214d5-27844515]] stages the error publicly during a dating match, making the mismatch socially consequential.

## Counterevidence & Qualifications
The episode provides a vivid case, not a statistical evaluation of identity-resolution systems. The page should treat Jeannie's example as a mechanism demonstration rather than proof of error rates across every matching product.

## What Changed
- Created a concept for the false-positive matching risk surfaced by the dating-event source.

## Related Concepts
- [[DataOperationalization]] - upstream process that can make identity links actionable.
- [[CrossDatasetPrivacyLinkage]] - mechanism through which weak identifiers become stronger or more misleading.
- [[ConsentlessFacialSearch]] - adjacent photo-search pathway that can worsen identity errors.
- [[AIRecognitionBias]] - related computer-vision bias concept.
- [[CivilLibertiesSurveillanceRisk]] - broader consequence when wrong matches enter enforcement or public-decision contexts.
