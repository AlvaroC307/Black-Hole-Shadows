import csv
from math import pi
import sys


def Read_Input():
    # Leer el fichero de inputs y de constantes
    csv_Input = open('./Input/Input.csv', 'r')
    Reader_Input = csv.reader(csv_Input)

    # Escribir el fichero de inputs en una lista
    list_Input = []
    for row in Reader_Input:
        content_input = row[1]
        list_Input.append(content_input)
    csv_Input.close()

    
    return list_Input


def Read_Cte():
    csv_cte = open('./Input/Extra_Constants.csv', 'r')
    Reader_cte = csv.reader(csv_cte)

    # Escribir el fichero de contantes en una lista con su nombre asociado
    cte_names = []
    cte_values = []
    for row in Reader_cte:
        cte_names.append(row[0])
        cte_values.append(eval(row[1]))
        # Escribir un diccionario con las constantes y su nombre asociado
    constantes = {}
    for i in range(len(cte_names)):
        constantes[cte_names[i]] = cte_values[i]
    # Fin de la escritura de las constantes
    return constantes


list_Input=Read_Input()
constantes=Read_Cte()

# Asignar nombres a los inputs importantes--------------------
# Masa del agujero negro
M = eval(list_Input[0])

# Posicion inicial del Observador
t_0 = eval(list_Input[1])
r_0 = eval(list_Input[2])
phi_0 = eval(list_Input[3])
theta_0 = eval(list_Input[4])

# Numero de Pixeles en un lado, el numero de pixeles total será, N_pix * N_pix
N = eval(list_Input[5])
if (N % 4) != 0:
    # Para que sea facil de dividir por 4 el numero de pixeles
    N = N + 4 - (N % 4)

N_pix=N

# Factor multiplicativo para el tamaño de la pantalla
Factor_Screen = eval(list_Input[6])

# "C" es para la funcion de los cuadrantes de la esfera de colores. "I" es si ha dado el usuario una imagen de fondo.
Back_Im = list_Input[7]
if (Back_Im!="C") and (Back_Im!="I"):     # Comprobar que Back_Im tiene uno de los dos valores posibles:
    sys.exit("Hay un error, Back_im debe ser C o I, para colores o imagen respectivamente")


# Parámetro para ver a partir de que radio se considera que la métrica a degenerado a Minkowski y se corta el programa
r_limit = eval(list_Input[8])
