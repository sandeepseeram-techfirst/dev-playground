# Clustering

## What Clustering Is
Clustering groups similar data points into clusters based on inherent similarities, helping discover hidden structure and relationships in unlabeled data.

It is widely used for customer segmentation, image compression, anomaly detection, and recommender systems because it can reveal natural groupings without labels.

Clustering is presented as grouping similar data points into clusters based on their inherent similarities in feature space, allowing you to discover hidden structure and relationships in unlabeled data. It is positioned as a key unsupervised learning technique used in applications like customer segmentation, image compression, anomaly detection, and recommendation systems.

## Popular Algorithms 
K‑Means (requires specifying number of clusters, simple and efficient), hierarchical clustering (builds a tree/dendrogram for multiple granularity levels), and DBSCAN (finds arbitrarily shaped clusters and identifies outliers).


# Hierarchical Clustering & DBSCAN

## Hierarchical Clustering
It is an unsupervised method that builds a **hierarchy** of clusters to show relationships at different levels of granularity.

**Two types**:
- **Agglomerative** (bottom-up): Each point starts as its own cluster and closest clusters merge until one cluster remains
- **Divisive** (top-down): Start with one big cluster and split downwards

**Used in**: Biological taxonomy, social network analysis, and document clustering because it exposes multi-level structure.

## DBSCAN (Density-Based Clustering)
DBSCAN is a density-based method that finds clusters as dense regions of points and labels sparse points as outliers.

**Key features**:
- Can discover clusters of arbitrary shape
- Handles outliers well

**Hyperparameters**:
- **Epsilon**: Maximum distance to consider neighbors
- **Min_samples**: Minimum number of points to form a dense region

**Applied in**: Outlier detection, spatial data analysis, and image segmentation.
