from src.domain.lead import Lead
from src.storage.lead_repository import LeadRepository
from src.workflows.lead_workflow import LeadWorkflow


class LeadService:
    """
    Application service responsible for lead operations.
    """

    def __init__(self):
        self.workflow = LeadWorkflow()
        self.repository = LeadRepository()

    def create_lead(self, request: str) -> Lead:
        """
        Analyze and persist a new lead.
        """

        lead = self.workflow.execute(request)

        self.repository.save(lead)

        return lead


    def get_all_leads(self):
        """
        Retrieve stored leads.
        """

        return self.repository.get_all()