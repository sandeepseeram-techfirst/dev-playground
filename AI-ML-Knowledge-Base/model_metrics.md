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

### What these aggregators do?
Platforms like OpenRouter, Fireworks.ai, and Replicate act as “model gateways” or aggregators.

OpenRouter, Fireworks, and Replicate all expose hosted inference endpoints for many models, often including Anthropic, OpenAI-compatible, and open‑weights models. They host or proxy many different models behind their own unified API, set pricing per input/output token or per second, and handle routing, billing, and sometimes load‑balancing or caching for you.

### Why aggregators exist? 
Aggregators like OpenRouter, Fireworks, and Replicate act as a single API in front of many providers and models. They try to solve problems like “I don’t want to integrate 5 different vendor SDKs and auth schemes” and “I want to switch models/providers without rewriting app code.”

Aggregators exist because they add extra capabilities (routing, one API, extra models, etc.) 

**Unified API:** OpenRouter and Fireworks offer OpenAI‑style or unified APIs so you can swap models with minimal code changes.

**Routing and failover:** OpenRouter, for example, can route across multiple providers for higher availability, better latency, or cost optimization, and even has BYOK to use your own provider keys.

**Expanded catalog:** Replicate exposes a large catalog of open models you can call with simple HTTP, without managing GPUs yourself.

### Design Decision: An aggregator is more compelling if you:

1. Want to experiment with many models/providers quickly without lots of separate integrations.

2. Need automatic fallback/routing when a provider is down or rate‑limited, or want to route some traffic to cheaper/faster models.

3. Like BYOK patterns (especially with OpenRouter) where you keep your Anthropic/OpenAI accounts and negotiated rates, but still use the aggregator for routing/unification.

