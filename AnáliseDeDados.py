import os
import pandas as pd


lista_arquivo = os.listdir(r'C:\Users\vitor\OneDrive\Documentos\Projetos\Mini_Curso_Python\Vendas')
tabela_total = pd.DataFrame()

for arquivo in lista_arquivo:
    if 'vendas' in arquivo.lower():
       tabela = pd.read_csv(r'C:\Users\vitor\OneDrive\Documentos\Projetos\Mini_Curso_Python\Vendas/{}'.format(arquivo))
       tabela_total = tabela_total._append(tabela)

# print(tabela_total)

# Calcular o produto mais vendido (em quantidade)
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=True)
print(tabela_produtos)

# Calcular o produto que mais faturou (em faturamento)
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False)
print(tabela_faturamento)

# Calcular a loja/cidade que mais vendeu (em faturamento) - criar um gráfico/dashboard
tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']]
print(tabela_lojas)

import plotly.express as px

grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico.show()