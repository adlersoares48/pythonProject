import pandas as pd

# Abrir os 6 arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# Para cada arquivo verificar se algum valor na coluna de vendas daquele arquivo é maior que 55 mil
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} o vendedor {vendedor} bateu a meta de vendas. Ele vendeu R$ {vendas}')
