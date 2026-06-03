"""
vertically (row-wise)
horizontally (column-wise)

pd.concate([df1, df2], axis=0, ignore_index=True)

[df1, df2] = 
axis = 1

ignore_index=True
"""

import pandas as pd

# Region1
df_Region1 = pd.DataFrame({
    'CustomerID': [1,2],
    'Name': ['Salman', 'Saif']
})

# Region2
df_Region2 = pd.DataFrame({
    'CustomerID': [3,4],
    'Name': ['Asad', 'Shawaiz']
})

# Concatenate vertically
print("Concatenate vertically")
df_concat_ver = pd.concat([df_Region1, df_Region2], ignore_index=True)
print(df_concat_ver)

# Concatenate horizontally
print("Concatenate horizontally")
df_concat_hori = pd.concat([df_Region1, df_Region2], axis=1, ignore_index=True)
print(df_concat_hori)

