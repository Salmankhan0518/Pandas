import pandas as pd

data = {
    "Name": ["Salman", "Saif", "Zain", "Asad"],
    "Age": [10, 2, 30, 10],
    "Salary": [40000, 80000, 20000, 10000]
}


df = pd.DataFrame(data)
avg_salary = df["Salary"].mean()
max_salary = df["Salary"].max()
min_salary = df["Salary"].min()

print(avg_salary)
print(max_salary)
print(min_salary)