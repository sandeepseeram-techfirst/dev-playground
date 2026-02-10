 ### Lab 01
 
 TensorFlow, an open-source machine learning library popular in industry. 
 Recent versions of TensorFlow automatically detect if there is a GPU available for computation.

import tensorflow as tf
tf.config.list_physical_devices('GPU')

[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]