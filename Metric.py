# Importar Librerias utiles
import numpy as np
import sympy as sp
import math
import csv

# Definir los simbolos en sympy a utilizar
M, a = sp.symbols("M,a")
t, r, phi, theta = sp.symbols("t,r,phi,theta")

prueba=r**2+sp.cos(theta)

# Definicion de la metrica
g00 = -(1-(2*M*r)/(r**2+(a*sp.cos(theta))**2))
g01 = 0
g02 = -(2*M*r*a*(sp.sin(theta))**2)/(r**2+(a*sp.cos(theta))**2)
g03 = 0
g10 = 0
g11 = (r**2+(a*sp.cos(theta))**2)/(r**2+a**2-2*M*r)
g12 = 0
g13 = 0
g20 = -(2*M*r*a*(sp.sin(theta))**2)/(r**2+(a*sp.cos(theta))**2)
g21 = 0
frac_g22= (2*M*r*(a*sp.sin(theta))**2)/(r**2+(a*sp.cos(theta))**2)
g22 = ((r**2+a**2+frac_g22))*(sp.sin(theta))**2
g23 = 0
g30 = 0
g31 = 0
g32 = 0
g33 = r**2+(a*sp.cos(theta))**2


# Metrica en forma matricial y cálculo de su inversa
G = sp.Matrix([[g00, g01, g02, g03], [g10, g11, g12, g13],
              [g20, g21, g22, g23], [g30, g31, g32, g33]])
Inv_G = G.inv(method="LU")



# Escribir la métrica y la métrica inversa en un fichero
# Definimos un fichero en el que escribir los resultados que nos interesen
file_Metric = open("./Data/Metric.csv", "w", newline="")
csv_Metric = csv.writer(file_Metric)
file_Inv_Metric = open("./Data/Inverse_Metric.csv", "w", newline="")
csv_Inv_Metric = csv.writer(file_Inv_Metric)

for i in range(4):
    for j in range(4):
            csv_Metric.writerow([i,j,G[i,j]])
            csv_Inv_Metric.writerow([i,j,Inv_G[i,j]])


file_Metric.close()
file_Inv_Metric.close()
print("Escritura de los elementos de la métrica y la métrica inversa finalizada")
