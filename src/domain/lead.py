from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class LeadStatus(str, Enum):
    NEW = "new"
    QUALIFIED = "qualified"
    PROPOSAL_SENT = "proposal_sent"
    ACCEPTED = "accepted"
    PRODUCTION = "production"
    QA = "qa"
    DELIVERED = "delivered"
    ARCHIVED = "archived"


@dataclass
class Lead:
    """
    Core business entity representing a potential client request.
    """

    raw_request: str

    service: str = ""
    summary: str = ""
    priority: str = "normal"
    questions: list[str] = field(default_factory=list)

    status: LeadStatus = LeadStatus.NEW

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )