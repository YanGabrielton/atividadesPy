import pandas as pd
import numpy as np



data= {
    'Nome:':['GABRILO','JOAO CARLOS','GABRILO','Kirlei','joseide'],
    'Idade:':[19,24,19,34,None],
    'Cidade:':['Brasilia','goias','recanto','ceilandia','samambaia'],
    'Curso Favorito':['PHP','JAVA','PHP','PYTHON','programação web']
}
dataframe2= pd.DataFrame(data)
dataframe2.isnull()
#dataframe2['Nome:'].unique()

#mdIdade= dataframe2['Idade: '].mean() # fazer a media da idade 
#mdPrencherIdade=dataframe2.fillna({'Idade: ':mdIdade}) # aqui vai preencher o campo idade com a media

#prencher agora como não informado
dataframe2['Idade:']=dataframe2['Idade:'].fillna('Não Informado')
print(dataframe2)

#dataframe2.dropna() vai remover a linha como tratamento
#dataframe2.fillna(14) vai prencher o campo faltando como tratamento



