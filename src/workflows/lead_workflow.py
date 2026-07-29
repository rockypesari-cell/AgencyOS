from src.domain.lead import Lead
from src.agents.lead_intake import LeadIntakeAgent


class LeadWorkflow:
    """
    Orchestrates the lead intake process.
    """

    def __init__(self):
        self.agent = LeadIntakeAgent()

    def execute(self, request: str) -> Lead:
        analysis = self.agent.analyze(request)

        return Lead(
            raw_request=request,
            service=analysis.service,
            summary=analysis.summary,
            priority=analysis.priority,
            questions=analysis.questions,
        )