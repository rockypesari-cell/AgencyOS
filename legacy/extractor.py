import requests

URL = "http://127.0.0.1:1234/v1/chat/completions"


def extract_info(customer_text):

    system_prompt = """
You are an information extraction AI.

Extract the following fields from the user's request.

Return ONLY valid JSON.

{
    "customer":"",
    "service":"",
    "budget":"",
    "deadline":""
}

Rules:
- No explanation.
- No markdown.
- If a field is missing, use "Unknown".
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
                "content": customer_text
            }
        ],
        "temperature": 0
    }

    response = requests.post(URL, json=payload)

    return response.json()["choices"][0]["message"]["content"]