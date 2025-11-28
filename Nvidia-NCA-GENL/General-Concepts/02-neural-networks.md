### Neural Networks 

1. An artificial neural network is a collection of interconnected units (neurons) organized in layers that transform input data through learned weights and biases.

2. Standard feedforward networks (multi‑layer perceptrons) have an input layer, one or more hidden layers, and an output layer.

3. Each neuron computes a weighted sum of its inputs plus a bias, then passes it through a nonlinear activation function such as ReLU or sigmoid.

### Forward pass and loss
In forward propagation, data flows from input to output layer, with each layer applying linear transformations and nonlinear activations. A loss (or cost) function measures how far predictions are from targets; examples include mean squared error (regression) and cross‑entropy (classification).
​
### How neural networks learn: backpropagation

1. Training adjusts weights and biases to minimize the loss on the training data, typically using gradient descent or its variants.

Backpropagation efficiently computes gradients of the loss with respect to all parameters by applying the chain rule layer by layer from output back to input.

The training loop iterates: forward pass → loss computation → backpropagation → weight update, repeated over many epochs until performance converges.