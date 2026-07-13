import pandas as pd
data = {
    "name": ["Alice", None, "Charlie", "David", "Eva"],
    "age": [25, None, 35, 40, 45],
    "city": ["New York", None, "Chicago", None, "Phoenix"],
    "salary": [70000, 80000, None, 100000, 110000]
}

df = pd.DataFrame(data)
# print(df)
# df.dropna(inplace=True)
# print(df)

df.fillna('0', inplace=True)
print(df)