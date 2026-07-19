import pandas as pd
data = {
    "name":['arun', "varun", "tarun", "Narun","Marun"], 
    "age": [28,34,22,34,28],
    "salary": [50000,60000,45000,52000,480000]
}

df = pd.DataFrame(data)

grouped = df.groupby('age')["salary"].sum()
print(grouped) 
grouped = df.groupby(['age','name'])["salary"].sum()
print(grouped) 

