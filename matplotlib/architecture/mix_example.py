# Step 1: Import necessary modules
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

# Step 2: Create a blank Figure object
# A Figure in Matplotlib represents the whole window or page that everything is drawn on.
fig = Figure()

# Step 3: Associate the Figure with a backend canvas
# FigureCanvas is a representation of the rendering surface for the Figure.
# In this case, we're using the Agg backend, which stands for "Anti-Grain Geometry"
# and is a high-quality rendering engine for producing raster graphics (i.e., pixel-based, like PNGs).
canvas = FigureCanvas(fig)

# Step 4: Generate sample data
# Here we're generating 10,000 random numbers from a normal (Gaussian) distribution
# with a mean (mu) of 0 and standard deviation (sigma) of 1.
x = np.random.randn(10000)

# Step 5: Create an Axes object in the Figure
# The add_subplot(111) is a shorthand for add_subplot(1, 1, 1) which means
# we're adding a single subplot in a grid that's 1x1 (i.e., only one plot in the Figure).
# 'ax' is an Axes object, which represents a single plot in the Figure.
ax = fig.add_subplot(111)

# Step 6: Plot a histogram on the Axes
# We're plotting a histogram of the data with 100 bins.
# A histogram is useful for visualizing the distribution of a dataset.
ax.hist(x, 100)

# Step 7: Set the title for the Axes
# We're using LaTeX notation (between $ symbols) to format the title.
# This makes it easy to include mathematical symbols and equations in the title.
ax.set_title("Normal distribution with $\mu=0, \sigma=1$")

# Step 8: Save the Figure to an image file
# This saves the entire Figure (including all its Axes) to a PNG image file named 'matplotlib_histogram.png'.
# The image will be saved in the current working directory.
fig.savefig("matplotlib_histogram.png")
