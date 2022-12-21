# Importar Librerias utiles
import numpy as np
import sympy as sp
import math

# Importar otros ficheros 

import Metric
from Metric import*

# Definir los simbolos a usar y las coordenadas
M=sp.symbols("M")
t,r,theta,phi=sp.symbols("t,r,theta,phi")
coord=[t,r,theta,phi]

# Definicion de una funcion para calcular las parciales de la metrica,
# el imput (k) es el numero de la lista de coordenadas sobre la que se divide

def partial_metric(i,j,k):
    return sp.diff(metric(i,j),coord[k])

# Definicion Simbolo de Christoffel, gamma(i,j,k), el input (i) es el superindice mientras que (j,k) son subindices
def Christoffel(i,j,k):
    suma=0
    for alpha in range(4):
        suma+=0.5*inverse_metric(alpha,i)*(partial_metric(alpha,j,k)+partial_metric(alpha,k,j)-partial_metric(j,k,alpha))
    return sp.simplify(suma)


for i in range(4):
    for j in range(4):
        for k in range(4):
            print("[",i,j,k,"] ",Christoffel(i,j,k))