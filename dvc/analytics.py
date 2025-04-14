import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt

df=sns.load_dataset('penguins')
print(df.head())


plt.figure(figsize=(8, 6))
sns.regplot(x="bill_length_mm", y="bill_depth_mm", data=df, scatter_kws={'color':'blue'}, line_kws={'color':'red'})
plt.title("Regression: Bill Length vs Bill Depth", fontsize=14)
plt.xlabel("Bill Length (mm)", fontsize=12)
plt.ylabel("Bill Depth (mm)", fontsize=12)
plt.show()


plt.figure(figsize=(8, 6))
sns.heatmap(df.iloc[:,2:6].corr(), annot=True, cmap="coolwarm", fmt=".2f",linewidths=0.5)
plt.title("Correlation Heatmap of Penguin Features", fontsize=14)
plt.show()

sns.pairplot(df, kind="reg", hue="species", palette="muted")
plt.show()