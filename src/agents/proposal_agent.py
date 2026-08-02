"""
ProposalAgent - Generates professional project proposals.

Architecture:
    - Inherits BaseAgent
    - Uses PricingService for pricing (no pricing logic here)
    - Uses LLMService for AI generation (optional)
    - Falls back to template if LLM unavailable
"""

from typing import Any, Dict, Optional
from core.base_agent import BaseAgent
from services.pricing_service import PricingService


class ProposalAgent(BaseAgent):
    """Generates project proposals from lead data."""

    def __init__(self, llm_service=None, pricing_service=None):
        super().__init__(
            name="proposal_generator",
            description="Generates professional proposals from lead data.",
            version="0.3.0",
            skills=["proposal_writing"],
            tools=["llm_service", "pricing_service"],
        )
        self._llm = llm_service
        self._pricing = pricing_service or PricingService()

    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        service = input_data.get("service", "unknown")
        summary = input_data.get("summary", "")
        priority = input_data.get("priority", "normal")
        complexity = input_data.get("complexity", "normal")
        client_name = input_data.get("client_name", "Valued Client")
        rush = input_data.get("rush", False)

        # Get pricing from PricingService
        price_info = self._pricing.calculate(
            service=service,
            priority=priority,
            complexity=complexity,
            rush=rush,
        )

        price = price_info["final_price"]
        timeline = price_info["timeline"]
        currency = price_info["currency"]

        # Generate proposal text
        if self._llm:
            try:
                proposal_text = self._generate_with_llm(
                    service, summary, client_name, price, timeline, currency
                )
            except Exception:
                proposal_text = self._generate_template(
                    service, summary, client_name, price, timeline, currency
                )
        else:
            proposal_text = self._generate_template(
                service, summary, client_name, price, timeline, currency
            )

        return {
            "proposal_text": proposal_text,
            "pricing": price_info,
            "suggested_price": price,
            "currency": currency,
            "timeline": timeline,
            "service": price_info["service"],
            "priority": priority,
            "status": "draft",
        }

    def _generate_with_llm(
        self, service, summary, client_name, price, timeline, currency
    ) -> str:
        service_name = service.replace("_", " ").title()
        prompt = f"""Write a professional project proposal for:

Service: {service_name}
Client: {client_name}
Project Summary: {summary}
Price: ${price} {currency}
Timeline: {timeline}

Requirements:
- Professional tone
- 3-4 paragraphs
- Include scope, timeline, pricing
- End with next steps
"""
        return self._llm.generate(prompt)

    def _generate_template(
        self, service, summary, client_name, price, timeline, currency
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
Total: ${price} {currency}
Payment: 50% upfront, 50% upon delivery

NEXT STEPS
1. Confirm this proposal
2. Share detailed requirements
3. We begin work immediately

We look forward to working with you.

Best regards,
AgencyOS Team"""