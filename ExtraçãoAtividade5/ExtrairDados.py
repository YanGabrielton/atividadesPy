import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




explorar_dados =pd.read_csv("receitas_tres_ultimos_anos.csv",sep=';',encoding='latin-1')
explorar_dados.head()


# explorar_dados.isnull().sum()



dashboard=explorar_dados

plt.figure(figsize=(10,6))
plt.title('Dados Da ANTAQ')
sns.scatterplot(x="ï»¿ANO",y="RECEITA ORCAMENTARIA (LIQUIDA)",data=dashboard)
plt.xlabel("Ano")
plt.ylabel("Receita Orçamentária (Líquida)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico_barras.png')


plt.figure(figsize=(10,6))
plt.title('Dados Da ANTAQ')
sns.lineplot(x="ï»¿ANO",y="RECEITA ORCAMENTARIA (LIQUIDA)",data=dashboard)
plt.xlabel("Ano")
plt.ylabel("Receita Orçamentária (Líquida)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico_line.png')


plt.figure(figsize=(10,6))
plt.title('Dados Da ANTAQ')
sns.boxplot(x="ï»¿ANO",y="RECEITA ORCAMENTARIA (LIQUIDA)",data=dashboard)
plt.xlabel("Ano")
plt.ylabel("Receita Orçamentária (Líquida)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico_box.png')

print(explorar_dados.isnull().sum())



