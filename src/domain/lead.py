from dataclasses import dataclass, field
from datetime import datetime


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

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )