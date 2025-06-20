# Placeholder for local model runner /local_model_runner.py

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import time


# Placeholder for local_runner.py
# This function runs a local model inference using the specified model name and prompt.
# It returns the generated text as a string.
# It uses the transformers library to load the model and tokenizer, and PyTorch for tensor operations


def run_local(model_name: str, prompt: str) -> str:
    try:
        # Check if the model is available locally
        AutoModelForCausalLM.from_pretrained(model_name)
    except OSError:
        print(
            f"Model '{model_name}' not found locally. Please ensure it is downloaded."
        )
        return ""

    try:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        torch_dtype = torch.float16 if device.type == device else torch.float32
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(
            model_name, torch_dtype=torch_dtype
        )
        # Tokenize once and move everything to the target device
        inputs = tokenizer(prompt, return_tensors="pt")
        inputs = {k: v.to(device) for k, v in inputs.items()}

        # Move model to device
        model = model.to(device)

        # Generate without gradients

        start_time = time.time()  # ⏳ capture start
        with torch.no_grad():
            outputs = model.generate(
                **inputs, pad_token_id=tokenizer.eos_token_id, max_length=100
            )
        end_time = time.time()  # ⏹️ capture end
        duration = end_time - start_time
        print(f"⏱️ Generation took {duration:.2f} seconds.")

    except Exception as e:
        print(f"An error occurred during model inference: {e}")
        return ""

    # Convert the output tensor to text
    outputText = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Return the generated text
    if not outputText:
        print(" No response generated.")
        return "NO RESPONSE!!"

    return outputText
