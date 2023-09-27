import numpy as np
import matplotlib.pyplot as plt


# Random data for scatter
x = np.random.rand(500)
y = np.random.rand(500)

# Create a scatter plot
plt.scatter(x, y, color="purple", marker="*", s=100, label="Data points")

# Add labels and title
plt.xlabel("X-values")
plt.ylabel("Y-values")
plt.title("Scatter Plot with pyplot")
plt.legend()

# Display the plot
plt.show()
