from fastapi import FastAPI

from src.api.schemas import LeadCreateRequest, LeadResponse
from src.workflows.lead_workflow import LeadWorkflow


app = FastAPI(
    title="AgencyOS API",
    version="0.1.0"
)


workflow = LeadWorkflow()


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

    return LeadResponse(
        raw_request=lead.raw_request,
        service=lead.service,
        summary=lead.summary,
        priority=lead.priority,
        questions=lead.questions,
        status=lead.status.value,
    )