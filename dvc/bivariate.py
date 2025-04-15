import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df=sns.load_dataset("penguins")

print(df.head())


sns.displot(data=df,x="bill_length_mm",y="bill_depth_mm", hue="species")
plt.show()


sns.displot(data=df,x="bill_length_mm",y="bill_depth_mm", hue="species",kind="kde")
plt.show()

sns.scatterplot(data=df,x="bill_length_mm",y="bill_depth_mm",hue="species")
plt.show()