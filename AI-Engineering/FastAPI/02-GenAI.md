### Generative AI basics

* A generative model learns patterns and distributions from training data (e.g., many butterfly images) and then samples new data that looks similar but is not identical, using randomness so outputs are varied and probabilistic.

* Using the trained model to produce outputs is called inference.

#### Generative adversarial networks (GANs):

Two nets: generator vs discriminator, competing during training; after training, you keep the generator to produce new samples.

#### Transformers:

* Use self-attention to model long sequences efficiently (texts, code, multimodal inputs).

* Power large language models (LLMs) such as GPT-based systems.


#### Variational autoencoders (VAEs):

* Encode input into a compressed latent space, then decode back.

* Latent space = low-dimensional representation containing the essential information to reconstruct the original input.
