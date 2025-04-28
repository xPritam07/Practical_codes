# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# Load a sample dataset (Iris dataset)
data = load_iris()
X = data.data  # features
y = data.target  # labels (not used in PCA, but useful for plotting)

# Step 1: Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 2: Apply PCA
pca = PCA(n_components=2)  # reduce to 2 principal components
X_pca = pca.fit_transform(X_scaled)

# Step 3: Plot the PCA-reduced data
plt.figure(figsize=(8, 6))
for label in np.unique(y):
    plt.scatter(X_pca[y == label, 0], X_pca[y == label, 1], label=data.target_names[label])
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title('PCA on Iris Dataset')
plt.legend()
plt.grid(True)
plt.show()

# Step 4: Explained Variance
print("Explained variance by each component:", pca.explained_variance_ratio_)
print("Total variance explained:", np.sum(pca.explained_variance_ratio_))
