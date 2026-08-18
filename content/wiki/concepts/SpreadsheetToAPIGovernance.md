---
title: "Spreadsheet to API Governance"
type: concept
tags: [spreadsheets, api, governance, insurance]
sources: [ep-11-growing-technology-footprints-in-insurance-sector]
last_updated: 2026-08-18
---

# Spreadsheet to API Governance

Spreadsheet to API governance is the pattern of converting business-owned spreadsheet calculations into version-controlled, auditable, reusable APIs. In [[ep-11-growing-technology-footprints-in-insurance-sector]], [[NickBlamer]] describes [[CoherentSpark]] as taking [[MicrosoftExcel|Excel]] spreadsheets, identifying inputs and outputs, and generating APIs that can run faster and scale in the cloud.

The concept treats spreadsheets as repositories of business logic rather than only as shadow IT. The governance problem is to preserve what business users know while adding production controls: versioning, auditability, reusable interfaces, integration plumbing, and IT promotion paths.

## Key Claims
- Spreadsheet logic can contain real actuarial, underwriting, valuation, projection, and sales knowledge.
- The problem is not only speed; uncontrolled spreadsheets also create audit, version, and reuse problems.
- APIs can turn a spreadsheet calculation into a reusable component that other systems can call.
- Business units can remain accountable for the logic, while IT owns integration and productionization.
- The pattern supports [[InsuranceTechnologyModernization]] when it connects familiar work surfaces to cloud and enterprise systems.

## Connections
- [[CoherentSpark]], [[Coherent]], and [[NickBlamer]] - product and source context.
- [[MicrosoftExcel]] - spreadsheet surface at the center of the pattern.
- [[BusinessLogicAPIs]] and [[APIProductDesign]] - interface and product-design context.
- [[ActuarialScience]], [[ActuaryDataScientistPartnership]], and [[InsuranceModelRegulatoryConstraint]] - insurance accountability context.
