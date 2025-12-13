from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

_model_cache = {}

def load_model(model_name):
    if model_name in _model_cache:
        return _model_cache[model_name]

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        dtype=torch.float16,
        device_map="auto"
    )

    _model_cache[model_name] = (tokenizer, model)
    return tokenizer, model