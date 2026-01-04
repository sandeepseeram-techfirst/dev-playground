### ML Frameworks
ML frameworks are like a fully equipped workshop for building AI models: they give you tools, blueprints, and prebuilt parts so you do not have to “forge your own hammer” or mix your own cement every time.

Without framework (ML from scratch)
-----------------------------------
- Implement tensors, autograd, GPU kernels
- Write all training loops manually
- Implement loaders, checkpointing, etc.

With ML framework (TensorFlow / PyTorch)
----------------------------------------
- Use ready-made layers, losses, optimizers
- Use built-in training utilities
- Use built-in data loaders, saving, versioning

#### What an ML framework provides
ML frameworks (e.g., PyTorch, TensorFlow) provide a complete toolbox and blueprints:
​
**Building blocks for models:**

* Layers (convolution, dense, RNN, transformers).

* Loss functions (cross‑entropy, MSE, etc.).

* Optimizers (SGD, Adam, etc.).
​

**Hardware acceleration:**

* Automatic use of GPUs (and TPUs) for faster training.

* Optimized kernels so you do not manage CUDA directly.
​

**Data utilities:**

* Data loading, batching, shuffling.

* Data augmentation tools (especially for images).
​

**Training lifecycle tools:**

* Saving and loading models.

* Model versioning.

* Evaluation and testing helpers.
​
So instead of coding everything from scratch, you assemble models from these prebuilt components and focus on architecture and experimentation.