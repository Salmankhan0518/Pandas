# Sorting data
# Sorting Data 1 column sort_values()

# df.sort_values(by="Columns Name", True/False, inplace = True)

import pandas as pd

data = {
    "Name": ["Salman", "Saif", "Zain", "Asad"],
    "Age": [10, 2, 30, 4],
    "Salary": [10000, 20000, 30000, 40000]
}

df = pd.DataFrame(data)

df.sort_values(by="Age", ascending=True, inplace=True)
print("Sorted Age by Descending order")
print(df)