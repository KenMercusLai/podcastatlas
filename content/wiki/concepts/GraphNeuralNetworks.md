---
title: "Graph Neural Networks"
type: concept
tags: [machine-learning, graphs, ai-for-science]
sources:
  - ai-for-science-baofa-ai-neng-jiesuo-weidade-kexuefaxianma-s10e29-b59d5e79-65af-4a1a-ac50-b54e665474ad
last_updated: 2026-09-09
knowledge_schema: synthesis-v1
---

# Graph Neural Networks

## Definition
Graph neural networks are machine-learning architectures for data represented as nodes and edges, such as molecules, protein interactions, signaling pathways, social networks, and financial transaction networks.

## Current Synthesis
The source introduces graph neural networks through [[SongLe]]'s research path. It treats them as a durable method family for scientific and structured-data problems, not as a pre-LLM dead end. In life science, graphs remain relevant because molecules, pathways, protein interactions, knowledge graphs, and cellular regulatory systems all contain relational structure.

For [[AIForScience]], the main synthesis is architectural pluralism. Sequence models and protein language models matter, but proteins have three-dimensional geometry and cells have regulatory networks; graph and geometric methods can encode structure that ordinary text-like sequence modeling may miss.

## Key Claims
- Graph neural networks are useful when the domain's structure is relational rather than purely sequential.
- Life-science examples include molecular graphs, protein interactions, signaling pathways, and cellular regulatory networks.
- GNNs can support drug-synthesis route prediction, small-molecule representation, knowledge-graph representation, and perturbation prediction.
- The method remains complementary to foundation models and protein language models.
- Biology's structure makes architecture choice a scientific modeling decision, not only a software preference.

## Evidence
- Research-history claim: [[ai-for-science-baofa-ai-neng-jiesuo-weidade-kexuefaxianma-s10e29-b59d5e79-65af-4a1a-ac50-b54e665474ad]] says Song worked on graph learning and deep learning at Georgia Tech.
- Life-science applications: [[ai-for-science-baofa-ai-neng-jiesuo-weidade-kexuefaxianma-s10e29-b59d5e79-65af-4a1a-ac50-b54e665474ad]] names small-molecule synthesis paths, protein interactions, signaling pathways, and perturbation prediction.
- Architecture boundary: [[ai-for-science-baofa-ai-neng-jiesuo-weidade-kexuefaxianma-s10e29-b59d5e79-65af-4a1a-ac50-b54e665474ad]] says protein structure and cellular networks require graph or geometric deep learning alongside sequence models.

## Counterevidence & Qualifications
The source does not benchmark GNNs against transformers or prove they are superior across biology. It only establishes that graph and geometric inductive biases remain relevant where the scientific object has explicit relational or spatial structure.

## What Changed
- Created the graph neural networks concept from the episode's technical lineage.
- Connected GNNs to biological modeling and virtual-cell architecture constraints.
- Positioned GNNs as complementary to protein language models rather than opposed to them.

## Related Concepts
- [[ProteinLanguageModels]] - sequence-scaling route that GNNs complement.
- [[BiologicalHarnessEngineering]] - broader constraint and architecture layer for biology.
- [[VirtualCellWorldModel]] - cell-modeling target where graph structure can matter.
- [[AIProteinDesign]] - application area where molecular and protein structure are central.
- [[AIForScience]] - scientific-AI field using graph methods.
