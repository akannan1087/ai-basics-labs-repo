import os

from dotenv import load_dotenv
from openai import OpenAI


# ---------------------------------------------------------
# AI Lab 03 - Build Your First DevOps AI Assistant
# ---------------------------------------------------------

# Load environment variables from .env
load_dotenv()

# Get OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("ERROR: OPENAI_API_KEY is not configured.")
    print("Please add your API key to the .env file.")
    exit()


# Create OpenAI client
client = OpenAI(api_key=api_key)


# ---------------------------------------------------------
# System Prompt - Defines how the AI Assistant should behave
# ---------------------------------------------------------

system_prompt = """
You are a Senior DevOps Engineer and DevOps Coach.

Help students learn and troubleshoot:

- CI/CD
- Jenkins
- Git and GitHub
- Docker
- Kubernetes
- Terraform
- AWS
- Azure
- DevSecOps
- SRE

Always provide:

1. Simple Explanation
2. Recommended Solution
3. Commands or Code when useful
4. Best Practices
5. Learning Tips

Keep the response beginner-friendly.
"""


# ---------------------------------------------------------
# Get question from student
# ---------------------------------------------------------

user_question = input(
    "\nEnter your DevOps question: "
)


print("\nAnalyzing your question...\n")


# ---------------------------------------------------------
# Send System Prompt + User Question to LLM
# ---------------------------------------------------------

response = client.responses.create(
    model="gpt-5.2",
    input=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_question
        }
    ]
)


# ---------------------------------------------------------
# Display AI Response
# ---------------------------------------------------------

print("=" * 60)
print("🤖 CoachDevOps AI Assistant")
print("=" * 60)

print(response.output_text)

print("\n" + "=" * 60)
print("AI Lab 03 Completed Successfully! 🚀")
print("=" * 60)
