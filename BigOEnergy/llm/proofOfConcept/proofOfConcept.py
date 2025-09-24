from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "gpt2-medium"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

def generate_text(question):

    prompt = f"""Answer the following question clearly and concisely:
Question: {question}    
Answer:"""

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, 
                             max_new_tokens=50,
                             do_sample=True,
                             top_k=30, # avoid loops
                             top_p=0.85, # avoid loops
                             temperature=0.5, # less randomness
                             repetition_penalty=1.3,
                             pad_token_id=tokenizer.eos_token_id) # forces it not to echo itself 
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return response.split("Answer:")[-1].strip()

print(generate_text("What is Python?"))
print(generate_text("how do neural networks work?"))