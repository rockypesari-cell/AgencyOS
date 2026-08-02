# AgencyOS Architecture

## Vision

AgencyOS is an AI Operating System for running a Drop Servicing business.

---

# High-Level Architecture

```
                Dashboard / CLI
                       │
                API Layer
                       │
               Workflow Engine
                       │
               Agent Registry
                       │
        ┌──────────────┼──────────────┐
        │              │              │
    Sales Agent    QA Agent      ADA Agent
        │              │              │
        └──────────────┼──────────────┘
                       │
                 Tool Registry
                       │
        ┌──────────────┼──────────────┐
        │              │              │
      Git          LM Studio      SQLite
```

---

# Layers

- Presentation
- API
- Workflows
- Agents
- Tools
- Services
- Domain
- Storage

---

# Core Components

- Agent Registry
- Workflow Engine
- Tool Registry
- Memory
- Event Bus
- Knowledge Graph
- Documentation Engine

---

# External Systems

- LM Studio
- Git
- SQLite
- Future PostgreSQL

---

# Current Status

Architecture is under active development.

Current milestone:

Architecture Freeze (v0.1)