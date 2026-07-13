import pandas as pd
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [25, 30, 35, 40, 45],
    "city": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
    "salary": [70000, 80000, 90000, 100000, 110000]
}

df = pd.DataFrame(data)
print(df)
print(df.describe())