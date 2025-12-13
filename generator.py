from transformers import TextStreamer

def generate_text(model, tokenizer, prompt, temperature, max_new_tokens):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    streamer = TextStreamer(
        tokenizer,
        skip_prompt=True,
        skip_special_tokens=True
    )

    model.generate(
    **inputs,
    do_sample=True,           # 🔥 REQUIRED
    temperature=temperature,
    max_new_tokens=max_new_tokens,
    streamer=streamer
    ) 