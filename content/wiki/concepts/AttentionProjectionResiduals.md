---
title: "Attention Projection Residuals"
type: concept
tags: [ai, model-architecture, attention]
sources: [151-17sui-bei-2026-nian-icml-shoulu-lunwen-de-xiao-shaonian-wo-bet-kaixin-kaixin-kaixin-lgs-qedm2hdrxrfkgnsphg4i5h5u]
last_updated: 2026-08-24
---

# Attention Projection Residuals

Attention projection residuals are the source-scoped model-architecture idea [[SuTinghao|苏廷昊]] describes in [[151-17sui-bei-2026-nian-icml-shoulu-lunwen-de-xiao-shaonian-wo-bet-kaixin-kaixin-kaixin-lgs-qedm2hdrxrfkgnsphg4i5h5u]]. Starting from value residual learning, he says he added normalization on residual paths, extended the residual idea from value to key and query projections, and widened the first-layer attention projection so one split serves the current layer while another split carries information forward.

The source distinguishes this from [[AttentionResidues]] in [[KimiK3|Kimi K3]]. Su treats his approach as related attention-depth information flow, but he is cautious about claiming more than his own scale demonstrates. The page should therefore be read as an episode-grounded research note rather than a full technical report.

## Key Claims
- The mechanism tries to preserve early-layer attention projection information across later layers.
- The source's described change is projection-specific: value, key, and query pathways matter, not only the ordinary residual stream.
- The proposed first-layer width split creates a separation between current-layer computation and residual information reserved for later layers.
- The evidence level is source-scoped because the podcast summary does not include paper tables, ablations, or reproduction details.
- The idea connects to the broader shift where [[TransformerArchitecture|Transformer]] variants modify attention, residuals, cache behavior, and training stability while still remaining Transformer-adjacent.

## Connections
- [[SuTinghao]] and [[InternationalConferenceOnMachineLearning|ICML 2026]] — source researcher and publication venue.
- [[TransformerArchitecture]], [[AttentionResidues]], and [[KimiDeltaAttention]] — adjacent attention-architecture branch.
- [[AIResearchFeedbackCompression]] and [[ResearchTaste]] — experiment loop and judgment context.
- [[AINativeYouthResearch]] — youth-research pathway that produced the source-scoped idea.
