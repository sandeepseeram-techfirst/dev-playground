### Lab 01

TensorFlow is an open-source machine learning library widely used in industry.  
Recent versions of TensorFlow automatically detect if a GPU is available for computation.

#### Check GPU Availability

import tensorflow as tf
tf.config.list_physical_devices('GPU') 

[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]