# What is a Vector Database? 

## Definition  
A **vector database** is a database designed to store, index, and query **vector embeddings** — numerical representations of unstructured data like text, images, or audio.  

## What are Vector Embeddings?  
- These are numerical vectors (lists of numbers) that capture semantics of the data: items that are similar semantically end up close in vector-space.  
- Allows things like “find items that are similar to this query” based on distance in that space.  
- Vector databases enable storage and retrieval of those embeddings for building things like semantic search, recommendation, knowledge-base retrieval.

## How It Works  
- Since vectors don’t have a natural linear ordering (unlike numbers or text), you need specialized indexes.  
- Common query: “Find the *k* nearest vectors to this query vector” by metrics like cosine similarity, dot product, Euclidean distance.  
- Indexing strategies include: clustering vectors, graphs connecting nearest neighbours, trees partitioning vector space, etc.  
- Example: ScaNN (from Google Research) is used under the hood of Google’s “Vector Search” to power efficient nearest-neighbour queries.

## Why It Matters  
- As generative AI, search, recommendations, and retrieval workflows become more semantic (understanding meaning rather than keywords), vector databases are core infrastructure.  
- With the rise of large language models and embedding-based retrieval, storing and querying embeddings at scale is increasingly important.  
- Google suggests that eventually *every* database may support vector embeddings as a first-class feature.

## Use Cases  
- Semantic search: “Find documents that are semantically similar to this query.”  
- Recommendation systems: “Find users/items similar in embedded space.”  
- Knowledge base retrieval in LLM/RAG (retrieval-augmented generation) workflows: embed text, store in vector DB, query to provide context to a model.  
- Multi-modal search: combining embeddings of images + text to allow “find images similar to this text prompt”.

## Considerations / Architecture Implications  
- You need infrastructure that supports efficient indexing and querying of high-dimensional vectors—performance matters (latency, throughput).  
- Data modelling: embedding generation, storage (along with metadata), indexing, query interface.  
- Choice of system: some databases are “pure” vector DBs; others are general-purpose DBs which now add vector support.  
- On Google Cloud many of their database services now include vector support or integrate with “Vector Search” offerings.

---

## Summary  
A vector database is a specialized storage + query system for semantic embeddings of unstructured data. It enables similarity-based queries (e.g., “what is most like this?”) rather than exact key lookups. As AI/ML workloads proliferate (embeddings, semantic search, RAG), vector databases are becoming foundational infrastructure.

