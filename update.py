import pandas as pd

data = {
    "name": ["Michael", "lewis", "sebastian", "max"],
    "team": ["ferrari", "mercedese", "redbull", "redbull"],
    "titles": [7,7,4,4],
    "country": ["Germany", "UK", "Germany", "Netherlands"]
}
df = pd.DataFrame(data)

df.loc[1, 'titles'] = 8
print(df)

# removing the column

df.drop(columns=['titles','team'], inplace=True)
print(df)