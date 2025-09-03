import pandas as pd
import tkinter as tk
from tkinter import filedialog,messagebox
 #widget elemento grafico,dispositivo ou ferramenta
 
chunk_size=50_000
arquivo= r"extracaoReceitaEstabelecimentos\estabelecimento0\K3241.K03200Y0.D50809.ESTABELE"
encoding='latin-1'
sep=';'




chunk_iter=None
chunk_current=None
