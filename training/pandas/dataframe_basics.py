import pandas as pd

# Define a simple DataFrame with numbers
data = {"A": [1, 2, 3, 4], "B": [5, 6, 7, 8], "C": [9, 10, 11, 12]}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

column_A = df["A"]
print(column_A)

rows_with_A_greater_than_2 = df[df["A"] > 2]
print(rows_with_A_greater_than_2)
