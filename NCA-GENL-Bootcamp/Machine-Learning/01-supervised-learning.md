# Supervised Machine Learning

## Classification
Classification is a supervised machine learning task where input data is assigned into predefined categories or classes.

### Workflow Steps
1. Prepare a labeled dataset with relevant attributes that help predict the target.
2. Choose a classification algorithm that learns the pattern between features and classes, train it, evaluate performance on unseen data to check accuracy and generalization, then use the trained model to classify new, unseen inputs.

### Algorithms
- **Decision Trees**: Easy to interpret and visualize but prone to overfitting.
- **Logistic Regression**: Simple and efficient, particularly for binary classification.
- **Support Vector Machines**: Effective for high-dimensional data and complex decision boundaries.
- **Neural Networks**: Powerful and flexible but computationally expensive and data-hungry.

## Regression
Regression is a supervised ML task for predicting continuous numerical values (e.g., market trends, crop yield, customer lifetime value) from structured data with features X and continuous target Y.

### Workflow and Algorithms
**Steps**: 
- Collect labeled data with features and numeric target
- Select and transform relevant features (preprocessing)
- Train a regression algorithm to learn X–Y patterns
- Evaluate with metrics such as R-squared and mean squared error
- Use the trained model for new predictions

**Algorithms**:
- **Linear Regression**: Assumes linear relationship, simple and interpretable
- **Polynomial Regression**: Captures non-linearity
- **Decision Tree Regression**: Handles non-linearity and feature interactions but can overfit if not pruned
- **Support Vector Regression**: Good for complex, high-dimensional data
- **Neural Networks**: Model highly complex relationships but need lots of data and compute

## Key Practical Issues and Applications

### Key Considerations
- Handle outliers (remove or transform extreme values)
- Manage overfitting and underfitting (use regularization, adjust model complexity and training data)
- Scale features (e.g., with StandardScaler to zero mean and unit variance) for algorithms like linear regression and SVR
- Perform careful model selection and hyperparameter tuning

### Real-World Use Cases
- Stock price prediction and portfolio optimization in finance
- Demand forecasting and pricing in economics
- Patient length-of-stay and disease progression prediction in healthcare
- Equipment failure prediction and manufacturing optimization in engineering
- Weather and air-pollution forecasting in environmental science
