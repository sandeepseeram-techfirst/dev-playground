### Augmenting the LLM: Memory, Tools, Planning

**Memory:** Vanilla LLMs are stateless and forget past turns; memory modules (short-term and long-term) re-inject or store past interactions, but must manage information overload via context engineering to balance amount vs quality of context.

**Tools:** LLMs are text-in/text-out and can only express an intent to act (e.g., “multiply(2.3, 8.1)”), so external software must parse this text and actually invoke tools; Chapter 5 covers tool use patterns and the Model Context Protocol to standardize tool interfaces.

