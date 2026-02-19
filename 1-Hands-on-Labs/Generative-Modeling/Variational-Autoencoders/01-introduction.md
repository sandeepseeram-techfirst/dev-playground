### Variational Autoencoders [VAE]

A Variational Autoencoder (VAE) is a generative neural network model that learns to encode data into a probabilistic latent space and then decode it — enabling it to both reconstruct existing data and generate entirely new, realistic samples.

### The Core Idea
A standard autoencoder compresses input data into a single fixed point in a latent space, then reconstructs it from that point. 
VAEs take this further by encoding inputs into a probability distribution (typically Gaussian), defined by a mean and variance, rather than a single fixed vector. This probabilistic twist is what gives VAEs their generative power.

Key Applications
Image synthesis and data augmentation — Sample from latent space to generate new images

Anomaly detection — Inputs that reconstruct poorly indicate deviations from learned distributions

Data denoising and imputation — Reconstruct clean data from noisy or incomplete inputs, useful in medical imaging

Feature learning — The latent vectors serve as compact feature representations for classification or clustering

