# Gradient Descent 

**gradient** descent optimization algorithm used to train deep learning models by minimizing the loss function through iterative parameter updates. 

## What is gradient descent?

- Gradient descent is an optimization algorithm used to minimize the loss function of a model. 
- It adjusts model parameters (weights and biases) to reduce the error between predicted and actual outputs. 
- The goal is to find an optimal set of parameters that gives the lowest possible loss. 

## Intuitive analogy

- Imagine a hiker descending a mountain in thick fog, taking small steps downhill. 
- The mountain represents the loss landscape, and the hiker is the optimization algorithm. 
- Each step follows the direction of the steepest downward slope (negative gradient) to reach a minimum. 

## How gradient descent works (steps)

1. Initialize weights and biases with random values. 
2. Perform a forward pass to compute the model output and the loss. 
3. Compute gradients: partial derivatives of the loss with respect to each parameter 
(for example, \(\partial L / \partial W\), \(\partial L / \partial b\)).  
4. Update parameters using the negative gradient direction.  
5. Repeat steps 2–4 until the loss is sufficiently small or a fixed number of iterations is reached. 

## Parameter update rule

- Generic update rule for a weight \(W\):  
  \[
  W_{\text{new}} = W_{\text{old}} - \eta \cdot \frac{\partial L}{\partial W}
  \] 
- Here \(\eta\) is the learning rate, controlling the step size for each update. 
- Using the negative gradient moves the parameters toward the direction of steepest descent in the loss landscape. 

## Variants of gradient descent

- **Batch** gradient descent: Uses the entire training dataset to compute the gradient at each iteration, accurate but computationally expensive for large datasets. 
- **Stochastic** gradient descent (SGD): Uses a single randomly chosen training example per update, computationally efficient but produces noisy updates. 
- **Mini-batch** gradient descent: Uses small batches of training examples, balancing efficiency and stability, and is commonly used in practice. 

## Practical challenges

- Choosing the learning rate is critical:  
  - Too high: algorithm may overshoot and fail to converge.  
  - Too low: convergence is very slow.  
- Risk of getting stuck in local minima, where loss is lower than neighbors but not globally minimal. 

## Common solutions and improvements

- Use learning rate scheduling or adaptive optimizers like Adam to handle learning rate challenges. 
- Use momentum-based gradient descent, better initialization strategies, and stochasticity in mini-batch selection to help escape local minima. 

## Exam-oriented points

- Understand the conceptual role of gradient descent as an optimization algorithm for deep learning models. 
- Be able to explain and write the parameter update rule with learning rate and gradient. 
- Know the differences between batch, stochastic, and mini-batch gradient descent, including pros and cons. 
- Be aware of challenges (learning rate, local minima) and typical mitigation strategies (schedulers, Adam, momentum, mini-batches). 