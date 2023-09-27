# First, we import necessary libraries.
import numpy as np  # NumPy for numerical computations.
import matplotlib.pyplot as plt  # Matplotlib's PyPlot module for plotting.

# ------------------------------------------------
# 1. Basic Line Plot
# ------------------------------------------------

# Generate an array of 100 evenly spaced numbers between 0 and 10.
# This will serve as our x-axis values.
x = np.linspace(0, 10, 100)

# Compute the sine of each number in the x array.
# This gives us our y-axis values for the sine wave.
y = np.sin(x)

# Plot the x and y values on a graph.
plt.plot(x, y)

# Add a title to the plot.
plt.title("Basic Sine Wave")

# Label the x and y axes.
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Display a grid in the background to make reading the plot easier.
plt.grid(True)

# Display the plot.
plt.show()

# ------------------------------------------------
# 2. Multiple Plots in One Figure
# ------------------------------------------------

# Compute the cosine of each number in the x array.
# This gives us our y-axis values for the cosine wave.
y2 = np.cos(x)

# Plot the sine wave with label 'Sine Wave'.
plt.plot(x, y, label="Sine Wave")

# Plot the cosine wave with a dashed line style and label 'Cosine Wave'.
plt.plot(x, y2, label="Cosine Wave", linestyle="--")

# Add a title to the plot.
plt.title("Sine and Cosine Waves")

# Label the x and y axes.
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Display the legend to differentiate between sine and cosine waves.
plt.legend()

# Display a grid.
plt.grid(True)

# Show the plot.
plt.show()

# ------------------------------------------------
# 3. Histogram
# ------------------------------------------------

# Generate 1000 random numbers from a standard normal distribution.
data = np.random.randn(1000)

# Plot a histogram of the data with 30 bins. 'alpha' makes bars semi-transparent.
plt.hist(data, bins=30, alpha=0.75)

# Add a title to the histogram.
plt.title("Histogram")

# Label the x and y axes.
plt.xlabel("Value")
plt.ylabel("Frequency")

# Display a grid.
plt.grid(True)

# Show the histogram.
plt.show()

# ------------------------------------------------
# 4. Scatter Plot
# ------------------------------------------------

# Generate 100 random numbers from a standard normal distribution for x and y axes.
x_scatter = np.random.randn(100)
y_scatter = np.random.randn(100)

# Create a scatter plot using x_scatter and y_scatter.
# Points are colored red and use 'o' as the marker symbol.
plt.scatter(x_scatter, y_scatter, color="red", marker="o")

# Add a title to the scatter plot.
plt.title("Scatter Plot")

# Label the x and y axes.
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Display a grid.
plt.grid(True)

# Show the scatter plot.
plt.show()
