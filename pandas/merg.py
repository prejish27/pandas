import pandas as pd

df_characters = pd.DataFrame({
    "id": [1,2,3,4],
    "name":['luna', 'ellie', 'diana', 'rose']
})
df_abilities = pd.DataFrame({
    "id": [1,2,3,5],
    "level": [250, 400, 300, 200]
})

# df_merge = pd.merge(df_characters, df_abilities, on='id', how="inner")
# df_merge = pd.merge(df_characters, df_abilities, on='id', how="outer")
# df_merge = pd.merge(df_characters, df_abilities, on='id', how="left")
# df_merge = pd.merge(df_characters, df_abilities, on='id', how="right")


print(df_merge)