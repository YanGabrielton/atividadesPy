import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('CAGED_Salarios_Julho-2025.csv')
print(df.columns)
df.head()

# Clean the 'Salário Médio Real de Admissão' column
df['Salário Médio Real de Admissão'] = df['Salário Médio Real de Admissão'].astype(str).str.replace('R$', '', regex=False).str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
df['Salário Médio Real de Admissão'] = pd.to_numeric(df['Salário Médio Real de Admissão'])

media = df['Salário Médio Real de Admissão'].mean()
mediana = df['Salário Médio Real de Admissão'].median()
moda = df['Salário Médio Real de Admissão'].mode()[0]

df['Salário Médio Real de Admissão'].describe()



# Frequência absoluta
freq_abs = df[ 'Mês' ].value_counts()
# Frequência relativa
freq_rel = df[ 'Mês' ].value_counts(normalize= True ) * 100


# Configuração visual
plt.figure(figsize=(10, 6))
sns.set_style('whitegrid')
# Criando o histograma
plt.hist(df['Salário Médio Real de Admissão'], bins=10, color='#0066cc', alpha=0.7)
plt.title('Distribuição de Salários')
plt.xlabel('Salário (R$)')
plt.ylabel('Frequência')
plt.grid(True, alpha=0.3)
plt.show()



