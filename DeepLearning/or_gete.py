import matplotlib.pyplot as plt
import numpy as np

# Step 1: OR Gate Inputs and Outputs
inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
outputs = [0, 1, 1, 1]

# Step 2: Initialize weights and bias
w1 = w2 = bias = 0.0
lr = 0.1 # learning rate

# Step 3: Train the model
for _ in range(10):
    for i in range(4):
        x1, x2 = inputs[i]
        y = outputs[i]
        z = x1 * w1 + x2 * w2 + bias
        pred = 1 if z >= 0.5 else 0
        error = y - pred
        w1 += lr * error * x1
        w2 += lr * error * x2
        bias += lr * error

# Step 4: Test the model
print("OR Gate Results:")
for x1, x2 in inputs:
    z = x1 * w1 + x2 * w2 + bias
    result = 1 if z >= 0.5 else 0
    print(f"{x1} OR {x2} = {result}")

# Step 5: Simple Plot
plt.scatter(*zip(*inputs), c=outputs, cmap='RdYlGn', s=100)
x = np.linspace(-0.2, 1.2, 100)
plt.plot(x, [(-w1 * xi - bias + 0.5) / w2 for xi in x], 'b')
plt.title("OR Gate Output")
plt.grid(True)
plt.show()