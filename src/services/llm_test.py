from src.services.llm_service import LLMService


def main():
    llm = LLMService()

    response = llm.generate(
        "Say hello and confirm that you are running."
    )

    print(response)


if __name__ == "__main__":
    main()