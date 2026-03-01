### Training a Random Forest Model to Predict Income

### STEP 1 - Importing Necessary Libraries

**numpy:** Numpy is a library for the Python programming language that adds support for large, multidimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. We're using it for numerical operations.

**pandas:** Pandas is a software library for data manipulation and analysis. It offers data structures and operations for manipulating numerical tables and time series. We're using it to load and manipulate our dataset.

**matplotlib:** Matplotlib is a plotting library. We'll use it for creating plots and charts of our data.


import numpy as np   
import pandas as pd   
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split  
from sklearn.ensemble import RandomForestClassifier  
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import make_pipeline
from sklearn.metrics import roc_auc_score, roc_curve

#ensure reproducibility
np.random.seed(123) 

# To disable warnings
import warnings  
warnings.filterwarnings("ignore") 