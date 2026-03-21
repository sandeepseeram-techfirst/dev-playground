### Model Metrics

**Max Output Tokens**
Max Output Tokens is the maximum number of tokens a model is allowed to generate in its response for a single request. 

**What a “token” is**
A token is a small chunk of text (a few characters or part of a word) that the model processes.

When providers price “per 1M tokens” and show max input/output tokens, they are counting these chunks, not whole words or characters.

**Input tokens:** Everything you send to the API in that call (system prompt, user messages, tools schema, previous conversation, etc.).

**Output tokens:** Everything the model returns in that response, up to the “Max Output Tokens” limit for that model.

**Costing Example:** 
Suppose a model is listed as 2 USD per 1M input tokens and 8 USD per 1M output tokens.

If a call uses 2,000 input tokens and returns 1,000 output tokens, the billable tokens are 3,000 total, but split by rate: 2,000 at the input price and 1,000 at the output price.

### Note: Almost all providers charge separately for input tokens (your prompt/context) and output tokens (the model’s response).
This means you pay one rate for the tokens you send in (prompt + system messages + history) and another rate for the tokens the model generates.

### Inference Providers 
Providers are just brokering access to Anthropic’s hosted endpoints and enforcing Anthropic’s usage and privacy policies alongside their own.

OpenRouter, Fireworks, and Replicate all expose hosted inference endpoints for many models, often including Anthropic, OpenAI-compatible, and open‑weights models