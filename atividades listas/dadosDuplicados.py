import pandas as pd
import numpy as np

data= {
    'Nome:':['GABRILO','JOAO CARLOS','GABRILO','Kirlei','joseide'],
    'Idade:':[19,24,19,34,None],
    'Cidade:':['Brasilia','goias','Brasilia','ceilandia','samambaia'],
    'Curso Favorito':['PHP','JAVA','PHP','PYTHON','programação web']
}


listaFrame= pd.DataFrame(data)
listaFrame.duplicated().sum() # faz a contagem de dados duplicados
listaFrame[listaFrame.duplicated()] # mostra quais dados são duplicados


listaFrame.drop_duplicates(inplace=True)



listaFrame.duplicated().sum()
print(listaFrame) #aqui vai mostrar a nova lista ja com a correção
