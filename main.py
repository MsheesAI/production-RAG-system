from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

load_dotenv()

def main():
    llm = ChatOpenAI(model="gpt-4o-mini")
    response = llm.invoke("What is the capital of France?")
    print(response.content)

if __name__ == "__main__":
    main()