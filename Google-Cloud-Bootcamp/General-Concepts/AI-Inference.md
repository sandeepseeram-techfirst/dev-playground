## What is AI Inference?

### Definition  
AI inference is the phase where a trained AI model is used to make predictions on new, unseen data. It’s the “doing” part — the model uses what it has learned and applies it.  

---

### How it differs from other phases  

| Phase             | Objective                                     |
|-------------------|-----------------------------------------------|
| Training           | Build a new model from scratch               |
| Fine-tuning        | Adapt a pre-trained model for a specific task|
| **Inference**      | Use the trained or fine-tuned model to make predictions on live/unseen data  |
| Serving            | Deploy and manage the model so that inference requests can be processed efficiently |

---

### How AI Inference Works  
Typical steps when a model does inference:  
1. **Input preparation** – The new data (e.g., a photo, text input) is formatted and pre-processed for the model.   
2. **Model execution** – The model performs a forward pass using its learned parameters to generate an output.  
3. **Output generation** – The model returns a prediction or decision (for example, “dog: 95%”) which the application can use.  

---

### Types of Inference & Deployment Modes  

- **Cloud Inference**: Runs in remote servers/data centres – good for scale and heavy computation.  
  - *Real-time (online)*: Immediate responses for single requests.  
  - *Batch (offline)*: Many inputs processed together, not necessarily instantly. 

- **Edge Inference**: The model runs on device (mobile, IoT) – less reliance on network, lower latency.  

---

### Why it Matters  
Inference is where the value of an AI model is realised — you train or fine-tune a model, but unless it's used in production via inference it doesn’t deliver business value. Key operational concerns include:  
- Latency: how quickly a prediction is returned  
- Scale: how many requests can be handled  
- Cost and compute efficiency: running inference might be less demanding than training, but handling many requests still requires infrastructure. :contentReference[oaicite:13]{index=13}  

---

### Considerations for Infrastructure/Operations  
- Choose appropriate hardware (GPUs, TPUs, accelerators) for inference workloads. :contentReference[oaicite:14]{index=14}  
- Optimize deployment: consider latency, throughput, batch vs online processing.  
- Decide: cloud vs edge depending on connectivity, privacy, cost, latency requirements.  
- Monitor and scale: inference endpoints may require autoscaling, monitoring of performance and cost.  

---

### Summary  
In short:  
> **AI inference** = using a trained model to generate predictions or outputs on new data.  
It’s a critical step in turning AI research/training into real-world applications. Ensuring inference is fast, scalable, and cost-effective is key to successful AI deployment.

