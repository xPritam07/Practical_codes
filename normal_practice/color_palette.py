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

# import matplotlib.pyplot as plt
# import numpy as np

# # Generate univariate normal data
# data = np.random.normal(loc=0, scale=1, size=1000)
# plt.plot(sorted(data), color='purple')
# plt.title("Sorted Line Plot of Data")
# plt.xlabel("Index")
# plt.ylabel("Value")
# plt.grid(True)
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Sample data
# x = np.random.rand(20) * 100
# y = np.random.rand(20) * 100
# sizes = np.random.rand(20) * 1000  # Bubble size

# # Bubble plot
# plt.figure(figsize=(8, 6))
# plt.scatter(x, y, s=sizes, alpha=0.6, c='skyblue', edgecolors='black')

# plt.title("Bubble Plot with Matplotlib")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.grid(True)
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
line, = ax.plot([], [], 'r-')
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    line.set_data(xdata, ydata)
    ax.set_xlim(max(0, frame - 10), frame + 1)
    return line,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 20, 200),
                    interval=100, blit=True)

plt.show()
