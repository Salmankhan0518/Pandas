import pandas as pd

data = {
    "Name": ["Varyam", None, "Salman", "Haris", "Asad", "Shawaiz", "Ahmad", "Zain"],
    "Age": [10, None, 30, 40, 50, 60, 55, 70],
    "Salary": [50000, None, 70000, 80000, 90000, 450000, 850000, 650000],
    "Performance_Score": [85, None, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)
print(df)

# df.fillna({"Name": "Missing", "Age": 0, "Salary": 0, "Performance_Score": 0}, inplace=True)
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df)