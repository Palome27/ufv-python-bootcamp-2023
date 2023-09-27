import matplotlib.pyplot as plt
import numpy as np

# Generate sample data for demonstration
np.random.seed(42)  # for reproducibility
data1 = np.random.randn(200) + 1  # Normally distributed data centered at 1
data2 = np.random.randn(150) * 2  # Normally distributed data with larger variance
data3 = np.random.randn(100) - 1  # Normally distributed data centered at -1

# Create a new figure and a set of subplots
fig, ax = plt.subplots(figsize=(8, 6))

# Creating a boxplot using the Axes object
# The boxplot method of the Axes object allows us to visualize the distribution of multiple datasets side-by-side.
# The box represents the interquartile range (IQR: Q3 - Q1),
# the whiskers usually extend to data within 1.5 * IQR from Q1 and Q3, and any data points outside of this range are considered outliers.
ax.boxplot([data1, data2, data3])

# Setting the title of the plot
ax.set_title("Boxplot of Three Datasets")

# Setting the y-axis label
ax.set_ylabel("Value")

# Setting the x-axis tick labels to describe our three datasets
ax.set_xticks([1, 2, 3])
ax.set_xticklabels(["Data 1", "Data 2", "Data 3"])

# Display the plot
plt.show()
