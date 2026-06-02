import pandas as pd

df = pd.read_json("sample_Data.json")

print("Display first 10 rows\n")
print(df.head())

print("Display last 10 rows\n")
print(df.tail())


