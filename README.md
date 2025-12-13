# Local LLM CLI Tool

This project is a simple command-line tool to run **local language models** using **Hugging Face Transformers**.  
It allows users to select the model, prompt, and generation parameters directly from the terminal.

The main goal is to understand how local LLM inference works without using any external APIs.

---

## Features
- Run LLMs locally
- Choose models from Hugging Face
- Control temperature and max tokens
- Streaming output for GPT-style models

---

## Installation

```bash
git clone https://github.com/<your-username>/llm_cli.git
cd llm_cli
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
##usage
```bash
python cli.py \
  --model gpt2 \
  --prompt "Explain machine learning in simple words." \
  --temperature 0.8 \
  --max_new_tokens 200
```
