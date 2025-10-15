
import pandas as pd
import numpy as np
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Etapa 2: Carregamento do dataset do Kaggle (Adult Income)
file_path = "adult.csv"
df = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "mosapabdelghany/adult-income-prediction-dataset",
    "adult.csv"
)

df.columns = df.columns.str.strip().str.lower().str.replace('-', '_').str.replace(' ', '_').str.replace('.', '_')

df.replace('?', np.nan, inplace=True)

df = df.copy()
df['workclass'] = df['workclass'].fillna(df['workclass'].mode()[0])
df['occupation'] = df['occupation'].fillna(df['occupation'].mode()[0])
df['native_country'] = df['native_country'].fillna(df['native_country'].mode()[0])

df_renda_maior_50k = df[df['income'] == '>50K']
df_selecionado = df[['age', 'education', 'income']]
df['faixa_etaria'] = pd.cut(df['age'], bins=[0, 25, 45, 65, 100], labels=['Jovem', 'Adulto', 'Meia_idade', 'Idoso'])

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())