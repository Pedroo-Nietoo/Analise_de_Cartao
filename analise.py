# -*- coding: utf-8 -*-
"""Analise.ipynb

Automatically generated by Colaboratory.

# Desafio: 

Você trabalha em uma grande empresa de Cartão de Crédito e o diretor da empresa percebeu que o número de clientes que cancelam seus cartões tem aumentado significativamente, causando prejuízos enormes para a empresa

O que fazer para evitar isso? Como saber as pessoas que têm maior tendência a cancelar o cartão?

Referência: https://www.kaggle.com/sakshigoyal7/credit-card-customers
"""

import pandas as pd

tabela = pd.read_csv("/content/drive/MyDrive/Minicurso Análise de Dados/ClientesBanco.csv", encoding="latin1")
tabela = tabela.drop("CLIENTNUM", axis=1)
display(tabela)

"""# Tratando valores vazios e exibindo um resumo das colunas da base de dados"""

tabela = tabela.dropna()
display(tabela.info())
display(tabela.describe())

"""# Divisão entre Clientes X Cancelados"""

qtde_categoria = tabela["Categoria"].value_counts()
display(qtde_categoria)
print()
qtde_categoria_percentual = tabela["Categoria"].value_counts(normalize=True).round(1)
display(qtde_categoria_percentual)

"""# Criação de gráficos/Análise gráfica"""

import plotly.express as px
for coluna in tabela:
  grafico = px.histogram(tabela, x=coluna, color="Categoria")
  grafico.show()

"""# Informações da análise 👀
- Quanto mais produtos contratados um cliente tem, menor a chance de cancelamento;
- Quanto mais transações e maior valor de transação, menor a chance de cancelamento;
- Quanto maior a quantidade de contatos que o cliente teve que fazer, maior a chance de cancelamento. ***Entrou em contato 6 vezes = cancelou.***

# Extra - Gráfico de pizza
"""

g2 = px.pie(tabela, values="Idade", names="Dependentes", title="Análise teste")
g2.show()
