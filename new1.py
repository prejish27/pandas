import pandas as pd
# print(pd.__version__)

# df = pd.DataFrame([7, 2, 4, 7,  4], columns=['WDC'])
# print(df)

# print(df.dtypes)

# print(type(df))


data = {
    "Driver": ['Michael Schumacher','Fernando Alonso','Kimmi Raikkonen','Sebastian Vettel','Nico Rosberg','Lewis Hamilton','Max Verstappen', ],
    "Title":['7wdc','2wdc','1wdc','4wdc','1wdc','7wdc','4wdc'],
    "Team": ['Ferrari','McLaren','Ferrari','Redbull','Mercedese','Mercedese','Redbull']
}

df = pd.DataFrame(data)

# print(df)

# print(df.head(1))

# print(df.tail(2))

# print(df.shape)

# print(df.rename(columns={'Driver': 'Pilot'}))
# print(df)

# print(df.rename(columns={'Title': 'Championship'}))
# print(df)

# df.rename(columns={'Driver': 'Pilot'}, inplace=True)
# df.rename(columns={'Title': 'Championship'}, inplace=True)

# print(df)

# print(df.info())

# drivers = df.to_csv('drivers.csv')
drivers = df.to_excel('drivers.xlsx')


