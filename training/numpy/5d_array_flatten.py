import numpy as np

# Create a 5D array. Let's keep the shape simple, say (2, 2, 2, 2, 2).
# Here, each dimension has 2 elements, so the total number of elements is 2^5 = 32.

array_5d = np.arange(32).reshape(2, 2, 2, 2, 2)

print("Original 5D array:")
print(array_5d)
# This will print a 5D array, which is a bit challenging to visualize, but it will look like a series of nested lists.

# Now, let's flatten the array
flattened_array = array_5d.flatten()

print("\nFlattened array:")
print(flattened_array)
# Output: [ 0  1  2  3 ... 29 30 31]
# It's now a simple 1D array with 32 elements, ranging from 0 to 31.

"""

When you flatten this 5D array, it collapses all the nested structure and gives you back a simple, one-dimensional array with all the elements. The ordering is retained, so you'll see the elements in the order they appeared in the original 5D array.

"""
