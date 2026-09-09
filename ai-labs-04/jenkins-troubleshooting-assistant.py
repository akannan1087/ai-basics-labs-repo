import os

from dotenv import load_dotenv
from openai import OpenAI

# ---------------------------------------------------------
# AI Lab 04 - AI-Powered Jenkins Troubleshooting Assistant
# ---------------------------------------------------------

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("ERROR: OPENAI_API_KEY is not configured.")
    exit()

client = OpenAI(api_key=api_key)

system_prompt = """
You are a Senior Jenkins and DevOps Engineer.

Analyze Jenkins build errors and help junior DevOps engineers
understand and fix the problem.

Always provide:

1. Problem
2. Probable Root Cause
3. Recommended Fix
4. Commands or Configuration Changes
5. How to Verify the Fix

Keep the response simple and practical.
"""

print("\n🤖 CoachDevOps Jenkins Troubleshooting Assistant")
print("=" * 60)

jenkins_error = input(
    "\nPaste your Jenkins build error:\n"
)

print("\nAnalyzing Jenkins error...\n")

response = client.responses.create(
    model="gpt-5.2",
    input=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": jenkins_error
        }
    ]
)

print("=" * 60)
print("🔍 Jenkins Troubleshooting Report")
print("=" * 60)

print(response.output_text)

print("\n" + "=" * 60)
print("AI Lab 04 Completed Successfully! 🚀")
print("=" * 60)
