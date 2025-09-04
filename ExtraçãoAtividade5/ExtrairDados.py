import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




explorar_dados =pd.read_csv("receitas_tres_ultimos_anos.csv",sep=';',encoding='latin-1')
explorar_dados.head()


# explorar_dados.isnull().sum()

converterReceita=explorar_dados['RECEITA ORCAMENTARIA (LIQUIDA)'].str.replace(',','.').astype(float)

dashboard=explorar_dados

plt.figure(figsize=(10,6))
plt.title('Dados Da ANTAQ')
sns.barplot(x="ï»¿ANO",y=converterReceita,data=dashboard)
plt.xlabel("Ano")
plt.ylabel("Receita Orçamentária (Líquida)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico_barras.png')

#errorbar=none 
plt.figure(figsize=(10,6))
plt.title('Dados Da ANTAQ')
sns.lineplot(x="ï»¿ANO",y=converterReceita,data=dashboard)
plt.xlabel("Ano")
plt.ylabel("Receita Orçamentária (Líquida)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico_line.png')


dashboard['RECEITA ORCAMENTARIA (LIQUIDA)'] = dashboard['RECEITA ORCAMENTARIA (LIQUIDA)'].str.replace(',', '.', regex=False).astype(float)
valor_por_Ano = dashboard.groupby('ï»¿ANO')['RECEITA ORCAMENTARIA (LIQUIDA)'].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 8))
plt.pie(valor_por_Ano, labels=valor_por_Ano.index, autopct='%1.2f%%', startangle=140)
plt.title('Distribuição da Receita Orçamentária (Líquida) por Ano')
plt.axis('equal') 
plt.show()


