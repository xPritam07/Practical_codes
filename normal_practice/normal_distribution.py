import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate normally distributed data
data = np.random.normal(loc=0, scale=1, size=1000)  # mean=0, std=1, 1000 samples

# Plot the distribution
sns.histplot(data, kde=True, color='skyblue', bins=30)
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


from scipy.stats import norm

x = np.linspace(-4, 4, 100)
y = norm.pdf(x, loc=0, scale=1)

plt.plot(x, y, color='red')
plt.title("Theoretical Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.grid(True)
plt.show()
