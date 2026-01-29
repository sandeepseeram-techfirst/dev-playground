### Agents 101 

An agent is anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators.


![Agent](image.png)

Traditionally, an LLM is a model that does nothing more than predict the next word based on a given input text. The LLM therefore predicts the next token, uses the predicted token to update its input, and then continues the predictions. 
By doing this iteratively (which is called **autoregression**), it can create entire answers to the user’s query. 

![Reasoning - LLM](image-1.png)

### Reasoning Large Language Models

OpenAI and many other LLM providers have focused on scaling GPT-3.5-like models to new heights by throwing more data, compute, and parameters at these models. This is called **train-time scaling**, where training these models on more data and making them larger had a proportional effect on performance. The idea was that pre-training (the first and most expensive part of training an LLM) is the fossil fuel of AI. The larger your pre-training budget, the better the resulting model will be.

### Multi Agent Systems 
 These are systems where multiple different Agents are deployed that are each responsible for different tasks. Compared to single-agent systems, Multi-Agent systems interact with one another and might consult each other’s specialties.

![Multi-Agent-Systems](image-2.png)