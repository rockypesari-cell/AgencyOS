"""
ProposalWorkflow - Orchestrates the proposal generation process.

Flow:
    1. Receive lead data
    2. Call ProposalAgent
    3. Format output
    4. Return proposal package

Architecture:
    - Inherits BaseWorkflow
    - Uses ProposalAgent (from registry)
    - No AI logic here. Just orchestration.
"""

from typing import Any, Dict
from core.base_workflow import BaseWorkflow


class ProposalWorkflow(BaseWorkflow):
    """Orchestrates proposal generation from lead data."""

    def __init__(self, proposal_agent=None):
        super().__init__(
            name="proposal_workflow",
            description="Generates proposals from qualified leads.",
            version="0.1.0",
            steps=[
                "validate_lead",
                "generate_proposal",
                "format_output",
            ],
        )
        self._agent = proposal_agent

    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        # Step 1: Validate
        lead_data = context.get("lead_data", {})
        if not lead_data:
            raise ValueError("No lead_data provided in context.")

        # Step 2: Generate
        if self._agent:
            result = self._agent.run(lead_data)
        else:
            result = {
                "success": False,
                "error": "No ProposalAgent configured.",
            }

        if not result.get("success"):
            raise RuntimeError(
                f"Proposal generation failed: {result.get('error', 'Unknown')}"
            )

        # Step 3: Format output
        return {
            "proposal": result,
            "lead_data": lead_data,
            "ready_to_send": True,
        }