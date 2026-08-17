---
title: "Data Engineering For Data Science"
type: concept
tags: [data-engineering, data-science, mlops]
sources: [ep-7-data-science-mlops]
last_updated: 2026-08-18
---

# Data Engineering For Data Science

Data engineering for data science is the practice of getting data into places, formats, and access patterns that let data scientists analyze and model without constant manual handoffs. In [[ep-7-data-science-mlops]], [[AaronBlythe]] contrasts mature data engineering with the common weak pattern where data scientists repeatedly request CSV files, move data locally, and manipulate it outside the source system.

The source frames data engineering as a foundation rather than a separate back-office concern. When data stays in a warehouse or other shared system, tools such as BigQuery can let analysis happen close to the data. That reduces friction and helps [[MachineLearningEngineering]] and [[MLOps]] work because models, pipelines, and feedback loops depend on reliable data access.

This concept complements [[DataEngineeringDemand]]. That page tracks labor-market demand for data engineering; this page tracks the workflow reason data engineering matters inside production ML.

## Key Claims
- Data scientists often lose time moving, cleaning, and locally manipulating requested files.
- A strong data engineering practice puts data where analysis and model work can happen reliably.
- Data warehouses can reduce copying and handoff friction by letting analysis run near the data.
- Data engineering is upstream of MLOps because model deployment and feedback loops depend on stable data access.
- Better data engineering improves collaboration by letting data scientists focus less on plumbing and more on modeling and interpretation.

## Connections
- [[MLOps]] and [[MachineLearningEngineering]] - downstream production ML practices.
- [[DataEngineeringDemand]] - adjacent labor-market and implementation-demand concept.
- [[ProductionMLFeedbackLoops]] - feedback loops need data returned in usable form.
- [[IntegratedMLTeams]] - team structure where data engineers work with data scientists and ML engineers.
- [[GoogleCloud]] and [[AaronBlythe]] - source context for the BigQuery/data-warehouse example.
