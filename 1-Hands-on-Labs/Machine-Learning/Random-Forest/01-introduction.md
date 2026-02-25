### Random Forest 

A Random Forest is an ensemble machine learning algorithm that builds many decision trees and combines their outputs for a more accurate and robust prediction. It's called a "forest" because it literally creates a forest of decision trees, where each tree votes on the final answer.

### Core Concept: Ensemble Learning

A single decision tree is like asking one expert — it can be wrong or biased. Random Forest is like asking hundreds of experts and taking a majority vote. This idea is grounded in Condorcet's Jury Theorem: if each model is more than 50% accurate and they are independent, combining more models increases the overall accuracy. With 11 such trees, majority voting can push accuracy to ~75% even if each tree alone is only 60% accurate.

### How It Works — Step by Step

1. **Bootstrap Sampling (Bagging):** The algorithm creates multiple random samples from the original dataset with replacement, meaning some records may appear more than once and some may be excluded entirely. This introduces diversity between trees. 

2. **Random Feature Selection:** At each node split within a tree, only a random subset of features is considered — not all columns. This prevents dominant variables from overwhelming every tree and ensures each tree learns different patterns.

3. **Each Tree Predicts Independently:** Every tree produces its own prediction based on its unique data subset and feature selections.

4. **Aggregate the Outputs:**

**Classification** (e.g., income > $50K or not): Final class = majority vote across all trees

**Regression** (e.g., predicting a salary value): Final output = average of all tree predictions

### Why It Reduces Overfitting

A single decision tree tends to overfit — it memorizes the training data too well. Random Forest counters this because each tree sees different data and features, so the errors of individual trees don't align. The uncorrelated trees reduce variance collectively, making the model generalize better to unseen data.

### Key Hyperparameters 

| Hyperparameter    | What It Controls                                             |
| ----------------- | ------------------------------------------------------------ |
| n_estimators      | Number of trees; more trees → more stable but slower builtin |
| max_features      | Max features considered at each split builtin                |
| max_depth         | How deep each tree can grow                                  |
| min_samples_split | Minimum samples needed to split a node                       |
