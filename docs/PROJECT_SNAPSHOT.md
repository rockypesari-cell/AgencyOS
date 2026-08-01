# AgencyOS Project Snapshot

Version: 0.1.0
Last Updated: 2026-08-01

---

# Project Identity

AgencyOS is an AI Operating System for running service-based businesses.

Initial market:
AI-powered Drop Servicing Agency

Long-term vision:
A platform that can operate different service businesses using AI agents, workflows, tools, and automation.

AgencyOS is NOT a marketplace.

Business model:

Client
  |
  v
AgencyOS
  |
  v
Freelancer
  |
  v
QA
  |
  v
Client

AgencyOS owns client communication, quality control, and project management.

---

# Development Tracks

## Track 1 - ADA (AgencyOS Development Assistant)

Purpose:
Build an internal AI assistant that understands and manages the AgencyOS codebase.

Responsibilities:

- Project Memory
- Architecture Understanding
- Documentation Management
- ADR Generation
- Code Analysis
- Developer Assistance

Current Status:

NEXT:
Agent Registry


---

## Track 2 - Revenue Engine

Purpose:
Generate real business revenue as early as possible.

MVP Services:

- Logo Design
- Brand Identity
- Social Media Design
- Presentation Design
- Web Design
- Illustration

Workflow:

Lead
 |
 v
Requirement Analysis
 |
 v
Pricing
 |
 v
Proposal
 |
 v
Client


Current Status:

NEXT:
Proposal Generator
First Client Acquisition


---

## Track 3 - AgencyOS Core

Purpose:
Build the operational system.

Main Workflow:

Lead
 |
 v
Qualification
 |
 v
Proposal
 |
 v
Accepted
 |
 v
Production
 |
 v
QA
 |
 v
Delivery
 |
 v
Archive


Current Status:

NEXT:
Agent Registry


---

# Current Architecture

Technology:

- Python
- FastAPI
- SQLite
- LM Studio
- Local LLM
- JSON APIs


Project Structure:

src/

- core
- agents
- workflows
- services
- domain
- storage
- tools
- skills
- memory
- api
- config


---

# Existing Components

## Domain

Implemented:

- Lead Entity
- LeadStatus


## Agents

Implemented:

- LeadIntakeAgent


## Workflows

Implemented:

- LeadWorkflow


## Services

Implemented:

- LeadService
- LLMService


## Skills

Implemented:

- LeadAnalysisSkill


## Storage

Implemented:

- SQLite Database
- LeadRepository


## API

Implemented:

- FastAPI layer
- Lead endpoints


---

# Core Decisions

## Architecture Rules

1. New development happens only inside src/

2. legacy/ folder is read-only.

3. Agents do not contain business logic.

4. LLM access happens only through LLMService.

5. Business entities live inside domain/.

6. Workflows orchestrate processes.

7. Skills transform and validate data.

8. Tools provide external capabilities.


---

# Current Feature

Feature:
C-001 Agent Registry


Business Purpose:

Manage all AI agents from a central registry.


Inputs:

Agent Definition


Outputs:

Agent Object


Success Criteria:

- Register Agent
- Find Agent
- List Agents
- Remove Agent
- Check existence


Location:

src/core/agent_registry.py


---

# Next Development Steps

1. Implement Agent Registry

2. Add tests

3. Update documentation

4. Commit changes

5. Start Proposal Generator


---

# Important Notes For AI Assistants

Before making changes:

Read:

- PROJECT_SNAPSHOT.md
- PROJECT_STATUS.md
- ARCHITECTURE.md


Do not:

- recreate existing components
- modify legacy code
- bypass architecture layers


Always:

- explain architectural decisions
- keep business logic outside prompts
- prefer modular design
- update documentation after major features

---

# Current State

Architecture:
🟡 Active Development

Business:
🟡 Searching first clients

Core:
🟡 Building foundation

Next milestone:

Architecture Freeze + Agent Registry