### Nvidia AI Workflows
NVIDIA defines an AI workflow as four main stages: 
**data processing → model training → model optimization → inference/deployment** and maps one key NVIDIA tool to each stage (RAPIDS, PyTorch/TensorFlow, TensorRT, Triton Inference Server).

#### High‑level AI workflow (4 stages)

1. **Data processing**
Clean, transform, augment, and prepare raw data so it is suitable for training.
​Handle errors, missing values, and wrong formats; optionally increase data volume via augmentation when you have too little data (e.g., image flips/rotations, synthetic samples).
​
**Examples:**

* Fix missing fields in transaction logs.

* Normalize numeric features; encode categorical variables.

* Augment medical images to improve robustness.

2. **Model training**
Choose a model (from public domain or built in‑house) and teach it by feeding processed data so it learns patterns.
​
**Example:** fraud detection model for credit cards trained on historical valid vs fraudulent transactions.
​Training details depend on the data type and model architecture you pick.
​

3. **Model optimization**
Take the trained model and refine/compress it for deployment:

**Quantization** – reduce precision of weights/activations to speed up inference and shrink model size.

**Pruning** – remove less important weights/neurons to reduce complexity.
​
Goals can be higher accuracy, lower latency, or smaller footprint to fit less powerful hardware.
​

4. **Inference / deployment**
Deploy the optimized model into a production environment where it receives new inputs and returns predictions.
​The model is now an online service or batch pipeline making real decisions (e.g., fraud alerts, recommendations, anomaly flags). 
