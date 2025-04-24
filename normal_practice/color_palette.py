# import seaborn as sns
# import matplotlib.pyplot as plt

# # Display the 'pastel' palette
# palette = sns.color_palette("pastel")
# sns.palplot(palette)
# plt.title("Pastel Palette")
# plt.show()



# import seaborn as sns
# import matplotlib.pyplot as plt

# # List of palettes to display
# palettes = ['deep', 'muted', 'pastel', 'dark', 'colorblind', 'bright', 'Oranges', "Blues"]

# # Set up the figure
# plt.figure(figsize=(8, len(palettes) * 1))

# for i, name in enumerate(palettes):
#     plt.subplot(len(palettes), 1, i + 1)
#     sns.palplot(sns.color_palette(name))
#     plt.title(name, loc='left', fontsize=10)
#     plt.axis('off')

# plt.tight_layout()
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Generate univariate normal data
data = np.random.normal(loc=0, scale=1, size=1000)
plt.plot(sorted(data), color='purple')
plt.title("Sorted Line Plot of Data")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)
plt.show()
