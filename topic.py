"""
1- how big is your dataset
2- what are the names pf columns

shape and columns
"""

import pandas as pd

data = {
    "Name": ["Varyam", "Saif", "Salman", "Haris", "Asad", "Shawaiz", "Ahmad", "Zain"],
    "Age": [10, 20, 30, 40, 50, 60, 55, 70],
    "Salary": [50000, 60000, 70000, 80000, 90000, 450000, 850000, 650000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)
print(df)
print(f'Shape: {df.shape}')
print(f'Columns: {df.columns}')