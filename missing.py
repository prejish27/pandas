import pandas as pd
data = {
    "name": ["Alice", None, "Charlie", "David", "Eva"],
    "age": [25, None, 35, 40, 45],
    "city": ["New York", "Los Angeles", "Chicago", None, "Phoenix"],
    "salary": [70000, 80000, None, 100000, 110000]
}

df = pd.DataFrame(data)

print(df.isnull())
print(df.isnull().sum())