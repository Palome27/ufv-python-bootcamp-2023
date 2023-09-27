import numpy as np

# Create a 3D array. Let's consider a shape of (3, 4, 2) for simplicity.
# This means we have 3 matrices, each of size 4x2.

array_3d = np.arange(24).reshape(3, 4, 2)

print("Original 3D array:")
print(array_3d)

# The 3D array can be thought of as:
# [
#   [[ 0,  1],   <- First matrix (4x2)
#    [ 2,  3],
#    [ 4,  5],
#    [ 6,  7]],
#
#   [[ 8,  9],   <- Second matrix (4x2)
#    [10, 11],
#    [12, 13],
#    [14, 15]],
#
#   [[16, 17],   <- Third matrix (4x2)
#    [18, 19],
#    [20, 21],
#    [22, 23]]
# ]

# Accessing individual matrices (2D arrays) from our 3D array:
first_matrix = array_3d[0]
print("\nFirst matrix:")
print(first_matrix)

# You can think of the first index as specifying which "layer" or "slice" you want from the 3D array.

# Accessing rows from the first matrix:
first_row_first_matrix = array_3d[0, 0]
print("\nFirst row of the first matrix:")
print(first_row_first_matrix)
# Output: [0 1]

# Accessing an individual element:
element = array_3d[0, 0, 1]
print(
    "\nAn individual element (second element from the first row of the first matrix):"
)
print(element)
# Output: 1

# Sum all elements in our 3D array:
sum_elements = np.sum(array_3d)
print("\nSum of all elements in 3D array:")
print(sum_elements)
# Output: 276

# Flattening the 3D array:
flattened = array_3d.flatten()
print("\nFlattened 3D array:")
print(flattened)
# Output: [ 0  1  2 ... 21 22 23]
# This takes all the values in the 3D array and puts them in a 1D list.

# Performing an operation on the 3D array, e.g., adding 10 to each element:
added = array_3d + 10
print("\n3D array after adding 10 to each element:")
print(added)

# Taking a slice of the 3D array, say first 2 matrices:
slice_3d = array_3d[:2]
print("\nFirst 2 matrices from the 3D array:")
print(slice_3d)

# Using mathematical operations:
mean_val = np.mean(array_3d)
print("\nMean value of the 3D array:")
print(mean_val)
# Output: 11.5

# You can also compute the mean along a specific axis, say along the first axis (i.e., across the 3 matrices).
mean_across_matrices = np.mean(array_3d, axis=0)
print("\nMean value across the matrices:")
print(mean_across_matrices)
# This will give you a 4x2 matrix showing the average value at each position across the 3 matrices.


# Computing the mean along axis=1 (rows of each matrix):
mean_rows = np.mean(array_3d, axis=1)
print("Mean along axis=1 (rows of each matrix):")
print(mean_rows)

# Here's what happens:
# For the first matrix:
# [[ 0,  1],
#  [ 2,  3],
#  [ 4,  5],
#  [ 6,  7]]
# The mean of all rows will be: [3.  4.]

# And similarly for the next matrices.

# Computing the mean along axis=2 (columns of each matrix):
mean_columns = np.mean(array_3d, axis=2)
print("\nMean along axis=2 (columns of each matrix):")
print(mean_columns)

# For the first matrix:
# [[ 0,  1],
#  [ 2,  3],
#  [ 4,  5],
#  [ 6,  7]]
# The mean of the first row (across columns) is 0.5, the second row is 2.5, and so on.

# The resulting structure will be:
# [
#   [0.5, 2.5, 4.5, 6.5],  <- Mean for each row of the first matrix
#   [8.5, 10.5, 12.5, 14.5],  <- Mean for each row of the second matrix
#   ...
# ]
