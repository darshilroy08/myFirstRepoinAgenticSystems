import pandas as pd
import numpy as np

data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    
    "Salary": [
        60000, 50000, np.nan, 70000,
        52000, np.nan, 65000, 48000
    ],
    
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

df["Salary"].fillna(df["Salary"].mean(), inplace=True)

df.drop(columns=["Temporary_Notes"], inplace=True)

df.rename(columns={"Salary": "Annual_Salary"}, inplace=True)

summary = df.groupby("Department").agg(
    Mean_Salary=("Annual_Salary", "mean"),
    Employee_Count=("Employee", "count")
)

print("\nFinal Summary Table:")
print(summary)