import matplotlib.pyplot as plt

# 1. Create a Figure object (the entire canvas or container)
fig = plt.figure()

# 2. Add an Axes to the figure. This creates a single plot.
# The list [0,0,1,1] represents the dimensions of the Axes on the Figure,
# ranging from 0 to 1 in both dimensions, essentially filling the whole figure.
ax = fig.add_axes([0, 0, 1, 1])

# 3. Plot data on the Axes.
# Here, we plot a simple line from (0,0) to (1,1).
ax.plot([0, 1], [0, 1])

# 4. Display the Figure with the Axes and the line.
plt.show()
