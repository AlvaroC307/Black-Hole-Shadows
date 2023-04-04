# Importar Librerias utiles
import sympy as sp
import csv

# Importar otros ficheros de la carpeta

from Metric import*

# Definir los simbolos en sympy a usar y la lista de las coordenadas
M, a=sp.symbols("M, a")
t, r, phi, theta=sp.symbols("t, r, phi, theta")
coord=[t,r,phi,theta]

# Definicion de una funcion para calcular las parciales de la metrica,
# el imput (k) es el numero de la lista de coordenadas sobre la que se deriva


def partial_metric(i, j, k):
    return sp.diff(G[i,j], coord[k])

# Definicion Simbolo de Christoffel, gamma(i,j,k), el input (i) es el superindice mientras que (j, k) son los subindices
def Christoffel(i, j, k):
    suma=0
    for alpha in range(4):
        suma+=0.5*Inv_G[alpha,i]*(partial_metric(alpha, j, k)+partial_metric(alpha, k, j)-partial_metric(j, k, alpha))
    return sp.simplify(suma)



# Escribir cada simbolo de Christoffel en un fichero
# Definimos un fichero en el que escribir los resultados que nos interesen
file_Chris = open("./Data/Christoffel_symbols.csv", "w", newline="")
csv_Chris = csv.writer(file_Chris)


# Se escribe cada componente junto a sus 3 indices. También aparece en un print el progreso para así saber mejor cuanto falta
for i in range(4):
    for j in range(4):
        for k in range(4):
            Chris_ijk=Christoffel(i, j, k)
            print("Progreso: [",i,j,k,"]")
            csv_Chris.writerow([i, j, k, Chris_ijk])

file_Chris.close() # Cerrar el fichero
print("Escritura de los símbolos de Christoffel finalizada")