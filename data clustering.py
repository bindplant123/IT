#py --version
#py -m pip install pandas
#py -m pip install matplotlib
#py -m pip install seaborn
#py -m pip install scikit-learn

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Create synthetic dataset
X, y = make_blobs(
    n_samples=300,
    centers=4,
    cluster_std=1.0,
    random_state=42
)

# Plot original data
plt.figure(figsize=(7,5))
plt.scatter(X[:,0], X[:,1], color="gray")
plt.title("Original Data Distribution")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

# Apply K-Means
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
kmeans.fit(X)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Plot clustering result
plt.figure(figsize=(7,5))
plt.scatter(X[:,0], X[:,1], c=labels, cmap="viridis")
plt.scatter(
    centroids[:,0],
    centroids[:,1],
    s=200,
    c="red",
    marker="X",
    label="Centroids"
)

plt.title("K-Means Clustering Result")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()

# Elbow Method
wcss = []

for k in range(1,11):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X)
    wcss.append(km.inertia_)

plt.figure(figsize=(7,5))
plt.plot(range(1,11), wcss, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.show()
