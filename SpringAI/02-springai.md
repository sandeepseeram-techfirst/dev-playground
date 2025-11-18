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
