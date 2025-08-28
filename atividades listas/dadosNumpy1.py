import numpy as np
import matplotlib.pyplot as plt

numeros = np.array([85,95,74,32,41])
plt.figure(figsize=(8,5))
plt.plot(numeros)   #para linhas utikliza xlabel e ylabel
plt.title("Resultado Grafico")
plt.xlabel("Comprador")
plt.ylabel("valores")
plt.show()

# numeros=np.array([78,1,56,98,541,665])
plt.figure(figsize=(8, 5))

vendedores=["ana","pedro","carlos","jorge","liout"]
plt.bar(vendedores,numeros)
plt.title("Numero dos compradores")
plt.show()