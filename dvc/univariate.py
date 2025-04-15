import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df=sns.load_dataset("penguins")

print(df.head())

sns.histplot(df,x="flipper_length_mm",bins=30,kde=True)
plt.title("Histogram Plot")
plt.show()


sns.lineplot(x=df.index,y=df["flipper_length_mm"],markers='d',hue=df["species"])
plt.title("Lineplot")
plt.show()


sns.swarmplot(x=df["species"],y=df["flipper_length_mm"],hue=df["species"],palette="dark")
plt.title("Swarm Plot")
plt.show()