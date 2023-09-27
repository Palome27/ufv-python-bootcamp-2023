import matplotlib.pyplot as plt
import numpy as np

# Some sample data
x = np.linspace(0, 2 * np.pi, 100)  # Generating 100 points between 0 and 2*pi
y1 = np.sin(x)
y2 = np.cos(x)

# Using subplots to generate a 2x2 grid of plots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))  # 2 rows and 2 columns

# Adding plots to the grid

# Row 1, Column 1
axs[0, 0].plot(x, y1, color="red")
axs[0, 0].set_title("Sine Wave")
axs[0, 0].set_xlabel("X-axis")
axs[0, 0].set_ylabel("Y-axis")

# Row 1, Column 2
axs[0, 1].plot(x, y2, color="blue")
axs[0, 1].set_title("Cosine Wave")
axs[0, 1].set_xlabel("X-axis")
axs[0, 1].set_ylabel("Y-axis")

# Row 2, Column 1
axs[1, 0].plot(x, y1, color="green")
axs[1, 0].set_title("Sine Wave (Green)")
axs[1, 0].set_xlabel("X-axis")
axs[1, 0].set_ylabel("Y-axis")

# Row 2, Column 2
axs[1, 1].plot(x, y2, color="purple")
axs[1, 1].set_title("Cosine Wave (Purple)")
axs[1, 1].set_xlabel("X-axis")
axs[1, 1].set_ylabel("Y-axis")

# Adjusting space between the plots for clarity
plt.tight_layout()

# Display the figure with subplots
plt.show()
