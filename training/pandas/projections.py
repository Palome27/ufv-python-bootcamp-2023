import pandas as pd

# Sample DataFrame for illustration.
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

# Display the initial state.
print("Original DataFrame:")
print(df)
print("-" * 30)

# ------------------------------
# 1. Projection by Selecting Columns
# ------------------------------

# Create a projection by selecting column 'A'.
col_proj = df[["A"]]
print(type(col_proj))

print(col_proj)

# Modify values in the projected column.
col_proj["A"] = [10, 11, 12]
print(col_proj)

# Check if the original DataFrame is affected.
print("Original DataFrame after modifying column projection:")
print(df)
print("Notice: Original DataFrame is NOT affected.")
print("-" * 30)

# ------------------------------
# 2. Projection by Selecting Rows (Boolean Indexing)
# ------------------------------

# Create a row projection based on a condition.
row_proj = df[df["A"] > 1]

# Try modifying values in the row projection.
# Pandas will throw a SettingWithCopyWarning here.
row_proj["A"] = [20, 30]

# Check if the original DataFrame is affected.
print("Original DataFrame after modifying row projection:")
print(df)
print("Notice: Original DataFrame is STILL NOT affected (but with a warning).")
print("-" * 30)

# ------------------------------
# 3. Modifying Original DataFrame with .loc
# ------------------------------

# Use .loc to modify values in the original DataFrame based on a condition.
df.loc[df["A"] > 1, "A"] = [20, 30]

# Check if the changes are reflected.
print("Original DataFrame after modifying with .loc:")
print(df)
print("Notice: Original DataFrame IS affected.")
print("-" * 30)

# ------------------------------
# 4. Chain Assignments
# ------------------------------

# Reset the DataFrame to its initial state for clarity.
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

# Attempt a chained assignment.
df[df["A"] > 1]["A"] = [99, 100]

# Check if the original DataFrame is affected.
print("Original DataFrame after chained assignment:")
print(df)
print("Notice: Original DataFrame is NOT affected (and we get a warning).")
print("-" * 30)

# ------------------------------
# Conclusion:
# It's crucial to be aware of how modifications in projections might
# or might not impact the original DataFrame. Using .loc or .iloc
# ensures direct modifications to the original DataFrame.
