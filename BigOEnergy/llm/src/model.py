from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os
from pathlib import Path

def setup_model_and_tokenizer(model_name="gpt2", device=None):
    print(f'setting up model: {model_name}')

    if device is None:
        device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
        print(f"Using {device}")
    
    print("Loading tokenizer")
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    #Adding padding token
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        print("Added padding token 👍")

    print("Loading the model")
    # Precision testing
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype = torch.float16 if device.type == 'mps' else torch.float32,
        device_map = 'auto' if device.type == 'mps' else None
    )

    # if we add new tokens
    if len(tokenizer) != model.config.vocab_size:
        model.resize_token_embeddings(len(tokenizer))
        print("Resized model embeddings")

    if device.type == 'cpu':
        model = model.to(device)
    
    print(f"Model setup complete 👍")
    print(f"   Model parameters: {get_model_parameters(model):,}")
    print(f"   Vocab size: {len(tokenizer):,}")

    return model, tokenizer, device

def get_model_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

def save_model(model, tokenizer, save_path, config=None):
    """
    Save trained model and tokenizer
    
    Args:
        model: Trained model
        tokenizer: Tokenizer
        save_path: Directory to save to
        config: Optional config to save
    """
    print(f"Saved to {save_path}")

    Path(save_path).mkdir(parents=True, exist_ok=True)

    model.save_pretrained(save_path)
    tokenizer.save_pretrained(save_path)

    if config:
        import json
        with open(f"{save_path}/training_config.json", 'w') as f:
            json.dump(vars(config), f, indent=2)
    
    print(f"Model saved 👍")

def loaded_trained_model(model_path, device=None):
    print(f"Loading training model from {model_path}")
    if device == None:
        device = torch.device("mps" if torch.mps.is_available() else "cpu")

    tokenizer = AutoTokenizer.from_pretrained(model_path)

    model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype = torch.float16 if device.type == 'mps' else torch.float32,
            device_map='auto' if device.type =='mps' else None

    )

    if device.type =='cpu':
        model = model.to(device)

    print(f"Loaded model wiith {get_model_parameters(model)}: parameters")

    return model, tokenizer, device

def prepare_model_for_training(model, learning_rate=5e-5):
    print("preparing model for training")

    model.train()

    optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)

    print(f"✅ Training setup complete!")
    print(f"   Learning rate: {learning_rate}")
    print(f"   Optimizer: AdamW")
    
    return model, optimizer

def get_model_info(model, tokenizer):
    info = {
        "model_type": model.config.model_type,
        "num_parameters": get_model_parameters(model),
        "vocab_size": len(tokenizer),
        "max_position_embeddings": model.config.max_position_embeddings,
        "num_layers": model.config.num_hidden_layers,
        "hidden_size": model.config.hidden_size,
        "num_attention_heads": model.config.num_attention_heads,
    }

    return info

def print_model_info(model, tokenizer):
    """Print detailed model information"""
    info = get_model_info(model, tokenizer)
    
    print("\n📊 Model Information:")
    print(f"   Type: {info['model_type']}")
    print(f"   Parameters: {info['num_parameters']:,}")
    print(f"   Vocab size: {info['vocab_size']:,}")
    print(f"   Max sequence length: {info['max_position_embeddings']:,}")
    print(f"   Layers: {info['num_layers']}")
    print(f"   Hidden size: {info['hidden_size']}")
    print(f"   Attention heads: {info['num_attention_heads']}")

def quick_setup(model_name='gpt2'):
    return setup_model_and_tokenizer(model_name)

def production_setup(model_name='gpt2', save_base_model=True):
    model, tokenizer, device = setup_model_and_tokenizer(model_name)

    if save_base_model:
        save_model(model, tokenizer, f"models/base/{model_name}")
        print(f"saved to models/base/{model_name}")
    
    return model, tokenizer, device

 






