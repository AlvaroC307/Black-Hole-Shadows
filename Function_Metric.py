# Importar Librerias utiles
from math import * #Se debe importar entera para evitar problemas con el eval()
import csv
import numpy as np
from Initial_Values import M, constantes


# Lectura de los ficheros Metric, Inverse_Metric y Christoffel_symbols
# Empezamos leyendo Metric y Inverse_Metric
csv_Metric= open('./Data/Metric.csv', 'r')
Reader_Metric = csv.reader(csv_Metric)
csv_Inv_Metric= open('./Data/Inverse_Metric.csv', 'r')
Reader_Inv_Metric = csv.reader(csv_Inv_Metric)
csv_Chris= open('./Data/Christoffel_symbols.csv', 'r')
Reader_Chris = csv.reader(csv_Chris)


n=0
list_Metric=[] # Lista para escribir una sola linea de 4 elementos (1 indice fijo)
Matrix_Metric=[] # Lista de Listas con todos los elementos

for row in Reader_Metric:
    content = row[2] # Extraer el contenido del elemento 2 de la row en cuestion
    list_Metric.append(content)
    n+=1
    if n==4: # Cuando esten 4 elementos en list_Metric meterlos en Matrix_Metric y reiniciar
        Matrix_Metric.append(list_Metric)
        list_Metric=[]
        n=0

csv_Metric.close()

n=0 # Exactamente el mismo método para la metrica inversa que para la metrica 
list_Inv_Metric=[]
Matrix_Inv_Metric=[]

for row in Reader_Inv_Metric:
    content = row[2]
    list_Inv_Metric.append(content)
    n+=1
    if n==4:
        Matrix_Inv_Metric.append(list_Inv_Metric)
        list_Inv_Metric=[]
        n=0

csv_Inv_Metric.close()

# Eso era para la lectura de Metric y Inverse Metric, ahora toca Christoffel symbols 


n=0 # Se usa el mismo metodo que antes pero ahora se requieren de una lista, una lista de listas para pasarlas a la total
m=0
list_Chris=[] # Lista (2 indice fijos)
Matrix_Chris=[] # Lista de listas (1 indices fijo)
Tri_Matrix_Chris=[] # Matriz total con todos los datos
for row in Reader_Chris:
    content = row[3]
    list_Chris.append(content)
    n+=1
    if n==4:
        Matrix_Chris.append(list_Chris)
        list_Chris=[]
        n=0
        m+=1
        if m==4:
            Tri_Matrix_Chris.append(Matrix_Chris)
            Matrix_Chris=[]
            m=0

csv_Chris.close()

#-------------------Definicion de las funciones Metric, Inverse Metric y Christoffel Symbols 

# Cada elemento de estos tensores es un string creado por Sympy, al evaluar pasa a ser un numero en funcion de las coord o constantes
# que se le hayan pasado

def G(i:int, j:int, t:float, r:float, phi:float, theta:float) -> float:
    return eval(Matrix_Metric[i][j], None, {'t': t, 'r': r, 'phi': phi, 'theta': theta, 'M':M, **constantes}) 


def Inv_G(i:int, j:int, t:float, r:float, phi:float, theta:float) -> float:
    return eval(Matrix_Inv_Metric[i][j], None, {'t': t, 'r': r, 'phi': phi, 'theta': theta, 'M':M, **constantes})


# i hace referencia al superindice, j y k son los subindices

def Christoffel(i:int, j:int, k:int, t:float, r:float, phi:float, theta:float) -> float:
    return eval(Tri_Matrix_Chris[i][j][k], None, {'t': t, 'r': r, 'phi': phi, 'theta': theta, 'M':M, **constantes})


