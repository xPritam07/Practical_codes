import numpy as np
from scipy.sparse import csr_matrix

# Regular dense matrix
dense_matrix = np.array([
    [5, 0, 0, 0],
    [0, 0, 8, 0],
    [0, 0, 0, 0],
    [0, 3, 0, 0]
])

print("Dense Matrix:")
print(dense_matrix)

# Convert to Compressed Sparse Row (CSR) format
sparse_matrix = csr_matrix(dense_matrix)

print("\nSparse Matrix (CSR format):")
print(sparse_matrix)

# View the nonzero data
print("\nNonzero values:")
print(sparse_matrix.data)

print("\nRow indices of nonzero values:")
print(sparse_matrix.indices)

print("\nPointer to row start:")
print(sparse_matrix.indptr)

# If needed, convert back to dense
reconstructed_matrix = sparse_matrix.toarray()
print("\nReconstructed Dense Matrix:")
print(reconstructed_matrix)
