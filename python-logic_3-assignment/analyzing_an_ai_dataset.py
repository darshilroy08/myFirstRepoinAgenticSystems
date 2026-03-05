import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Score": [95, 88, 92, 76, 85, 90],
    "Passed": [True, True, True, False, True, True],
    "Category": ["A", "B", "A", "C", "B", "A"]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

print("\nSingle Column (Score):")
print(df["Score"])

print("\nMultiple Columns (Name, Score):")
new_df = df[["Name", "Score"]]
print(new_df)

print("\nFirst 3 rows using iloc:")
print(df.iloc[0:3])

df_indexed = df.set_index("Name")
print("\nUsing loc after setting Name as index:")
print(df_indexed.loc["Alice"])

print("\nStudents with Score > 85:")
print(df[df["Score"] > 85])

print("\nStudents with Score > 85 and Passed = True:")
print(df[(df["Score"] > 85) & (df["Passed"] == True)])

print("\nSorted High Performing Students:")
high_performers = df[df["Score"] > 85].sort_values(by="Score", ascending=False)
print(high_performers)