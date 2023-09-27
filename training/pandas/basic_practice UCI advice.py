# Import necessary libraries
from ucimlrepo import fetch_ucirepo
import pandas as pd

# Fetch the wine quality dataset using its ID (186 for Wine Quality Data Set)
wine_quality = fetch_ucirepo(id=186)

# Extract the feature data (inputs) and target data (outputs, if available) into DataFrames
X = wine_quality.data.features
y = wine_quality.data.targets

# Display the first 5 rows of the feature dataset
# This provides a snapshot of the dataset and the columns available.
print("First 5 rows of the feature dataset:")
print(X.head())

# Display the last 5 rows of the feature dataset
print("\nLast 5 rows of the feature dataset:")
print(X.tail())

# Get general information about the feature dataset
# This includes details like the number of entries, columns, data types of each column, and memory usage.
print("\nInformation about the feature dataset:")
print(X.info())

# Check for missing values in each column of the feature dataset
# Important to ensure there are no gaps in the data that might impact further analysis.
print("\nMissing values in the feature dataset:")
print(X.isnull().sum())

# If target data (y) is available, you can also explore it similarly
if y is not None:
    print("\nFirst 5 rows of the target dataset:")
    print(y.head())
    print("\nLast 5 rows of the target dataset:")
    print(y.tail())
    print("\nInformation about the target dataset:")
    print(y.info())
    print("\nMissing values in the target dataset:")
    print(y.isnull().sum())

# Display metadata and variable information
# Metadata often provides context about the dataset, its source, and its features.
print("\nMetadata about the Wine Quality dataset:")
print(wine_quality.metadata)

print("\nInformation about the variables in the Wine Quality dataset:")
print(wine_quality.variables)


# 1. SELECCIONAR UNA COLUMNA
# We can select a column from a DataFrame using its column name.
# Here we're selecting the 'pH' column and assigning it to a variable.
ph_series = X["pH"]
print("\nFirst 5 rows of 'pH' column:")
print(ph_series.head())

# 2. SELECCIONAR MÚLTIPLES COLUMNAS
print(X.columns)


selected_columns = X[["citric_acid", "residual_sugar"]]
# This line selects two columns: 'citric_acid' and 'residual_sugar' from the DataFrame X.
# selected_columns is a new DataFrame containing only these two columns.

# 3. Filtrar el dataframe por vinos con un nivel de alcohol mayor a 10.
wines_with_high_alcohol = X[X["alcohol"] > 10]
# This line filters the rows in the DataFrame X where the 'alcohol' column has values greater than 10.
# wines_with_high_alcohol is a new DataFrame containing only the rows where the condition is met.

# 4. Usar .loc y .iloc para seleccionar datos específicos.
# .loc is label-based indexing. You use labels to get rows or columns.
# For example, let's select the 'pH' value from the third row:
ph_third_row = X.loc[2, "pH"]

# .iloc is integer-location based indexing. You use integer indices to get rows or columns.
# Let's select the 'pH' value from the third row again, but this time using .iloc:
ph_third_row_iloc = X.iloc[2, X.columns.get_loc("pH")]
# Here, we need to find the integer index of the 'pH' column using `X.columns.get_loc('pH')`.

# Note: Indexing in Python is 0-based, so the third row has index 2.
