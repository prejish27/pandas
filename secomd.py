import pandas as pd

data = {
    "name": ["Michael", "lewis", "sebastian", "max"],
    "team": ["ferrari", "mercedese", "redbull", "redbull"],
    "titles": [7,7,4,4]
}
df = pd.DataFrame(data)
print(df.info())

# print(df)

# df.to_csv("pandas/drivers.csv", index=False)
# df.to_excel("pandas/drivers.xlsx", index=False)
# df.to_json("pandas/drivers.json", index=False)
