
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

token = os.getenv("HF_TOKEN")

if not token:
    raise ValueError("Token not found in .env file")

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=token
)

try:
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b:fastest",
        messages=[
            {"role": "user", "content": "Say hello in one sentence."}
        ],
        max_tokens=50
    )

    print("SUCCESS!")
    print(response.choices[0].message.content)

except Exception as e:
    print("ERROR:", type(e).__name__)
    print(e)
