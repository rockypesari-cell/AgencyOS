from src.domain.lead import Lead, LeadStatus


class LeadStateService:
    """
    Controls valid Lead status transitions.
    """

    transitions = {
        LeadStatus.NEW: [
            LeadStatus.QUALIFIED
        ],
        LeadStatus.QUALIFIED: [
            LeadStatus.PROPOSAL_SENT
        ],
        LeadStatus.PROPOSAL_SENT: [
            LeadStatus.ACCEPTED
        ],
        LeadStatus.ACCEPTED: [
            LeadStatus.PRODUCTION
        ],
        LeadStatus.PRODUCTION: [
            LeadStatus.QA
        ],
        LeadStatus.QA: [
            LeadStatus.DELIVERED
        ],
        LeadStatus.DELIVERED: [
            LeadStatus.ARCHIVED
        ],
    }

    def change_status(
        self,
        lead: Lead,
        new_status: LeadStatus
    ):
        allowed = self.transitions.get(
            lead.status,
            []
        )

        if new_status not in allowed:
            raise ValueError(
                f"Invalid transition: "
                f"{lead.status.value} -> {new_status.value}"
            )

        lead.status = new_status

        return lead