### What is Spring AI? 

#### 1. Spring AI’s Core Idea: The `Model`

##### 1.1 What is a Model? 

In Spring AI, everything is built around the concept of a **Model**:

- A **Model**:
  - Accepts a **request**.
  - Returns a **response** in some format.

Types of models include:

- **Chat models** → text in, text out.
- **Image models** → generate or process images.
- **Audio models** → speech/text transformations.
- A general **`Model` abstraction** exists to handle future or custom mechanisms.

> Think of **“Model”** as: *“a configured AI service that takes some input and produces an output.”*


#### 1.2 Blocking vs Streaming Chat Models

For **chat models**, there are two variants:

1. **Blocking chat model**
   - Returns a **complete answer** in one go.
   - You call it, and it responds when the entire message is ready.

2. **Streaming chat model**
   - Returns the answer in **pieces**, as they are generated.
   - Feels like watching someone type the answer.


#### Visualization: Chat Model Types

 User Prompt
   │
   ├─► Blocking Chat Model ─► Whole answer at once
   │
   └─► Streaming Chat Model ─► Answer arrives chunk by chunk


#### Open AI vs. Ollama 

**OpenAI** 
   - ✔ Predictable performance
   - ✔ No special hardware needed
   - ✖ Paid (usage-based costs)

**Ollama (alternative)**
   - ✔ Free per request
   - ✖ Needs strong local hardware 
   - ✖ Performance depends on your machine 

- **Spring AI Model abstraction**:
    - General “request → response” concept; chat, image, audio, etc.
    - Chat models can be **blocking** or **streaming**.

- **Provider choice**:
    - Book uses **OpenAI** for:
        - Predictability,
        - Scalability,
        - Hardware-independence.
    - **Ollama** is possible but requires strong local hardware.

