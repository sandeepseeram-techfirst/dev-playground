## Generative Modeling: Variational Autoencoders

Variational autoencoders provide a mechanism for understanding how data/images are distributed. Understanding how data is distributed allows us to build new forms of similarly but like content.

#### Step 1: Load and Prepare Data

We will first import some standard libraries like TensforFlow, numpy, and matplotlib:

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from scipy.stats import norm

from tensorflow.keras.layers import Input, Dense, Lambda
from tensorflow.keras.models import Model
from tensorflow.keras import backend as K
from tensorflow.keras.datasets import mnist

>>> (x_train, y_train), (x_test, y_test) = mnist.load_data()
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz
11490434/11490434 [==============================] - 1s 0us/step
>>> x_train = x_train.astype('float32') / 255.
>>> x_test = x_test.astype('float32') / 255.
>>> x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
>>> x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))
>>> print(x_train.shape)
(60000, 784)
>>> print(x_test.shape)
(10000, 784)
>>> 

#### Step 2: Building the VAE
Variational autoencoders are similar to autoencoders in that they encode data down to a latent or intermediary representation. VAEs differ in that they learn how that internal representation is distributed.

