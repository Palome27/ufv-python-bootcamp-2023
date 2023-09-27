import pandas as pd
import numpy as np

# Sample Series
s = pd.Series([1, np.nan, 3, 4, np.nan])
print("Original Series:")
print(s)

# Mean Imputation without inplace
s_mean_imputed = s.fillna(s.mean())
print("\nSeries after Mean Imputation (without inplace):")
print(s_mean_imputed)

# Original Series remains unchanged
print("\nOriginal Series (unchanged):")
print(s)

# Zero Imputation without inplace
s_zero_imputed = s.fillna(0)
print("\nSeries after Zero Imputation (without inplace):")
print(s_zero_imputed)

# Mean Imputation with inplace
s.fillna(s.mean(), inplace=True)
print("\nSeries after Mean Imputation (with inplace):")
print(s)

# Reset Series for next inplace example
s = pd.Series([1, np.nan, 3, 4, np.nan])

# Zero Imputation with inplace
s.fillna(0, inplace=True)
print("\nSeries after Zero Imputation (with inplace):")
print(s)


# DataFrame example with the same principles
df = pd.DataFrame(
    {"A": [1, 2, np.nan, 4], "B": [5, np.nan, 7, 8], "C": [9, 10, 11, np.nan]}
)

print("\nOriginal DataFrame:")
print(df)

# Mean Imputation without inplace for DataFrame
df_mean_imputed = df.apply(lambda col: col.fillna(col.mean()))
print("\nDataFrame after Mean Imputation (without inplace):")
print(df_mean_imputed)

# Zero Imputation with inplace for DataFrame
df.fillna(0, inplace=True)
print("\nDataFrame after Zero Imputation (with inplace):")
print(df)
