# 🚀 AI News Summarizer and LinkedIn Post Generator

This project creates an AI agent that fetches the latest AI news, summarizes it, and generates a LinkedIn post about the most relevant news item. It is built using the **smolagents** framework from Hugging Face, a minimalist AI agent library designed for simplicity and efficiency.

## ✨ Features

- 📰 Fetches the most recent AI news from an RSS feed
- 🧠 Summarizes the news using an AI agent
- 📝 Generates a LinkedIn post based on the summarized news
- 🤖 Supports OpenAI API and Ollama for local models
- 📦 Dependency management using `uv`

## 🔧 Prerequisites

- 🐍 Python 3.7+
- 🔑 OpenAI API key

## 📥 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ai-news-summarizer.git
cd ai-news-summarizer
```

2. Install the required dependencies:

```bash
uv sync --frozen --no-cache
```

3. Set up your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY='your-api-key-here'
```

## ▶️ Usage

Run the main script:

```bash
python main.py
```

The script will fetch the latest AI news, summarize it, and generate a LinkedIn post.

## 📂 Project Structure

- `main.py` 📌 Entry point of the application
- `agents.py` 🏗 Contains the agent creation logic using smolagents
- `models.py` ⚙️ Handles model selection and initialization
- `tools.py` 🛠 Defines utility functions used by the agents
- `prompts.py` 📝 Contains prompt templates for the agents

## 🤖 About SmolAgents

**Smolagents** is a minimalist AI agent framework developed by the Hugging Face team. It allows developers to create and run powerful AI agents with minimal code, focusing on simplicity and efficiency. Smolagents supports code agents, which write and execute Python code snippets to perform actions, enhancing efficiency and flexibility.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 🚀

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
