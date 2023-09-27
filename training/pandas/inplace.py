import pandas as pd
import numpy as np

# ==============================================
# Handling Series
# ==============================================
print("============== Series Operations ==============")

# Create a sample Series with missing values
s = pd.Series([1, np.nan, 3, 4, np.nan])
print("\nOriginal Series:")
print(s)

# Using dropna() without inplace returns a new Series
s_without_na = s.dropna()
print("\nSeries after dropna() without inplace:")
print(s_without_na)

# Original Series remains unchanged
print("\nOriginal Series (unchanged):")
print(s)

# Using dropna() with inplace=True modifies the original Series
s.dropna(inplace=True)
print("\nOriginal Series after dropna() with inplace=True:")
print(s)


# ==============================================
# Handling DataFrames
# ==============================================
print("\n\n============== DataFrame Operations ==============")

# Create a sample DataFrame with missing values
df = pd.DataFrame(
    {"A": [1, 2, np.nan, 4], "B": [5, np.nan, 7, 8], "C": [9, 10, 11, np.nan]}
)

print("\nOriginal DataFrame:")
print(df)

# Using dropna() without inplace on DataFrame; by default it drops rows with any NaN values
df_without_na = df.dropna()
print("\nDataFrame after dropna() without inplace:")
print(df_without_na)

# Original DataFrame remains unchanged
print("\nOriginal DataFrame (unchanged):")
print(df)

# Using dropna() with inplace=True on DataFrame
df.dropna(inplace=True)
print("\nOriginal DataFrame after dropna() with inplace=True:")
print(df)


# ==============================================
# Conclusion
# ==============================================
print(
    "\n\nBy default, many operations in Pandas produce a new object, leaving the original unchanged."
)
print(
    "However, with the 'inplace=True' parameter, these operations modify the original object directly."
)
