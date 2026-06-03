import pandas as pd

data = {
    "Name": ["Salman", "Saif", "Zain", "Asad"],
    "Age": [10, 2, 30, 10],
    "Salary": [40000, 80000, 20000, 10000]
}

print('Before sorting Data')
df = pd.DataFrame(data)
print(df)

df.sort_values(by=["Age", "Salary"], ascending=[True, True], inplace=True)
print('After sorting Data')
print(df)
