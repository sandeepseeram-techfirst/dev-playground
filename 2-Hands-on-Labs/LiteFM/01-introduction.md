### LiteFM

LightFM is a Python library for building hybrid recommendation systems that combines collaborative filtering and content-based filtering into a single, unified model. 

* It was originally developed by the fashion e-commerce company Lyst and is now widely used for building personalized recommendation engines.

### How LightFM Works

LightFM is built on hybrid matrix factorization — it represents every user and item as a sum of latent (learned) embeddings of their features. This means it doesn't just rely on who interacted with what (collaborative filtering), but also uses metadata like genre, tags, or price (content-based filtering).

### Here's the core flow:

1. Build an interaction matrix — rows are users, columns are items, and values represent ratings (explicit) or clicks/views (implicit feedback)

2. Add feature matrices — optional user/item metadata (age, genre, tags) is encoded as sparse feature vectors

Train embeddings — the model learns a latent vector for each feature; a user/item's final embedding is the sum of all its feature embeddings

Score and rank — the dot product of a user embedding and an item embedding gives a relevance score; higher scores = better recommendations

Choose a loss function — LightFM supports WARP (Weighted Approximate-Rank Pairwise, great for ranking), BPR (Bayesian Personalized Ranking), and logistic for explicit ratings

