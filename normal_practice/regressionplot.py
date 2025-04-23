import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'hours': [1, 2, 3, 4, 5, 6],
    'score': [50, 55, 60, 63, 67, 70],
    'subject': ['Math', 'Math', 'Science', 'Science', 'Math', 'Science']
})

sns.lmplot(data=df, x='hours', y='score', hue='subject', height=5)
plt.title("Regression by Subject")
plt.show()


# Sample data
x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 5, 4, 5, 6]

sns.regplot(x=x, y=y)
plt.title("Simple Linear Regression")
plt.xlabel("Independent Variable")
plt.ylabel("Dependent Variable")
plt.show()