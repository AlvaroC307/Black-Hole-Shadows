# Importar Librerias utiles

import math
from math import *
import csv
import Function_Metric
from Function_Metric import *

N_pix=10
L_screen=12 # Multiplicamos por 4 para que haya espacio para verlo bien
paso=L_screen/N_pix


for i in range(N_pix+1):
    for j in range(N_pix+1): 
            x=i*paso-L_screen/2
            y=j*paso-L_screen/2 # Estan mal definidas

            print(x,y)

