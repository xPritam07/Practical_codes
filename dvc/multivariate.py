import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df=sns.load_dataset("penguins")

print(df.head())


sns.pairplot(df,hue="species",palette="dark")
plt.show()

sns.heatmap(df.iloc[:,2:6].corr(), annot=True, cmap="coolwarm", fmt=".2f",linewidths=0.5)
plt.show()