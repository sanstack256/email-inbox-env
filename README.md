---
title: Email Inbox Environment
emoji: 📧
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---


# Email Inbox Manager Environment

## Overview
This project simulates a real-world email inbox where an AI agent must manage and classify emails.

## Motivation
Email management is a common real-world task. This environment allows AI agents to learn decision-making across different types of emails.

## Observation Space
Each email contains:
- id
- subject
- body
- type (work, spam, personal)

## Action Space
The agent can take the following actions:
- mark_spam
- mark_important
- reply
- archive
- escalate

## Tasks

### Easy
Classify emails correctly.

### Medium
Make consistent and accurate decisions across the inbox.

### Hard
Optimize full inbox management with penalties for incorrect actions.

## Reward System
- Correct action: +1
- Smart action (escalate work): +2
- Neutral action (archive): 0
- Incorrect action: -1


## Future Improvements
- Integrate LLM-based agent
- Add priority-aware decision making


## How to Run

```bash
python3 main.py