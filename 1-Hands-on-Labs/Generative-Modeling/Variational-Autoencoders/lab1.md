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

