---
title: "EP 5: Implementation of Data Science in Cybersecurity"
type: source
tags: [podcast, data-science, cybersecurity, fraud]
sources: []
date: 2022-12-26
source_file: "/home/ken/repos/podcastatlas/content/episodes/7C45399A1138EF35D358938E12EE81BB~8584441_2026-08-10-210741-8787-0-0-10.128 [7C45399A1138EF35D358938E12EE81BB~8584441_2026-08-10-210741-8787-0-0-10.128.mp3？cdn_id=99&uuid=d325d582-a05a-2ed9-abc9-3f4efbef3ddc&wuuid=6a8383b3].md"
source_url: "https://pdcn.co/e/serve.castfire.com/audio/8584441/8584441_2026-08-10-210741.128.mp3?rssID=6736"
duration: "1885"
last_updated: 2026-08-18
---

## Summary
This [[DataScienceWithSam]] episode has [[SamDataScienceWithSam|Sam]] interview [[BenjaminLarson|Benjamin Larson]], a data science manager in [[Verizon]]'s consumer-side cybersecurity organization, about how data science supports risk management against customer-account attacks, fraud, and social engineering. The source connects [[CybersecurityDataScience]], [[CybersecuritySimulationModeling]], [[SocialEngineeringNLP]], [[AuthenticationRiskModeling]], and [[SecurityDataAccessConstraint]] into a practical security workflow rather than a generic AI story. Its core synthesis is that useful cybersecurity data science is adversarial, temporary, and organizational: simple models can work when the data is strong, but defenders must keep adapting, earn security-team trust, respect sensitive-data access, and hand off findings to domain experts who close vulnerabilities.

## Key Claims
- [[BenjaminLarson]] works under the CISO area in [[Verizon]]'s consumer group, focusing on threats to phone, Fios, and customer accounts.
- The source frames [[CybersecurityDataScience]] as applied risk work: known bad-actor data, threat scoring, basic classifiers, simulations, NLP, and clustering are valuable when they map to operational security decisions.
- [[CybersecuritySimulationModeling]] helps defenders prioritize scarce resources by modeling attacks, estimating damage, and testing whether vulnerabilities such as authentication bypasses can be exploited.
- Ben says bots and simulation programs can probe systems repeatedly in ways that would require many humans to perform manually.
- [[SocialEngineeringNLP]] appears through recorded customer-support calls that are transcribed, clustered, and analyzed for repeated phrases or scripts that may reveal social-engineering attacks.
- The source says suspicious call language can trigger warnings for representatives, making fraud detection a live operational tool rather than only after-the-fact analytics.
- [[AuthenticationRiskModeling]] is central to the consumer-side threat problem: attackers may fake identity, access accounts, or order products through someone else's account.
- Ben says a simple logistic regression can sometimes catch about 85% of bad actors when the dataset is strong, showing that model simplicity can beat technical novelty when the signal is good.
- Successful cybersecurity models may be short-lived because once a model reveals a vulnerability, the organization can close that path and retire or replace the model.
- [[SecurityDataAccessConstraint]] is part of the work: Ben says security teams are tight with data, may require high-level approval, and often need explicit use cases before granting access.
- The episode treats [[DomainExpertAlignment]] as a social requirement. Data scientists entering cybersecurity need early wins, humility, and clear storytelling so experts do not hear findings as attacks on their competence.
- The future-risk section links [[AIImpersonationFraudRisk]] to deepfakes, realistic voice or video, identity cloaking, and attacker tools that no longer require rare compute.
- Brand and domain monitoring appear in the [[Verizon]] example: teams scan newly registered domains and use bots or computer vision to identify sites that resemble Verizon and request credentials.
- The closing personal advice is basic but high leverage: turn on two-factor authentication, change passwords, and avoid leaving passwords exposed.

## Key Quotes
> "known bad actors" - Ben's practical starting point for classifier-style cybersecurity work.

> "85%" - Ben's example of how much a simple model might catch when the data is strong.

> "not a question of if, but when" - Ben's warning about personal exposure to cyber victimization.

## Connections
- [[DataScienceWithSam]], [[SamDataScienceWithSam]], [[BenjaminLarson]], and [[Verizon]] - show, host, guest, and company context.
- [[CybersecurityDataScience]], [[CybersecuritySimulationModeling]], [[SocialEngineeringNLP]], [[AuthenticationRiskModeling]], and [[SecurityDataAccessConstraint]] - main concepts added by the source.
- [[SocialEngineeringFraud]], [[AIImpersonationFraudRisk]], [[AIEnabledScamIndustrialization]], and [[BrandImpersonationMonitoring]] - broader fraud and identity-risk branch.
- [[AICyberDefenseUtility]], [[CybersecurityAISupervision]], [[DomainExpertAlignment]], [[AIVerification]], and [[HumanJudgmentUnderAI]] - AI and expert-supervision context.
- [[ContactCenterAI]], [[VoiceInteraction]], and [[PersonalSecurityTiering]] - call-analysis, voice trust, and personal safety context.

## Contradictions
- No direct contradiction found.
- The source qualifies broad AI-cybersecurity enthusiasm by showing that operational cybersecurity often benefits from strong data, simple classifiers, simulations, and expert handoff before it benefits from more advanced model architecture.
