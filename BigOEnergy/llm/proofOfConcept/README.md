# 🚀 LLM Design Experiments  

This repo documents my ongoing experiments in designing and iterating on large language model (LLM) behavior.  
The project is a **work in progress** — I’m tracking versions as I test new models, tweak generation settings, and learn about instruction vs. completion style LLMs.  

---

## 📖 Progress Log  

### **v0.0.1 — First Steps with GPT-2**  
- **Model:** `gpt2` (base)  
- **Issue:** Severe repetition and looping text.  
- **Example:**  
  > Once upon a time, the world was a place of great beauty and great danger. The world was a place of great danger, and the world was a place of great danger...  
- **Learned:**  
  - GPT-2 is a **completion model**, not an **instruction model**.  
  - Out-of-the-box, it extends text rather than following instructions.  

---

### **v0.1.0 — Tweaking Generation Settings**  
- Adjusted **decoding settings**:  
  - `temperature` (controls randomness)  
  - `top_p` / `top_k` (controls diversity and reduces loops)  
  - `repetition_penalty` (discourages echoes)  
- **Results:**  
  - Avoided infinite loops.  
  - More coherent samples, though still completive rather than conversational.  
- **Limitation:**  
  - Still no instruction-following behavior.  
  - Responses often verbose and unfocused.  

---

### **v1.0.0 — Upgrading to GPT-2 Medium**  
- **Model:** `gpt2-medium`  
- **Results:**  
  - More conversational than base GPT-2.  
  - But… issues with:  
    - Rambling / incoherent answers  
    - No clear Q&A structure  
    - Hallucinations (fake facts, studies)  
    - Weak sentence structure  

---

### **v1.1.0 — Prompt Engineering + Focused Settings**  
- Refined **prompts** + stricter decoding:  
  - Lower `temperature` for less randomness.  
  - Lower `top_k` and `top_p` for tighter responses.  
  - Higher `repetition_penalty` for less echo.  
  - Reduced `max_tokens` for concise outputs.  
- **Results:**  
  - Better answers than before.  
  - Still suffers from hallucinations and inconsistent conversational flow.  
- **Takeaway:**  
  - Using prebuilt GPT-2 models can only go so far.  
  - Instruction-following requires either fine-tuning or moving to models built for chat.  

---


### **v2.1.0 — Traingn my GTPT2s**  

different gpus for different things in model.py

```
import torch

# Better device detection for Apple Silicon
if torch.backends.mps.is_available():
    device = torch.device("mps")  # Use Apple Metal GPU
elif torch.cuda.is_available():
    device = torch.device("cuda")  # Use NVIDIA GPU (unlikely on Mac)
else:
    device = torch.device("cpu")   # Use CPU as fallback

print(f"Using device: {device}")
```

mps for mac

prcision setting 

`torch_dtype=torch.float16 if device.type == "mps" else torch.float32`

On MPS using float16 half the mem but faster computaion 

But can be less precusine and potential for numerical instability 

Where as float32 is more accurate and stable but using more mem and is slower


apple gpus have limied VRAM compared to dedicated GPUS so flaot16 helps fit into larger models memeory

return Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
RuntimeError: MPS backend out of memory (MPS allocated: 16.06 GB, other allocations: 1.32 GB, max allowed: 18.13 GB). Tried to allocate 785.27 MB on private pool. Use PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0 to disable upper limit for memory allocations (may cause system failure).

Memory Overflow Issue Summary
Problem:
Your Mac Mini ran out of memory (18GB unified RAM exceeded) while training GPT-2 on your anime dataset, causing:

Runtime crash with MPS out of memory error
Loss became nan (not a number) indicating numerical instability

Root Cause:

Batch size of 4 with sequence length 512 was too memory-intensive
GPT-2 (124M parameters) in float16 + activations + gradients exceeded available memory
876 training conversations being processed in batches of 4

Solution:
Reduce memory footprint by:

Lower batch size: 4 → 1
Shorter sequences: 512 → 256 tokens
Gradient accumulation: Accumulate gradients over 4 steps before updating weights (simulates batch_size=4 without the memory cost)
Lower learning rate: 5e-5 → 3e-5 (helps with nan loss stability)

Trade-offs:

Training will be slower (4x more forward passes)
Shorter sequences mean truncated conversations
Still achieves similar results through gradient accumulation

This is a common issue when training language models on consumer hardware with limited memory.

- **Results:**  

- **Takeaway:**  
 

---

## 🔮 Next Steps / Ideas  
- Try **instruction-tuned models** (e.g. GPT-NeoX, LLaMA-based, T5, FLAN, etc.).  
- Explore **fine-tuning GPT-2** with a conversational dataset (Q&A / instruction data).  
- Experiment with **RLHF-style techniques** (human preference scoring).  
- Build a **wrapper layer** that reformats user input → completion → structured conversational output.  

---

## 📝 Notes  
This repo is less about "building the best LLM" right away and more about:  
- Learning the difference between **completion models** and **instruction models**.  
- Understanding how **decoding strategies** impact coherence and repetition.  
- Documenting pitfalls (hallucinations, rambling, incoherence).  
