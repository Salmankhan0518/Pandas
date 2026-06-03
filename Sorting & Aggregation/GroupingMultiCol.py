import pandas as pd

data = {
    "Name": ["Salman", "Saif", "Zain", "Asad", "Salman"],
    "Age": [28, 34, 22, 34, 28],
    "Salary": [50000, 60000, 45000, 52000, 480000]
}

df = pd.DataFrame(data)
print("Grouped Data")
grouped = df.groupby(["Name", "Age"])["Salary"].sum()
print(grouped)