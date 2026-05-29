from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

#TEXT model
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

coversation = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(coversation.choices[0].message.content)

#EMB model
response = client.embeddings.create(
    input="Hello world",
    model="text-embedding-3-small"
)
print(response)