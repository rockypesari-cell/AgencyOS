import json


class LeadAnalysisSkill:
    """
    Converts LLM response into structured lead data.
    """

    def parse_response(self, response: str) -> dict:
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {
                "service": "",
                "summary": response,
                "priority": "normal",
                "questions": []
            }