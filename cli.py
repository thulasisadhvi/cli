import argparse
from model_loader import load_model
from generator import generate_text

def main():
    parser = argparse.ArgumentParser(description="Local LLM CLI Tool")
    parser.add_argument("--model", required=True, help="Model name")
    parser.add_argument("--prompt", required=True, help="Input prompt")
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--max_new_tokens", type=int, default=100)

    args = parser.parse_args()

    try:
        tokenizer, model = load_model(args.model)
        generate_text(
            model,
            tokenizer,
            args.prompt,
            args.temperature,
            args.max_new_tokens
        )
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()