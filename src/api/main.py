import json

from fastapi import FastAPI

from src.api.schemas import (
    LeadCreateRequest,
    LeadResponse,
    LeadListResponse,
)

from src.workflows.lead_workflow import LeadWorkflow

from src.storage.database import initialize_database
from src.storage.lead_repository import LeadRepository


app = FastAPI(
    title="AgencyOS API",
    version="0.1.0"
)


workflow = LeadWorkflow()
repository = LeadRepository()


# Initialize SQLite database
initialize_database()


@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "AgencyOS"
    }


@app.post(
    "/leads",
    response_model=LeadResponse
)
def create_lead(
    data: LeadCreateRequest
):
    lead = workflow.execute(
        data.request
    )

    repository.save(lead)

    return LeadResponse(
        raw_request=lead.raw_request,
        service=lead.service,
        summary=lead.summary,
        priority=lead.priority,
        questions=lead.questions,
        status=lead.status.value,
    )


@app.get(
    "/leads",
    response_model=LeadListResponse
)
def get_leads():

    rows = repository.get_all()

    leads = []

    for row in rows:
        leads.append(
            LeadResponse(
                raw_request=row[1],
                service=row[2],
                summary=row[3],
                priority=row[4],
                questions=json.loads(row[5]),
                status="new",
            )
        )

    return LeadListResponse(
        leads=leads
    )