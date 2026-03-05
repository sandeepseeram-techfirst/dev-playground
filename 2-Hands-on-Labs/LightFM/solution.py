# ============================================================
# LightFM: Build an Explicit Feedback Recommendation Engine
# Complete Solution Code
# ============================================================

# --- Dependencies ---
# pip install lightfm pandas scipy scikit-learn numpy

import numpy as np
import pandas as pd
import scipy.sparse as sp
from sklearn.preprocessing import LabelEncoder

from lightfm import LightFM
from lightfm.cross_validation import random_train_test_split
from lightfm.evaluation import precision_at_k


# ============================================================
# STEP 1: Quickstart (LightFM with built-in MovieLens data)
# ============================================================
# This is the "hello world" of LightFM — uses the bundled dataset.
# Only for orientation; the real lab replaces this with candy data.

from lightfm.datasets import fetch_movielens

data = fetch_movielens(min_rating=5.0)

quickstart_model = LightFM(loss='warp')
quickstart_model.fit(data['train'], epochs=30, num_threads=2)

print("MovieLens precision@5:", precision_at_k(quickstart_model, data['test'], k=5).mean())
# Output: ~0.0518


# ============================================================
# STEP 2: Candy — Load and explore the custom dataset
# ============================================================
# The candy.csv file has three columns: user, item, review
# Each row = one user's star rating of one candy

df = pd.read_csv("data/candy.csv")

# Peek at random rows
print(df.sample(5))

# Inspect a single user's ratings
print(df[df['user'] == 'zjohnson'])

# Dataset dimensions
print("Unique candy items:", df['item'].unique().shape)   # (142,)
print("Unique users:", df['user'].unique().shape)          # (2531,)


# ============================================================
# STEP 3: Sparse — Build a sparse user-item matrix
# ============================================================
# LightFM expects a scipy sparse matrix, not a dense DataFrame.
# User-item data is inherently sparse: most users rate only a
# fraction of available items, so most cells are empty (zero).
# Using coo_matrix (Coordinate format) is memory-efficient.

# But wait — users and items are STRINGS. coo_matrix needs integers.
# That leads to Step 4.

ratings = np.array(df['review'])   # star ratings (1–5)
users   = np.array(df['user'])     # string usernames
items   = np.array(df['item'])     # string candy names


# ============================================================
# STEP 4: Strings — Encode string labels to integer indices
# ============================================================
# LabelEncoder maps each unique string to a unique integer.
# e.g. 'Twix' → 134, 'zsmith' → some integer index
# It also lets you go BACK from integer → string (inverse_transform)

user_encoder = LabelEncoder()
item_encoder = LabelEncoder()

u = user_encoder.fit_transform(users)   # integer user indices
i = item_encoder.fit_transform(items)   # integer item indices

lu = len(np.unique(u))   # 2531 unique users
li = len(np.unique(i))   # 142 unique candies

# Now build the sparse matrix: shape = (num_users, num_items)
# coo_matrix takes (data, (row_indices, col_indices))
matrix = sp.coo_matrix((ratings, (u, i)), shape=(lu, li))

print("Sparse matrix shape:", matrix.shape)   # (2531, 142)

# You can inspect the encoded class names:
print("First 10 candy names:", item_encoder.classes_[:10])
print("First 10 user names:", user_encoder.classes_[:10])


# ============================================================
# STEP 5: Model — Train/test split and fit the LightFM model
# ============================================================
# Split: 80% train, 20% test (randomly)
train, test = random_train_test_split(matrix, test_percentage=0.2)

# Instantiate and fit the model on training data
model = LightFM()
model.fit(train)

# Evaluate: precision@10 (how many of top-10 recommendations are relevant)
score = precision_at_k(model, test, k=10).mean()
print("Candy model precision@10:", score)   # ~0.0278


# ============================================================
# STEP 6: Predict — Generate ranked recommendations for a user
# ============================================================
# model.predict() does NOT take the matrix directly.
# It needs: a scalar user_id + an array of item_ids to score.

user = 'zsmith'

# Encode the username to its integer ID
user_id = int(user_encoder.transform([user])[0])

# Score ALL candies for this user
all_candy_ids = np.arange(len(item_encoder.classes_))
preds = model.predict(user_id, all_candy_ids)

# Build a ranked DataFrame of candies + scores
candies = pd.DataFrame({
    'item': item_encoder.classes_,
    'prediction': preds
}).sort_values('prediction', ascending=False)

print("\nTop 10 candy recommendations for", user)
print(candies.head(10))

# IMPORTANT: Filter out candies the user has already rated!
# Serving already-rated items as "recommendations" is bad UX.
tried = df[df['user'] == user]['item'].values
top5_new = list(candies[~candies['item'].isin(tried)]['item'].values[:5])

print("\nTop 5 NEW candy recommendations for", user, "(not yet rated):")
print(top5_new) 