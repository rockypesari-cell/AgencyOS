from reviewer import review
import json
import os
from datetime import datetime

import requests

from extractor import extract_info
from formatter import clean_output
from lead_manager import LeadManager
from prompts import SYSTEM_PROMPT

os.environ["NO_PROXY"] = "127.0.0.1,localhost"

URL = "http://127.0.0.1:1234/v1/chat/completions"

lead_manager = LeadManager()


def ask_agent(customer_need):

    payload = {
        "model": "qwen2.5-7b-instruct",
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": customer_need
            }
        ],
        "temperature": 0.1,
        "max_tokens": 900
    }

    response = requests.post(
        URL,
        json=payload,
        headers={"Content-Type": "application/json"}
    )

    print("STATUS:", response.status_code)

    response.raise_for_status()

    data = response.json()

    result = clean_output(
    data["choices"][0]["message"]["content"]
    )

    result = review(result)

    try:
        info = json.loads(extract_info(customer_need))

        lead_manager.add_lead(
            customer=info.get("customer", "Unknown"),
            service=info.get("service", "Unknown"),
            budget=info.get("budget", "Unknown"),
            deadline=info.get("deadline", "Unknown"),
            notes=customer_need
        )

    except Exception as e:
        print("Extractor Error:", e)

    return result


def main():

    with open("input.txt", "r", encoding="utf-8") as f:
        customer_need = f.read()

    result = ask_agent(customer_need)

    print(result)

    os.makedirs("outputs", exist_ok=True)

    filename = f"outputs/result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(result)

    print("Saved:", filename)


if __name__ == "__main__":
    main()