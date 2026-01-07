### Model Training vs. Model Inference 
Model training is the long, compute‑heavy process of teaching a model from lots of data via many forward–backward passes, while inference is the fast, lightweight process of using the trained model to make predictions on new data.

#### Intuition: cooking analogy

**Training** = learning to cook: many experiments, mistakes, corrections, and repeated practice until you master the recipe.
​
**Inference** = serving dishes in a restaurant: you already know the recipe, you just execute it quickly for many customers.
​
So training is slow, iterative learning; inference is fast, repeatable serving.
​

#### Model training
Objective: build the model by learning parameters from large datasets through multiple iterations.
​
**Workflow:**

​* Forward pass → compute predictions on training data.

* Compare with labels → compute errors (loss).

* Backward pass → propagate errors and update weights.

* Repeat many times (epochs) over the dataset.

**Model Inference:**
Objective: use the trained model to make predictions on new, unseen data.
​
Only forward pass is needed: input → model → output (no backward/weight updates).
​
Example: trained on many cat/dog images, then given a new image, the model outputs “cat” or “dog.”
​

