# Import necessary libraries
import pandas as pd

# URL for the wine quality dataset (red wine)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"

# Load the dataset directly from the URL into a DataFrame
# The dataset uses ';' as a delimiter instead of the more common comma ','.
df = pd.read_csv(url, sep=";")

# Display the first 5 rows of the DataFrame
# This gives us a quick snapshot of the dataset, including the available columns and some sample data points.
print("First 5 rows of the dataset:")
print(df.head())

# Display the last 5 rows of the DataFrame
# This helps to verify that the entire dataset has been loaded properly, especially if you're familiar with the data.
print("\nLast 5 rows of the dataset:")
print(df.tail())

# Get general information about the DataFrame
# This includes the number of entries, columns, data types of each column, and memory usage.
# It's a great way to understand the structure of your dataset at a glance.
print("\nInformation about the dataset:")
print(df.info())

# Check for missing values in each column
# This is crucial because missing data can cause errors in analysis. It's good to be aware of them early on.
print("\nMissing values in the dataset:")
print(df.isnull().sum())
