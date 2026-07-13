import pandas as pd

df = pd.read_csv("pandas/circuits.csv")

# print(df.shape)
# print(df.columns)

name = df["name"]
# print(name)

# two rows
two = df[["name", "location"]]
# print(two)

# filtering 
filtered = df[df["country"]=="France"]
# print(filtered)

new_filter = df[(df["country"]=="France") |(df["country"]=="USA") |(df["country"]=="Germany")]
print(new_filter)