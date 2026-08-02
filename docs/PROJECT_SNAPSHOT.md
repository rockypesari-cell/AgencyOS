# AgencyOS Project Snapshot v0.2

Last Update: 2026-08-02

---

## Project Identity

AgencyOS is an AI-native operating system for service agencies.
It is NOT a marketplace. It is NOT a chatbot.
It is an Agency Broker platform.

Model: Client -> AgencyOS -> Freelancer -> AgencyOS -> Client

---

## Technology Stack

- Python 3.x
- FastAPI
- SQLite (dev) / PostgreSQL (future)
- LM Studio + Local LLMs
- Git / GitHub

Repository: https://github.com/rockypesari-cell/AgencyOS

---

## Architecture

Client -> FastAPI -> Services -> Workflows -> Agents -> Domain -> Storage -> SQLite

Key Principles:
- Agents decide. Workflows execute. Skills are reusable.
- Business logic lives OUTSIDE prompts.
- All new code goes in src/. legacy/ is read-only.
- Every agent inherits from BaseAgent.
- No direct agent instantiation. Use AgentLoader.

---

## Folder Structure

src/
├── core/           <- System heart
│   ├── base_agent.py
│   └── agent_registry.py
├── bootstrap/      <- Wiring layer
│   └── agent_loader.py
├── agents/
│   └── lead_intake.py
├── workflows/
│   └── lead_workflow.py
├── services/
│   ├── lead_service.py
│   ├── lead_state_service.py
│   ├── llm_service.py
│   └── llm_test.py
├── domain/
│   └── lead.py
├── storage/
│   ├── database.py
│   └── lead_repository.py
├── api/
│   ├── main.py
│   └── schemas.py
├── config/
├── tools/
├── skills/
└── memory/

tests/
├── test_base_agent.py
├── test_agent_registry.py
└── test_agent_loader.py

docs/
├── PROJECT_SNAPSHOT.md
├── SYSTEM_PROMPT_FOR_NEW_CHATS.md
├── PROJECT_STATUS.md
├── ARCHITECTURE.md
├── VISION.md
├── ADR/
├── research/
└── sprints/

---

## Completed Features

| ID | Feature | Status |
|----|---------|--------|
| F-001 | Project Init | Done |
| F-002 | Lead Domain Entity | Done |
| F-003 | Lead Intake Agent | Done |
| F-004 | Lead Workflow | Done |
| F-005 | LM Studio Integration | Done |
| F-006 | FastAPI POST /leads | Done |
| F-007 | API Schemas | Done |
| F-008 | GET /leads | Done |
| F-009 | SQLite Persistence | Done |
| F-010 | Lead Service Layer | Done |
| C-001 | Agent Registry | Done |
| C-002 | BaseAgent | Done |
| C-003 | Agent Loader | Done |

---

## Current Sprint

Sprint 1: Core Foundation

---

## Next Features (in order)

1. C-004: Workflow Registry
2. C-005: Service Container
3. Architecture Freeze v1.0
4. R-001: Proposal Generator (Revenue Engine)
5. R-002: Pricing Engine

---

## Development Tracks

### Track 1: ADA (1 hour/day)
Current: C-004 Workflow Registry
Next: Project Memory System

### Track 2: Revenue Engine (1 hour/day)
Current: Manual lead finding + proposals
Next: R-001 Proposal Generator

### Track 3: AgencyOS Core (1 hour/day)
Current: C-004 Workflow Registry
Next: C-005 Service Container

---

## Rules for AI Assistants

1. Read this file FIRST before doing anything.
2. Do NOT recreate existing files.
3. Do NOT ask "what is the project structure?"
4. All new agents MUST inherit from BaseAgent.
5. All new agents MUST be registered via AgentLoader.
6. Business logic goes in services/, NOT in agents/.
7. New code goes in src/, NOT in legacy/.
8. Every feature: implement -> test -> commit -> update snapshot.

---

## Glossary

- ADA = AgencyOS Documentation/Automation Agent (NOT cryptocurrency)
- BDR = Business Decision Record
- ADR = Architecture Decision Record