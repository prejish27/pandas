import pandas as pd
data = {
    "name":['arun', "varun", "tarun"], 
    "age": [28,34,22],
    "salary": [ 10000,2000,30000]

}

df = pd.DataFrame(data)
# df.sort_values(by='age', ascending=True, inplace=True)
df.sort_values(by=['age','salary'], ascending=True, inplace=True)
print(df)
