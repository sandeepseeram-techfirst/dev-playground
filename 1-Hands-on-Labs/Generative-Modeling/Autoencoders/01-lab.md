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