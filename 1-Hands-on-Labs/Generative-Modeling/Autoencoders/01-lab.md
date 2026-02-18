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

 **Autoencoders use a form of learning called unsupervised or self-supervised.**

 ### Step 2: 

 With the data loaded, we can move on to visualizing the digits. 
 Visualization is important in generative modeling since it confirms to us what our baseline data looks like.

import math

def plot_data(file, num_images, images, labels):
  grid = math.ceil(math.sqrt(num_images))
  plt.figure(figsize=(grid*2,grid*2))
  for i in range(num_images):
      plt.subplot(grid,grid,i+1)
      plt.xticks([])
      plt.yticks([])
      plt.grid(False)     
      plt.imshow(images[i].reshape(28,28))
      plt.xlabel(class_names[labels[i]])      
  plt.savefig(file)

  file = 'contents/before.png'
  plot_data(file, 25, x_train, y_train)

### Step 3: 
With the data loaded, prepared, normalized, and visualized we can move on to building the autoencoder model.

Autoencoders consist of two submodels: an encoder and a decoder.  The encoder portion of the model encodes the data into some lower representation. It is then the decoder's job to rebuild the original based on the encoded representation.

**First we will import some abstractions from TensorFlow/Keras for building the deep learning model:**

from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model

encoding_dim = 32

**We also defined the middle encoding dimension size with encoding_dim. This means we will reduce the data from a vector of 784 to 32.**
##### Encoder 

input_img = Input(shape=(784,))
encoded = Dense(encoding_dim, activation='relu')(input_img)
encoder = Model(input_img, encoded)
encoded_input = Input(shape=(encoding_dim,))

##### Decoder 
decoded = Dense(784, activation='sigmoid')(encoded)
autoencoder = Model(input_img, decoded)
decoder_layer = autoencoder.layers[-1]
decoder = Model(encoded_input, decoder_layer(encoded_input))

**Notice that the input into the decoder is the output from the encoded layer. Also note that the output from the decoder is a vector of size 784, the full image.**


We have built the model, so we can now proceed to compile and train the model.

**Compiling the model is fairly simple:**

autoencoder.compile(optimizer='adam', loss='mse')

**Notice the use of mse or Mean Squared Error for the loss. Since we are training the autoencoder on the images themselves our measure of loss will be how well the images are generated. We can do this simply by taking pixelwise comparisons using MSE for the loss.**


>>> autoencoder.summary()
Model: "model_2"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 input_3 (InputLayer)        [(None, 784)]             0         
                                                                 
 dense_1 (Dense)             (None, 32)                25120     
                                                                 
 dense_2 (Dense)             (None, 784)               25872     
                                                                 
=================================================================
Total params: 50992 (199.19 KB)
Trainable params: 50992 (199.19 KB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________
>>> 

**Finally, we can train the model with:**

autoencoder.fit(x_train, x_train,
                epochs=50,
                batch_size=256,
                shuffle=True,
                validation_data=(x_test, x_test))

**Notice how the input and labels for training are the same: x_train. Again, we are training the autoencoder to replicate the images.**

