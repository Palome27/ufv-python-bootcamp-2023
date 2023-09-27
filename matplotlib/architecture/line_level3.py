import matplotlib.pyplot as plt

# Create data
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

# Use pyplot's plot function to create the line plot
plt.plot(x, y)

# Display the plot
plt.show()


"""

In the Artist layer approach, you have explicit control over the Figure and Axes. Every component you want in the plot has to be added manually. This gives you fine-grained control over the elements of the plot.

In the pyplot approach, a lot of things are automated for you. When you call plt.plot(), it automatically deals with creating a Figure, an Axes, a Line2D object, etc. It abstracts away many of the details, making the code shorter and more intuitive for simple tasks.

"""
