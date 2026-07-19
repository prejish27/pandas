import pandas as pd

df_region1 = pd.DataFrame({
    'id': [1,2],
    'name':['luna','ellie']
})
df_region2 = pd.DataFrame({
    'id':[3,4],
    'name':['rose','lily']
})

df_concate = pd.concat([df_region1, df_region2], axis=1,ignore_index=True)
print(df_concate)
