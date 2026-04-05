# NVIDIA - Agentic AI Certification Notes 

1. Agentic systems need explicit decomposition: a planner or coordinator defines the work, specialized agents or tools execute bounded actions, and memory/state is preserved only where it improves the next decision. 

**This structure increases maintainability because each agent role, message contract, and state transition can be tested independently under load.**

2. For tool-using agents, the durable pattern is schema-bound function invocation with timeouts, typed outputs, retry policy, and traceable execution rather than free-form endpoint guessing.

