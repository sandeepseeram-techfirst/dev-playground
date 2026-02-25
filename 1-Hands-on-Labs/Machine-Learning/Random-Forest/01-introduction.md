### Random Forest 

A Random Forest is an ensemble machine learning algorithm that builds many decision trees and combines their outputs for a more accurate and robust prediction. It's called a "forest" because it literally creates a forest of decision trees, where each tree votes on the final answer.

### Core Concept: Ensemble Learning

A single decision tree is like asking one expert — it can be wrong or biased. Random Forest is like asking hundreds of experts and taking a majority vote. This idea is grounded in Condorcet's Jury Theorem: if each model is more than 50% accurate and they are independent, combining more models increases the overall accuracy. With 11 such trees, majority voting can push accuracy to ~75% even if each tree alone is only 60% accurate.

### How It Works — Step by Step

1. **Bootstrap Sampling (Bagging):** The algorithm creates multiple random samples from the original dataset with replacement, meaning some records may appear more than once and some may be excluded entirely. This introduces diversity between trees. 

2. 
