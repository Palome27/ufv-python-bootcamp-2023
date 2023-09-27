# Importing necessary libraries
import pandas as pd
import numpy as np

# Creating a DataFrame 'df' with two columns A and B
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

# Using the `apply()` method to apply the `sum` function along axis=0 (default)
# This will compute the sum for each column
print(df.apply(sum, axis=0))

# Using the `apply()` method to apply the `sum` function along axis=1
# This will compute the sum for each row
print(df.apply(sum, axis=1))

# Creating another DataFrame 'df2' with some missing values represented as `np.nan`
df2 = pd.DataFrame({"A": [1, np.nan, 3, np.nan], "B": [4, 5, np.nan, 7]})

# Using the `dropna()` method with axis=0 to drop any row containing at least one NaN value
# This results in a DataFrame where all rows have complete data
print(df2.dropna(axis=0))

# Using the `dropna()` method with axis=1 to drop any column containing at least one NaN value
# Since both columns A and B contain NaN values, the resulting DataFrame is empty, but it retains the original row indices
print(df2.dropna(axis=1))
