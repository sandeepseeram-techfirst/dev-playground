### Generative Modeling 

Generative modeling is a branch of machine learning where a model learns the underlying distribution of a training dataset in order to generate new, similar data samples. In contrast to discriminative models (which classify or predict labels), generative models understand how data is created from the ground up.

### How It Works
Training involves feeding a large dataset into the model, which adjusts its internal parameters to match the data's distribution. Once trained, the model can sample from that learned distribution to produce new data. 

### Key Model Types

1. Autoencoders (AE) — Compress data into a latent representation and reconstruct it; useful for dimensionality reduction and anomaly detection. 

2. Variational Autoencoders (VAE) — Extend AEs by learning a probabilistic latent space, enabling controlled generation. 

3. Generative Adversarial Networks (GANs) — Two networks (generator vs. discriminator) compete, pushing the generator to produce increasingly realistic outputs.

4. Transformers / LLMs — Predict the next token in a sequence, making them generative models for text. 

5. Diffusion Models — Iteratively denoise random noise into structured data (used in image generation tools like Stable Diffusion). 

**Generative modeling is the basis for applications of:**

1. Text generation—Fake News
2. Facial swapping—Deep Fakes
3. Pose translation
4. Static image animation
5. Medical imaging analysis
6. Generating fake art
7. Feature image analysis
8. Restoring images and video

Autoencoders are the first step to understanding generative modeling. 


**Note: Latent representation (also called the latent space or encoding) is a compact, compressed version of your input data that captures its most essential features in a lower-dimensional form.** 

**Think of it like summarizing a 10-page document into 5 bullet points. The summary isn't the original — but it captures the core meaning. A latent representation does the same for data like images, audio, or text.**