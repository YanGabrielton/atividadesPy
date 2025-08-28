import pandas as pd


listaAlunos = {'name':['gari','liout','kilyt'],
               'idade':[18,30,40],
               'cidade': ['sao paulo','  goias','   mato grosso']}

dataFrame1 = pd.DataFrame(listaAlunos)
print(dataFrame1)
