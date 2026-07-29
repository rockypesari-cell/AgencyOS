from pydantic import BaseModel


class LeadCreateRequest(BaseModel):
    """
    Incoming client lead request.
    """

    request: str


class LeadResponse(BaseModel):
    """
    API response for a created lead.
    """

    raw_request: str
    service: str
    summary: str
    priority: str
    questions: list[str]
    status: str