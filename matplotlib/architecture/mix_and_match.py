import matplotlib.pyplot as plt

# DATA
x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2 = [0, 2, 8, 18, 32]

# Create a new Figure object - our main canvas.
# This uses pyplot (Level 3) for convenience.
fig, axes = plt.subplots(nrows=2, ncols=1)  # This creates a figure and 2x1 grid of Axes

# --- First Subplot: Using Artist Layer (Level 2) ---

# Select the first Axes for plotting
ax1 = axes[0]

# Plot data on ax1 using the Artist's method
line1 = plt.Line2D(x, y1, color="blue", label="y = x^2")
ax1.add_line(line1)

# Customize ax1
ax1.set_title("Using the Artist Layer")
ax1.set_xlabel("X-axis")
ax1.set_ylabel("Y-axis")
ax1.set_xlim(min(x), max(x))
ax1.set_ylim(min(y1), max(y1))
ax1.legend()

# --- Second Subplot: Using pyplot (Level 3) ---

# Use the convenience of pyplot's plot function directly on ax2
axes[1].plot(x, y2, color="red", label="y = 2x^2")

# Customize ax2 using pyplot-style calls directly on the Axes object
axes[1].set_title("Using pyplot (Level 3)")
axes[1].set_xlabel("X-axis")
axes[1].set_ylabel("Y-axis")
axes[1].legend()

# Adjust layout to ensure it looks neat
plt.tight_layout()

# Display the Figure
plt.show()
