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
