import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Prompt 1 — Basic
prompt = """
What is Jenkins?
"""

# Prompt 2 — Add a Role
prompt2 = """
You are a Senior DevOps Engineer.
Explain Jenkins to a beginner.
"""

# Prompt 3 — Add Structure
prompt3 = """
You are a Senior DevOps Engineer and DevOps Coach.

Explain Jenkins to a beginner.

Provide:

1. What is Jenkins?
2. Why do companies use Jenkins?
3. How does Jenkins fit into CI/CD?
4. Give one real-world example.

Keep the explanation simple.
"""
response = client.responses.create(
    model="gpt-5.2",
    input=prompt3
)

print(response.output_text)
