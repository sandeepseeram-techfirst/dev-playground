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
Variational autoencoders are similar to autoencoders in that they encode data down to a latent or intermediary representation. VAEs differ in that they learn how that internal representation is distributed. With a VAE we estimate how the data is distributed by learning the parameters for a matching distribution.

>>> batch_size = 32
>>> original_dim = 784
>>> latent_dim = 2 
>>> intermediate_dim = 256
>>> epochs = 50
>>> x = Input(shape=(original_dim,))
>>> x1 = Dense(original_dim//2, activation='relu')(x)
>>> x2 = Dense(original_dim//3, activation='relu')(x1)
>>> h = Dense(intermediate_dim, activation='relu')(x2)
>>> z_mean = Dense(latent_dim)(h)
>>> z_log_var = Dense(latent_dim)(h)
>>> def sampling(args):
...     z_mean, z_log_var = args
...     epsilon = K.random_normal(shape=K.shape(z_mean))
...     return z_mean + K.exp(z_log_var / 2) * epsilon
... 
>>> z = Lambda(sampling, output_shape=(latent_dim,))([z_mean, z_log_var])
>>> decoder_h = Dense(intermediate_dim, activation='relu')
>>> decoder_mean = Dense(original_dim, activation='sigmoid')
>>> dc1 = Dense(original_dim//3, activation='relu')
>>> dc2 = Dense(original_dim//2, activation='relu')
>>> 
>>> h_decoded = decoder_h(z)
>>> h_decoded = dc1(h_decoded)
>>> h_decoded = dc2(h_decoded)
>>> x_decoded_mean = decoder_mean(h_decoded)
>>> 

