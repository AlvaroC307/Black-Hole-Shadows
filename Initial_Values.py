import csv
from math import pi
import sys


def Read_Input()->list:
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


def Read_Cte()->dict:
    csv_cte = open('./Input/Extra_Constants.csv', 'r')
    Reader_cte = csv.reader(csv_cte)

    # Escribir el fichero de contantes en una lista con su nombre asociado
    cte_names = []
    cte_values = []
    for row in Reader_cte:
        cte_names.append(row[0])
        cte_values.append(float(row[1]))
        # Escribir un diccionario con las constantes y su nombre asociado
    constantes = {}
    for i in range(len(cte_names)):
        constantes[cte_names[i]] = cte_values[i]
    # Fin de la escritura de las constantes
    return constantes


def Read_Input_Geodesic()->list:
    # Leer el fichero de inputs y de constantes
    csv_Input_Geo = open('./Input/Input_Geodesic.csv', 'r')
    Reader_Input_Geo = csv.reader(csv_Input_Geo)

    # Escribir el fichero de inputs en una lista
    list_Input_Geo = []
    for row in Reader_Input_Geo:
        content_input_geo = row[1]
        list_Input_Geo.append(content_input_geo)
    csv_Input_Geo.close()

    
    return list_Input_Geo


list_Input = Read_Input()
constantes = Read_Cte()
list_Input_Geo = Read_Input_Geodesic()

# Asignar nombres a los inputs importantes--------------------
# Masa del agujero negro
M = float(list_Input[0])


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


# Parámetro para ver a partir de que radio se considera que la métrica a degenerado a Minkowski y se corta el programa
r_limit = eval(list_Input[7])

# Nombre de la métrica que se va a elegir en la base de datos
name=list_Input[8]

# "Colours" es para la funcion de los cuadrantes de la esfera de colores. "Image" es si ha dado el usuario una imagen de fondo.
Back_Im = list_Input[9]
if (Back_Im != "Colours") and (Back_Im != "Image"):     # Comprobar que Back_Im tiene uno de los dos valores posibles:
    sys.exit("Hay un error, Back_im debe ser Colours o Image, para colores o imagen respectivamente")


# Nombre de la imagen que se va a elegir en la base de datos para el fichero Background
Image_name=list_Input[10]

# Nombre de la imagen que se va a elegir en la base de datos para el fichero Background
sound=list_Input[11]

# Yes o No al tener ejes en la imagen. Lo bueno de no tenerlos es poder ver a que punto corresponde cada imagen.
axis=list_Input[12]

#---------------------------------------------------------------------------------------------------------------------


# Asignar nombres a los inputs importantes Para el cálculo de una geodésica-----------------------


# Posicion inicial del Observador
t_0_Geo = eval(list_Input_Geo[0])
r_0_Geo = eval(list_Input_Geo[1])
phi_0_Geo = eval(list_Input_Geo[2])
theta_0_Geo = eval(list_Input_Geo[3])

# "Momentum" es para elegir el cuatrimomento de la partícula. "Screen" es para dar un pixel de la pantalla y obtener su trayetoria.
Momentum_or_Screen = list_Input_Geo[4]
if (Momentum_or_Screen != "Momentum") and (Momentum_or_Screen != "Screen"):     # Comprobar que Back_Im tiene uno de los dos valores posibles:
    sys.exit("Hay un error, Momentum_or_Screen debe ser Momentum o Screen")

# Cuatrimomento inicial del Observador
p_r_0_Geo = eval(list_Input_Geo[5])
p_phi_0_Geo = eval(list_Input_Geo[6])
p_theta_0_Geo = eval(list_Input_Geo[7])

# Punto de la pantalla para obtener el Cuatrimomento
i_Geo = int(list_Input_Geo[8])
j_Geo = int(list_Input_Geo[9])
if (i_Geo<0) or (i_Geo>N_pix):
    sys.exit("Hay un error, el valor de i_Geo no es válido. No se encuentra en el intervalo [0,N_pix]")
if (j_Geo<0) or (j_Geo>N_pix):
    sys.exit("Hay un error, el valor de j_Geo no es válido. No se encuentra en el intervalo [0,N_pix]")

# Precision para el cálculo de una geodésica independiente
precision_Geo=float(list_Input_Geo[10])

# Masa de una partícula para el cálculo de una geodésica independiente (debe ser pequeña m<<M=1 para no deformar significativamente el BH)
m_Geo=float(list_Input_Geo[11])

# Parámetro para ver a partir de que radio se considera que la métrica a degenerado a Minkowski y se corta el programa (GEODESICA ÚNICA)
r_limit_Geo=eval(list_Input_Geo[12])