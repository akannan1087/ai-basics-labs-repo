import os

from dotenv import load_dotenv
from openai import OpenAI


# ---------------------------------------------------------
# AI Lab 01 - Build Your First AI-Powered DevOps Assistant
# ---------------------------------------------------------


# Load environment variables from the .env file
load_dotenv()


# Get OpenAI API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")


# Check if API key exists
if not api_key:
    print("ERROR: OPENAI_API_KEY is not configured.")
    print("Please add your API key to the .env file.")
    exit()


# Create OpenAI client
client = OpenAI(api_key=api_key)

# Create a simple DevOps prompt
prompt = """
You are a Senior DevOps Engineer and DevOps Coach.

Explain CI/CD in simple terms for a beginner.

Please provide:

1. What is CI?
2. What is CD?
3. Why do companies use CI/CD?
4. Give one simple real-world example.
"""


print("Sending question to CoachDevOps AI...\n")


# Send prompt to the AI model
response = client.responses.create(
    model="gpt-5.2",
    input=prompt
)


# Display AI response
print("=" * 60)
print("🤖 CoachDevOps AI Response")
print("=" * 60)

print(response.output_text)

print("\n" + "=" * 60)
print("AI Lab 01 Completed Successfully! 🚀")
print("=" * 60)
