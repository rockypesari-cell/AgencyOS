import requests

URL = "http://127.0.0.1:1234/v1/chat/completions"


def review(text):

    system_prompt = """
You are a professional Persian editor.

Your job is ONLY to improve the Persian writing.

Rules:

- Keep the same structure.
- Keep numbering.
- Keep the English AI prompt exactly unchanged.
- Fix grammar.
- Make Persian natural.
- Remove repeated sentences.
- Remove phrases like "قوانین دریافت شد."
- Return only the final text.
"""

    payload = {
        "model": "qwen2.5-7b-instruct",
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": text
            }
        ],
        "temperature": 0
    }

    response = requests.post(
        URL,
        json=payload,
        headers={"Content-Type": "application/json"}
    )

    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]