---
title: "Echomind"
type: entity
tags: [ai, enterprise-ai, auto-rl, post-training]
sources:
  - ai-xia-banchang-buhui-zhisheng-yige-chaoji-moxing-duitan-kevin-ding-pyromind-chuangshiren-ceo-lsq-rke8nfrbi5xalgst3a8uncfd
last_updated: 2026-08-31
knowledge_schema: synthesis-v1
---

# Echomind

## Overview
Echomind is described as [[Pyromind]]'s Auto RL product for improving production agents from trajectory capture through reward construction, training, and redeployment.

## Current Profile
Echomind is the product surface where Pyromind tries to turn enterprise agent feedback into a repeatable improvement loop. A customer places a proxy URL into an agent, Echomind captures trajectories, generates reward structure and a training pipeline, trains a model, and returns the improved model to the production scene.

## Key Characteristics
- Captures production trajectories through an agent proxy.
- Builds or adapts reward structure and training pipeline from real scene data.
- Trains models and deploys improved outputs back to the customer scene.
- Prices by scenario value and quota, including update frequency, data volume, training rounds, and reward value.
- Depends on FDE cold-start work for first scene entry but aims to make reward adaptation reusable across similar modalities.

## Evidence
Auto RL loop:
- [[ai-xia-banchang-buhui-zhisheng-yige-chaoji-moxing-duitan-kevin-ding-pyromind-chuangshiren-ceo-lsq-rke8nfrbi5xalgst3a8uncfd|AI 下半场，不会只剩一个超级模型]] describes Echomind as a proxy-based Auto RL product that collects trajectories, constructs rewards and training, trains, and deploys.

Scenario pricing:
- [[ai-xia-banchang-buhui-zhisheng-yige-chaoji-moxing-duitan-kevin-ding-pyromind-chuangshiren-ceo-lsq-rke8nfrbi5xalgst3a8uncfd|AI 下半场，不会只剩一个超级模型]] says Echomind is priced by scenario value and quota rather than simple resource use.

FDE boundary:
- [[ai-xia-banchang-buhui-zhisheng-yige-chaoji-moxing-duitan-kevin-ding-pyromind-chuangshiren-ceo-lsq-rke8nfrbi5xalgst3a8uncfd|AI 下半场，不会只剩一个超级模型]] says first entry into a new scene still requires data, knowledge, benchmark, and reward-agent adaptation work.

## Qualifications
The episode does not provide a full technical account of reward construction, privacy handling inside Echomind, deployment contracts, or failure modes. Product details and pricing ranges remain source-scoped.

## What Changed
- Added Echomind as Pyromind's Auto RL product.
- Added its proxy, trajectory, reward, training, and deployment flow.
- Added scenario-value/quota pricing as its economic boundary.

## Relationships
- [[Pyromind]] - parent company and product owner.
- [[PyromindStudio]] - infrastructure layer distinguished from Echomind's Auto RL loop.
- [[AutoRLProductionLoop]] - operational loop Echomind implements.
- [[ScenarioLevelRewardSignal]] - reward abstraction Echomind depends on.
- [[ForwardDeployedEngineer]] - cold-start role needed to enter new production scenes.
- [[OutcomeBasedAIPricing]] - pricing frame Echomind partially resembles through scenario-value charging.
