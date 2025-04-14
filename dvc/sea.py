import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="darkgrid")
df = sns.load_dataset("penguins")

print(df.head())

plt.figure(figsize=(8, 6))
sns.histplot(df["body_mass_g"], bins=30, kde=True, color="purple",edgecolor="black")
plt.title("Penguin Body Mass Distribution", fontsize=14, fontweight="bold")
plt.xlabel("Body Mass (g)", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.show()


plt.figure(figsize=(8, 6))
sns.scatterplot(x="flipper_length_mm", y="bill_length_mm", data=df, hue="species", palette="dark", s=80)
plt.title("Flipper Length vs Bill Length", fontsize=14)
plt.xlabel("Flipper Length (mm)", fontsize=12)
plt.ylabel("Bill Length (mm)", fontsize=12)
plt.grid(True)
plt.show()


plt.figure(figsize=(8, 6))
sns.boxplot(x="species", y="body_mass_g", data=df, palette="coolwarm")
sns.despine(left=True, bottom=True)
plt.title("Body Mass by Species", fontsize=14)
plt.xlabel("Species", fontsize=12)
plt.ylabel("Body Mass (g)", fontsize=12)
plt.show()