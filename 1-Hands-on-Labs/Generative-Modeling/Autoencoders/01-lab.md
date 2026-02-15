### Autoencoders 
Autoencoders are the foundation of all generative modeling, encoding, and embedding we perform in deep learning. 

### Step 1: 
Import some standard libraries like TensforFlow, numpy, and matplotlib. 

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

**This loads the 70 thousand image dataset into x_train and x_test. The labels for these images are y_train and y_test.**