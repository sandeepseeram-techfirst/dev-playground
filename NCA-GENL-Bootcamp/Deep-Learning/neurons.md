# How Data Is Processed in a Neuron  
what an artificial neuron is and how it processes input data using weights, bias, and an activation function. 

## What is a neuron?

- A neuron is the **fundamental** unit of a neural network that analyzes data. 
- Its structure is inspired by biological neurons in the human brain. 
- Like the brain receives sensory inputs and produces outputs, an artificial neuron receives input signals, processes them, and produces an output signal. 

## Structure of an artificial neuron

- Inputs are denoted as \(x_1, x_2, x_3, \dots, x_n\), typically features from the dataset. 
- Each input has an associated weight \(w_1, w_2, w_3, \dots, w_n\) indicating its importance. 
- The neuron also has a bias term \(b\), which is a constant added to the weighted sum to increase model flexibility (shifts the decision boundary away from the origin). 

## Data processing steps inside a neuron

1. Compute weighted sum (summation step). 
   \[
   z = w_1 x_1 + w_2 x_2 + \dots + w_n x_n + b
   \]
   This is the dot product of the input vector and weight vector plus bias. 

2. Apply activation function to the weighted sum. 
   \[
   y = \text{activation}(z)
   \]
   The output of the activation function is the neuron’s final output. 

## Numerical example from the video

- Inputs: \(x_1 = 0.5\), \(x_2 = 0.8\). 
- Weights: \(w_1 = 0.3\), \(w_2 = 0.6\). 
- Bias: \(b = -0.1\). 
- Weighted sum:  
  \[
  z = 0.3 \times 0.5 + 0.6 \times 0.8 - 0.1 = 0.53
  \][page:1]
- Activation function used: ReLU, which in this case outputs \(0.53\) because it is positive. 

## Activation functions to know for exam

- Sigmoid: Squashes values between 0 and 1, used for probabilities. 
- ReLU: Outputs zero for negative values and the same value for positive inputs. 
- Tanh: Outputs values between -1 and 1, centered around zero. 

## Exam-focused points highlighted

- Be clear on the definition of a neuron and its role in a neural network. 
- Remember the steps: compute weighted sum, add bias, apply activation function. 
- Be able to manually calculate the weighted sum and apply an activation function for simple numeric examples. 
- Know common activation functions (sigmoid, ReLU, tanh) and their basic properties. 

