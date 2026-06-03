import pandas as pd

# Customer dataframe
df_customers = pd.DataFrame({
    'CustomerID': [1,2,3],
    'Name': ['Salman', 'Saif', 'Asad']
})


# Order dataframe
df_orders = pd.DataFrame({
    'CustomerID': [1,2,4],
    'OrderAmount': [250, 450, 350]
})

# Merge
# df_merged = pd.merge(df_customers, df_orders, on='CustomerID', how="inner")
# print("Inner Join")
# print(df_merged)

# df_merged = pd.merge(df_customers, df_orders, on='CustomerID', how="outer")
# print("Outer Join")
# print(df_merged)

# df_merged = pd.merge(df_customers, df_orders, on='CustomerID', how="left")
# print("Left Join")
# print(df_merged)

df_merged = pd.merge(df_customers, df_orders, on='CustomerID', how="right")
print("Right Join")
print(df_merged)