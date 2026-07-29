from fastapi import FastAPI

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


@app.post("/leads")
def create_lead(request: dict):
    lead_request = request.get(
        "request",
        ""
    )

    lead = workflow.execute(
        lead_request
    )

    return {
        "raw_request": lead.raw_request,
        "service": lead.service,
        "summary": lead.summary,
        "priority": lead.priority,
        "questions": lead.questions,
        "status": lead.status.value,
    }