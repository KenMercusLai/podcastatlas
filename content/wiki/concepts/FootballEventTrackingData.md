---
title: "Football Event and Tracking Data"
type: concept
tags: [football, data, computer-vision, analytics]
sources: [ep-12-insightful-conversation-with-a-football-analytics-professional]
last_updated: 2026-08-18
---

# Football Event and Tracking Data

Football event and tracking data is the structured and semi-structured record of what happens on and off the ball during a match. In [[ep-12-insightful-conversation-with-a-football-analytics-professional]], [[AnnaDSouza|Anna D'Souza]] describes football technology through video/data tools, JSON files, text files, event data, tracking data, and unstructured sports data.

The source distinguishes on-ball and off-ball information. On-ball events may be manually tagged or derived from event feeds, while off-ball activity can require computer vision and tracking systems. Machine-learning techniques can help synchronize event data with tracking data so analysts can connect actions, positions, movement, and game context.

The concept links applied football analytics to both scouting and modeling. It can support [[DataDrivenFootballScouting]] by making player actions comparable, while also supporting [[SportsPredictiveModeling]] through richer variables for match, possession, counterattack, or penalty analysis.

## Key Claims
- Football analytics depends on event and tracking data that are often messy before analysis.
- On-ball and off-ball information require different collection and synchronization methods.
- Computer vision can help capture off-ball movement that ordinary event data misses.
- Data formats such as JSON, text files, event feeds, and video-derived records become part of the analyst's everyday work.
- Synchronization work can be as important as the downstream model because mismatched data can distort the football question.

## Connections
- [[AnnaDSouza]], [[SportsAnalytics]], and [[FootballAnalyticsModernization]] - source and domain context.
- [[StatsBomb]] and [[FIFA]] - organizations named in the source around data and ML examples.
- [[SportsOfficiatingAutomation]] - adjacent technology branch through referee and tracking systems.
- [[DataDrivenFootballScouting]], [[SportsPredictiveModeling]], and [[AthleteDataPrivacyGovernance]] - scouting, modeling, and governance uses.
