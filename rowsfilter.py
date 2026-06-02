import pandas as pd

data = {
    "Name": ["Varyam", "Saif", "Salman", "Haris", "Asad", "Shawaiz", "Ahmad", "Zain"],
    "Age": [10, 20, 30, 40, 50, 60, 55, 70],
    "Salary": [50000, 60000, 70000, 80000, 90000, 450000, 850000, 650000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)
print(df)

high_salary = df[df["Salary"] > 50000]
print("Employee with salary > 50000")
print(high_salary)

# filtering rows salary > 50k & age > 30
filtered = df[(df["Salary"] > 60000) & (df["Age"] > 30)]
print("Employees with salary > 50k & age > 30")
print(filtered)


filtered2 = df[(df["Age"] > 35) | (df["Performance Score"] > 90)]
print("Employees with Age > 35 OR Performance Score > 90")
print(filtered2)