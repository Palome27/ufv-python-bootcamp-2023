import matplotlib.pyplot as plt

# Create a new Figure object - this is your canvas
fig = plt.figure()

# Add an Axes to the Figure - this is your plot area
ax = fig.add_subplot(1, 1, 1)  # add_subplot(1, 1, 1) means a 1x1 grid, first subplot.

# Create data
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

# Plot data on the Axes using Line2D primitive
line = plt.Line2D(x, y)
ax.add_line(line)

# Set the limits of the plot
ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y))

# Display the Figure
plt.show()
