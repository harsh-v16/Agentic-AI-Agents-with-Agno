<div align="center">

# Agentic AI with Agno

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Agno](https://img.shields.io/badge/Framework-Agno-blue?style=for-the-badge)](#)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--5-412991?style=for-the-badge&logo=openai&logoColor=white)](https://platform.openai.com/)
[![LLM](https://img.shields.io/badge/LLM-Agentic%20AI-success?style=for-the-badge)](#)

> A collection of practical Agentic AI examples built with the Agno framework, demonstrating tool-enabled agents, financial assistants, memory-enabled agents, and multi-agent collaboration using OpenAI GPT models.

</div>

---

# 📖 Project Overview

This repository contains a collection of Agentic AI examples developed using the **Agno Framework** and **OpenAI GPT models**.

Instead of creating a single chatbot, this project explores different capabilities of modern AI agents, including:

- Tool Calling
- Web Search
- Financial Analysis
- Persistent Memory
- Multi-Agent Collaboration

Each example demonstrates a core concept commonly used when building production-ready AI agents.

---

# 🤖 Examples Included

## 🌍 Travel Research Agent

A travel assistant capable of searching the web for travel-related information using DuckDuckGo.

### Features

- Web Search
- Travel Assistance
- Real-time Information Retrieval
- Date & Time Awareness

Example Query

```text
Is it safe to travel to UAE today?
```

---

## 📈 Financial Research Agent

An investment research assistant that combines Yahoo Finance with web search.

### Features

- Stock Price Lookup
- Analyst Recommendations
- Company Fundamentals
- Financial Research

Example Query

```text
Share the MSFT stock price and analyst recommendations.
```

---

## 🧠 Memory-enabled AI Agent

A conversational AI agent capable of remembering user information using a SQLite database.

### Features

- Persistent User Memory
- Conversation History
- Personalized Responses
- Long-Term Memory

Example

```text
User:
I am Rahul and I am a Data Analyst.

↓

Later...

Who am I?

↓

Agent:
You are Rahul and you are a Data Analyst.
```

---

## 👥 Multi-Agent Team

Demonstrates collaboration between multiple specialized AI agents.

Agents included:

- 🇬🇧 English Agent
- 🇨🇳 Chinese Agent
- 🇮🇳 Hindi Agent

A Team Leader coordinates all agents to answer the same query in different languages.

Example Query

```text
What is the capital of India?
```

---

# 🧠 Agent Architecture

```text
                  User

                    │

                    ▼

             OpenAI GPT Model

                    │

      ┌─────────────┼─────────────┐

      ▼             ▼             ▼

 Travel Agent   Finance Agent   Memory Agent

                    │

                    ▼

             Multi-Agent Team

                    │

                    ▼

             AI Generated Response
```

---

# 🚀 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Agno | AI Agent Framework |
| OpenAI GPT | Language Model |
| DuckDuckGo Search | Web Search |
| Yahoo Finance | Financial Data |
| SQLite | Persistent Memory |
| dotenv | Environment Variables |

---

# 📂 Project Structure

```text
Agentic-AI-with-Agno/
│
├── travel_agent.py
├── finance.py
├── memory.py
├── team.py
│
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

---

# 🖥️ Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/harsh-v16/Agentic-AI-with-Agno.git

cd Agentic-AI-with-Agno
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Configure Environment Variables

Create a `.env` file in the project root and add your OpenAI API key.

```text
OPENAI_API_KEY=your_openai_api_key_here
```

---

## 4️⃣ Run Any Agent

### Travel Research Agent

```bash
python travel_agent.py
```

### Financial Research Agent

```bash
python finance.py
```

### Memory-enabled Agent

```bash
python memory.py
```

### Multi-Agent Team

```bash
python team.py
```

---

# 📦 Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains all the required Python libraries for running every agent in this repository.

---

# 🔐 Environment Variables

This project uses the OpenAI API.

Create a `.env` file using the provided `.env.example` file.

Example:

```text
OPENAI_API_KEY=your_openai_api_key_here
```

---

# 🎯 Learning Outcomes

Through this repository, I explored several core concepts of Agentic AI, including:

- Building AI agents using the Agno Framework
- Integrating OpenAI GPT models into applications
- Tool Calling with external services
- Real-time web search using DuckDuckGo
- Financial data retrieval using Yahoo Finance
- Persistent memory with SQLite
- Managing conversation history
- Multi-Agent collaboration and orchestration
- Context-aware AI responses
- Environment variable management for secure API usage

---

# 🔮 Future Improvements

- 🌐 Build a Streamlit or Flask web interface
- 🤖 Add support for additional specialized agents
- 🧩 Integrate more external tools and APIs
- 🗄️ Replace SQLite with PostgreSQL or a vector database
- 📄 Add PDF document question answering
- 🧠 Implement Retrieval-Augmented Generation (RAG)
- 🔄 Build autonomous multi-agent workflows
- ☁️ Deploy the agents as cloud-hosted APIs

---

# 🤝 Contributing

Contributions, suggestions, and improvements are always welcome.

If you'd like to enhance these Agentic AI examples, feel free to fork this repository, open an issue, or submit a pull request.

---

# 👤 Author

<div align="center">

**Harsh Chaudhary**

AI Engineer | Machine Learning • Deep Learning • Generative AI Enthusiast

[![GitHub](https://img.shields.io/badge/GitHub-harsh--v16-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/harsh-v16)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Harsh%20Chaudhary-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/harsh-chaudhary-6ba5b8395)

</div>

---

<div align="center">

### ⭐ If you found this repository useful, consider giving it a star!

It motivates me to continue building and sharing practical AI, LLM, and Agentic AI projects with the community.

**Thank you for visiting this repository! 🚀**

</div>
