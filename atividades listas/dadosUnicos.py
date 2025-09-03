import pandas as pd

data= {
    'Nome:':['GABRILO','JOAO CARLOS','GABRILO','Kirlei','joseide'],
    'Idade:':[19,24,19,34,None],
    'Cidade:':['Brasilia','goias','Brasilia','ceilandia','samambaia'],
    'Curso Favorito':['PHP','JAVA','PHP','PYTHON','programação web']
}
listaUnica=pd.DataFrame(data)

listaUnica["Cidade:"].unique()
listaUnica['Cidade:']= listaUnica['Cidade:'].str.title() # vou estar deixando todos os textos em maiusculo
listaUnica['Cidade:'].unique()

#str.lower() para converter em minuscula
#str.strip()Remove Espaços extras
#str.upper()converte para MAISCULAS
#str.replace() substitui textos especificos coloco o (antigo, novo)

