import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create X and Y vectors
X = np.linspace(-2, 2, 100)
Y = 2 * X + 1
print(X)
print("-" * 80)
print(Y)

plt.figure()
plt.xlabel("X")
plt.ylabel("Y")
plt.xlim((-7, 7))  # Fix xlim syntax
plt.ylim((-7, 7))  # Fix ylim syntax
# Draw lines to split quadrants
plt.plot([-6, 6], [0, 0], linewidth=2, color='black')
plt.plot([0, 0], [6, -6], linewidth=2, color='black')
plt.plot(X, Y)
plt.title("Line Plot: Y = 2X + 1")
plt.grid(True)
plt.show()

# Plotting two lines
X = np.linspace(-2, 2, 100)
Y = 2 * X + 1
Y1 = 2 * X + 3
print(X)
print("-" * 80)
print(Y)
print("-" * 80)
print(Y1)

plt.figure()
plt.xlabel("X")
plt.ylabel("Y")
plt.xlim((-7, 7))
plt.ylim((-7, 7))
plt.plot([-6, 6], [0, 0], linewidth=2, color='black')
plt.plot([0, 0], [6, -6], linewidth=2, color='black')
plt.plot(X, Y, label="Y = 2X + 1")
plt.plot(X, Y1, label="Y = 2X + 3", linestyle='--')
plt.title('Two Linear Functions')
plt.legend()
plt.grid(True)
plt.show()

# Meshgrid and transformation
x = np.arange(-10, 10, 1)
y = np.arange(-10, 10, 1)
xx, yy = np.meshgrid(x, y)
print(xx, yy)
plt.figure()
plt.scatter(xx, yy, s=20, c=xx + yy)
plt.xlabel("XX")
plt.ylabel("YY")
plt.xlim((-10, 10))
plt.ylim((-10, 10))
plt.plot([-9, 9], [0, 0], linewidth=2, color='black')
plt.plot([0, 0], [9, -9], linewidth=2, color='black')
plt.title("Original Grid")
plt.grid(True)
plt.show()

# Linear transformation
T = np.array([[-1, 0], [0, -1]])
xy = np.vstack([xx.flatten(), yy.flatten()])
print(xy.shape)
print(T @ xy[:, 0])
trans = T @ xy
print(trans.shape)

xx_transformed = trans[0].reshape(xx.shape)
yy_transformed = trans[1].reshape(yy.shape)
f, axes = plt.subplots(1, 2, figsize=(6, 3))
axes[0].scatter(xx, yy, s=10, c=xx + yy)
axes[0].set_xlabel("XX")
axes[0].set_ylabel("YY")
axes[0].plot([-9, 9], [0, 0], linewidth=2, color="lightgray")
axes[0].plot([0, 0], [9, -9], linewidth=2, color="lightgray")
axes[0].set_title("Original")

axes[1].scatter(xx_transformed, yy_transformed, s=10, c=xx + yy)
axes[1].set_xlabel("XX")
axes[1].set_ylabel("YY")
axes[1].plot([-9, 9], [0, 0], linewidth=2, color="lightgray")
axes[1].plot([0, 0], [9, -9], linewidth=2, color="lightgray")
axes[1].set_title("Reflected")
plt.tight_layout()
plt.show()

# Another transformation
T = np.array([[1.3, -2.4], [0.1, 2]])
trans = T @ xy
xx_transformed = trans[0].reshape(xx.shape)
yy_transformed = trans[1].reshape(yy.shape)
f, axes = plt.subplots(1, 2, figsize=(6, 3))
axes[0].scatter(xx, yy, s=10, c=xx + yy)
axes[0].set_xlabel("XX")
axes[0].set_ylabel("YY")
axes[0].plot([-9, 9], [0, 0], linewidth=2, color="lightgray")
axes[0].plot([0, 0], [9, -9], linewidth=2, color="lightgray")
axes[0].set_title("Original")

axes[1].scatter(xx_transformed, yy_transformed, s=10, c=xx + yy)
axes[1].set_xlabel("XX")
axes[1].set_ylabel("YY")
axes[1].plot([-40, 40], [0, 0], linewidth=1, color="lightgray")
axes[1].plot([0, 0], [40, -40], linewidth=1, color="lightgray")
axes[1].set_title("Transformed")
plt.tight_layout()
plt.show()

# Inverse transformation
T = np.array([[1.3, -2.4], [0.1, 2]])
trans = T @ xy
T_inv = np.linalg.inv(T)
un_trans = T_inv @ trans
f, axes = plt.subplots(1, 3, figsize=(9, 3), dpi=100)
axes[0].scatter(xx, yy, s=10, c=xx + yy)
axes[0].set_xlabel("XX")
axes[0].set_ylabel("YY")
axes[0].plot([-15, 15], [0, 0], linewidth=2, color="lightgray")
axes[0].plot([0, 0], [15, -15], linewidth=2, color="lightgray")
axes[0].set_title("Initial")

axes[1].scatter(trans[0].reshape(xx.shape), trans[1].reshape(yy.shape), s=10, c=xx + yy)
axes[1].set_xlabel("XX")
axes[1].plot([-40, 40], [0, 0], linewidth=1, color="lightgray")
axes[1].plot([0, 0], [40, -40], linewidth=1, color="lightgray")
axes[1].set_title("Transformed")

axes[2].scatter(un_trans[0].reshape(xx.shape), un_trans[1].reshape(yy.shape), s=10, c=xx + yy)
axes[2].set_xlabel("XX")
axes[2].plot([-15, 15], [0, 0], linewidth=2, color="lightgray")
axes[2].plot([0, 0], [15, -15], linewidth=2, color="lightgray")
axes[2].set_title("Transformed Back")
plt.tight_layout()
plt.show()

# Singular transformation
T = np.array([[3, 6], [2, 4]])  # This is a singular matrix
trans = T @ xy
f, axes = plt.subplots(1, 2, figsize=(6, 3), dpi=100)
axes[0].scatter(xx, yy, s=10, c=xx + yy)
axes[0].set_xlabel("XX")
axes[0].set_ylabel("YY")
axes[0].plot([-15, 15], [0, 0], linewidth=2, color="lightgray")
axes[0].plot([0, 0], [15, -15], linewidth=2, color="lightgray")
axes[0].set_title("Original")

axes[1].scatter(trans[0].reshape(xx.shape), trans[1].reshape(yy.shape), s=10, c=xx + yy)
axes[1].set_xlabel("XX")
axes[1].set_ylabel("YY")
axes[1].plot([-50, 50], [0, 0], linewidth=2, color="lightgray")
axes[1].plot([0, 0], [50, -50], linewidth=2, color="lightgray")
axes[1].set_title("Transformed (Singular)")
plt.tight_layout()
plt.show()
