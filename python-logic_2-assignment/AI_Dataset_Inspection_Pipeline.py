import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace"],
    "Age": [21, 22, 23, 21, 22, 24, 23],
    "Score": [85, 78, 92, 88, 76, 95, 81],
    "Label": ["Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass"]
}

df = pd.DataFrame(data)
df.to_csv("dataset.csv", index=False)

df = pd.read_csv("dataset.csv")

print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

age_column = df["Age"]
print("\nSingle Column (Age):")
print(age_column)

selected_columns = df[["Name", "Score"]]
print("\nMultiple Columns (Name, Score):")
print(selected_columns)

filtered_rows = df[df["Score"] > 80]
print("\nFiltered rows (Score > 80):")
print(filtered_rows)