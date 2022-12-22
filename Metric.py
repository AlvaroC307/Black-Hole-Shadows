# Importar Librerias utiles
import numpy as np
import sympy as sp
import math

# Definir los simbolos en sympy a utilizar
M=sp.symbols("M")
t,r,theta,phi=sp.symbols("t,r,theta,phi")

# Definicion de la metrica
g00=-(1-2*M/r)
g01=0
g02=0
g03=0
g10=0
g11=1/(1-2*M/r)
g12=0
g13=0
g20=0
g21=0
g22=r**2
g23=0
g30=0
g31=0
g32=0
g33=r**2*sp.sin(theta)**2

# Metrica en forma matricial
G = sp.Matrix([[g00,g01,g02,g03],[g10,g11,g12,g13],[g20,g21,g22,g23],[g30,g31,g32,g33]])

# Funcion para sacar un elemento de la metrica

def metric(i,j):
    return G[i,j]

# FUncion para sacar un elemento de la metrica inversa
def inverse_metric(i,j):
    return G.inv(method="LU")[i,j]


#print(G[0,0])    
#print(metric(0,0)) 
#print(inverse_metric(0,0)) 