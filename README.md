# 🚀 AI-Assisted DevOps Hands-on Labs

Welcome to the **AI-Assisted DevOps Hands-on Labs**.

This repository is designed to help DevOps engineers learn how to use **Generative AI, Large Language Models (LLMs), Prompt Engineering, AI Assistants, and AI Agents** to improve DevOps productivity.

Repository:

```text
https://github.com/akannan1087/ai-basics-labs-repo
```

---

# 🖥️ Lab Environment

For these labs, we will use:

* AWS EC2
* Ubuntu 24.04 LTS
* t2.small
* Python 3
* Git
* Python Virtual Environment
* OpenAI Python SDK
* OpenAI API

---

# ☁️ Step 1 — Create Ubuntu EC2 Instance

Create an EC2 instance with:

```text
OS            : Ubuntu 24.04 LTS
Instance Type : t2.small
Storage       : 10 GB+
Security      : Allow SSH - Port 22
```

---

# 🔐 Step 2 — Connect to EC2

```bash
ssh -i your-key.pem ubuntu@EC2-PUBLIC-IP
```

---

# 🔄 Step 3 — Update Ubuntu

```bash
sudo apt update
```

Verify:

```bash
cat /etc/os-release
```

You should see:

```text
Ubuntu 24.04 LTS
```

---

# 🐍 Step 4 — Verify Python

```bash
python3 --version
```

Ubuntu 24.04 normally includes Python 3.

---

# 📦 Step 5 — Install Required Packages

```bash
sudo apt install git python3-pip python3-venv -y
```

Verify:

```bash
git --version
pip3 --version
```

---

# 🔑 Step 6 — Create OpenAI API Key

Go to:

```text
https://platform.openai.com/
```

Login to your OpenAI account.

Navigate to:

```text
Dashboard
   ↓
API Keys
   ↓
Create new secret key
```

Give the key a name such as:

```text
coachdevops-ai-labs
```

Copy and save the API key securely.

⚠️ **Never share or commit your API key to GitHub.**

> Note: ChatGPT subscription and OpenAI API usage are separate. API usage may require billing or credits.

---

# 📥 Step 7 — Clone the Repository

```bash
git clone https://github.com/akannan1087/ai-basics-labs-repo.git
```

Verify:

```bash
ls
```

You should see:

```text
ai-basics-labs-repo
```

Enter the repository:

```bash
cd ai-basics-labs-repo
```

---

# 🌿 Step 8 — Create Python Virtual Environment

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

Your terminal should now show:

```text
(venv)
```

Example:

```text
(venv) ubuntu@ip-172-31-xx-xx:~/ai-basics-labs-repo$
```

---

# 📦 Step 9 — Install Python Dependencies

Upgrade pip:

```bash
pip install --upgrade pip
```

Install:

```bash
pip install openai python-dotenv
```

Verify:

```bash
pip list
```

You should see:

```text
openai
python-dotenv
```

---

# 🔐 Step 10 — Configure OpenAI API Key

Create the `.env` file:

```bash
nano .env
```

Add:

```text
OPENAI_API_KEY=your-openai-api-key
```

Save in nano:

```text
CTRL + O
Enter
CTRL + X
```

---

# ⚠️ Protect Your API Key

Never commit `.env` to GitHub.

Make sure `.gitignore` contains:

```text
.env
venv/
__pycache__/
```

Verify:

```bash
cat .gitignore
```

---

# 🧪 Step 11 — Run AI Lab 01

Navigate to Lab 01:

```bash
cd ai-lab-01
```

Verify:

```bash
ls
```

You should see:

```text
hello-ai.py
README.md
```

Run:

```bash
python hello-ai.py
```

---

# 🤖 Expected Flow

```text
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
```

---

# ✅ Expected Result

You should see output similar to:

```text
Sending question to CoachDevOps AI...

============================================================
🤖 CoachDevOps AI Response
============================================================

CI/CD stands for Continuous Integration
and Continuous Delivery/Deployment.

...

============================================================
AI Lab 01 Completed Successfully!
============================================================
```

🎉 Congratulations!

You have successfully executed your first **AI-powered DevOps application**.

---

# 🔄 How to Continue Later

When you reconnect to the EC2 instance:

```bash
cd ~/ai-basics-labs-repo
```

Activate the environment:

```bash
source venv/bin/activate
```

Navigate to a lab:

```bash
cd ai-lab-01
```

Run:

```bash
python hello-ai.py
```

---

# 🔄 Get Latest Lab Updates

To download newly added labs:

```bash
cd ~/ai-basics-labs-repo

git pull
```

---

# 🗺️ Learning Journey

```text
AI Lab 01
First LLM Call
      ↓
AI Lab 02
Prompt Engineering
      ↓
AI Lab 03
DevOps AI Assistant
      ↓
AI Lab 04
Multiple DevOps AI Experts
      ↓
AI Lab 05
Web-Based AI Assistant
      ↓
Tool Integration
      ↓
AI Agent
      ↓
SRE Agent
```

---

# 🚀 Happy Learning!

**CoachDevOps — AI-Assisted DevOps Hands-on Labs**

> Learn AI Basics. Apply AI to DevOps. Automate Intelligently.
