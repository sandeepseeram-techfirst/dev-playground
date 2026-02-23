### PyTorch 

PyTorch is an open-source machine learning framework developed by Meta (Facebook) AI Research, first released in 2016. It provides tools to build and train machine learning models — especially deep neural networks — using Python. 

Think of it as a scientific computing library, but supercharged for AI workloads and GPU acceleration.

### Why Was PyTorch Created?

Before PyTorch, the dominant framework was TensorFlow (by Google), which used a static computation graph — you had to define the entire model architecture before running it. 

PyTorch introduced dynamic computation graphs (called "define-by-run"), meaning the graph is built on the fly as your code executes. This made debugging and experimentation dramatically easier, which is why researchers loved it immediately.

### What is PyTorch Used For?

1. Computer Vision — image classification, object detection, image generation (think DALL-E style models)

2. Natural Language Processing — sentiment analysis, translation, chatbots, LLMs

3. Generative AI — most modern LLMs (LLaMA, Mistral, etc.) are built and trained in PyTorch

4. Reinforcement Learning — training AI agents to play games or control robots

5. Scientific Research — protein folding, drug discovery, physics simulations

6. Custom ML Model Development — anything requiring a custom neural network architecture


### NumPy vs. PyTorch 

| Feature               | NumPy          | PyTorch             |
| --------------------- | -------------- | ------------------- |
| GPU acceleration      | ❌ CPU only     | ✅ CUDA/GPU native   |
| Automatic gradients   | ❌ Manual       | ✅ Built-in autograd |
| Neural network layers | ❌ Not built-in | ✅ torch.nn module   |
| Production deployment | Limited         | ✅ TorchScript, ONNX |


### How PyTorch fits into ML Stack

Your Python Code
      ↓
  PyTorch API         ← you write this
      ↓
Computation Graph     ← PyTorch builds this automatically
      ↓
CUDA / cuDNN          ← runs on your NVIDIA GPU
      ↓
GPU Hardware          ← your familiar territory!