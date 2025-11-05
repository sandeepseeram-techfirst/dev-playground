# AI Concepts 

##### Large Language Model (LLM) 
is a neural network trained to predict the next token in a sequence (e.g., “all that glitters” → “is not gold”).

##### Tokenization 
splits text into tokens (words, subwords, suffixes like “ing”) that models can understand, while vectorization maps tokens into high‑dimensional vectors where similar meanings are close together.

##### Attention 
lets the model focus on relevant surrounding words to resolve ambiguity (e.g., “tasty apple” vs “Apple revenue”), and self‑supervised learning trains models by hiding parts of existing data and asking the model to predict them without manual labels.

##### Transformer 
is the specific architecture that stacks attention and feed‑forward layers to repeatedly refine token representations before predicting the next token.

##### Fine‑tuning 
takes a base model and trains it on curated question‑answer pairs so it behaves in a specific way (e.g., medical, financial, or customer‑support assistant).

##### Few‑shot prompting 
improves answers by sending example Q&A pairs along with the user’s query, while Retrieval‑Augmented Generation (RAG) adds relevant documents (like policies or manuals) fetched at runtime.

##### A vector database 
stores document embeddings so the system can find semantically similar documents to a query. 

### Model Context Protocol (MCP) 
lets models call external tools/servers (e.g., airline APIs) to fetch live data or perform actions.

### Context engineering 
combines all of this: examples, retrieved documents, MCP tools, plus tricks like summarizing long histories or remembering user preferences so the model always has the right context.

##### AI Agents 
are long‑running processes that orchestrate LLM calls, tools, and other agents to complete multi‑step tasks (like planning and booking a full trip) instead of just answering one prompt.




