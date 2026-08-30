# ai-basics-labs-repo
🚀 AI-Assisted DevOps Hands-on Labs

Welcome to the AI-Assisted DevOps Hands-on Labs.

This repository is designed to help DevOps engineers learn how to use Generative AI, Large Language Models (LLMs), and AI Agents to improve DevOps productivity.

Repository:

https://github.com/akannan1087/ai-basics-labs-repo
🖥️ Lab Environment

For these labs, we will use:

AWS EC2
Ubuntu 24.04 LTS
Python 3
Git
Python Virtual Environment
OpenAI Python SDK

☁️ Step 1 — Create an Ubuntu EC2 Instance with instance type t2.small

🔐 Step 2 — Connect to the EC2 Instance

🔄 Step 3 — Update Ubuntu

After connecting to the EC2 instance:
sudo apt update

Verify Ubuntu version:
cat /etc/os-release

You should see something similar to:
Ubuntu 24.04 LTS

🐍 Step 4 — Verify Python

Ubuntu 24.04 normally includes Python 3.

Verify:
python3 --version

📦 Step 5 — Install Python Virtual Environment Support

Install the required Python packages:
sudo apt install python3-pip python3-venv -y
Verify pip:
pip3 --version

📥 Step 6 — Clone the AI Labs Repository
Clone the repository:

git clone https://github.com/akannan1087/ai-basics-labs-repo.git

Verify:
ls

You should see:
ai-basics-labs-repo

Enter the repository:
cd ai-basics-labs-repo

🌿 Step 7 — Create a Python Virtual Environment

From inside the repository:

python3 -m venv venv

Activate the virtual environment:

source venv/bin/activate

Your terminal should now show:

(venv)

Example:

(venv) ubuntu@ip-172-31-xx-xx:~/ai-basics-labs-repo$

📦 Step 8 — Install Python Dependencies

Upgrade pip:
pip install --upgrade pip
Install the required packages:
pip install openai python-dotenv

Verify:

pip list

You should see packages such as:

openai
python-dotenv

🔑 Step 9 — Configure the OpenAI API Key
nano .env

Add:

OPENAI_API_KEY=your-openai-api-key

Save the file.
In nano:
CTRL + O Enter CTRL + X

⚠️ Important — Protect Your API Key

Never commit your .env file to GitHub.

Verify .gitignore contains:

.env
venv/
__pycache__/

You can verify with:

cat .gitignore

🧪 Step 10 — Run AI Lab 01
Navigate to the AI Lab 01 directory if the lab is stored in a separate folder:

cd ai-lab-01

Verify files:

ls

You should see something similar to:

hello-ai.py
README.md

Run the application:

python hello-ai.py

🤖 Expected Flow
DevOps Engineer
       |
       | Prompt
       ↓
hello-ai.py
       |
       | API Request
       ↓
OpenAI API
       |
       ↓
LLM
       |
       ↓
AI Response
       |
       ↓
Ubuntu Terminal

✅ Expected Result

You should see output similar to:

Sending question to CoachDevOps AI...

============================================================
🤖 CoachDevOps AI Response
============================================================

CI/CD stands for Continuous Integration and
Continuous Delivery/Deployment.

...

============================================================
AI Lab 01 Completed Successfully!
============================================================

🔄 How to Continue the Lab Later

When you reconnect to your EC2 instance:

cd ~/ai-basics-labs-repo

Activate the virtual environment:

source venv/bin/activate

Then navigate to the required lab.

Example:

cd ai-lab-01

Run:

python hello-ai.py
