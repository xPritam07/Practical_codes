import numpy as np
import matplotlib.pyplot as plt

# Define the original points (like corners of a square)
points = np.array([
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 1],
    [0, 0]  # to close the square
])

# Define a transformation matrix (example: scaling by 2 in x and 0.5 in y)
transformation_matrix = np.array([
    [2, 0],
    [0, 0.5]
])

# Apply the linear transformation
transformed_points = points @ transformation_matrix.T

# Plot the original shape
plt.plot(points[:, 0], points[:, 1], 'b-', label='Original Shape')

# Plot the transformed shape
plt.plot(transformed_points[:, 0], transformed_points[:, 1], 'r--', label='Transformed Shape')

plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.legend()
plt.gca().set_aspect('equal')
plt.title('Linear Transformation Example')
plt.grid(True)
plt.show()
