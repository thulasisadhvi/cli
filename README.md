# CLI Text Generator
## Overview

This project is a Python-based Command Line Interface (CLI) tool for generating text using Hugging Face Transformers.
It supports multiple models, configurable generation parameters, and streaming output where tokens are displayed progressively in the terminal.

This tool is designed to demonstrate correct usage of the transformers library, clean CLI design, and robust error handling.

---

## Features
- Run LLMs locally
- Choose models from Hugging Face
- Control temperature and max tokens
- Streaming output for GPT-style models

---

## Requirements
-Python 3.9 or higher
-pip
-Internet connection (models are downloaded from Hugging Face on first run)

---

## SET UP
## clone the repository

```bash
git clone https://github.com/thulasisadhvi/cli.git
cd cli
```

## Install dependencies

```bash
pip install -r requirements.txt
```
## usage
Basic text generation
```bash
python cli.py \
  --model gpt2 \
  --prompt "Explain machine learning in simple words." \
  --temperature 0.8 \
  --max_new_tokens 200
```
