import pandas as pd
df = pd.read_csv("pandas/circuits.csv")
print(df.head(5))
print(df.tail(5))
print(df.info())