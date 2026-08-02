# AgencyOS Project Snapshot v0.3

Last Update: 2026-08-02

---

## Project Identity

AgencyOS is an AI-native operating system for service agencies.
NOT a marketplace. NOT a chatbot. An Agency Broker platform.
Model: Client -> AgencyOS -> Freelancer -> AgencyOS -> Client

---

## Technology Stack

Python 3.14, FastAPI, SQLite, LM Studio, Local LLMs, JSON APIs, Git
Repository: https://github.com/rockypesari-cell/AgencyOS

---

## Architecture

Client -> FastAPI -> Services -> Workflows -> Agents -> Domain -> Storage -> SQLite

Core Principles:
- Agents decide. Workflows execute. Skills transform. Services hold business logic.
- All agents inherit BaseAgent. All workflows inherit BaseWorkflow.
- No direct instantiation. Use AgentLoader / AppBootstrap.
- Business logic NEVER inside agents or prompts.
- New code in src/. legacy/ is read-only.

---

## Folder Structure

src/
├── core/                  <- System heart (FROZEN v1.0)
│   ├── base_agent.py
│   ├── agent_registry.py
│   ├── base_workflow.py
│   ├── workflow_registry.py
│   └── service_container.py
├── bootstrap/             <- Wiring layer
│   ├── agent_loader.py
│   └── app_bootstrap.py
├── agents/
│   ├── lead_intake.py
│   └── proposal_agent.py
├── workflows/
│   ├── lead_workflow.py
│   └── proposal_workflow.py
├── services/
│   ├── lead_service.py
│   ├── lead_state_service.py
│   ├── llm_service.py
│   └── pricing_service.py
├── skills/
│   ├── lead_parser.py
│   └── proposal_formatter.py
├── cli/
│   └── propose.py
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
└── memory/

tests/
├── test_base_agent.py
├── test_agent_registry.py
├── test_agent_loader.py
├── test_base_workflow.py
├── test_workflow_registry.py
├── test_service_container.py
├── test_app_bootstrap.py
├── test_proposal_agent.py
├── test_proposal_workflow.py
├── test_pricing_service.py
├── test_lead_parser.py
├── test_lead_to_proposal.py
├── test_proposal_formatter.py
└── test_cli_propose.py

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

### Core (FROZEN v1.0)
| ID | Feature | Status |
|----|---------|--------|
| C-001 | Agent Registry | Done |
| C-002 | BaseAgent | Done |
| C-003 | Agent Loader | Done |
| C-004 | BaseWorkflow + WorkflowRegistry | Done |
| C-005 | ServiceContainer + AppBootstrap | Done |

### Foundation
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

### Revenue Engine
| ID | Feature | Status |
|----|---------|--------|
| R-001 | ProposalAgent | Done |
| R-002 | PricingService | Done |
| R-003 | LeadParserSkill | Done |
| R-004 | ProposalFormatterSkill | Done |
| R-005 | CLI Revenue Tool | Done |

---

## Test Count

150+ tests, all passing, 0 warnings.

---

## CLI Usage

cd src
python -m cli.propose "Need a logo. Budget $500. Urgent!"
python -m cli.propose --service web_design --summary "Company site" --priority high
python -m cli.propose --file lead.txt
python -m cli.propose --interactive

---

## Development Tracks

### Track 1: ADA (1 hour/day)
Done: Agent Registry, BaseAgent, WorkflowRegistry, ServiceContainer
Next: Project Memory System, Documentation Engine

### Track 2: Revenue Engine (1 hour/day)
Done: LeadParser, PricingService, ProposalAgent, Formatter, CLI
Next: R-006 Freelancer Matcher, R-007 Email Sender, R-008 Client Follow-up

### Track 3: AgencyOS Core (1 hour/day)
Done: Architecture Freeze v1.0
Next: Event Bus, Plugin System, Dashboard API

---

## Next Features (priority order)

1. R-006: Freelancer Matcher (match leads to freelancers)
2. R-007: Email/Send Tool (send proposals to clients)
3. R-008: Client Follow-up (auto follow-up sequences)
4. ADA-001: Project Memory System
5. CORE-006: Event Bus

---

## Rules for AI Assistants

1. Read this file FIRST.
2. Do NOT recreate existing files.
3. Do NOT ask "what is the project structure?"
4. All agents inherit BaseAgent.
5. All workflows inherit BaseWorkflow.
6. All agents registered via AgentLoader.
7. Business logic in services/, NOT in agents/.
8. New code in src/, NOT in legacy/.
9. Every feature: implement -> test -> commit -> update snapshot.
10. Respond in Persian (Farsi), RTL.

---

## Glossary

- ADA = AgencyOS Development Assistant (NOT cryptocurrency)
- BDR = Business Decision Record
- ADR = Architecture Decision Record