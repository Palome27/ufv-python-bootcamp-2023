# series.py

import pandas as pd

# Creating a basic Series
s = pd.Series([1, 2, 3, 4], name="Numbers")

# ---- DISPLAYING BASIC PROPERTIES ----
# Displaying the series
print(s)
print("\n")

# The values of the Series: returns an array
print("Values:", s.values)
print("\n")

# The index of the Series: default is range if not specified during creation
print("Index:", s.index)
print("\n")

# The name of the Series: could be None if not specified
print("Name:", s.name)
print("\n")

# ---- ACCESSING DATA ----
# Accessing data by position
print("Element at position 2:", s.iloc[2])  # Should print '3'
print("\n")

# Accessing data by index label
print(
    "Element at index 2:", s.loc[2]
)  # Again, should print '3' because default index is range
print("\n")

# ---- MODIFYING SERIES ----
# Changing a value using index label
s.loc[2] = 100
print("After changing value at index 2: \n", s)
print("\n")

# Changing the index of the Series
s.index = ["a", "b", "c", "d"]
print("After changing index:", s)
print("\n")

# Accessing data with new index
print("Element at new index 'c':", s.loc["c"])  # Should print '100'
print("\n")

# ---- BOOLEAN INDEXING ----
# Filtering values based on conditions
print("Values greater than 2:", s[s > 2])
print("\n")

# ---- BASIC OPERATIONS ----
# Applying operations on Series
print("Series after adding 10 to each element:\n", s + 10)
print("\n")

# ---- HANDLING MISSING DATA ----
# Creating a Series with missing values
s_missing = pd.Series([1, 2, None, 4, None], name="With Missing Values")
print("Series with missing values:\n", s_missing)
print("\n")

# Checking for missing values
print("Is NULL check:\n", s_missing.isnull())
print("\n")

# Removing missing values
print("After dropping missing values:\n", s_missing.dropna())
print("\n")

# Replacing missing values
print("After replacing missing values with 0:\n", s_missing.fillna(0))
print("\n")

# ---- DESCRIPTIVE STATISTICS ----
# Getting basic statistics
print("Mean of Series:", s.mean())
print("Maximum value of Series:", s.max())
print("Minimum value of Series:", s.min())

# And so on, you can continue to explore many more methods and properties of a Series.
