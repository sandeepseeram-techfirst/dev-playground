### Transformer Model

What a transformer model is? 
A transformer is a deep learning architecture introduced in the paper **“Attention Is All You Need,”** and it underpins most modern generative AI systems.

Its key strength is **attention**, which lets the model understand relationships between words in a sentence and scale efficiently using parallel computation on large hardware (like GPUs).

#### High-level Architecture  
Text input (tokens) → Embeddings (vectors) → Transformer layers with attention → Probability distribution over next token → Chosen next word.

#### How the model reasons (conceptually)
It encodes each word (quick, brown, fox, jumps, over, the, lazy) into a vector in some high‑dimensional space.
​It uses attention to compare how strongly each word relates to potential next words (person, rabbit, dog, etc.).
​It evaluates both semantic compatibility and statistical frequency learned from huge text corpora.

Each step is run in parallel across tokens, which is why transformers can scale to long sequences and large models.

### Autoregressive Generation Flow 
Prompt → Model predicts next token → Append token → Feed back into model → Repeat, forming longer text.
This loop, powered by the transformer architecture and attention on large datasets, is the core mechanism behind modern generative text models.
​