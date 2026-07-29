from src.domain.lead import Lead
from src.agents.lead_intake import LeadIntakeAgent
from src.storage.lead_repository import LeadRepository


class LeadWorkflow:
    """
    Orchestrates the lead intake process.
    """

    def __init__(self):
        self.agent = LeadIntakeAgent()
        self.repository = LeadRepository()

    def execute(self, request: str) -> Lead:
        analysis = self.agent.analyze(request)

        lead = Lead(
            raw_request=request,
            service=analysis.service,
            summary=analysis.summary,
            priority=analysis.priority,
            questions=analysis.questions,
        )

        self.repository.save(lead)

        return lead