from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_name: str = "AgencyOS"
    version: str = "0.1.0"

    llm_base_url: str = "http://127.0.0.1:1234/v1"
    llm_model: str = "qwen2.5-7b-instruct"


settings = Settings()