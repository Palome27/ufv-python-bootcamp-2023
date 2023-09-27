import numpy as np
import matplotlib.pyplot as plt


# Random data for histogram
data = np.random.randn(1000)

# Create a histogram
plt.hist(data, bins=30, color="cyan", edgecolor="black", label="Frequency")

# Add labels and title
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.title("Histogram with pyplot")
plt.legend()

# Display the plot
plt.show()
