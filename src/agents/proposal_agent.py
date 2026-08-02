"""
ProposalAgent - Generates professional project proposals.

Input:  Lead data (service, summary, priority, budget)
Output: Proposal text, suggested price, timeline

Architecture:
    - Inherits BaseAgent
    - Uses LLMService for AI generation
    - Falls back to template if LLM unavailable
    - No business logic. Just generation.
"""

from typing import Any, Dict, Optional
from core.base_agent import BaseAgent


# ─── Pricing Reference (MVP) ─────────────────────────────────
# Later this moves to a PricingService.
BASE_PRICES = {
    "logo_design": 150,
    "brand_identity": 400,
    "web_design": 600,
    "presentation": 200,
    "illustration": 250,
    "social_media": 180,
    "poster": 120,
    "video": 500,
    "content": 200,
    "translation": 100,
    "unknown": 200,
}

TIMELINES = {
    "logo_design": "3-5 days",
    "brand_identity": "7-14 days",
    "web_design": "14-21 days",
    "presentation": "3-5 days",
    "illustration": "5-7 days",
    "social_media": "3-5 days",
    "poster": "2-3 days",
    "video": "7-14 days",
    "content": "5-7 days",
    "translation": "3-5 days",
    "unknown": "5-7 days",
}


class ProposalAgent(BaseAgent):
    """Generates project proposals from lead data."""

    def __init__(self, llm_service=None):
        super().__init__(
            name="proposal_generator",
            description="Generates professional proposals from lead data.",
            version="0.2.0",
            skills=["proposal_writing", "pricing_estimation"],
            tools=["llm_service"],
        )
        self._llm = llm_service

    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        service = input_data.get("service", "unknown").lower().replace(" ", "_")
        summary = input_data.get("summary", "")
        priority = input_data.get("priority", "normal")
        client_name = input_data.get("client_name", "Valued Client")

        price = BASE_PRICES.get(service, BASE_PRICES["unknown"])
        timeline = TIMELINES.get(service, TIMELINES["unknown"])

        if priority == "high":
            price = int(price * 1.3)
            timeline = timeline.replace("days", "days (rush)")

        # Try LLM first, fallback to template
        if self._llm:
            try:
                proposal_text = self._generate_with_llm(
                    service, summary, client_name, price, timeline
                )
            except Exception:
                proposal_text = self._generate_template(
                    service, summary, client_name, price, timeline
                )
        else:
            proposal_text = self._generate_template(
                service, summary, client_name, price, timeline
            )

        return {
            "proposal_text": proposal_text,
            "suggested_price": price,
            "currency": "USD",
            "timeline": timeline,
            "service": service,
            "priority": priority,
            "status": "draft",
        }

    def _generate_with_llm(
        self, service, summary, client_name, price, timeline
    ) -> str:
        prompt = f"""Write a professional project proposal for:

Service: {service.replace('_', ' ').title()}
Client: {client_name}
Project Summary: {summary}
Price: ${price} USD
Timeline: {timeline}

Requirements:
- Professional tone
- 3-4 paragraphs
- Include scope, timeline, pricing
- End with next steps
"""
        response = self._llm.generate(prompt)
        return response

    def _generate_template(
        self, service, summary, client_name, price, timeline
    ) -> str:
        service_name = service.replace("_", " ").title()
        return f"""PROJECT PROPOSAL

Dear {client_name},

Thank you for your interest in our {service_name} services.

PROJECT OVERVIEW
{summary if summary else 'Based on your requirements, we will deliver a professional ' + service_name + ' solution.'}

SCOPE OF WORK
- Professional {service_name}
- Up to 2 revision rounds
- Final delivery in standard formats

TIMELINE
Estimated delivery: {timeline}

INVESTMENT
Total: ${price} USD
Payment: 50% upfront, 50% upon delivery

NEXT STEPS
1. Confirm this proposal
2. Share detailed requirements
3. We begin work immediately

We look forward to working with you.

Best regards,
AgencyOS Team"""