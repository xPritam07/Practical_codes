import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create a skewed population (Exponential distribution)
population = np.random.exponential(scale=2.0, size=100000)
plt.figure(figsize=(10, 5))
plt.hist(population, bins=100, color='skyblue', edgecolor='black')
plt.title('Original Skewed Population (Exponential Distribution)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Step 2: Simulate the sampling process
sample_means = []
sample_size = 30  # Each sample will have 30 points
num_samples = 1000  # We take 1000 samples

for _ in range(num_samples):
    sample = np.random.choice(population, size=sample_size)
    sample_means.append(np.mean(sample))

# Step 3: Plot the distribution of sample means
plt.figure(figsize=(10, 5))
plt.hist(sample_means, bins=30, color='lightgreen', edgecolor='black')
plt.title('Distribution of Sample Means (Central Limit Theorem)')
plt.xlabel('Sample Mean Value')
plt.ylabel('Frequency')
plt.show()
