from openai import OpenAI

from src.config.settings import settings


class LLMService:
    """
    Wrapper around LLM providers.
    Currently uses local LM Studio.
    """

    def __init__(self):
        self.client = OpenAI(
            base_url=settings.llm_base_url,
            api_key="lm-studio"
        )

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=settings.llm_model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content