import numpy as np
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

# AND gate data
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])
y = np.array([0, 0, 0, 1])

# Input shape
input_size = X.shape[1]

# Initialize weights and bias as ones (including bias term)
parameters = np.ones(input_size + 1)  # [bias, w1, w2]

def activation_function(z):
    """Step activation function"""
    return 1 if z >= 0 else 0

def plot(epoch):
    """Plot decision boundary and data points"""
    # slope (m) and intercept (c) of the decision boundary line
    m = -(parameters[1] / parameters[2])
    c = -(parameters[0] / parameters[2])

    x_input = np.linspace(-0.5, 1.5, 100)
    y_input = m * x_input + c

    plt.figure(figsize=(5, 3))
    plt.plot(x_input, y_input, color='red', linewidth=2, label='Decision boundary')
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='winter', s=200, edgecolor='k')
    plt.title(f'Epoch {epoch + 1}')
    plt.xlim(-0.5, 1.5)
    plt.ylim(-0.5, 1.5)
    plt.legend()
    plt.show()

# Training parameters
epochs = 7
learning_rate = 0.2

for epoch in range(epochs):
    for i in range(X.shape[0]):
        # Add bias input 1
        x = np.insert(X[i], 0, 1)

        # Linear combination
        z = parameters.dot(x)

        # Apply activation
        y_hat = activation_function(z)

        # Calculate error
        e = y[i] - y_hat

        # Update parameters
        parameters += learning_rate * e * x

    # Plot decision boundary after each epoch
    plot(epoch)

print("Learned parameters (bias, w1, w2):", parameters)
