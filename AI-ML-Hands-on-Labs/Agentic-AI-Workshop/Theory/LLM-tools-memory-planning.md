### Augmenting the LLM: Memory, Tools, Planning

**Memory:** Vanilla LLMs are stateless and forget past turns; memory modules (short-term and long-term) re-inject or store past interactions, but must manage information overload via context engineering to balance amount vs quality of context.

**Tools:** LLMs are text-in/text-out and can only express an intent to act (e.g., “multiply(2.3, 8.1)”), so external software must parse this text and actually invoke tools; This workshop covers tool use patterns and the Model Context Protocol to standardize tool interfaces.

**Planning & reflection:** Agents decompose tasks into plans, execute steps sequentially (often revisiting the plan), and reflect to adjust future steps, e.g., adding new data sources mid-run; this creates a loop of planning, acting, and reflecting that relies heavily on reasoning LLMs. 

