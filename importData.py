import pandas as pd

data = pd.read_excel('./data/vendaCarros.xlsx')

print(data)

print(data.head(10))

print(data['Fabricante'].value_counts())