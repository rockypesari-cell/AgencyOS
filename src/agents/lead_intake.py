from dataclasses import dataclass

from src.config.prompts import LEAD_ANALYSIS_PROMPT
from src.services.llm_service import LLMService
from src.skills.lead_analysis import LeadAnalysisSkill


@dataclass
class LeadAnalysis:
    service: str
    summary: str
    priority: str
    questions: list[str]


class LeadIntakeAgent:
    """
    Converts raw client requests into structured lead information
    using local LLM.
    """

    def __init__(self):
        self.llm = LLMService()
        self.skill = LeadAnalysisSkill()

    def analyze(self, request: str) -> LeadAnalysis:
        prompt = f"""
{LEAD_ANALYSIS_PROMPT}

Client request:
{request}
"""

        response = self.llm.generate(prompt)

        data = self.skill.parse_response(response)

        return LeadAnalysis(
            service=data.get("service", ""),
            summary=data.get("summary", ""),
            priority=data.get("priority", "normal"),
            questions=data.get("questions", [])
        )