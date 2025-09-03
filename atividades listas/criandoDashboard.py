import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



dados= {
  
    'Cidade':['Brasilia','goias','Sao paulo','rio de janeiro','mato grosso'],
    'População':[12.33,4.44,2.72,2.88,3.05], #em milhoes
    'Area':[1521,1200,331,693,5802] #KM
}


dashboard= pd.DataFrame(dados)

#criando um grafico de barras
plt.figure(figsize=(10,6))
sns.barplot(x='Cidade',y='População',data=dashboard)
plt.title('Tamanho de População por cidade')
plt.xlabel('cidade')
plt.ylabel('População')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico_barras.png')

#criando um grafico de dispersão

plt.figure(figsize=(10,6))
sns.scatterplot(x='Area',y='População',data=dashboard)
plt.title('relação entre area e população')
plt.xlabel('Area em km', color='green')
plt.ylabel('População(milhoes)')
for i,txt in enumerate(dashboard.Cidade):
    plt.annotate(txt,(dashboard.Area[i],dashboard.População[i]))
plt.tight_layout()
plt.savefig('grafico_dispersão.png')
