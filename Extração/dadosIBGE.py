import pandas as pd

df = pd.read_csv("prestadoras_acreditadas_QUALISS.csv", sep=';', encoding="latin-1")
df.isnull().sum()






