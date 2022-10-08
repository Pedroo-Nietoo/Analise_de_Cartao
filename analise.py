#IDE: Google Colab
#Feito por @Pedroo-Nietoo

#Gerando acesso ao Drive
from google.colab import drive
drive.mount('/content/drive')

#Tratando a base de dados:
import pandas as pd

tabela = pd.read_csv("/content/drive/MyDrive/Minicurso Análise de Dados/ClientesBanco.csv", encoding="latin1")
tabela = tabela.drop("CLIENTNUM", axis=1)
display(tabela)

#Informações da tabela:
tabela = tabela.dropna()
display(tabela.info())
display(tabela.describe().round(1))

#Clientes X Cancelados
qtd_categoria = tabela["Categoria"].value_counts()
display(qtd_categoria)
print()
qtd_categoria_percentual = tabela["Categoria"].value_counts(normalize=True).round(1)
display(qtd_categoria_percentual)

#Gráficos:
import plotly.express as px

for coluna in tabela:
  grafico = px.histogram(tabela, x=coluna, color="Categoria")
  grafico.show()
  
#grafico2 = px.pie(tabela, values="Idade", names="Dependentes", title="Análise teste")
#grafico2.show()
