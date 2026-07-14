import pandas as pd 

data = {
    "Name": ['Michael Schumacher', 'Lewis Hamilton', 'Max Verstappen', 'Fernando Alonso'],
    "Title": ['7 WDC', '7 WDC', '4 WDC', '2 WDC'],
    "Team": ['Ferrari', 'Mercedes', 'Red Bull', 'McLaren']
}

df = pd.DataFrame(data)
print(df)