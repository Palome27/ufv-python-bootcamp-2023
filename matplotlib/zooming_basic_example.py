import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(-10, 10, 400)
y = 1 / (1 + np.exp(-x))  # This computes the sigmoid function.

# Create a figure and a 1x2 subplot (1 row, 2 columns)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plot the complete sigmoid curve on the first subplot
ax1.plot(x, y, label="Sigmoid Curve")
ax1.set_title("Complete Sigmoid Curve")
ax1.set_xlabel("X-axis")
ax1.set_ylabel("Y-axis")
ax1.legend()
ax1.grid(True)  # Just adding a grid for clarity

# Plot the same sigmoid curve on the second subplot
ax2.plot(x, y, label="Sigmoid Curve", color="blue")
ax2.set_title("Zoomed-in Sigmoid Curve")
ax2.set_xlabel("X-axis")
ax2.set_ylabel("Y-axis")

# Here we zoom in to see the steepest part of the curve around x=0, say between x=-2 to x=2
ax2.axis([-2, 2, 0.1, 0.9])  # This gives us a "zoomed-in" view.
ax2.legend()
ax2.grid(True)  # Just adding a grid for clarity

plt.tight_layout()
plt.show()
