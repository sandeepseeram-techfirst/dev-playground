# LangChain 

LangChain is an open-source framework designed to help developers build applications powered by large language models (LLMs) — such as chatbots, agents, and AI-driven workflows — by connecting language models with external data, tools, and APIs in a structured way.

TL;DR LangChain makes the complicated parts of working and building with language models easier. It helps do this in two ways:

### Integration  
Bring external data, such as your files, other applications, and API data, to LLMs. 

### Agents 
Allows LLMs to interact with its environment via decision making and use LLMs to help decide which action to take next. 


Google's foundation models are officially integrated with the LangChain Python SDK, making it convenient to build applications with Google models using LangChain. The Google integrations also offer components for conveniently loading documents from BigQuery, Bigtable, Cloud SQL, Cloud Storage, Google Drive, and more data sources. You can also use many Google databases as vector stores. You can also call other models hosted in Vertex AI's Model Garden, like Anthropic's Claude or Meta's Llama from LangChain.

### Models
Models are the building block of LangChain providing an interface to different types of AI models. Large Language Models (LLMs), Chat and Text Embeddings models are supported model types.

### Prompts
Prompts refers to the input to the model, which is typically constructed from multiple components. LangChain provides interfaces to construct and work with prompts easily - Prompt Templates, Example Selectors and Output Parsers.

### Memory 
Memory provides a construct for storing and retrieving messages during a conversation which can be either short term or long term.

### Indexes 
Indexes help LLMs interact with documents by providing a way to structure them. LangChain provides Document Loaders to load documents, Text Splitters to split documents into smaller chunks, Vector Stores to store documents as embeddings, and Retrievers to fetch relevant documents.

### Chains
Chains let you combine modular components (or other chains) in a specific order to complete a task.

### Agents
Agents are a powerful construct in LangChain allowing LLMs to communicate with external systems via Tools and observe and decide on the best course of action to complete a given task.