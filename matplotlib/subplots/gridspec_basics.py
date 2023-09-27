import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

# Sample data
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Creating a GridSpec layout
fig = plt.figure(figsize=(10, 10))
gs = gridspec.GridSpec(3, 3)  # Creating a 3x3 grid

# Creating subplots of different sizes and positions using the GridSpec layout

# This subplot spans the entire first row
ax1 = fig.add_subplot(gs[0, :])
ax1.plot(x, y1, color="red")
ax1.set_title("Sine Wave - Spanning entire first row")
ax1.set_xlabel("X-axis")
ax1.set_ylabel("Y-axis")

# This subplot occupies the first two cells of the second row
ax2 = fig.add_subplot(gs[1, :-1])
ax2.plot(x, y2, color="blue")
ax2.set_title("Cosine Wave - First two cells of second row")
ax2.set_xlabel("X-axis")
ax2.set_ylabel("Y-axis")

# This subplot occupies the third cell of the second row and all cells of third row
ax3 = fig.add_subplot(gs[1:, -1])
ax3.plot(x, y1, color="green")
ax3.set_title("Sine Wave - Different grid span")
ax3.set_xlabel("X-axis")
ax3.set_ylabel("Y-axis")

# Adjusting layout
plt.tight_layout()
plt.show()
