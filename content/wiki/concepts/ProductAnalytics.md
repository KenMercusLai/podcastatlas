---
title: "Product Analytics"
type: concept
tags: [product, analytics, retention, saas]
sources: [peter-tsr-v3-audio-converted-peter-tsr-v3-audio-converted, tsr-s5-spenserskates-v2audio-tsr-s5-spenserskates-v2audio]
last_updated: 2026-07-25
---

# Product Analytics

Product analytics is the use of behavioral data to understand how people actually use a product, where they retain, and what product decisions should change. [[tsr-s5-spenserskates-v2audio-tsr-s5-spenserskates-v2audio]] adds the concept through [[Amplitude]]'s origin: [[SpenserSkates]] and [[CurtisLiu]] needed to understand why [[Sonalight]] users tried the voice app but did not keep using it.

The source makes product analytics narrower and more operational than generic traffic analytics. The founders wanted to answer whether a successful first voice-recognition match predicted later retention, what cohorts behaved differently, and which product changes could improve behavior. Existing tools such as [[GoogleAnalytics]], [[Flurry]], [[Mixpanel]], [[Kissmetrics]], and [[Adobe]] did not answer those questions in the way the founders needed, so their internal tool became Amplitude.

[[peter-tsr-v3-audio-converted-peter-tsr-v3-audio-converted]] adds [[Segment]] as an adjacent product-analytics infrastructure case. [[PeterReinhardt]] says [[AnalyticsJS|analytics.js]] began as a small routing library for sending [[ClassMetric]] events to tools such as [[Mixpanel]], [[GoogleAnalytics|Google Analytics]], and [[Kissmetrics]], but user demand pointed toward a hosted service that could route behavioral data across many destinations without repeated engineering work.

## Key Claims
- Product analytics is most useful when it answers a decision question rather than only reporting usage counts.
- Retention questions can expose whether the product has a reliability, onboarding, habit, or value problem.
- The same behavioral visibility can become a company when multiple teams recognize the pain and will pay to solve it.
- Product analytics connects [[DataDrivenProductCulture]] to concrete founder decisions: what to fix, whether to pivot, and how to explain value to customers.
- Product analytics infrastructure can also be valuable when it reduces the integration burden around many downstream tools, not only when it supplies dashboards or cohort reports.

## Connections
- [[Amplitude]], [[SpenserSkates]], [[CurtisLiu]], and [[Sonalight]] - source case.
- [[Segment]], [[PeterReinhardt]], [[AnalyticsJS|analytics.js]], [[ClassMetric]], and [[OpenSourceWedge]] - routing-library and hosted-product case added by The Social Radars.
- [[TechnicalDemoRetentionGap]] - failure pattern that created the analytics need.
- [[InternalToolProductization]], [[CustomerEvidenceStrategy]], and [[FounderLedSales]] - path from internal tool to product.
- [[GoogleAnalytics]], [[Flurry]], [[Mixpanel]], [[Kissmetrics]], and [[Adobe]] - named comparison tools.
- [[Zynga]] and [[TwelveGigs|12gigs]] - early market context where the value was legible.
