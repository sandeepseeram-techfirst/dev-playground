### Supervised Machine Learning

**Classificiation** is a supervised machine learning task - where the input data is assigned into predefined categories or classes. 

#### Workflow steps

1. Prepare a labeled dataset with relevant attributes that help predict the target.
2. Choose a classification algorithm that learns the pattern between features and classes, train it, evaluate performance on unseen data to check accuracy and generalization, then use the trained model to classify new, unseen inputs.

#### Algorithms

**Decision trees:** easy to interpret and visualize but prone to overfitting.
​**Logistic regression:** simple and efficient, particularly for binary classification.
​**Support Vector Machines:** effective for high‑dimensional data and complex decision boundaries.
​**Neural networks:** powerful and flexible but computationally expensive and data‑hungry. 


**Regression** 
Regression is a supervised ML task for predicting continuous numerical values (e.g., market trends, crop yield, customer lifetime value) from structured data with features X and continuous target Y.

**Workflow and Algorithms**

**Steps:** collect labeled data with features and numeric target, select and transform relevant features (preprocessing), train a regression algorithm to learn X–Y patterns, evaluate with metrics such as R‑squared and mean squared error, then use the trained model for new predictions.
​
**Algorithms covered:** linear regression (assumes linear relationship, simple and interpretable), polynomial regression (captures non‑linearity), decision tree regression (handles non‑linearity and feature interactions but can overfit if not pruned), support vector regression (good for complex, high‑dimensional data), and neural networks (model highly complex relationships but need lots of data and compute).

#### Key practical issues and applications
**Key considerations:** handle outliers (remove or transform extreme values), manage overfitting and underfitting (use regularization, adjust model complexity and training data), scale features (e.g., with StandardScaler to zero mean and unit variance) for algorithms like linear regression and SVR, and perform careful model selection and hyperparameter tuning.
​
**Real‑world use cases** include stock price prediction and portfolio optimization in finance, demand forecasting and pricing in economics, patient length‑of‑stay and disease progression prediction in healthcare, equipment failure prediction and manufacturing optimization in engineering, and weather and air‑pollution forecasting in environmental science.
​