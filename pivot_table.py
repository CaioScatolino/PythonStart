import pandas as pd

data = pd.read_excel('./data/vendaCarros.xlsx')

# print(data)

df = data[['Fabricante', 'ValorVenda', 'Ano']]
print(df)

# Criando a tabela Pivot

pivot_table = df.pivot_table(
    index='Ano',
    columns='Fabricante',
    values='ValorVenda',
    aggfunc='sum'
)

print(pivot_table)

pivot_table.to_excel('./data/pivot_table.xlsx', 'Relatorio')