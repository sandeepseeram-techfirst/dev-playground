### Model Selection, Training and Evaluation

Model Selection & Training - will include the Hands on Labs 

#### Evaluation Metrics
Evaluation metrics are quantitative measures to assess how well a ML model performs on a dataset and how well it generalizes to unseen data.

**Metrics Explained** 

**Accuracy:** proportion of correct predictions out of all predictions; e.g., 80 correctly classified rows out of 100 gives 80% accuracy.
​
**Precision:** proportion of true positives among all predicted positives; measures how often “positive” predictions are actually correct.
​
**Recall:** proportion of true positives among all actual positives; measures how well the model finds all positive instances.
​
**F1 score:** harmonic mean of precision and recall, giving a single balanced score that is useful for imbalanced classes.


****Spam Email Example****

- Out of 100 emails, if the model correctly classifies 90 as spam/not spam, accuracy is 90%.
​- If 50 emails are predicted as spam and 45 are truly spam, precision for spam is 45/50 = 90%.
​- If there are actually 60 spam emails and the model correctly identifies 45, recall is 45/60 = 75%.
​- Using precision 90% and recall 75%, the F1 score is about 81.8%, illustrating how F1 summarizes both aspects.