from dataclasses import dataclass


@dataclass
class LeadAnalysis:
    service: str
    summary: str
    priority: str
    questions: list[str]


class LeadIntakeAgent:
    """
    Responsible for converting raw client requests
    into structured lead information.
    """

    def analyze(self, request: str) -> LeadAnalysis:
        return LeadAnalysis(
            service="Unknown",
            summary=request,
            priority="normal",
            questions=[]
        )