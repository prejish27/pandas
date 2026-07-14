import pandas as pd

data = {
    "name": ["Michael", "lewis", "sebastian", "max"],
    "team": ["ferrari", "mercedese", "redbull", "redbull"],
    "titles": [7,7,4,4]
}
df = pd.DataFrame(data)

df.insert(1, "country", ["Germany", "UK", "Germany", "Netherlands"])
print(df)